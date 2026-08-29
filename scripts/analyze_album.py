#!/usr/bin/env python3
"""Extract a compact, reproducible palette and tonal profile from an album cover."""

from __future__ import annotations

import argparse
import colorsys
import json
from pathlib import Path

from PIL import Image, ImageOps


def hex_colour(rgb: tuple[int, int, int]) -> str:
    return "#%02X%02X%02X" % rgb


def metrics(rgb: tuple[int, int, int]) -> tuple[float, float]:
    red, green, blue = (channel / 255 for channel in rgb)
    _, lightness, saturation = colorsys.rgb_to_hls(red, green, blue)
    return round(lightness, 3), round(saturation, 3)


def distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    return sum((left - right) ** 2 for left, right in zip(a, b)) ** 0.5


def extract_palette(image: Image.Image, colours: int = 16) -> list[dict[str, object]]:
    quantized = image.quantize(colors=colours, method=Image.Quantize.MEDIANCUT)
    palette = quantized.getpalette()
    total = image.width * image.height
    ranked = sorted(quantized.getcolors() or [], reverse=True)
    selected: list[dict[str, object]] = []

    for count, index in ranked:
        rgb = tuple(palette[index * 3 : index * 3 + 3])
        match = next((item for item in selected if distance(rgb, item["rgb"]) < 34), None)
        if match:
            match["count"] += count
            continue
        if len(selected) == 7:
            continue
        lightness, saturation = metrics(rgb)
        selected.append(
            {
                "hex": hex_colour(rgb),
                "rgb": rgb,
                "count": count,
                "lightness": lightness,
                "saturation": saturation,
            }
        )
    selected.sort(key=lambda item: item["count"], reverse=True)
    for item in selected:
        item["share"] = round(item.pop("count") / total, 4)
    return selected


def infer_profile(palette: list[dict[str, object]]) -> dict[str, object]:
    if not palette:
        return {"dominant": [], "neutral_bridge": None, "memory_accent": None, "shadow_tone": None}

    dominant = palette[:3]
    neutrals = [item for item in palette if item["saturation"] < 0.18]
    accents = [
        item
        for item in palette
        if item["saturation"] >= 0.38 and item["share"] <= 0.24 and item["lightness"] >= 0.18
    ]
    shadows = [item for item in palette if item["lightness"] <= 0.35]
    selected_share = sum(float(item["share"]) for item in palette) or 1.0
    average_lightness = sum(float(item["lightness"]) * float(item["share"]) for item in palette) / selected_share
    average_saturation = sum(float(item["saturation"]) * float(item["share"]) for item in palette) / selected_share

    if average_saturation < 0.18:
        structure_hint = "minimal-mono"
    elif average_lightness < 0.30 or average_saturation > 0.48:
        structure_hint = "sculptural-studio"
    else:
        structure_hint = "editorial-meadow"

    return {
        "dominant": [item["hex"] for item in dominant],
        "neutral_bridge": (
            max(neutrals, key=lambda item: item["lightness"])
            if neutrals
            else min(palette, key=lambda item: item["saturation"])
        )["hex"],
        "memory_accent": max(accents, key=lambda item: item["saturation"])["hex"] if accents else None,
        "shadow_tone": (min(shadows, key=lambda item: item["lightness"]) if shadows else min(palette, key=lambda item: item["lightness"]))["hex"],
        "average_lightness": round(average_lightness, 3),
        "average_saturation": round(average_saturation, 3),
        "structure_hint": structure_hint,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="Path to a PNG, JPEG, or WebP album cover")
    parser.add_argument("--output", type=Path, help="Optional path for JSON output")
    args = parser.parse_args()

    with Image.open(args.image) as source:
        image = ImageOps.exif_transpose(source).convert("RGB")
        image.thumbnail((512, 512))
        palette = extract_palette(image)

    result = {
        "source": args.image.name,
        "palette": [{key: value for key, value in item.items() if key != "rgb"} for item in palette],
        "profile": infer_profile(palette),
        "note": "Colour and structure fields are visual evidence only; infer mood from the cover carefully.",
    }
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)


if __name__ == "__main__":
    main()

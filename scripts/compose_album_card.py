#!/usr/bin/env python3
"""Place an exact, borderless album-cover card on a finished floral scene."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageFilter, ImageStat


POSITIONS = ("auto", "top-left", "top-right", "bottom-left", "bottom-right")
INTEGRATIONS = ("ambient", "shadow", "none")


def parse_width_ratio(value: str) -> float | None:
    if value == "auto":
        return None
    try:
        ratio = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("use 'auto' or a decimal ratio") from exc
    if not 0.12 <= ratio <= 0.30:
        raise argparse.ArgumentTypeError("ratio must be between 0.12 and 0.30")
    return ratio


def automatic_width_ratio(scene: Image.Image) -> float:
    aspect = scene.width / scene.height
    if aspect < 0.82:
        return 0.24
    if aspect > 1.25:
        return 0.21
    return 0.26


def card_position(
    scene: Image.Image, card: Image.Image, position: str, margin: int
) -> tuple[int, int]:
    left = margin
    right = scene.width - margin - card.width
    top = margin
    bottom = scene.height - margin - card.height
    return {
        "top-left": (left, top),
        "top-right": (right, top),
        "bottom-left": (left, bottom),
        "bottom-right": (right, bottom),
    }[position]


def region_detail_score(
    scene: Image.Image, card: Image.Image, position: str, margin: int
) -> float:
    """Estimate local visual activity so the cover avoids dense botanicals."""
    x, y = card_position(scene, card, position, margin)
    pad = max(2, round(card.width * 0.06))
    left = max(0, x - pad)
    top = max(0, y - pad)
    right = min(scene.width, x + card.width + pad)
    bottom = min(scene.height, y + card.height + pad)
    region = scene.convert("L").crop((left, top, right, bottom))
    edges = region.filter(ImageFilter.FIND_EDGES)
    colour_region = scene.convert("RGB").crop((left, top, right, bottom))
    saturation = colour_region.convert("HSV").getchannel("S")
    edge_mean = float(ImageStat.Stat(edges).mean[0])
    saturation_variation = float(ImageStat.Stat(saturation).stddev[0])
    return edge_mean + 0.35 * saturation_variation


def automatic_position(scene: Image.Image, card: Image.Image, margin: int) -> str:
    candidates = (
        ("top-left", "top-right")
        if scene.height > scene.width * 1.18
        else ("bottom-left", "bottom-right")
    )
    scores = {
        position: region_detail_score(scene, card, position, margin)
        for position in candidates
    }
    preferred, alternate = candidates
    if scores[alternate] < scores[preferred] * 0.78:
        return alternate
    return preferred


def add_soft_shadow(scene: Image.Image, card: Image.Image, pos: tuple[int, int]) -> None:
    pad = max(4, round(card.width * 0.10))
    shadow = Image.new(
        "RGBA", (card.width + 2 * pad, card.height + 2 * pad), (0, 0, 0, 0)
    )
    shadow_box = Image.new("RGBA", card.size, (0, 0, 0, 82))
    shadow.alpha_composite(shadow_box, (pad, pad))
    shadow = shadow.filter(ImageFilter.GaussianBlur(max(2, round(card.width * 0.045))))
    scene.alpha_composite(shadow, (pos[0] - pad, pos[1] - pad + max(1, pad // 5)))


def add_ambient_wash(scene: Image.Image, card: Image.Image, pos: tuple[int, int]) -> None:
    """Feather cover colours into the local scene without drawing a frame."""
    pad = max(8, round(card.width * 0.22))
    wash = Image.new(
        "RGBA", (card.width + 2 * pad, card.height + 2 * pad), (0, 0, 0, 0)
    )
    wash.alpha_composite(card, (pad, pad))
    wash = wash.filter(ImageFilter.GaussianBlur(max(4, round(card.width * 0.12))))
    alpha = wash.getchannel("A").point(lambda value: round(value * 0.30))
    wash.putalpha(alpha)
    scene.alpha_composite(wash, (pos[0] - pad, pos[1] - pad))
    add_soft_shadow(scene, card, pos)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scene", type=Path, help="Finished floral scene image")
    parser.add_argument("cover", type=Path, help="Exact source album cover")
    parser.add_argument("output", type=Path, help="Output image path")
    parser.add_argument(
        "--width-ratio",
        type=parse_width_ratio,
        default=None,
        metavar="auto|RATIO",
        help="Cover width relative to scene width; default adapts to orientation",
    )
    parser.add_argument("--margin-ratio", type=float, default=0.06)
    parser.add_argument("--position", choices=POSITIONS, default="auto")
    parser.add_argument(
        "--integration",
        choices=INTEGRATIONS,
        default="ambient",
        help="Borderless edge treatment; ambient is the default",
    )
    args = parser.parse_args()

    if not 0.01 <= args.margin_ratio <= 0.12:
        parser.error("--margin-ratio must be between 0.01 and 0.12")

    scene = Image.open(args.scene).convert("RGBA")
    cover = Image.open(args.cover).convert("RGB")

    width_ratio = args.width_ratio or automatic_width_ratio(scene)
    card_width = max(1, round(scene.width * width_ratio))
    cover.thumbnail((card_width, round(scene.height * 0.30)), Image.Resampling.LANCZOS)
    card = cover.convert("RGBA")

    margin = round(scene.width * args.margin_ratio)
    position = (
        automatic_position(scene, card, margin)
        if args.position == "auto"
        else args.position
    )
    pos = card_position(scene, card, position, margin)

    if args.integration == "ambient":
        add_ambient_wash(scene, card, pos)
    elif args.integration == "shadow":
        add_soft_shadow(scene, card, pos)
    scene.alpha_composite(card, pos)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    suffix = args.output.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        scene.convert("RGB").save(args.output, quality=95, subsampling=0)
    else:
        scene.save(args.output)


if __name__ == "__main__":
    main()

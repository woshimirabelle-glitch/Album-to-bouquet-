#!/usr/bin/env python3
"""Create reproducible, compatible Album Object variant scaffolds."""

from __future__ import annotations

import argparse
import hashlib
import json
import random


PROFILES = {
    "soft-mineral": {
        "heroes": ["dahlia", "anthurium", "calla lily", "garden rose"],
        "effects": ["none", "chalk-white preserved foliage", "pearl-matte paper edge"],
        "signals": ["dusty pink", "mist lilac", "sage green"],
        "lighting": "soft high-key or balanced editorial, chosen from the cover",
    },
    "electric-botanical": {
        "heroes": ["anthurium", "calla lily", "gladiolus", "gerbera"],
        "effects": ["brushed silver preserved foliage", "matte blue paper or wire", "graphite preserved leaves"],
        "signals": ["coral orange", "acid yellow", "electric violet"],
        "lighting": "balanced editorial, preserving saturated petal separation",
    },
    "dark-couture": {
        "heroes": ["deep burgundy calla lily", "anthurium", "dahlia", "iris"],
        "effects": ["preserved black foliage", "brushed bronze dried seed heads", "graphite paper or preserved leaves"],
        "signals": ["oxblood", "cold silver", "deep violet"],
        "lighting": "low-key dramatic with readable floral midtones",
    },
    "natural-signal": {
        "heroes": ["lily", "dahlia", "garden rose", "anthurium"],
        "effects": ["none", "chalk-white preserved foliage", "one translucent paper surface"],
        "signals": ["saffron yellow", "coral orange", "mineral blue"],
        "lighting": "soft high-key or balanced editorial, chosen from the cover",
    },
}

MODES = ["Architectural Object", "Raw Couture", "Living Sculpture"]
SIZES = ["Mini Object", "Standard Handheld", "Statement Sculpture"]
BACKBOARDS = [
    "three offset matte planes",
    "one torn fibre board with one counter-plane",
    "two translucent sheets over one rigid plane",
]
CRADLES = [
    "raw mulberry-fibre paper",
    "open botanical mesh",
    "crumpled translucent vellum",
    "deckled handmade paper",
]
BINDINGS = ["narrow raw-silk tape", "soft paper cuff", "loose natural twine", "thin matte ribbon"]
GIFT_CAMERAS = [
    "upright front-facing studio portrait",
    "handheld editorial portrait with the hand outside the final frame",
    "complete bouquet on a dark seat with no person visible",
]
DENSITIES = ["compact", "medium-open", "sparse sculptural"]
GESTURES = [
    "one tall vertical stem",
    "one lateral calligraphic branch",
    "one curved line escaping the core",
    "one isolated bloom beyond the backboard",
]


def seed_value(value: str) -> int:
    return int.from_bytes(hashlib.sha256(value.encode("utf-8")).digest()[:8], "big")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", choices=sorted(PROFILES), required=True)
    parser.add_argument("--count", type=int, choices=range(1, 4), default=2)
    parser.add_argument("--seed", default="album-to-bouquet")
    args = parser.parse_args()

    rng = random.Random(seed_value(args.seed))
    profile = PROFILES[args.profile]
    variants = []
    used = set()

    while len(variants) < args.count:
        variant = {
            "profile": args.profile,
            "structural_mode": rng.choice(MODES),
            "size_tier": rng.choice(SIZES),
            "hero_flower": rng.choice(profile["heroes"]),
            "core_density": rng.choice(DENSITIES),
            "wrapping": {
                "backboard": rng.choice(BACKBOARDS),
                "cradle": rng.choice(CRADLES),
                "binding": rng.choice(BINDINGS),
            },
            "material_effect": rng.choice(profile["effects"]),
            "signal_suggestion": rng.choice(profile["signals"]),
            "gesture": rng.choice(GESTURES),
            "default_output": {
                "mode": "Gift Bouquet",
                "camera": rng.choice(GIFT_CAMERAS),
                "lighting": profile["lighting"],
                "exact_cover_card": "adaptive borderless deterministic composite",
            },
        }
        signature = json.dumps(variant, sort_keys=True)
        if signature not in used:
            used.add(signature)
            variants.append(variant)

    print(json.dumps({"seed": args.seed, "variants": variants}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

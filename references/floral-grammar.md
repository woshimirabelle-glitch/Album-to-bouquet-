# Floral Grammar

Use this reference to turn album evidence into a stable Floral Prescription and generation prompt.

## 1. Prescription schema

```json
{
  "palette": {
    "dominant": ["colour family"],
    "tonal_neighbours": ["lighter/darker related colours"],
    "neutral_bridge": "ivory, cream, grey-green, stone, or warm grey",
    "memory_accent": "one small contrasting colour",
    "shadow_tone": "the dark value that gives depth"
  },
  "mood": ["two or three visual-emotional words"],
  "structure": "editorial-meadow | minimal-mono | sculptural-studio",
  "flowers": {
    "hero": "one species",
    "support": ["two or three species"],
    "line": ["one or two species"],
    "texture": ["one or two species"],
    "album_note": "optional small botanical gesture"
  },
  "wrapping": "warm-white or ivory matte paper",
  "lighting": "soft high-key | balanced editorial | low-key dramatic",
  "explanation": "one sentence connecting visible album evidence to the bouquet"
}
```

## 2. Choose the structure

### Editorial Meadow

Use for romantic, cinematic, bright, garden-like, or gently moving covers. Build a loose asymmetrical triangle or natural arc with clear high and low lines. This is the default.

### Minimal Mono

Use for sparse, monochrome, black-and-white, quiet, or highly restrained covers. Use two to five varieties, strong negative space, close tonal variation, and readable internal stem lines. The lower handle still needs a finished paper sheath unless raw exposed stems were explicitly requested. Sparse must still feel intentional and finished.

### Sculptural Studio

Use for dark, electronic, experimental, graphic, or sharply contrasted covers. Use calla lily, anthurium, orchid, allium, amaranthus, sea holly, or similarly directional botanicals. Include one dramatic gesture, not a full installation.

## 3. Colour translation

Use the cover's colours as roles rather than exact dye targets:

- blue: delphinium, sea holly, naturally grey-blue hydrangea, pale clematis, white flowers under cool light;
- black: burgundy, chocolate cosmos, ink-purple, dark foliage and shadow—never a mass of dyed black roses;
- red: wine, raspberry, garnet, dusty rose and ivory;
- green: hellebore, green hydrangea, viburnum, cymbidium orchid, olive and sage foliage;
- yellow: butter ranunculus, pale narcissus, honey dahlia and cream;
- orange: apricot, copper, terracotta, rust and white—not fluorescent orange;
- purple: clematis, scabiosa, lisianthus, anemone and delphinium;
- white/grey: ranunculus, tulip, calla lily, orchid, lisianthus, dusty miller and olive.

Ignore small text, logos, borders, parental-advisory labels, and skin tone unless they are visually central to the cover's atmosphere. A saturated accent should usually remain under 10% of the bouquet.

## 4. Botanical hierarchy

- Hero: one species that carries the main emotional read; usually three to five blooms.
- Support: two or three species that build volume without competing.
- Line: one or two tall or directional species that create rhythm and air.
- Texture: one or two fine materials that connect gaps without filling every gap.
- Album note: optional small gesture representing the cover's most memorable contrast.

Prefer ranunculus, dahlia, lisianthus, anemone, orchid, calla lily, delphinium, hydrangea, tulip, clematis, cosmos, scabiosa, allium, sea holly, smokebush, fern and olive. Use baby's breath only sparingly, if at all.

## 5. Composition and photography

- Keep the bouquet fully visible and upright on a real surface.
- Reserve roughly 18–25% negative space around the silhouette.
- Let the tallest line rise off-centre; keep the centre of mass stable.
- Keep wrapping in the lower third and clearly secondary.
- Finish the lower handle with a slim paper sheath; do not leave a long fan of bare stems visible by default.
- Use a single believable light direction and consistent depth of field.
- Choose exposure from the album. Even in low-key mode, preserve readable midtones, petal separation and species-specific softness on the hero and support flowers.
- Show at least two credible hero-flower cues: petal thickness, fine veins, folds, edge translucency, natural irregularity or a readable centre. Avoid uniform wax, artificial wetness, airbrushed petals, sharpening halos and HDR-like microcontrast.
- Background may borrow the album's shadow tone but should not duplicate the cover.
- The image should look commissioned by an editorial floral studio, never like e-commerce clip art.

## 6. Prompt skeleton

```text
Use case: photorealistic-natural
Asset type: square album-inspired bouquet portrait
Input image: Image 1 is the album-cover reference for palette, contrast, rhythm, negative space and atmosphere only; do not reproduce its people, text, logos, illustration or layout.
Primary request: create a one-of-one hand-tied bouquet from the Floral Prescription below.
Floral Prescription: [insert concise prescription]
Scene/backdrop: the complete bouquet stands upright on a quiet table or plinth; [background and surface].
Style/medium: high-end editorial floral still-life photography, real botanicals, tactile petals and stems, subtle analogue grain.
Composition/framing: square, centred and stable but naturally asymmetric; 18–25% breathing room; wrapping in the lower third; finished paper-wrapped handle with no long bare-stem bundle; reserve clean unmarked space for later cover compositing and do not draw a frame.
Lighting/mood: [insert lighting and mood].
Constraints: one hero species; credible natural flower colours; warm-white matte wrapping; no text, logo, watermark, album cover, hands or person.
Avoid: round bridal dome, dense flower ball, repeated identical flower assets, every bloom facing camera, fake blue or black roses, neon dye, plastic CGI petals, featureless airbrushed petals, sharpening halos, HDR-like edges, crushed floral shadows, giant envelope wrapping, giant bow, long exposed stem bundle, cover placeholder frame, excessive baby's breath, glitter, gold dust, Valentine's gift-shop styling.
```

## 7. Review rubric

Score each dimension from 0 to 2:

- album translation: connection is visible without literal copying;
- floral credibility: species, colours, stems and light look plausible;
- hierarchy: one hero, supporting levels and directional rhythm are clear;
- composition: upright, complete, stable and breathable;
- luxury restraint: wrapping and styling feel refined rather than decorative.

Revise once if the total is below 8/10 or any dimension scores 0. State the single most important correction in the revision prompt and preserve everything else.

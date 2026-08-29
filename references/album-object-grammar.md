# Album Object Grammar

Use this as the default grammar. It turns an album cover into a coherent floral art object rather than a conventional natural bouquet.

## Why the look works

The visual force comes from a total system: flowers, wrapping, material effects and one album-derived gesture all belong to the same graphic world. The object is frontal and relatively shallow, so it reads like an album cover made physical. Strong colour limitation, abrupt scale changes and tactile contrast create intensity without visual noise.

This is not automatically the same as traditional luxury floristry. Painted, preserved, metallic or artificial-looking elements can work when they are controlled like fashion materials. They fail when every surface is glossy, every bloom is dyed, or decorative effects accumulate without hierarchy.

## Object Prescription

```json
{
  "palette": {
    "field": "dominant family used across flowers and wrapping",
    "shadow": "dark structural value",
    "neutral": "light or quiet buffer",
    "signal": "one accent under 8 percent"
  },
  "geometry": {
    "structural_mode": "Architectural Object | Raw Couture | Living Sculpture",
    "size_tier": "Mini Object | Standard Handheld | Statement Sculpture",
    "silhouette": "vertical shield | asymmetric fan | narrow column | offset oval",
    "paper_planes": 4,
    "dominant_angle": "degrees or directional description",
    "core_density": "compact | medium | open"
  },
  "scale": {
    "hero": "one or two flowers at 1.4–1.8× median bloom size",
    "support": "medium flowers at 0.7–1.0×",
    "micro_texture": "fine material at 0.2–0.4×",
    "gesture": "one line reaching beyond the core"
  },
  "material_effect": "none | matte pigment | brushed silver | graphite | chalk white | preserved black",
  "album_symbol": "one abstract, non-copied gesture",
  "wrapping": {
    "backboard": "rigid graphic field and geometry",
    "cradle": "tactile material supporting the floral core",
    "binding": "restrained lower fixing"
  },
  "setting": "raw studio | black seat | dark plinth | pale stone",
  "lighting": "direction, softness and contrast",
  "explanation": "one sentence linking visible cover evidence to the object"
}
```

## Composition system

### Structural modes

- `Architectural Object`: frontal and relatively shallow; rigid graphic backboard; the clearest translation of album geometry. Use as the safest default.
- `Raw Couture`: deckled fibre paper, botanical mesh, visible twine and controlled experimental colour or finish. It should feel handmade and fashion-led, never rustic-crafty.
- `Living Sculpture`: less paper dominance and more botanical extension, while retaining one clear backboard or cradle and a deliberate silhouette. It is not a conventional garden bouquet.

### Size tiers

- `Mini Object`: one decisive hero occupying roughly 30–50% of the floral area, two or three supports and one fine gesture. Suitable for a small tabletop object.
- `Standard Handheld`: one or two heroes, two to four supports, micro-texture and one directional line. This is the default gift scale.
- `Statement Sculpture`: two heroes or one extreme hero, a larger backboard and longer gesture. Keep clear outer space; statement does not mean filling the frame.

### Overall frame

- Default to a vertical portrait `Gift Bouquet`. Do not switch to square or landscape unless the user explicitly asks. `Home Living Art` is an optional explicit mode, not a second default output.
- Place the object's optical centre within roughly 46–54% of frame width. The binding or vessel base, dense floral core and highest structural point should read as one central vertical axis.
- Distribute exterior negative space around the object. A directional branch may enter a side field, but do not leave one side with roughly twice the unused area of the other merely to reserve room for the album cover.
- Keep the main floral mass inside the central 60% of frame width. Internal asymmetry, diagonals and counter-movements remain desirable; whole-object side loading does not.
- Show the complete object upright, including a finished paper-wrapped handle/contact point. Unless raw exposed stems were explicitly requested, keep visible stem tips below roughly 4% of image height.
- Keep 15–22% clear space around the outer silhouette.
- Use a vertical object whose width is roughly 68–82% of its height.
- Keep the floral core relatively shallow and front-facing: this is closer to a poster in depth than a round bouquet.

### Floral core

- Floral core occupies roughly 52–64% of total object height.
- Core may be compact; breathing room belongs around the entire object and between the largest forms, not in every internal gap.
- Use one or two hero blooms. Their apparent diameter should be 1.4–1.8 times the median support bloom because they are naturally larger species or more open specimens—not because one flower has been artificially resized.
- Add two or three medium support forms, one micro-texture family and one directional gesture.
- Mix soft petals, rigid leaves and fine texture. Do not make all materials share the same size or surface.

### Wrapping architecture

Build three legible depth layers:

1. `Backboard`: one to three rigid or semi-rigid graphic planes. It carries the album field colour and primary geometry, usually extending 18–32% above the floral core.
2. `Cradle`: deckled handmade paper, open botanical mesh, crumpled vellum or another tactile layer that cups or supports the core without swallowing it.
3. `Binding`: a narrow paper cuff, raw-silk tape, natural twine or thin matte ribbon that resolves the lower structure. For a `Gift Bouquet`, continue a paper sheath below it so the handle is finished and a long bundle of bare stems is not visible.

Use one dominant diagonal and one counter-angle; random spikes are not structure. Side layers may overlap the core but should not cut through the hero flower. Shallow asymmetric cupping is allowed, especially in Raw Couture and Living Sculpture. Reject smooth, symmetrical, full-depth retail cones and large gift-shop bows.

## Colour system

Treat colour across the entire object, not flowers alone:

- 60–78% field colour and tonal neighbours;
- 15–28% shadow or neutral structure;
- 3–8% signal colour;
- at least three value levels: dark anchor, midtone field and light catch.

Use `ton-sur-ton` variation: several related blues, greys or reds are more dimensional than one identical sampled hue. Preserve one quiet neutral so the eye has somewhere to rest.

For monochrome covers, introduce depth through value and material: matte paper, soft petals, dry foliage and one metallic or translucent surface. Do not add unrelated rainbow colour for variety.

### Semantic accent review

Pixel share is evidence, not the final decision. Visually inspect the cover for one small colour that carries disproportionate identity: hair, a light, an eye, a dot, a garment detail, a drawn line or a single object. If it is meaningful, keep it to 3–8% and translate it into one small bloom, paper edge, wire, ribbon or directional gesture. Ignore interface marks, logos, compression artefacts and incidental noise. If no meaningful accent exists, do not invent one.

### Cover-to-object visual bridge

The exact cover is composited later, but the generated photograph must anticipate its presence without drawing a placeholder. Keep one upper quadrant quiet and use one restrained connection cue aimed toward it: a paper edge, stem line, soft light path or repeated signal colour. The cue stops before the cover zone. It should make the relationship legible while the centred floral object remains the primary hero.

The final match should be visible at three scales:

- field scale: background or wrapping shares the cover's dominant value/temperature;
- object scale: one major botanical or material family echoes a defining cover colour;
- signal scale: one small meaningful accent repeats near the visual path between cover and object.

## Controlled transformation

One non-natural material effect may carry the album concept. Apply it to wrapping, wire, dried/preserved foliage or another non-flower material family, never by changing fresh-petal geometry or making a bloom implausibly large or small:

- brushed silver foliage for cold, futuristic or metallic covers;
- graphite or preserved black leaves for dark, tense covers;
- chalk-white preserved foliage for monochrome motion or erasure;
- matte blue pigment on one paper, wire or dried-line family for electric blue covers;
- thin wire or ribbon loops for covers with drawn lines, orbits or repeated paths;
- one abstract fabric/cut-paper applique for highly graphic covers.

Do not combine painted flowers, rhinestones, metallic leaves, printed text, glitter and large bows in one object. One effect looks intentional; many effects look like craft decoration.

## Album symbol

Translate, do not copy. Convert the cover's most memorable non-colour feature into one abstract gesture:

- circular motif → one wire orbit or curved stem;
- motion blur → repeated pale line flowers moving in one direction;
- isolated figure → one vertical hero flower separated from the core;
- handwritten line → one looping ribbon or vine;
- sharp typography → stacked paper planes with a decisive angle;
- bright eye or dot → one small saturated bloom;
- collage → one abstract applique with no recognisable artwork or text.

Never reproduce a face, title, logo, lyric, parental-advisory mark or illustration inside the bouquet.

## Setting and photography

Choose one:

- `raw studio`: pale wall and rough concrete/stone support; best for blue, white and motion-led objects;
- `black seat`: black leather or matte black upholstery; best for metallic, red, purple and nocturnal objects;
- `dark plinth`: controlled black or charcoal studio; best for a clean public-facing product portrait;
- `pale stone`: cream or light-grey plinth; best for restrained red, ivory and soft graphic objects.

Choose the light from the album rather than applying one dark house look:

- `soft high-key`: for pale, open, luminous or tender covers;
- `balanced editorial`: for mixed-value covers and the safest default;
- `low-key dramatic`: for genuinely nocturnal, black, red or high-contrast covers.

Use one coherent directional source. Preserve paper grain, species-specific petal texture and different reflectance across materials. In low-key mode, keep readable flower midtones and put most darkness into the background, wrapping, foliage and cast shadows. The hero bloom should show at least two credible cues—petal thickness, fine veins, folds, edge translucency, natural irregularity or a readable centre. Avoid flat front flash, crushed floral blacks, blown highlights, uniform wax, airbrushed petals, sharpening halos and HDR-like microcontrast.

## Four colour profiles

### Electric Botanical

Teal, cobalt, violet or saturated green across paper and selected botanicals, with black or graphite structure and one small warm or light signal. One controlled pigment or metallic family is allowed.

### Soft Mineral

Chalk, shell, grey-pink, mist lilac or sage with soft value changes, fibrous paper and one quiet dark anchor. Avoid bridal symmetry and sugary pastel sameness.

### Dark Couture

Black, graphite, aubergine or bronze with one restrained colour signal. Create hierarchy through matte, velvet, translucent and metallic reflectance rather than recolouring every surface flat black.

### Natural Signal

Ivory, living green and raw fibre with one small yellow, orange, red or blue signal. Keep the natural base edited and sculptural rather than garden-random.

## Photography treatments

Choose one per requested image:

- `upright studio`: front-facing complete object against pale plaster, charcoal or a simple plinth; best for comparison and product presentation;
- `quiet tabletop`: object standing on wood, stone or a neutral woven surface, photographed at a restrained three-quarter angle; best for intimate gift scale;
- `editorial handheld`: the object is supported naturally but the final crop excludes the hand and person; preserve the immediacy of a florist's reveal without turning the person into the subject.

Use one directional side light. A pool of light and readable shadow are part of the object, but the shadow must not erase flower colour, petal separation or tactile softness.

## Generation prompt skeleton

```text
Use case: product-mockup
Asset type: vertical portrait album-derived floral art-object photograph
Input image: Image 1 is the album-cover reference for palette, value structure, geometry, rhythm and atmosphere only. Do not reproduce its people, text, logos, illustration or layout.
Primary request: create a new physical floral art object from the Object Prescription below.
Object Prescription: [insert concise prescription]
Subject: one complete floral object in [structural mode] at [size tier]; controlled core, decisive hero scale, medium supports, micro-texture and one directional gesture.
Materials: botanically accurate fresh flowers at plausible natural scale, tactile petals and preserved botanicals; [one selected material effect] only on a non-fresh-flower material family; a readable three-layer wrapping system of backboard, cradle and binding.
Composition: vertical portrait; complete object and finished paper-wrapped contact point visible; binding/base, floral core and highest point share an optical central axis; main mass remains inside the central 60% of frame width; 15–22% clear outer space distributed around the silhouette; paper and botanicals form one intentional silhouette with one dominant direction and one counter-movement; keep one quiet unmarked upper quadrant for a later cover at roughly 22–26% of frame width; create one subtle directional or colour bridge toward that quadrant without drawing a frame; do not move the whole object aside; no long bare-stem bundle unless explicitly requested.
Colour: 60–78% field family, 15–28% shadow/neutral, 3–8% signal; three value levels; ton-sur-ton variation rather than one flat sampled colour.
Setting and lighting: [selected setting], [soft high-key | balanced editorial | low-key dramatic] chosen from the album; one coherent directional source; readable midtones and species-specific petal surface; editorial fashion-object photography.
Constraints: one coherent album symbol, no literal cover reproduction, no visible album cover, no person, no hands, no text, no logo, no watermark.
Avoid: mutated petal shapes, artificial bloom enlargement or miniaturisation, unsuitable rooted or architectural plants forced into a bouquet, round bridal bouquet, equal-size blooms, random wrapping spikes, smooth symmetrical florist cone, identical recolouring of every material, glossy plastic, waxy CGI petals, airbrushed featureless flowers, sharpening halos, HDR-like edges, crushed floral shadows, multiple metallic effects, glitter, gold dust, rhinestone overload, giant bow, gift-shop styling, clip art or cutout collage.
```

## Review rubric

Score each from 0 to 2:

- cover-world coherence: the readable inset cover and object clearly share a world through field, material and signal evidence without copying;
- geometry: paper planes and floral mass form one intentional silhouette;
- scale hierarchy: hero, support, texture and gesture have distinct sizes;
- colour discipline: field, neutral/shadow and signal ratios are legible;
- material credibility: fresh flowers retain species-specific softness, edge structure and surface response while transformed non-flower materials feel tactile and controlled;
- photographic finish: complete object, outer breathing room, album-appropriate exposure and coherent lighting with readable floral midtones.

A smooth symmetrical florist cone is a geometry failure even when the flowers and palette are attractive. Shallow asymmetric cupping is not a failure when the backboard, cradle and binding remain visually distinct.

Revise once if the total is below 10/12 or any dimension scores 0. Correct one primary defect and preserve the rest.

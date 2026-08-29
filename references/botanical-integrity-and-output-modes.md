# Botanical Integrity and Output Modes

Read this before selecting flowers or generating any output.

## Biological hard gate

The album may change the selection and arrangement of plants, not their biology.

- Preserve each species' natural petal outline, edge, layering, centre, leaf form and growth habit. A rounded petal must not become pointed; a flat daisy form must not become a faceted star; a naturally matte petal must not become hard plastic or metal.
- Preserve plausible mature bloom and plant scale. Apparent hierarchy may come from choosing naturally large and small species, selecting an open or bud stage, changing camera distance, or placing forms at different depths. Never inflate one bloom or miniaturise a large architectural plant to make the composition work.
- Use hand-tied-compatible cut material in `Gift Bouquet`: plausible stem length, weight, balance, water needs and binding point. Do not place rooted cactus, agave, palm, large potted foliage or heavy unsupported branches inside an ordinary bouquet.
- Use vessel-compatible material in `Home Living Art`: branches and larger lines may extend farther when the vessel and mechanics could realistically support them. It is still an arrangement, not an impossible mixed ecosystem.
- When uncertain about a species, choose a common real cut flower with known florist use. Do not invent a hybrid or rely on a fantasy flower name.

Fresh petals stay botanically natural. Put transformed colour or surface effects on paper, wire, mesh, dried seed heads or preserved foliage. If the album calls for a sharp shape but the selected flower is soft and rounded, change species or use a non-botanical structural element; never sharpen the flower.

Before generation, record a compact feasibility ledger for every selected species:

- natural bloom/leaf silhouette and petal edge;
- plausible visible size band relative to a human hand or the chosen vessel;
- `cut`, `branch`, `dried/preserved` or `vessel-only` role;
- required stem length, binding or vessel support.

If a choice cannot pass this ledger confidently, replace it before prompting the image model.

## Default output: Gift Bouquet

- Use a vertical portrait frame. Centre the finished paper handle and main floral mass on the optical axis; directional flowers and paper may break symmetry without moving the entire bouquet to one side.
- A complete, physically sendable hand-tied bouquet with visible binding/contact point.
- Natural cut-flower scale and plausible stem relationships.
- Album-derived graphic wrapping may be expressive, but the result still reads immediately as a bouquet.
- Continue the wrapping below the binding as a finished paper sheath. By default no long bare-stem bundle is visible; only a few short irregular tips under roughly 4% of image height may show when useful.
- Tall line flowers may create height, but their stems must visibly converge toward a plausible hand-tied binding and paper-wrapped grip. Do not use a hatbox, pedestal, rigid flower box or flat-bottomed cylindrical container as hidden structural support. If the selected material cannot remain physically hand-held, move that structure to `Home Living Art` or choose a shorter/lighter cut-flower species.
- Avoid bridal domes, smooth retail cones, large bows and a screen-filling floral mass.

## Optional output: Home Living Art

Generate this only when the user explicitly requests a home, vessel or living-art version.

- A vessel-supported floral composition in a believable home interior.
- Use a vertical portrait frame with the vessel near the horizontal centre of the supporting table or cabinet. Build upward like a floral tree: a grounded vessel, a readable central trunk/core and an expanding crown with controlled side gestures.
- Keep the principal botanical mass visually centred. Do not place the vessel at the extreme right or left to manufacture empty space for the album card.
- More botanical extension, directional growth and spatial breathing room than the gift bouquet.
- The vessel, water/mechanics and base must plausibly support the chosen plants.
- Do not merely place the Gift Bouquet on a table; reinterpret the shared botanical prescription for space, depth and growth.

When both modes are requested, they share the cover-derived palette roles, emotional temperature, semantic signal and abstract album symbol. Flower species may overlap, but composition, support system and camera treatment must differ materially.

## Petal truth and album-dependent light

- Choose `soft high-key`, `balanced editorial`, or `low-key dramatic` from the cover's value structure and emotional temperature; do not impose one dark house style on every album.
- Low-key is allowed, but the hero and support flowers must retain readable midtones, colour separation and surface detail. Put most darkness into the background, wrapping, foliage and cast shadow.
- Render each species with its own credible surface: velvety, matte/powdery, thin and translucent, crisp, papery, or naturally waxy. Do not apply one uniform gloss, blur or mist to every bloom.
- The hero bloom should reveal at least two species-appropriate cues: petal thickness, fine venation, folds, translucent edges, softly irregular margins or a credible centre.
- Reject plastic shine, airbrushed featurelessness, sharpening halos, HDR-like edges, artificial dew, and wet gloss on species that are naturally matte.

## Exact album comparison card

Generate the optically centred floral scene first. Keep one corner of the existing background quiet and **unmarked**, but do not create a large unilateral void or push the object aside. Do not generate a frame or placeholder. Then place the exact source cover with `scripts/compose_album_card.py` rather than asking the image model to redraw it. The script adapts size and corner to orientation and uses borderless integration by default. Keep the source fully visible and unobstructed; do not add captions, crop, recolour or alter the artwork. Read [cover-integration-and-gift-finishing.md](cover-integration-and-gift-finishing.md) for placement and lower-bouquet finishing rules.

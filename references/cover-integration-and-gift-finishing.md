# Cover Integration and Gift Finishing

Read this when composing the exact source cover into a final result or generating a `Gift Bouquet`.

## Exact cover: preserve first, integrate second

The cover is evidence for comparison, not decoration. Preserve its complete source pixels and aspect ratio. Do not redraw, recolour, crop, blur, round its corners, add typography or place it inside a generated placeholder.

Integrate it through the world around it:

- generate a centred floral composition with one **unmarked** quiet upper quadrant whose value and temperature relate to the cover's neutral or shadow family; a quiet inset zone is enough—never reserve half the frame;
- establish one visual bridge from the floral object toward that quadrant: a restrained stem direction, paper angle, pool of light or repeated signal colour may lead the eye, but it must stop before the cover and must not draw a box around it;
- use `scripts/compose_album_card.py` after generation;
- default to a borderless ambient treatment: a very soft low-opacity colour wash plus a restrained shadow, never a visible outline or decorative frame;
- if the cover already sits naturally against the local value, use `--integration none`;
- use `--integration shadow` when separation is needed but colour bleed would be distracting.

Do not ask the image model to draw a square, frame, card slot, glowing box or placeholder. A visible empty rectangle remains a defect even if the exact cover will later be composited over it.

## Adaptive size and placement

`compose_album_card.py` defaults to `--width-ratio auto`:

- portrait scene: approximately 24% of scene width, normally upper-left;
- square scene: approximately 26%, normally lower-left;
- landscape scene: approximately 21%, normally lower-left.

Default edge inset is approximately 6% of scene width. The card should feel deliberately placed inside the photographic field, not pinned to the extreme corner of a phone interface.

In portrait mode, automatic placement compares the two upper quadrants. It prefers the upper-left reading position and moves right only when the right side is materially quieter. This avoids jitter from small lighting differences while still reducing collisions with substantial branches or paper.

These are starting points, not a reason to ignore composition. Keep the cover fully visible, separate from the main silhouette, and large enough to compare without becoming a second hero. Use an explicit ratio between 0.12 and 0.30 or another corner when the reserved negative space requires it.

Cover placement is subordinate to the floral composition, but the cover must remain visually consequential. Aim for roughly 22–26% of portrait width; reduce below 22% only when no upper quadrant can hold it without collision. If the default card would collide with a centred object, move it to the opposite upper quadrant before shrinking it. Do not regenerate or shift the floral object toward an edge to accommodate the card.

The cover must not touch the floral object, greeting card or image edge. It should feel deliberately placed within the same photographic field rather than pinned to an interface.

Do not brighten the cover independently until it looks pasted on, and do not darken the bouquet merely to make the cover dominant. Use the shared field, material and signal bridge to create connection. The cover is visually consequential; the flowers remain the tactile hero.

## Finished lower bouquet

A sendable bouquet needs a visually resolved handle. By default:

- continue the cradle or a separate paper sheath below the binding;
- wrap the gathered stems in one or two tactile paper layers that belong to the album palette;
- finish with a flat textile band, narrow matte tape or discreet twine;
- taper the sheath into a believable hand-held grip; it may be structured, but it must not have the visual weight, rigid rim or flat standing base of a hatbox, pedestal or flower container;
- show no long bundle of bare stems;
- allow at most a few short irregular stem tips, under roughly 4% of the image height, only when they improve physical credibility.

An exposed fan of stems is a failed `Gift Bouquet` finish even if the flowers are beautiful. Bare stems may be used only when the user explicitly requests a raw-stem editorial treatment. Do not solve the problem with a large bow or smooth retail cone.

## Final inspection

Reject or revise when:

- a visible frame, outline, placeholder box or hard matte surrounds the cover without being requested;
- the cover is too small to compare, dominates the bouquet, overlaps the object or sits against an unrelated colour field;
- the cover appears attached to the extreme image corner rather than inset into the composition;
- no colour, material, light or directional gesture visibly links the cover area to the floral object;
- the source cover has been redrawn, recoloured, cropped or distorted;
- the floral object's visual centre was displaced to create a large one-sided cover zone;
- more than a short hint of bare stems extends below the completed paper handle;
- the lower wrapping looks unfinished, bulky, symmetric or gift-shop-like.
- a supposed Gift Bouquet stands in a rigid cylinder, box or pedestal and therefore reads as a container arrangement rather than a sendable hand-tied bouquet.
- the cover remains readable but the hero flower is underexposed, colourless or missing species-specific petal texture;
- the flower surface looks airbrushed, uniformly waxy, over-sharpened or HDR-processed rather than naturally soft and tactile.

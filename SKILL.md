---
name: album-to-bouquet
description: "Turn one attached album-cover image into a vertical photorealistic sendable bouquet with the exact original cover integrated into the final photograph. Use for album-inspired bouquets, floral portraits of records, gift images derived from album artwork, or controlled bouquet variants; preserve real botanical morphology, scale and petal texture. Home living-art arrangements are optional only when explicitly requested. Do not use for literal cover copying, flower cutout collages, or ordinary photo recolouring."
---

# Album to Bouquet

Translate the album's visual character into a one-of-one floral object. The result must feel like evidence that the sender noticed the album's details—not like a palette pasted onto flowers.

## Required input

Use one attached album-cover image. If several images are attached and the target is unclear, ask which one is the album cover. Album title, artist, recipient, and message are optional; never block image generation on them.

## Workflow

1. Inspect the cover as a reference image, not an edit target. Do not reproduce its people, typography, logos, copyrighted illustration, or layout.
2. If the cover is locally available, run `scripts/analyze_album.py <image>` to obtain objective palette and tonal evidence. Then visually review the cover for one semantically meaningful colour that occupies less than roughly 8% of the image but carries strong identity. The script may miss small signals such as hair, a light, an eye, a garment detail or a single object. Use at most one such signal, and treat all automated mood and structure fields as hints, not facts.
3. Read [references/album-object-grammar.md](references/album-object-grammar.md). Use its `Album Object` system unless the user explicitly asks for a conventional natural bouquet; for that optional mode, read [references/floral-grammar.md](references/floral-grammar.md).
4. Read [references/botanical-integrity-and-output-modes.md](references/botanical-integrity-and-output-modes.md). Select only real cut-flower or arrangement-suitable species whose natural petal geometry, mature bloom size, stem behavior and weight work at the chosen scale.
5. Read [references/cover-integration-and-gift-finishing.md](references/cover-integration-and-gift-finishing.md) before generating a `Gift Bouquet` or compositing the exact source cover. Plan a readable inset cover zone and a subtle visual bridge between that zone and the floral object; never generate a frame or placeholder box.
6. Choose one structural mode: `Architectural Object`, `Raw Couture`, or `Living Sculpture`. Choose a size tier: `Mini Object`, `Standard Handheld`, or `Statement Sculpture`. The cover—not personal habit—should determine the best default.
7. Create one Botanical Prescription before generating: palette roles, a short feasibility ledger for each selected species (natural form, plausible size band, cut role and support), album symbol, composition, wrapping, background, album-dependent lighting and camera treatment. Add vessel notes only when the user explicitly requests `Home Living Art`.
8. When the user requests random or multiple versions, read [references/controlled-randomness.md](references/controlled-randomness.md) and create two or three meaningfully different prescriptions. Keep the album identity fixed while varying structure, scale, hero-flower family, material, and camera treatment. If locally available, `scripts/randomize_prescription.py` may be used to make the choices reproducible. By default each selected prescription produces one independent `Gift Bouquet`, not a paired home scene.
9. By default generate one complete portrait-orientation `Gift Bouquet`: a physically sendable hand-tied bouquet with a paper-finished handle and no long exposed stem bundle. Keep it optically centred on the vertical axis. Tall line flowers must converge into a believable hand-held binding; never support them with a hatbox, pedestal, rigid flower box or vessel-like cylindrical base. Generate `Home Living Art` only when explicitly requested; if requested, reinterpret the same album identity as a vessel-supported arrangement rather than reusing the bouquet render. Do not build either mode from flower cutouts or SVG flowers.
10. Generate floral scenes without asking the image model to redraw the cover. Keep the floral object centred first, then reserve a quiet, unmarked upper quadrant for a clearly readable inset cover. Connect that quadrant to the floral object through one restrained visual bridge—such as a directional stem, paper angle, background light path or repeated signal colour—that stops short of the cover zone and never becomes a frame. Never shift the bouquet or vessel to one side merely to create a large cover zone. When the original cover is locally available, use `scripts/compose_album_card.py` to place the exact source cover with adaptive size, inset position and borderless integration. If exact compositing is unavailable, show the cover beside the results rather than accepting a distorted generated copy.
11. Review each result independently against the biological hard gate and visual quality gate below. If one or two fixable defects remain, make one targeted revision. Stop after that revision and report any remaining limitation honestly.
12. Deliver the finished bouquet with the exact source cover clearly visible. Add the prescription or short gift explanation only when useful or requested. Include an optional Home Living Art image only when the user asked for it.

## Bouquet-first Album Object direction

- A complete, upright, front-facing 2.5D floral art object photographed like a limited-edition fashion accessory.
- Default to a vertical portrait frame. The handle or vessel, floral core and highest structural point should form a readable central axis; asymmetry belongs inside and around that axis, not as an entire object pushed to the frame edge.
- Dense but controlled floral core; clear external negative space around the complete object.
- One or two naturally larger hero species or fully opened specimens, medium support blooms, micro-texture and one directional gesture. Scale contrast must come from believable species selection and maturity—not artificial enlargement or miniaturisation.
- Two dominant colour families plus one neutral and one small accent. The wrapping participates in the palette instead of defaulting to white.
- Construct wrapping in three readable depth layers: a graphic backboard, a tactile cradle around the floral core, and a restrained binding. Their angles, overlap, colour and texture must derive from the cover. In a `Gift Bouquet`, continue the wrapping below the binding as a finished paper sheath instead of exposing a long fan of stems. The sheath must narrow into a credible hand-held grip and remain continuous with the binding; it must not become a flat-bottomed display container.
- One album symbol may use wire, ribbon, a cut-paper silhouette, a single metallic botanical element or an abstract applique. It must not copy cover art, logos, faces or legible text.
- Controlled non-natural finishes are allowed on wrapping, wire, dried/preserved foliage or another non-flower material family: matte pigment, brushed silver, graphite, chalk white or preserved black. Do not reshape, recolour or texture fresh petals into a form the species cannot naturally have.
- Choose an album-dependent light mode: `soft high-key`, `balanced editorial`, or `low-key dramatic`. One coherent directional source, tactile material detail, restrained analogue grain and a studio-object finish remain mandatory.
- “Premium” does not mean underexposed. Even in low-key mode, keep readable midtones on the hero and support blooms. Put most darkness in the background, wrapping, foliage and cast shadows rather than crushing the flowers.
- Render species-specific surfaces instead of one universal soft haze: velvety petals stay velvety, matte petals stay powdery, thin petals show restrained edge translucency, waxy species retain natural—not plastic—gloss. The hero bloom should reveal at least two cues among petal thickness, fine veins, folds, translucent edges and natural irregularity.
- Make the album relationship visible without explanation at three levels: a shared field or shadow family, a major floral/wrapping material echo, and one small semantic signal. Arrange at least one of those echoes along the visual path between the inset cover and the centred object.
- Keep text, logos, watermarks, hands, people and the album cover out of the AI-generated floral scene. Do not generate a frame or placeholder for the cover. The final deliverable adds the exact source cover only through deterministic borderless compositing.

## Quality gate

Reject before scoring if botanical integrity fails:

- a species' natural petal edge, petal geometry, bloom architecture or growth habit has been redesigned for the composition;
- a plant or bloom has been implausibly enlarged or miniaturised, including architectural plants such as cactus, agave, palm or oversized tropical foliage forced into an ordinary hand-tied bouquet;
- the stem length, weight, orientation or support would make the depicted hand-tied bouquet or vessel arrangement physically implausible;
- a fresh flower looks fabricated, plastic, metallic or fantasy-bred rather than like a credible specimen of a real species.

When a desired silhouette is biologically incompatible, choose another real cut-flower species with that natural form or translate the shape into paper, wire, mesh or the album symbol. Never mutate the plant.

Reject or revise when any of these are true:

- object is unintentionally tilted, cropped, floating, or fills nearly the entire frame;
- the floral object is visibly side-loaded, its main mass sits outside the central 40% of the frame, or one side's unused space is roughly twice the other side's without an explicit editorial reason;
- circular bridal-bouquet dome, equal-size flowers, or no clear scale hierarchy;
- repeated identical flowers, cutout edges, incompatible lighting, plastic/CGI texture, featureless airbrushed petals, sharpening halos, HDR-like microcontrast, implausible stems, or a hero flower whose surface and edge structure are unreadable;
- uncontrolled rainbow mixing, multiple competing metallic effects, glossy neon petals, glitter, gold dust, rhinestone overload, or excessive baby's breath;
- wrapping looks like an accidental giant envelope instead of an intentional system of planes;
- lower wrapping becomes a smooth, symmetric retail florist cone; shallow asymmetric cupping is acceptable when the backboard, cradle and binding remain distinct;
- a `Gift Bouquet` uses a hatbox, pedestal, rigid flower box or vessel-like cylindrical base to hold tall line flowers instead of converging into a hand-tied binding and wrapped grip;
- every material is recoloured identically, producing a flat monochrome blob;
- the album symbol is a literal copied face, logo, title, lyric or illustration;
- the object lacks outer breathing room, tactile contrast or a clear visual hierarchy.
- the default result does not clearly read as a physically sendable hand-tied bouquet;
- the album comparison card is missing, distorted, redesigned, partly hidden or not made from the exact source cover when deterministic compositing is available.
- the album comparison card reads as a tiny UI thumbnail, sits hard against the image edge, or feels visually unrelated to the floral scene;
- the generated scene contains a visible frame or placeholder box for the later cover composite;
- a large empty cover reservation displaces the floral object from the visual centre; the corner card must adapt to the scene, not dictate the scene's balance;
- a decorative outline or hard-edged matte makes the exact cover look like an unrelated UI tile;
- the cover-to-object relationship depends only on a written explanation instead of visible palette, material and directional evidence;
- a `Gift Bouquet` ends in a long exposed bundle of stems instead of a resolved paper-wrapped handle.
- the lighting ignores the album's value structure, or a dark treatment erases flower colour, petal separation and tactile softness.

An acceptable image should read at first glance as a commissioned floral fashion object, then reveal the album connection through colour, geometry and one memorable symbol.

Random variants are not successful merely because they differ. Every delivered variant must independently pass the gate and remain recognisably derived from the same album.

## Controlled revisions

When the user asks for a change, preserve the accepted object identity and alter only the requested dimension: lighter/deeper, softer/more graphic, denser/sparser core, hero scale, one material effect, accent ratio, background, or wrapping geometry. Do not silently redesign everything.

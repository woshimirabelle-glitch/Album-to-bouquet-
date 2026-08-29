# PETAL / NOTE — Project Journey

## The original idea

The project began with a simple wish: upload an album cover, extract its colours, and turn those colours into a beautiful virtual bouquet that could be sent to someone. The emotional premise was already larger than colour matching: a gift feels meaningful when it proves that the sender noticed another person's details.

## V1 — From palette to bouquet

The first working direction used an album cover to produce a natural wrapped bouquet, a floral recipe and an optional message card. It proved the interaction, but visual tests exposed serious limits: too few flower types, repeated cutout-like blooms, generic white wrapping, low-resolution export and a greeting-card feeling instead of editorial photography.

The key lesson was that colour extraction alone does not create taste.

## V2 — The Album Object

The project moved from “a bouquet in the album's colours” to “an album made physical through flowers.” The new default became a complete, frontal, 2.5D floral fashion object with architectural paper, controlled scale contrast, one abstract album symbol and clear outer breathing room.

References from Liberty, Wild at Heart, McQueens, Harrods and experimental botanical sculpture helped separate four concerns: natural giftability, colour translation, material quality and compositional discipline.

## V3 — Independent forward test

An independent test used Frank Ocean's *Blond*, a restrained grey-white cover with a very small but memorable green detail. Automated palette extraction missed that green, so the workflow gained semantic-accent review. The first generated object also drifted toward a conventional florist cone; a targeted revision produced shallower frontal paper planes and preserved the accepted floral identity.

V3 therefore added two non-obvious safeguards:

- pixel share is evidence, but a small meaningful colour may carry the album's identity;
- attractive flowers do not excuse ordinary retail wrapping geometry.

## V4 — Raw Botanical Couture and controlled randomness

Dozens of user-selected references revealed a richer grammar. The wrapping is not one surface but three depth layers: a graphic backboard, a tactile cradle and a restrained binding. The system now supports Architectural Object, Raw Couture and Living Sculpture; Mini, Standard and Statement scale tiers; and soft-mineral, electric-botanical, dark-couture and natural-signal colour profiles.

V4 also introduces controlled randomness. Album identity and quality standards remain fixed, while structure, size, hero flower, material, gesture and camera treatment may vary. Random output is successful only when every option is independently beautiful and recognisably belongs to the same album world.

## V5 — The final metre: cover integration and gift finishing

Testing revealed that a beautiful floral object could still feel unfinished in the final composite. A fixed cover size, decorative border or generated placeholder made the source image look like a UI tile pasted onto the photograph. A long exposed fan of stems similarly pulled attention away from the flowers and made the bouquet feel like a florist's work-in-progress rather than a completed gift.

V5 turns those observations into deterministic rules:

- the image model reserves unmarked negative space and never draws a cover frame;
- the exact source cover is composited after generation without cropping, recolouring or redrawing;
- cover size and default corner adapt to portrait, square and landscape outputs;
- borderless ambient integration replaces the former hard frame;
- a Gift Bouquet ends in a slim paper-finished handle, with no long bare-stem bundle unless explicitly requested.

The lesson is that the final metre matters: comparison media and lower wrapping belong to the same aesthetic system as the flowers.

## V6 — Centred growth and balanced space

Further paired-output tests exposed an overcorrection: reserving the upper-left corner for the album cover sometimes pushed the entire bouquet or home arrangement toward the right edge. The resulting empty field looked accidental rather than luxurious. The most successful test instead behaved like a floral tree, with its base, dense core and highest point aligned around a central vertical axis.

V6 makes that observation structural:

- both paired outputs default to vertical portrait orientation;
- the bouquet handle or vessel, main floral mass and highest point form an optical centre line;
- asymmetry remains inside the plant and paper gestures, not in an entire object shifted to the frame edge;
- Home Living Art uses a grounded vessel, central rise and controlled crown;
- the album card adapts in size or corner when necessary and never dictates the floral object's position.

The lesson is that negative space must support the object. Empty space is not automatically sophisticated when it destroys the centre of gravity.

## V7 — Stronger album presence and visual connection

The centred V6 compositions solved the side-loading problem, but the exact album cover became too polite: small, pressed against a corner and visually detached from the floral portrait. It functioned as evidence, yet did not feel like an active source of the object.

V7 restores that relationship without returning to a framed UI card:

- portrait covers default to roughly 24% of frame width;
- the cover moves inward from the image edge with an approximately 6% inset;
- automatic placement chooses the quieter upper quadrant to reduce collisions;
- a three-level match—field, major material and semantic signal—makes the album relationship visible without explanation;
- one restrained stem, paper angle, light path or colour echo bridges the cover quadrant and centred floral object;
- collision is solved by changing upper quadrant before shrinking the cover or moving the flowers.

The lesson is that the source image should be visually consequential. It is not the hero, but it must feel like the reason the hero exists.

## V7.1 — Public-release blind test

A final blind test used three visually unrelated covers: a dark portrait, a graphic red-and-black dance cover and a cool landscape of pink palms and reflection. Each cover produced both a Gift Bouquet and Home Living Art result. The test confirmed that the system could preserve album identity across very different palettes without reusing one default flower recipe, and that it could translate an unsuitable architectural plant such as a palm into vertical rhythm rather than miniaturising the plant.

The test also exposed one final ambiguity. A tall grove-like Gift Bouquet passed the botanical checks but its lower finish could be read as a cylindrical flower box instead of a hand-tied bouquet. V7.1 therefore distinguishes a structured paper grip from a container: tall stems must still converge into a credible binding and tapered hand-held sheath; flat-bottomed cylinders, hatboxes and pedestals belong outside the Gift Bouquet mode.

With that correction, the repository reached its first public-release candidate: the skill instructions, deterministic palette and cover tools, examples, MIT license, installation guide and project history are packaged together for GitHub.

## V7.2 — Light and petal realism

External review found that some results looked refined but too dark. A three-image study revisited previously generated floral scenes rather than changing their accepted composition. It showed that a bouquet can retain drama without sacrificing the physical information that makes flowers desirable: soft thickness, fine folds, delicate veins, restrained edge translucency and different surface responses across species.

V7.2 therefore separates mood from visibility:

- the album chooses soft high-key, balanced editorial or low-key dramatic light;
- even low-key scenes keep readable midtones on hero and support flowers;
- most darkness moves to background, wrapping, foliage and cast shadow;
- velvety, matte, translucent and naturally waxy species no longer share one generic surface treatment;
- plastic gloss, airbrushing, sharpening halos and HDR-like edges are quality failures.

The lesson is that darkness is only one kind of atmosphere. Tactile truth is what lets elegance remain emotionally alive.

## V8 — Bouquet First

Repeated testing made the product preference unmistakable: the most satisfying output is the sendable bouquet photographed together with the original album cover. The home living-art interpretation remains beautiful, but requiring it every time doubled generation cost and review effort while weakening the clarity of the core gift experience.

V8 simplifies the contract:

- one vertical, physically sendable Gift Bouquet is the default result;
- the exact original cover is always integrated as readable comparison evidence when local compositing is available;
- controlled randomness produces two or three independently judged bouquet candidates;
- Home Living Art becomes an optional extension only when explicitly requested;
- all botanical integrity, centred composition, cover connection, finished-handle and petal-realism gates remain in force.

The lesson is product focus: the strongest experience is not the one with the most outputs, but the one that most clearly turns “I noticed this about you” into a gift someone would want to send.

## Product meaning

PETAL / NOTE is no longer only an image generator. Its larger proposition is:

> Turn what I noticed about you into a floral object that could only have been made for you.

The album is the first reliable input because it already contains colour, rhythm, atmosphere and personal meaning. A later person-to-bouquet version may combine observable visual details with words and shared memories, but the current project remains focused on making the album experience genuinely beautiful, explainable and giftable.

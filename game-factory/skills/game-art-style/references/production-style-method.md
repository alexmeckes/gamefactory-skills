# Production art-style method

Use this reference to translate a locked aesthetic into a reproducible game-asset system.

## Contents

1. Preserve the aesthetic contract
2. Build the production benchmark
3. Construct viable translations
4. Compare generated evidence
5. Run production spikes
6. Lock production rules
7. Avoid common traps

## Preserve the aesthetic contract

Extract from `AESTHETIC_DIRECTION.md`:

- emotional thesis and allowed range;
- palette, light, motif, material-association, and atmosphere intent;
- world attitude and ordinary/extraordinary relationship;
- positive anchors, anti-anchors, and unwanted readings;
- invariants that every production method must preserve.

Treat these as constraints. The art-style stage may decide how a palette is encoded or how atmosphere is rendered, but not what the palette means or which atmosphere the world should have.

## Build the production benchmark

Use a difficult, representative gameplay frame rather than a beauty shot. Include:

- actual camera, viewing distance, display target, and crop;
- representative subject count, motion, occlusion, and information density;
- a hero/standard/background asset mix;
- common environment modules and high-volume props;
- interaction, danger, selection, navigation, or state cues;
- representative lighting, VFX, HUD, subtitles, and accessibility alternatives;
- one asset or state likely to stress animation and the content pipeline.

Keep game content and the aesthetic contract fixed across candidates. A candidate is invalid when it improves its presentation by changing the camera, density, mood, focal hierarchy, or world thesis.

## Construct viable translations

Generate only methods the team could plausibly ship. For each candidate, specify:

| Dimension | Decision |
|---|---|
| Representation | Sprite, pixel, painted 2D, cutout, billboard, low-poly 3D, stylized 3D, hybrid |
| Shape/proportion | How the aesthetic's forms become silhouettes, volumes, and reusable parts |
| Line/edge/value | Contours, edge hardness, value bands, focal contrast, distance behavior |
| Palette implementation | Exact swatches or ranges, lighting interaction, state colors, color-independent cues |
| Surface/material | Texture frequency, shader/material families, wear, detail hierarchy |
| Lighting/post | Light model, shadow rules, fog, outlines, post effects, fallback behavior |
| Animation | Frame, rig, cutout, skeletal, vertex, shader, or hybrid motion method |
| Modularity/variants | Reuse, seams, atlases, kits, recolors, damage/restored states |
| Pipeline | Authoring tools, source files, export, naming, integration, correction workflow |
| Runtime | Geometry, sprite, texture, material, memory, draw, effect, and load implications |

Default to three or four coherent candidates. Eight slight variants are less useful than three methods with clear pipeline consequences.

## Compare generated evidence

Use ImageGen to visualize the translation hypothesis, one call per candidate. Repeat the benchmark and aesthetic block verbatim. Vary only the production-style block.

Before scoring, classify:

- **Comparable:** preserves the benchmark and aesthetic sufficiently.
- **Questionable:** minor drift creates a stated caveat.
- **Invalid:** content, camera, aesthetic, or hierarchy changed enough to bias preference.

Score 1–5 with written evidence:

| Criterion | Weight | Evidence to seek |
|---|---:|---|
| Gameplay readability | 30 | Silhouette, overlap, motion, target-size downsample, interaction hierarchy |
| Production feasibility | 25 | Real team speed, skills, tools, revision burden, animation, cleanup |
| Aesthetic fidelity | 15 | Preserves thesis, mood range, palette meaning, motifs, and atmosphere |
| Consistency/modularity/extensibility | 10 | Works across tiers, variants, locations, common objects, and edge cases |
| Camera/platform/performance | 10 | Survives actual display and engine budgets |
| Animation/VFX/UI/accessibility | 10 | Works in motion and preserves non-color gameplay cues |

Calculate `sum(score / 5 × weight)` out of 100. Require at least 3/5 for readability and feasibility.

## Run production spikes

Generated images do not establish feasibility. Build the same representative slice for the top two in the intended method. Keep scope identical and record:

- hands-on creation and correction time;
- number and complexity of source files;
- reuse, variant, and modularity behavior;
- animation setup and iteration friction;
- engine import, materials, lighting, and post setup;
- runtime metrics relevant to the target platform;
- target-size readability in motion and dense scenes;
- accessibility and UI/VFX integration;
- which aesthetic properties were lost or expensive to preserve.

Use the spike to update feasibility scores. Prefer measured team performance over generic assumptions about whether 2D or 3D is easier.

## Lock production rules

Write rules with thresholds, examples, and fallbacks:

- silhouette targets and proportion ranges;
- line, edge, value, palette, and material implementation;
- detail tiers by distance, importance, and asset volume;
- light, shadow, fog, outline, and post-processing behavior;
- animation timing, deformation, pose, and transition rules;
- UI, VFX, interaction, and accessibility hierarchy;
- source/delivery formats, atlases, modular kits, variants, and naming implications;
- geometry, sprite, texture, material, memory, effect, and load budgets;
- hero, standard, background, and high-volume production tiers;
- acceptance tests and a cheap fallback that preserves the aesthetic.

Link every aesthetic rule to the upstream source. Keep generated images as anchors, not as the entire specification.

## Avoid common traps

- **Aesthetic drift:** The production candidate quietly changes the selected mood or world identity.
- **Medium lottery:** Candidates change content and camera as well as production method.
- **Key-art fallacy:** A beautiful illustration cannot survive the gameplay view.
- **Concept-only feasibility:** Generated imagery is mistaken for proof that the team can author it.
- **Generic 3D or generic pixel:** A familiar method erases the selected aesthetic's identity.
- **Hero-everything:** Ordinary props require the same detail and time as signature assets.
- **No motion test:** A still image hides deformation, overlap, and effect failures.
- **No real-team timing:** Feasibility is guessed instead of measured.
- **Image-only handoff:** Asset makers receive references but no thresholds, budgets, or fallbacks.
- **Upstream rewrite:** Art-style documentation redefines themes that belong in the aesthetic source.

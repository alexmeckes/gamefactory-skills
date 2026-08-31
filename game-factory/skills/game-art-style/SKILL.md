---
name: game-art-style
description: Translate an established game aesthetic into a production-ready art style and asset system. Use when Codex needs to choose or compare representation and production methods such as pixel art, painted or cutout 2D, low-poly or stylized 3D, or hybrid rendering; define shape, proportion, line, edge, value, material, lighting, animation, camera-readability, asset-tier, engine, and performance rules; run controlled ImageGen translations of a locked aesthetic; validate finalists with production spikes; or create and maintain an ART_STYLE_GUIDE.md for game asset production.
---

# Game Art Style

Answer “How will this team make the game look consistent and readable in production?” Translate a locked aesthetic into a reproducible visual language, engine treatment, and asset pipeline.

## Game Factory relationship

- **Consumes:** `$game-aesthetic` direction plus camera, platform, content, team, engine, readability, and performance constraints.
- **Produces:** Representation rules, shape treatment, rendering and material rules, asset tiers, budgets, pipeline choices, and a validation set.
- **Hands off to:** `$game-visual-blockout` for L3 production proxies and AI construction handoffs, then asset production and rendering implementation.
- **Boundary:** Translate an established aesthetic; do not redefine player rules, interaction states, or validated gameplay dimensions without an explicit upstream decision.

## Confirm the input boundary

Read the game's `AESTHETIC_DIRECTION.md` or equivalent first. Extract its thesis, emotional range, palette intent, motifs, world texture, atmosphere, positive anchors, anti-anchors, and explicit invariants.

If the user is still choosing the overall vibe, mood, symbolism, era/cultural cues, or aesthetic territory, use `$game-aesthetic` first. Do not quietly settle those questions while comparing pixel art, 2D, 3D, or hybrid methods. If the user explicitly wants a combined fast path, label the assumed aesthetic and keep it separate from art-style decisions.

Inspect production constraints:

- gameplay camera, motion, density, and target display size;
- platform, engine, lighting, performance, memory, and package budgets;
- team skills, tools, schedule, outsource constraints, and revision capacity;
- asset counts, variants, modularity, animation, VFX, UI, and accessibility needs;
- existing production assets and pipeline commitments.

Copy `assets/ART_STYLE_BRIEF.md` for durable work. Read `references/production-style-method.md` before comparing methods or locking rules.

## Compare production translations

Create only meaningfully viable methods that preserve the selected aesthetic. Default to three or four candidates when the production method is unresolved. Candidate differences may include:

- sprite, cutout, painted 2D, low-poly 3D, stylized 3D, billboard, or hybrid representation;
- shape and proportion implementation;
- contour, edge, value-grouping, palette, material, and lighting treatment;
- animation and deformation method;
- modularity, reuse, variant, and correction workflow;
- engine, camera, performance, and accessibility implications.

Hold aesthetic, gameplay content, camera, action, palette meaning, motifs, and atmosphere constant. Change only the production translation. Do not create new mood territories or rewrite the world thesis.

Default funnel:

1. **Translate:** Produce three or four art-style candidates from one difficult gameplay benchmark.
2. **Screen:** Reject candidates that fail aesthetic fidelity, gameplay readability, or known constraints.
3. **Compare:** Score the survivors with `assets/ART_STYLE_SCORECARD.md`.
4. **Spike:** Build a small real asset or in-engine sample for the top two using the intended production method.
5. **Lock:** Create `ART_STYLE_GUIDE.md` from `assets/ART_STYLE_GUIDE.md`.

Use this project layout unless an existing convention applies:

```text
art/art-style/
├── ART_STYLE_BRIEF.md
├── candidate-translations/   # S01–S04 images and exact prompts
├── production-spikes/        # Top-two real-method samples
├── contact-sheets/
├── ART_STYLE_SCORECARD.md
└── ART_STYLE_GUIDE.md
```

## Use ImageGen as evidence

Use the installed `$imagegen` workflow and built-in image generation tool by default. Make one call per candidate. Use the `stylized-concept` taxonomy and label input-image roles.

For every candidate:

- include the complete locked aesthetic block and anchor references;
- repeat the same benchmark subject, action, environment, camera, UI context, and information hierarchy;
- vary only the medium and production-style block;
- prohibit unintended text, logos, watermarks, borders, and presentation frames;
- keep IDs such as `S01` in filenames and records, not generated text;
- record exact prompts, reference roles, output paths, compliance, and production hypothesis;
- save requested project outputs into the project without overwriting existing candidates.

Generated art can demonstrate a translation hypothesis, but it cannot prove that the team can author, animate, revise, optimize, or render it consistently. Never select a production method from concept images alone.

## Evaluate the candidates

Normalize crop, size, and labels. Build a contact sheet with the bundled Pillow helper when useful:

```bash
python3 scripts/build_contact_sheet.py <candidate-directory> --output <contact-sheet.png>
```

First classify candidates as `Comparable`, `Questionable`, or `Invalid` based on benchmark and aesthetic compliance. Then score 1–5 with evidence using these weights:

- gameplay readability: 30%;
- production feasibility: 25%;
- fidelity to the locked aesthetic: 15%;
- consistency, modularity, and extensibility: 10%;
- camera, platform, and performance fit: 10%;
- animation, VFX, UI, and accessibility fit: 10%.

A candidate below 3/5 for readability or feasibility cannot win without an explicit exception. Treat weighted scores as recommendations, not automatic decisions.

## Run a production spike

Test the top two in the team's real tools. Choose the smallest sample that crosses the major pipeline boundaries, such as:

- one hero or standard character with idle, movement, and extreme action;
- one environment module kit with repetition and variant needs;
- one common prop and one high-volume asset tier;
- a representative material, lighting, and post-processing setup;
- a dense gameplay frame with interaction cues, HUD, VFX, and color-independent signals.

Measure hands-on creation time, revision time, source complexity, reuse, animation friction, engine setup, runtime cost, target-size readability, and cleanup required from generated references. Reject a candidate that only works as key art or requires hero effort for ordinary assets.

## Lock the art-style guide

Use `assets/ART_STYLE_GUIDE.md` to document:

- source aesthetic and invariants;
- production representation and pipeline thesis;
- shape, proportion, silhouette, line, edge, value, palette implementation, materials, lighting, and detail rules;
- camera, composition, readability, UI, VFX, and accessibility integration;
- character, environment, prop, and animation rules;
- hero, standard, background, and high-volume asset tiers;
- source/delivery formats, budgets, naming or modularity implications, and fallback rules;
- positive production anchors, anti-anchors, future prompt contract, and acceptance tests.

Do not redefine the game's themes, emotional promise, cultural cues, or symbolic meaning. Link back to the aesthetic source of truth.

## Finish the handoff

Report artifact paths, ImageGen call count and mode, the selected production style, production-spike evidence, rejected methods and failure reasons, unresolved pipeline risks, exact prompts and reference roles, and the next representative asset to build.

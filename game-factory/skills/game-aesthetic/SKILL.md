---
name: game-aesthetic
description: Discover, explore, compare, select, and document the overall aesthetic identity of a game using controlled batches of AI-generated concept art. Use when Codex needs to define a game's vibe, visual mood, emotional tone, palette logic, atmosphere, motifs, symbolic language, era or cultural cues, world texture, UI tone, or aesthetic territory; generate broad mood or concept directions with ImageGen; build and evaluate an aesthetic moodboard; or create an AESTHETIC_DIRECTION.md handoff before choosing a production art style.
---

# Game Aesthetic

Answer “What should this game world feel like?” Explore coherent visual territories and lock the winning emotional and thematic language. Leave production-medium decisions such as pixel art, painted 2D, or low-poly 3D to `$game-art-style` unless the user explicitly asks to combine both stages.

## Game Factory relationship

- **Consumes:** `$game-design-spec` player fantasy, pillars, themes, audience, world facts, and tone boundaries.
- **Produces:** A locked aesthetic thesis, palette intent, motifs, atmosphere, emotional range, anchors, and anti-anchors.
- **Hands off to:** `$game-art-style` for production translation and to narrative, audio, UI, and marketing for mood alignment.
- **Boundary:** Own emotional and symbolic direction, not production medium, geometry budgets, interaction rules, or engine implementation.

## Frame the aesthetic question

Inspect the game design specification, narrative premise, audience, existing references, and non-negotiable visual elements. Extract:

- player fantasy, themes, emotional promise, and design pillars;
- intended audience, tone boundaries, content rating, and market context;
- world condition, time/era cues, cultural influences, recurring places, and narrative contrasts;
- aesthetic tensions such as cozy/eerie, ancient/futuristic, sincere/playful, or pristine/decayed;
- existing visual or brand commitments that must remain compatible.

Copy `assets/AESTHETIC_BRIEF.md` for durable work. Treat missing choices as explicit assumptions. Do not let an accidental rendering technique choose the aesthetic.

## Explore coherent territories

Read `references/aesthetic-exploration.md` before creating territories or evaluating a batch.

Define one representative **world anchor** with invariant subjects, action, location, composition, story facts, and output intent. Hold the rendering medium and camera treatment as constant as practical. Vary the aesthetic territory:

- emotional temperature and contrast;
- palette behavior and light atmosphere;
- recurring motifs, symbols, and visual metaphors;
- era, cultural, architectural, and decorative cues;
- environmental condition, material associations, and signs of use or history;
- density, rhythm, negative space, and ornament;
- relationship between ordinary life and the game's extraordinary premise;
- UI, typography, motion, and sound analogs at the level of mood—not implementation.

Use descriptive visual properties rather than imitation of a named artist. Name each territory by its thesis, not a generic quality claim.

Default funnel when the user requests broad exploration without a count:

1. **Breadth:** Generate eight distinct aesthetic territories using the same world anchor and neutral rendering treatment.
2. **Shortlist:** Score all eight and select three with `assets/AESTHETIC_SCORECARD.md`.
3. **Range test:** Generate each finalist in three conditions: ordinary daily life, peak fantasy or aspiration, and pressure, danger, or loss.
4. **Converge:** Select one territory or run a single-variable refinement between the top two.
5. **Lock:** Create `AESTHETIC_DIRECTION.md` from `assets/AESTHETIC_DIRECTION.md`.

Adjust counts for explicit time or cost constraints. Do not stop at the first appealing image, mix medium exploration into this stage, or let every candidate depict different content.

Use this project layout unless an existing convention applies:

```text
art/aesthetic-exploration/
├── AESTHETIC_BRIEF.md
├── round-01-territories/    # E01–E08 images and exact prompts
├── round-02-range-tests/    # Finalist subfolders
├── contact-sheets/
├── AESTHETIC_SCORECARD.md
└── AESTHETIC_DIRECTION.md
```

## Generate with ImageGen

Use the installed `$imagegen` workflow and built-in image generation tool by default. Make one call per distinct candidate or range-test image. Keep prompts compact and use the `stylized-concept` taxonomy.

For every territory:

- repeat the full world anchor and neutral rendering treatment;
- vary only the declared aesthetic block;
- prohibit unintended text, logos, watermarks, frames, and unrequested subjects;
- keep IDs such as `E01` in filenames and records, not inside generated images;
- record the exact prompt, reference-image roles, output path, and content-compliance notes;
- save requested project candidates into the project and never overwrite existing outputs.

Label every input image as an aesthetic reference, composition reference, subject reference, or edit target. Use generation with references for mood guidance; use edit mode only when preserving an existing image while changing a specified part.

## Compare the territories

Normalize crop, size, and labels. Build a blind contact sheet when Pillow is available:

```bash
python3 scripts/build_contact_sheet.py <candidate-directory> --output <contact-sheet.png>
```

First mark each result `Comparable`, `Questionable`, or `Invalid` based on anchor compliance. Then score 1–5 with evidence using these default weights:

- game fantasy and pillar fit: 25%;
- emotional range: 20%;
- internal coherence: 15%;
- distinctiveness: 15%;
- world-building generativity: 10%;
- audience and marketing fit: 10%;
- clarity of future art-style handoff: 5%.

A candidate below 3/5 for game/pillar fit or emotional range cannot win without an explicit exception. Have reviewers score independently before discussing results when practical. Explain any override of the weighted result.

## Lock the aesthetic direction

Document the selected territory as a system of meaning, not a list of adjectives. Use `assets/AESTHETIC_DIRECTION.md` to capture:

- visual thesis and emotional promise;
- tone spectrum and boundaries;
- palette roles, temperature, saturation, and contrast intent;
- motifs, symbols, shapes, materials, architecture, and environmental storytelling;
- era and cultural cues, with research or sensitivity needs where relevant;
- light, weather, atmosphere, density, rhythm, ornament, and negative space;
- ordinary, aspirational, dangerous, comic, and tragic range examples;
- character/world relationship and UI/typography/motion/audio mood analogs;
- positive anchors, anti-anchors, prompt contract, and open questions.

Do not prescribe polygon counts, texture sizes, animation frame counts, shaders, or asset-production tiers here. Pass the locked aesthetic plus its anchors to `$game-art-style` for those decisions.

## Finish the handoff

Report artifact paths, ImageGen call count and mode, the selected territory and evidence, rejected finalists, exact retained prompts and reference roles, unresolved aesthetic risks, and the recommended `$game-art-style` next step.

---
name: game-visual-blockout
description: Create, compare, select, and document low-fidelity game silhouettes, greyboxes, massing studies, production proxies, and level blockouts, then turn each selected prototype into a precise AI-ready construction brief. Use when Codex needs to explore character, creature, prop, vehicle, building, environment, room, encounter, or modular-kit shapes before final art; validate recognition, proportions, spatial flow, camera readability, gameplay function, collision, animation clearance, or scale; generate controlled silhouette or neutral-grey concept variants; make Blender or engine-native blockouts; or prepare an AI asset handoff with orthographic views, dimensions, shape grammar, material zones, technical constraints, prompts, and acceptance checks.
---

# Game Visual Blockout

Resolve shape, scale, space, and function before surface finish. Produce prototypes that are deliberately cheap to change and descriptions precise enough for another AI or artist to construct the intended asset without guessing at the gameplay-critical parts.

## Game Factory relationship

- **Consumes:** `$game-design-spec` requirements, `$game-interaction-contracts` IDs and semantic hooks, gameplay camera/metrics, and optional `$game-art-style` constraints.
- **Produces:** Validated silhouettes, footprints, greyboxes, production proxies, spatial evidence, and AI-ready construction handoffs.
- **Hands off to:** Interaction bindings, Blender or engine production, asset review, and milestone verification.
- **Boundary:** Own shape and spatial evidence. Do not hide design, interaction, or production-style changes inside a more polished blockout.

## Choose the prototype mode

Select the lowest fidelity that answers the current question:

- **L0 footprint:** Bounding volume, floor plan, reach, traversal, camera, or occupancy. Use for rooms, encounters, buildings, large props, and spatial systems.
- **L1 silhouette:** Outer contour, negative space, proportion, stance, and recognition. Use for characters, creatures, props, vehicles, landmarks, and readable gameplay classes.
- **L2 greybox:** Primary and secondary masses, functional zones, articulation, clearances, collision, and scale. Use before detailed 3D modeling or level production.
- **L3 production proxy:** Validated blockout plus pivots, sockets, animation ranges, modular seams, material zones, budgets, and engine handoff constraints.

Do not advance fidelity merely because the current result looks plain. Advance when the present level answers its question and passes its hard gates.

Choose the medium that matches the evidence needed:

- Use `$imagegen` for 2D silhouette families, orthographic shape studies, or rapid massing concepts.
- Use relevant Blender game-development skills for inspectable 3D asset blockouts or `.blend`/GLB deliverables.
- Use engine-native primitives when movement, collision, camera, navigation, encounter timing, or spatial feel must be tested in play.

## Frame the blockout question

Inspect the relevant game-design requirement, locked aesthetic or art-style rules when they exist, camera, platform, engine, animation needs, and representative gameplay view. Copy `assets/BLOCKOUT_BRIEF.md` for durable work.

Define one question, such as:

- Can the enemy class be recognized in 200 ms at gameplay size?
- Can the shop counter support the required interactions and animations?
- Does the room create the intended navigation and sightline pressure?
- Can one modular kit produce the required building family without visible repetition?

Lock invariants before exploring: role, world scale, camera, occupied volume, required actions, attachment points, access routes, collision needs, and forbidden changes. Declare comparison tests, participants when relevant, and pass thresholds before generating candidates. Mark unknown measurements, engine coordinates, or budgets as assumptions with a validation method.

When behavior already has `$game-interaction-contracts` records, reference their IDs and derive required volumes, sockets, clearances, motion envelopes, access points, and semantic hooks from them. Do not duplicate the state rules inside the blockout.

## Explore controlled candidates

Read `references/blockout-method.md` before creating a multi-candidate batch, a level greybox, or a production proxy.

Default to six candidates when the user requests exploration without a count. Give every candidate a stable ID and vary one declared shape thesis while preserving the same functional brief, scale, camera, framing, and output treatment.

Keep the representation intentionally neutral:

- L1 uses a solid black silhouette on a plain high-contrast background. Add at most one neutral cut-line or value only when needed to explain a functional opening.
- L2 uses simple primitives and three neutral values for primary mass, secondary mass, and functional or interactive zones.
- L3 may add named material zones but no finish detail that hides unresolved geometry.
- Level blockouts use stable semantic colors only when they encode function, such as traversal, hazard, cover, objective, or inaccessible space.

Do not add textures, decorative wear, cinematic lighting, particles, expressive rendering, or costume detail to make a weak shape feel successful. Do not let candidates change pose, camera, content, and silhouette thesis simultaneously.

For each candidate, create a record from `assets/CANDIDATE_RECORD.md` containing:

- thumbnail or model path and exact generation or construction method, including tool/model version, settings, seed when exposed, reference roles, and any mask or background normalization;
- one-sentence shape thesis and intended player read;
- dimensions, proportions, primitive breakdown, negative spaces, and center of mass;
- gameplay function, interaction zones, collision, clearances, and camera behavior;
- animation, deformation, pivot, socket, and modularity implications;
- invariants, allowed variations, unresolved risks, and rejection conditions.

## Evaluate before refinement

Evaluate candidates at the real camera, expected on-screen size, and representative clutter. For silhouettes, compare solid fills before internal detail. For levels, test by moving through the blockout rather than judging only a plan view.

Score with evidence:

- gameplay recognition and role clarity: 25%;
- functional and spatial fit: 20%;
- distinctive outer shape and negative space: 15%;
- proportion and scale fit: 15%;
- animation, collision, and interaction viability: 10%;
- production and modularity feasibility: 10%;
- compatibility with locked aesthetic and art style: 5%.

A candidate cannot win if it fails any required footprint, clearance, collision, navigation, camera, or accessibility constraint, or scores below 3/5 for recognition or functional fit. Do not invent a participant count or confidence level; identify expert review, internal playtest, or user study explicitly and label evidence limitations. Record why rejected candidates fail; their failure modes help constrain the final AI prompt.

When visual judgment is close, run a single-variable refinement or make a crude playable/animated test. Do not add surface finish as a tiebreaker.

## Create the AI construction handoff

After selecting a candidate, copy `assets/AI_ASSET_HANDOFF.md`. Treat the blockout as the source geometry/shape contract and the handoff as the source intent contract.

Include:

1. **Target and use:** Deliverable type, gameplay role, engine, camera, viewing distance, scale, and reference-image roles.
2. **Shape contract:** Bounding dimensions, proportions, primary-to-tertiary mass hierarchy, contour landmarks, negative spaces, stance, orientation, and center of mass.
3. **Function contract:** Interaction areas, navigation footprint, collision intent, moving parts, grips, entry points, sockets, pivots, attack or effect origins, and clearance envelopes.
4. **Construction contract:** Orthographic and three-quarter views, primitive decomposition, symmetry, modular seams, topology or sprite-layer needs, deformation zones, material IDs, and naming.
5. **Style constraints:** Only the locked aesthetic and art-style rules that affect construction. Clearly separate required geometry from optional finish.
6. **Technical contract:** Target format, orientation, unit scale, origin, triangle or sprite budget, texture budget, UV and LOD needs, collision naming, and export target where applicable.
7. **Variation contract:** Invariants, safe variation ranges, prohibited changes, and which details the downstream AI may invent.
8. **Acceptance contract:** Side-by-side silhouette, dimension, function, camera, animation, collision, and technical checks with rejection triggers.

Write measurements and relationships, not adjective piles. Replace “large heroic shoulders” with a testable relationship such as “shoulder span is 1.8× pelvis width and remains the widest contour landmark in front and three-quarter views.”

Create separate downstream prompts when useful:

- an ImageGen prompt for a refined concept or turnaround;
- a Blender/modeling prompt for geometry and engine-ready construction;
- an engine implementation prompt for collision, sockets, prefabs, and validation.

Each prompt must name the blockout and handoff paths, state which reference is an edit target versus shape reference, repeat the non-negotiable geometry and function, and forbid invented changes to locked features.

## Validate the downstream result

Compare the produced asset against the blockout before judging polish:

1. Overlay or align front, side, top, and three-quarter views where available.
2. Check bounding dimensions, contour landmarks, negative spaces, footprint, pivots, sockets, and clearances.
3. Test at gameplay camera and expected display size.
4. Run representative animation, interaction, collision, navigation, or modular assembly checks.
5. Verify engine/export budgets and naming.
6. Classify differences as acceptable variation, fixable deviation, or contract failure.

Do not accept a polished asset that breaks the silhouette or gameplay contract. Update the handoff only when the intended design changed; otherwise repair the downstream asset.

## Finish the handoff

Report the prototype mode, question answered, candidate paths, selected ID, rejected directions, score and hard-gate evidence, blockout and AI-handoff paths, downstream prompts created, unresolved assumptions, and the next production action.

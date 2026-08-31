# Blockout method

## Contents

1. Shape language
2. Asset silhouette studies
3. Asset greyboxes
4. Level and encounter greyboxes
5. Modular-kit blockouts
6. Controlled AI generation
7. Comparison tests

## 1. Shape language

Describe form as relationships that can be constructed and checked:

- **Envelope:** Overall width, height, depth, footprint, and occupied volume.
- **Mass hierarchy:** Primary mass readable at distance; secondary masses explain category and function; tertiary masses support interaction or construction.
- **Proportion:** Ratios between masses rather than isolated adjectives.
- **Contour landmarks:** Peaks, steps, tapers, overhangs, appendages, and interruptions that survive a solid fill.
- **Negative space:** Gaps, arches, handles, limb separations, wheel wells, undercuts, and sight windows.
- **Axis and balance:** Dominant direction, symmetry, lean, center of mass, and grounded contact points.
- **Rhythm:** Repetition and spacing of masses or openings.
- **Shape semantics:** Which forms communicate friendly/hostile, agile/heavy, common/elite, safe/hazardous, or active/inactive in this game's established language.

Avoid relying on color, texture, decals, facial detail, or lighting to solve a silhouette problem.

## 2. Asset silhouette studies

Use the pose or state most representative of gameplay, then add stress states only after the base family is comparable. Keep every candidate at the same scale and orientation.

Minimum useful views:

- gameplay-camera view;
- front or functional-facing view;
- side view when depth, stance, reach, or articulation matters;
- top view for footprint, targeting, or navigation-critical assets.

Test silhouettes at three sizes: presentation size, ordinary gameplay size, and the smallest supported readable size. Compare against adjacent classes or interactables so distinctiveness is relational rather than abstract.

## 3. Asset greyboxes

Build in this order:

1. Ground plane, unit reference, world orientation, and bounding box.
2. Primary mass and contact points.
3. Secondary masses that establish class or function.
4. Functional voids, clearances, moving parts, and interaction zones.
5. Pivots, sockets, collision primitives, and animation envelopes.
6. Tertiary construction landmarks only when required by the handoff.

Use semantic names from the beginning. Keep collision and visual proxy objects distinct. Apply transforms and validate unit scale before a 3D handoff.

## 4. Level and encounter greyboxes

Start with metrics, not rooms:

- player capsule and movement speeds;
- jump, step, climb, dodge, attack, and interaction ranges;
- camera height, angle, field of view, zoom, and occlusion behavior;
- corridor, doorway, cover, platform, and encounter clearances;
- navigation and accessibility requirements;
- expected player count, enemy count, objective timing, and sightline lengths.

Create a critical path and alternate routes. Mark spawn, objective, hazard, cover, rest, reveal, gating, and inaccessible volumes. Test traversal time, decision visibility, backtracking, camera collision, navigation, combat spacing, and failure recovery in engine.

A top-down diagram cannot pass a feel-dependent spatial question by itself.

## 5. Modular-kit blockouts

Define the grid, module dimensions, pivot convention, connection faces, inside/outside rules, corner cases, elevation changes, collision policy, and material zones. Prove the kit with at least:

- one ordinary assembly;
- one edge or corner condition;
- one variation that avoids obvious repetition;
- one difficult transition such as slope, doorway, roof, or vertical join;
- one representative performance and lightmap test when applicable.

Avoid unique pieces that conceal a broken kit rule.

## 6. Controlled AI generation

For ImageGen silhouette or massing studies, use one call per distinct candidate. Repeat the full invariant block and change only the shape-thesis block. Use stable IDs in filenames and records, not inside the image. Record exact prompts, reference roles, tool/model version, settings, seed when exposed, and any post-generation mask, crop, scale, or background normalization. Preserve the unmodified output separately from normalized comparison images.

Prompt order:

1. output intent and use case;
2. invariant subject, function, scale, and view;
3. neutral representation contract;
4. candidate-specific shape thesis;
5. negative constraints;
6. output framing and background.

Treat generated counts, orthographic consistency, and exact measurements as hypotheses until checked. Image generation can explore shapes but cannot prove 3D construction, collision, or movement clearances.

For Blender or engine work, construct simple geometry from measurements instead of tracing perspective distortion. Save inspectable source files and export previews separately.

## 7. Comparison tests

Use tests appropriate to the question:

- **Blur test:** Does the primary mass remain recognizable without detail?
- **Solid-fill test:** Does the outer contour communicate the role?
- **Thumbnail test:** Is it distinct at expected gameplay size?
- **Grayscale test:** Are value groups and interactive zones separable?
- **Lineup test:** Is it distinct from adjacent classes at matched scale?
- **Mirror test:** Does accidental asymmetry or directional bias appear?
- **Turntable test:** Does recognition survive changing view angle?
- **Motion-envelope test:** Do limbs, doors, tools, attacks, or effects clear the body and environment?
- **Collision test:** Does the simplified collision match player expectation?
- **Traversal test:** Does the level support intended timing, routes, sightlines, and recovery?
- **Kit test:** Do modules connect across ordinary and difficult cases without unique fixes?

Record observable evidence. “Feels better” is a lead for another test, not a passing result.

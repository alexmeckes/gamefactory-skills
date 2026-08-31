# AI asset handoff — [asset or space]

## Target deliverable

- Deliverable type and format:
- Gameplay role:
- Engine and platform:
- Camera, viewing distance, and expected screen size:
- World orientation, unit scale, and origin:
- Selected blockout and candidate record:

## Reference manifest

| Path | Role: edit target, shape, composition, style, or subject | Must preserve |
|---|---|---|

## Shape contract

- Bounding width × height × depth:
- Footprint:
- Primary-to-secondary mass ratios:
- Contour landmarks by view:
- Required negative spaces:
- Stance, dominant axis, center of mass, and contact points:
- Orthographic and three-quarter view requirements:

## Function contract

- Interaction contract IDs:
- Required semantic hooks supplied to bindings:
- Interactions and access points:
- Visual and collision zones:
- Clearances and motion envelopes:
- Moving/deforming parts:
- Pivots, sockets, grips, entries, and effect origins:
- Navigation or encounter behavior:

## Construction contract

- Primitive decomposition:
- Symmetry and allowed asymmetry:
- Modular seams and connection rules:
- Topology, deformation, or sprite-layer requirements:
- Material ID zones:
- Naming and hierarchy:

## Style contract

- Locked aesthetic rules that affect form:
- Locked art-style rules that affect construction:
- Required geometry versus optional finish:
- Anti-anchors and prohibited motifs:

## Technical contract

- Target triangle, sprite, or module budget:
- Coordinate system, forward/up axes, handedness, and unit assumption:
- UV and texture requirements:
- LOD requirements:
- Collision representation and naming:
- Export format and engine target:
- Performance constraints:

## Variation contract

### Invariants

-

### Safe variation ranges

-

### AI may invent

-

### AI must not change or add

-

## Downstream prompts

### Refined concept or turnaround prompt

State the reference roles, geometry invariants, view contract, allowed finish, and prohibited changes.

### 3D or 2D production prompt

State dimensions, mass breakdown, topology/layering, pivots, sockets, materials, budgets, naming, and export requirements.

### Engine implementation prompt

State import settings, prefab or scene hierarchy, collision, sockets, interaction zones, validation scene, and tests.

## Acceptance matrix

| ID | Observable check | Method and threshold | Result |
|---|---|---|---|
| A-01 | Bounding dimensions | | Not tested |
| A-02 | Silhouette landmarks | | Not tested |
| A-03 | Gameplay-size recognition | | Not tested |
| A-04 | Collision and clearances | | Not tested |
| A-05 | Animation or modular behavior | | Not tested |
| A-06 | Technical/export contract | | Not tested |

## Rejection triggers

- Any locked mass, contour landmark, opening, footprint, pivot, socket, or clearance changes without approval.
- Surface detail hides or compensates for an unresolved shape failure.
- The result passes as an image but cannot satisfy the required view, animation, collision, modular, or engine checks.

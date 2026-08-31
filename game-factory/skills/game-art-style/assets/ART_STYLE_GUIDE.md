# {{GAME_TITLE}} — Art Style Guide

> Status: Selected
> Art owner: {{OWNER}}
> Last updated: {{YYYY-MM-DD}}
> Aesthetic source: {{AESTHETIC_DIRECTION_PATH}}
> Selected production style: {{CANDIDATE_ID_AND_NAME}}

## Production thesis

{{ONE_PARAGRAPH_EXPLAINING_HOW_THE_LOCKED_AESTHETIC_BECOMES_GAME_ASSETS}}

## Aesthetic invariants

| Upstream aesthetic rule | Production implementation | Validation evidence |
|---|---|---|
| {{AESTHETIC_RULE}} | {{IMPLEMENTATION}} | {{TEST_OR_REFERENCE}} |

## Representation and pipeline

- Representation method: {{PIXEL_SPRITE_CUTOUT_2D_3D_HYBRID_OR_OTHER}}
- Authoring tools and source formats: {{TOOLS_AND_FORMATS}}
- Export and delivery formats: {{FORMATS}}
- Engine/import treatment: {{PIPELINE}}
- Reuse, modularity, and variant strategy: {{RULES}}
- Generated-reference cleanup and human review: {{RULES}}
- Cheap fallback that preserves the aesthetic: {{FALLBACK}}

## Shape, proportion, and silhouette

- Primary/secondary/accent shape implementation: {{RULES}}
- Character proportions: {{RATIOS_AND_RANGES}}
- Environment and prop proportions: {{RULES}}
- Silhouette targets by distance/tier: {{TARGETS}}
- Avoid: {{ANTI_RULES}}

## Line, edge, value, and palette implementation

- Line and contour rules: {{WIDTH_COLOR_BREAK_RULES}}
- Edge behavior: {{HARD_SOFT_BROKEN_PIXEL_OR_OTHER}}
- Value groups and focal contrast: {{RULES}}
- Production palette/swatches and roles: {{RULES}}
- State colors and non-color alternatives: {{RULES}}
- Low-light and dense-scene behavior: {{RULES}}
- Avoid: {{ANTI_RULES}}

## Materials, texture, lighting, and post

- Material/shader families: {{RULES}}
- Texture frequency, wear, and detail hierarchy: {{RULES}}
- Light and shadow implementation: {{RULES}}
- Fog, rim, emissive, outline, and post effects: {{BOUNDS}}
- Platform/performance fallback: {{SIMPLIFIED_RULE}}
- Avoid: {{ANTI_RULES}}

## Camera, composition, UI, and VFX

- Gameplay camera and framing: {{RULES}}
- Minimum screen sizes and overlap rules: {{TARGETS}}
- Navigation, interaction, danger, and selection hierarchy: {{RULES}}
- HUD/subtitle integration: {{RULES}}
- VFX density and priority: {{RULES}}
- Accessibility validation: {{TESTS}}
- Key-art differences from gameplay: {{ALLOWED_DIFFERENCES}}

## Animation and motion

- Animation method: {{METHOD}}
- Pose language and exaggeration: {{RULES}}
- Timing, spacing, and frame/rate behavior: {{RULES}}
- Deformation and secondary motion: {{RULES}}
- Transition, damage, restored, and other state rules: {{RULES}}
- Motion-readability test: {{TEST}}

## Asset tiers and budgets

| Tier/family | Must preserve | Allowed simplification | Time target | Technical budget | Acceptance test |
|---|---|---|---|---|---|
| Hero/signature | {{RULES}} | {{SIMPLIFICATION}} | {{TIME}} | {{BUDGET}} | {{TEST}} |
| Standard | {{RULES}} | {{SIMPLIFICATION}} | {{TIME}} | {{BUDGET}} | {{TEST}} |
| Background | {{RULES}} | {{SIMPLIFICATION}} | {{TIME}} | {{BUDGET}} | {{TEST}} |
| High-volume/common | {{RULES}} | {{SIMPLIFICATION}} | {{TIME}} | {{BUDGET}} | {{TEST}} |
| VFX/UI | {{RULES}} | {{SIMPLIFICATION}} | {{TIME}} | {{BUDGET}} | {{TEST}} |

## Production anchors and anti-anchors

- Positive production anchors: {{PATHS_AND_REASONS}}
- Anti-anchors: {{PATHS_AND_REASONS}}
- Production-spike source and build: {{PATHS}}
- Exact retained prompts: {{PATH_OR_APPENDIX}}
- Reference-image roles: {{AESTHETIC_STYLE_COMPOSITION_SUBJECT_OR_OTHER}}

## Do and don't

| Do | Why | Don't | Failure caused |
|---|---|---|---|
| {{POSITIVE_RULE}} | {{RATIONALE}} | {{ANTI_RULE}} | {{FAILURE_MODE}} |

## Future ImageGen production block

```text
Use case: stylized-concept
Asset type: {{GAME_ASSET_TYPE}}
Primary request: {{SUBJECT_AND_ACTION}}
Input images: {{AESTHETIC_AND_PRODUCTION_ANCHOR_ROLES}}
Scene/backdrop: {{ENVIRONMENT}}
Aesthetic invariants: {{LOCKED_UPSTREAM_RULES}}
Production style/medium: {{PROPERTY_BASED_IMPLEMENTATION}}
Composition/framing: {{GAME_CAMERA_OR_TEST_VIEW}}
Lighting/materials: {{IMPLEMENTATION_RULES}}
Constraints: preserve {{INVARIANTS}}; no logos; no watermark; no unintended text
Avoid: {{ANTI_ANCHORS_AND_DRIFT}}
```

## Validation and change control

- Target-size and dense-gameplay test: {{METHOD}}
- Value/color-independent test: {{METHOD}}
- Motion and transition test: {{METHOD}}
- Asset-tier consistency test: {{METHOD}}
- Runtime/performance test: {{METHOD}}
- A change requires: {{OWNER_EVIDENCE_AND_AFFECTED_ASSET_REVIEW}}

## Open risks and decisions

| ID | Type | Statement | Impact | Resolution criterion |
|---|---|---|---|---|
| A-001 | Assumption | {{ASSUMPTION}} | {{IMPACT}} | {{EVIDENCE_NEEDED}} |

# {{GAME_TITLE}} — Vertical Slice Specification

> Status: Draft
> Owner: {{OWNER}}
> Last updated: {{YYYY-MM-DD}}
> Target milestone: {{MILESTONE}}

## Slice promise

{{WHAT_REPRESENTATIVE_PART_OF_THE_FINAL_EXPERIENCE_THIS_SLICE_PROVES}}

## Audience, platform, and constraints

- Target player: {{AUDIENCE}}
- Platform and input: {{PLATFORM_AND_INPUT}}
- Target playtime: {{SLICE_DURATION}}
- Performance target: {{FRAME_RATE_RESOLUTION_MEMORY_OR_LOAD_TARGETS}}
- Production constraints: {{ENGINE_TEAM_TIME_OR_PIPELINE_CONSTRAINTS}}

## Player fantasy and design pillars

1. **P1 — {{PILLAR}}:** {{TRADEOFF_RULE}}
2. **P2 — {{PILLAR}}:** {{TRADEOFF_RULE}}
3. **P3 — {{PILLAR}}:** {{TRADEOFF_RULE}}

## Core and slice loops

### Core loop

1. {{ACTION}}
2. {{SYSTEM_RESPONSE}}
3. {{REWARD_OR_DECISION}}
4. {{REPEAT}}

### Slice flow

| Phase | Player goal | Required systems | Exit condition |
|---|---|---|---|
| {{PHASE}} | {{GOAL}} | {{SYSTEM_IDS}} | {{OBSERVABLE_CONDITION}} |

## System requirements

### {{SYSTEM_ID}} — {{SYSTEM_NAME}}

- Player intent: {{PURPOSE}}
- Preconditions: {{VALID_STATE}}
- Inputs and triggers: {{INPUTS}}
- Rules and state transitions: {{ORDERED_BEHAVIOR}}
- Outputs: {{GAME_STATE_CHANGES}}
- Initial tuning: {{VALUES_OR_RANGES}}
- Failure and recovery: {{FAILURE_BEHAVIOR}}
- Edge cases: {{BOUNDARIES_AND_INTERRUPTS}}
- Feedback: {{VISUAL_AUDIO_HAPTIC_UI}}
- Dependencies: {{SYSTEMS_CONTENT_OR_TOOLS}}
- Accessibility: {{ALTERNATE_INPUT_OR_PERCEPTION_PATHS}}
- Acceptance: {{OBSERVABLE_TEST}}
- Supports: {{PILLAR_OR_LOOP}}

## Content and fidelity budget

| Category | Must count | Target fidelity | Reuse or cut strategy |
|---|---:|---|---|
| {{CATEGORY}} | {{COUNT}} | {{QUALITY_BAR}} | {{FALLBACK}} |

## UX, onboarding, and accessibility

- Entry and setup: {{START_FLOW}}
- Critical screen flow: {{SCREENS_AND_TRANSITIONS}}
- Teaching sequence: {{HOW_ACTIONS_ARE_LEARNED}}
- Failure and recovery: {{PLAYER_RECOVERY_PATH}}
- Settings and accessibility: {{SLICE_REQUIREMENTS}}

## Cross-discipline acceptance

| Discipline | Deliverable | Acceptance evidence |
|---|---|---|
| Design | {{RULES_TUNING_CONTENT}} | {{TEST_OR_REVIEW}} |
| Engineering | {{FUNCTIONAL_SYSTEM}} | {{TEST_OR_PROFILE}} |
| Art/Animation | {{ASSET_SET}} | {{IN_BUILD_REVIEW}} |
| Audio | {{EVENT_SET}} | {{IN_BUILD_REVIEW}} |
| UX/Writing | {{FLOW_OR_COPY}} | {{USABILITY_OR_REVIEW}} |
| QA | {{TEST_COVERAGE}} | {{PASS_CRITERIA}} |

## Scope

### Must

- {{SLICE_COMMITMENT}}

### Should

- {{VALUABLE_IF_CAPACITY_ALLOWS}}

### Out

- {{EXPLICIT_EXCLUSION}}

## Risks, assumptions, and decisions

| ID | Type | Statement | Impact | Resolution or mitigation |
|---|---|---|---|---|
| D-001 | Assumption | {{ASSUMPTION}} | {{IMPACT}} | {{EVIDENCE_OR_ACTION}} |

## Milestone exit criteria

- {{PLAYABLE_END_TO_END_CONDITION}}
- {{EXPERIENCE_VALIDATION_CONDITION}}
- {{PERFORMANCE_OR_STABILITY_CONDITION}}
- {{CONTENT_AND_FIDELITY_CONDITION}}

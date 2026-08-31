# {{GAME_TITLE}} — Systems Specification

## System map

| ID | System | Player purpose | Depends on | Supports | Status |
|---|---|---|---|---|---|
| {{SYSTEM_ID}} | {{NAME}} | {{PURPOSE}} | {{DEPENDENCIES}} | {{PILLAR_OR_LOOP}} | Proposed |

## Requirements

### {{SYSTEM_ID}} — {{SYSTEM_NAME}}

- Status: {{CONFIRMED_INITIAL_TUNING_EXPERIMENT_OR_ASSUMPTION}}
- Player intent: {{WHY_THE_PLAYER_USES_OR_ENCOUNTERS_IT}}
- Preconditions: {{VALID_START_STATE}}
- Inputs and triggers: {{WHAT_STARTS_IT}}
- Rules and state transitions: {{ORDERED_OBSERVABLE_BEHAVIOR}}
- Outputs: {{GAME_STATE_CHANGES}}
- Initial tuning: {{VALUES_OR_RANGES}}
- Resources and economy: {{SOURCES_SINKS_COSTS_CAPS}}
- Feedback: {{VISUAL_AUDIO_HAPTIC_UI}}
- Failure and recovery: {{WHAT_FAILS_AND_WHAT_HAPPENS_NEXT}}
- Edge cases: {{BOUNDARIES_INTERRUPTS_AND_CONFLICTS}}
- Dependencies: {{SYSTEMS_CONTENT_TOOLS_OR_PLATFORM_FEATURES}}
- Telemetry: {{EVENTS_PARAMETERS_AND_VALIDATION_PURPOSE}}
- Accessibility: {{ALTERNATE_INPUT_PERCEPTION_OR_TIMING_PATHS}}
- Acceptance criteria: {{OBSERVABLE_TESTS_WITH_CONDITIONS}}
- Traceability: {{PILLAR_LOOP_OR_REQUIREMENT}}

## Shared tuning glossary

| Parameter | Meaning and unit | Initial value/range | Affected requirements | Validation method |
|---|---|---|---|---|
| {{PARAMETER}} | {{DEFINITION}} | {{VALUE_OR_RANGE}} | {{SYSTEM_IDS}} | {{TEST_OR_TELEMETRY}} |

## Cross-system rules

{{PRIORITY_CANCELLATION_PERSISTENCE_DETERMINISM_OR_CONFLICT_RULES}}

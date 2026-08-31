# {{GAME_TITLE}} — Production Scope

## Product and technical constraints

- Engine and version: {{ENGINE}}
- Target platforms: {{PLATFORMS}}
- Input devices: {{INPUTS}}
- Frame rate and resolution: {{TARGETS}}
- Memory, package, and loading budgets: {{BUDGETS}}
- Connectivity and service assumptions: {{NETWORK_OR_NONE}}
- Team, schedule, tools, and pipeline constraints: {{CONSTRAINTS}}

## Milestone scope

| Feature or deliverable | Prototype | Vertical slice | MVP | Release | Owner | Dependencies |
|---|---|---|---|---|---|---|
| {{DELIVERABLE}} | Must | Must | Must | Must | {{OWNER_OR_UNKNOWN}} | {{DEPENDENCIES}} |

## Current milestone: {{MILESTONE}}

### Must

- {{COMMITTED_DELIVERABLE_WITH_ACCEPTANCE_LINK}}

### Should

- {{VALUABLE_IF_CAPACITY_ALLOWS}}

### Could

- {{OPTIONAL_DELIVERABLE}}

### Out

- {{EXPLICIT_EXCLUSION}}

## Performance and quality budgets

| Budget | Target | Worst acceptable | Test scene/device | Evidence |
|---|---|---|---|---|
| {{FRAME_TIME_MEMORY_LOAD_PACKAGE_OR_OTHER}} | {{TARGET}} | {{LIMIT}} | {{ENVIRONMENT}} | {{PROFILE_OR_TEST}} |

## Dependencies and risks

| ID | Type | Description | Probability | Impact | Mitigation or fallback | Trigger |
|---|---|---|---|---|---|---|
| R-001 | Risk | {{RISK}} | {{LOW_MEDIUM_HIGH}} | {{IMPACT}} | {{ACTION_OR_CUT}} | {{OBSERVABLE_SIGNAL}} |

## Milestone exit criteria

- Player experience: {{PLAYTEST_EVIDENCE}}
- Functionality: {{REQUIREMENT_OR_TEST_EVIDENCE}}
- Content: {{COUNT_AND_FIDELITY_EVIDENCE}}
- Performance: {{PROFILE_EVIDENCE}}
- Stability: {{DEFECT_OR_SESSION_EVIDENCE}}
- Production: {{DEPENDENCY_AND_SCOPE_EVIDENCE}}

## Cut order

1. {{FIRST_CUT_THAT_PRESERVES_THE_CORE_PROMISE}}
2. {{SECOND_CUT}}
3. {{LAST_RESORT_SCOPE_CHANGE}}

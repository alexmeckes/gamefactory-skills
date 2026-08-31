# Interaction model

## Contents

1. Contract boundaries
2. Participant capabilities
3. State and transition semantics
4. Timing and interruption
5. Effects and rollback
6. Feedback and bindings
7. Traceability and evolution
8. Flow vocabulary
9. Persistence contract

## 1. Contract boundaries

Center each contract on one player- or system-meaningful verb. The contract begins when eligibility can be evaluated and ends when its outcome and cleanup are stable.

Split a contract when a sub-behavior:

- is reused by another interaction;
- can be initiated, cancelled, retried, or failed independently;
- has a different authority or persistence boundary;
- has separate ownership or acceptance criteria;
- remains meaningful outside the parent flow.

Do not split animation beats or internal implementation calls that have no independent gameplay meaning.

## 2. Participant capabilities

Name roles by meaning, not concrete objects. A participant specifies:

- category: actor, target, tool, station, environment, observer, authority, or service;
- required capabilities or interfaces;
- cardinality and ownership;
- whether it may disappear or change eligibility during the interaction.

Bindings resolve roles to scene or runtime objects. Reusable contracts should not depend on prefab paths, skeleton bone names, or specific UI widgets.

## 3. State and transition semantics

Use states that matter to rules, feedback, authority, save/load, or interruption. Require exactly one initial state. Mark terminal outcomes or make their outgoing behavior explicit.

Every transition should answer:

- What event requests it?
- Which guards approve or block it?
- Who has authority to commit it?
- Does it reserve or consume anything?
- How long does it take, and which tuning value controls that?
- Can it be interrupted or cancelled, and where does it go?
- Which rule effects and feedback occur on entry, during, on exit, and on failure?

Avoid hidden transitions described only in prose.

## 4. Timing and interruption

Separate hard sequencing from initial tuning. Express windows and durations with named tuning keys when designers should adjust them.

Define behavior for:

- repeated input and input buffering;
- simultaneous requests and exclusivity;
- cancellation by player choice;
- interruption by damage, movement, authority loss, or target invalidation;
- timeout and stalled dependencies;
- pause, slow motion, and variable frame rate;
- late network response or reconciliation where relevant.

An interruptible transition must name a destination and cleanup. “Can cancel” is incomplete.

## 5. Effects and rollback

Classify effects as reserve, commit, release, spawn, destroy, transfer, modify, reveal, notify, or schedule. State when each effect becomes authoritative.

For currency, inventory, ownership, quest state, cooldowns, consumables, or scarce world objects, specify:

- idempotency or duplicate-request handling;
- rollback on cancel, failure, disconnect, or load;
- partial-commit policy;
- atomicity across participants;
- source of truth.

## 6. Feedback and bindings

The contract defines what players must perceive; bindings define how a context realizes it. Associate feedback with states or transitions, including blocked and recovery cases.

Specify redundant channels when critical information cannot rely on color, hearing, fine motor timing, text, or haptics alone. Record subtitle, remapping, hold/toggle, timing-window, reduced-motion, and camera-control implications where relevant.

Do not make animation completion the sole gameplay authority unless the architecture explicitly requires and tests it.

## 7. Traceability and evolution

Trace contracts to:

- design pillars and requirement IDs;
- visual blockouts and semantic hooks;
- flows and context bindings;
- code interfaces or systems, without turning design into architecture;
- automated and playtest evidence;
- telemetry events and privacy classification;
- dependent contracts.

Version when a change can alter callers, flows, bindings, save data, network messages, analytics interpretation, or acceptance results. Tuning within a declared safe range may avoid a version change; record the tuning change in project history.

## 8. Flow vocabulary

Use only these node types unless the project formally extends the schema:

- `entry`: the single flow entry;
- `interaction`: invokes one contract and emits its named outcome;
- `decision`: evaluates a named rule and emits `choice.<name>`;
- `wait`: waits for `event.<name>` or a timeout;
- `prompt`: presents tutorial or guidance UI and emits `prompt.dismissed`, `prompt.completed`, or `timed_out`;
- `exit`: terminates with a named flow outcome.

Use standard edge events `entered`, `succeeded`, `failed`, `blocked`, `cancelled`, `interrupted`, `invalidated`, and `timed_out`. Namespace custom events as `choice.<name>`, `event.<name>`, `condition.<name>`, or `prompt.<name>`. Do not use prose sentences as event identifiers.

## 9. Persistence contract

When `save_policy` is not `none`, define:

- persistence schema version and every saved field's key, owner role, type, and commit point;
- whether an in-progress interaction restarts, resumes, rolls back, or loads as a terminal outcome;
- target-missing, participant-mismatch, reserved-resource, and contract-version conflict behavior;
- migration policy for renamed fields, removed states, and breaking contract versions;
- authority for resolving conflicts and whether resolution is deterministic;
- acceptance coverage for save/load at every allowed checkpoint.

Do not serialize transient animation state as behavioral authority unless the contract explicitly depends on it.

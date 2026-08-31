---
name: game-interaction-contracts
description: Create, revise, index, validate, and reconcile structured game-interaction metadata for player actions, abilities, combat, traversal, interactive props, conversations, transactions, puzzles, quests, AI reactions, scripted sequences, and multiplayer behaviors. Use when Codex needs to specify behavior that spans multiple assets or systems; model participants, triggers, preconditions, state transitions, timing, interruption, effects, failure and recovery, feedback, spatial requirements, animation/UI/audio/VFX bindings, accessibility, persistence, networking, telemetry, or acceptance tests; connect greyboxes and production assets to gameplay verbs; compose atomic interactions into flows; or compare design intent with implementation and test evidence.
---

# Game Interaction Contracts

Describe behavior around verbs and state changes rather than burying it in asset notes. Keep reusable rules, scene-specific bindings, and multi-step flows separate so each can change without duplicating the others.

## Game Factory relationship

- **Consumes:** `$game-design-spec` requirement IDs, player intent, system rules, and implementation evidence.
- **Produces:** Reusable contracts, composed flows, scene bindings, semantic hooks, and behavioral acceptance cases.
- **Hands off to:** `$game-visual-blockout` for volumes, sockets, clearances, and motion envelopes; engineering, UX, and QA for implementation and verification.
- **Boundary:** Own dynamic behavior, not asset geometry, aesthetic meaning, or production rendering. Reference those sources by ID or path.

## Choose the record type

- **Interaction contract:** One reusable verb or exchange with a clear initiator, outcome, and interruption boundary. Examples: open door, appraise item, dodge, purchase stock, begin dialogue, revive ally.
- **Interaction flow:** A graph that composes contracts and decision points into a longer experience. Examples: tutorial sale, lockpicking sequence, boss phase, checkout journey, quest hand-in.
- **Interaction binding:** A context-specific mapping from contract roles and semantic hooks to scene instances, prefabs, sockets, volumes, animations, UI, audio, VFX, camera, or input actions.
- **Interaction index:** The registry of IDs, paths, ownership, maturity, and dependency relationships.

Split a behavior when a substep has its own eligibility, cancellation, reuse, ownership, or acceptance criteria. Keep it atomic when splitting would create bookkeeping without an independently meaningful state change.

## Establish identity and maturity

Use stable, namespaced kebab-case IDs such as `shop.appraise-cursed-item`. Never encode a scene instance, implementation class, or tuning number in the contract ID. Increment `version` when a behavioral change affects consumers or tests; preserve old decision history through version control rather than creating near-duplicate IDs.

Select maturity deliberately:

- **Concept:** Player intent, participants, trigger, state path, outcome, major failures, and experience-level acceptance.
- **Prototype:** Explicit rules, initial timing, interruption, spatial constraints, observable feedback, tuning variables, and test cases.
- **Implementation:** Complete bindings/interfaces, persistence and authority behavior, edge cases, accessibility, deterministic acceptance criteria, and resolved dependencies.
- **Shipping:** Representative validation evidence, telemetry/privacy treatment, localization/platform concerns, and known residual risks.

Do not mark a contract more mature because it is verbose. Maturity reflects resolved decisions and evidence.

## Author an interaction contract

Copy `assets/INTERACTION_CONTRACT.yaml`. Read `references/interaction-model.md` before specifying a multi-system interaction, revising an implemented behavior, or deciding contract boundaries.

1. **State player intent.** Separate the player's goal from the design purpose and implementation.
2. **Assign participant roles.** Define semantic capabilities such as `carrier`, `target_item`, or `appraisal_station`; do not hardwire asset filenames into reusable rules.
3. **Define eligibility and trigger.** Record input or AI event, range, facing, line of sight, authority, resources, ownership, concurrency, and other guards.
4. **Model states and transitions.** Name one initial state. For every transition, specify event, guards, timing, interruptibility, cancellation or timeout destination, and effects.
5. **Cover outcomes.** Define success, blocked, cancelled, interrupted, timeout, invalidated, and partial-completion behavior where relevant. Every consumed or reserved resource needs rollback semantics.
6. **Specify feedback.** Map state changes to visual, audio, UI, haptic, camera, animation, and world feedback. Do not rely on color alone or hide a required rule exclusively in presentation.
7. **Expose cross-cutting behavior.** Address save/load, multiplayer authority and reconciliation, AI use, accessibility, localization, telemetry/privacy, and platform/input differences when they can change the contract.
8. **Write acceptance scenarios.** Use stable IDs and `given/when/then` statements, including failure and recovery paths. Distinguish initial tuning from hard rules.

Use Mermaid only when a state or flow graph has enough branches that prose obscures it. The structured record remains the source of truth.

## Compose flows and bindings

Copy `assets/INTERACTION_FLOW.yaml` when sequencing contracts. Flow nodes reference contract IDs and named outcomes; they do not restate atomic rules. Define entry, exit, branch, retry, skip, rollback, save-resume, and abandonment behavior as relevant.

Copy `assets/INTERACTION_BINDING.yaml` for each context that realizes a contract. Bind semantic roles and hooks to concrete objects, volumes, sockets, animation states, prefabs, UI, audio, VFX, cameras, and input actions. A binding may narrow optional presentation or tuning within declared ranges, but it cannot silently change a contract rule.

Link visual blockouts by ID:

```yaml
related_blockouts:
  - id: appraisal-table.B03
    role: shape-and-spatial-contract
    provides: [item_socket, use_zone]
```

The blockout records `supports_interactions: [shop.appraise-cursed-item]`; the interaction contract records required semantic hooks; the binding connects those hooks to an actual scene or prefab.

## Maintain traceability

Use this layout unless the project already has an equivalent convention:

```text
design/interactions/
├── interaction-index.yaml
├── contracts/       # *.interaction.yaml
├── flows/           # *.flow.yaml
├── bindings/        # *.binding.yaml
└── evidence/        # playtest, test, trace, or profiling references
```

Copy `assets/INTERACTION_INDEX.yaml` for the registry. Record design requirements, assets/blockouts, code owners or system interfaces, tests, telemetry, and dependent flows by ID or path. Reference instead of copying. When a linked artifact changes, identify affected contracts and decide whether the change is compatible, needs a new contract version, or reveals an implementation defect.

When code and contract disagree, classify the mismatch:

- **Contract changed:** Update metadata, affected bindings/flows/tests, and version when consumers are impacted.
- **Implementation defect:** Preserve the contract and create a concrete discrepancy.
- **Binding drift:** Preserve reusable rules and repair the context-specific mapping.
- **Undecided:** Record both behaviors, player impact, owner, experiment, and decision threshold.

## Apply domain checks

Read `references/domain-checklists.md` only for the relevant interaction family. Use its combat, traversal, inventory/economy, dialogue/quest, AI, and multiplayer questions to expose missing behavior without adding irrelevant empty sections.

## Validate

Validate structural integrity and cross-references after creating or materially revising records:

```bash
python3 scripts/validate_interactions.py design/interactions
```

The validator supports JSON with the standard library. YAML requires PyYAML; if it is unavailable and dependency installation is not authorized, save canonical records as JSON instead of skipping validation. Use `--strict` before an implementation or milestone handoff.

Validation cannot prove that timing feels right or feedback communicates well. Run representative gameplay, interruption, save/load, accessibility, and multiplayer tests according to the contract.

## Finish the handoff

Report created or changed contract, flow, binding, and index paths; IDs and maturity; important decisions and initial tuning; linked blockouts/assets/code/tests; unresolved assumptions; compatibility or versioning impact; validator results; and the next implementation or playtest action.

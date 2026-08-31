# Game studio agent roster

Choose roles for the decision at hand. Each role must receive a bounded evidence packet and return the response contract from `SKILL.md`.

## Direction and definition

### Creative director

- **Purpose:** Resolve cross-discipline conflicts and protect the game's identity.
- **Use when:** Two or more disciplines recommend incompatible directions, or the next milestone needs a unifying thesis.
- **Inputs:** Pillars, player fantasy, accepted decisions, specialist reports, constraints, and build evidence.
- **Output:** One decision, rationale, explicit sacrifices, and the next milestone.
- **Authority:** Advisory. The orchestrator records the final decision.
- **Avoid:** Generating the first draft of every artifact or rubber-stamping consensus.

### Game design lead

- **Purpose:** Turn the fantasy into loops, systems, rules, tuning hypotheses, and acceptance criteria.
- **Use when:** Framing a concept, mechanic, prototype, progression system, or design discrepancy.
- **Inputs:** Concept sources, pillars, current mechanics, platform/input constraints, and playtest findings.
- **Output:** A buildable design recommendation with edge cases and a validation plan.
- **Authority:** Advisory unless assigned a design-document path.
- **Skill:** Apply `$game-design-spec`; apply `$game-interaction-contracts` when behavior spans participants, state transitions, or system boundaries.

### Player advocate

- **Purpose:** Represent comprehension, motivation, emotional experience, learning burden, and likely player behavior.
- **Use when:** A choice changes onboarding, feedback, difficulty, pacing, retention, audience fit, or fantasy fulfillment.
- **Inputs:** Target-player hypothesis, user flow, mechanic proposal, playtest evidence, and accessibility constraints.
- **Output:** Player-facing failure modes, priority issues, and a testable improvement.
- **Authority:** Read-only advisory.
- **Avoid:** Treating personal taste as user research.

### Scope producer

- **Purpose:** Bound the work and expose dependencies, schedule risk, content multipliers, and irreversible commitments.
- **Use when:** Selecting MVP scope, milestone content, feature cuts, or a recovery plan.
- **Inputs:** Candidate scope, team/tool constraints, dependencies, unknowns, and exit criteria.
- **Output:** Must/should/could/out scope, critical path, risk register, and recommended cut order.
- **Authority:** Read-only advisory.

## Visual direction

### Aesthetic director

- **Purpose:** Define what the world should feel like—tone, palette logic, motifs, atmosphere, cultural and era cues, and emotional range.
- **Use when:** The concept is coherent but the game's broader aesthetic territory is not locked.
- **Inputs:** Design pillars, narrative premise, audience, references, and tone boundaries.
- **Output:** Distinct aesthetic territories, comparison evidence, and a locked direction or next ImageGen experiment.
- **Authority:** Advisory unless assigned aesthetic-document or concept-art paths.
- **Skill:** Apply `$game-aesthetic` and `$imagegen` when generating images.

### Art style director

- **Purpose:** Translate locked aesthetic intent into a repeatable production visual system.
- **Use when:** Choosing 2D/3D medium, stylization, shape language, materials, rendering treatment, camera behavior, animation language, or asset tiers.
- **Inputs:** Locked aesthetic direction, representative gameplay views, platform constraints, and asset-production reality.
- **Output:** Comparable production-style candidates, a selected style, visual rules, anti-rules, and an asset validation set.
- **Authority:** Advisory unless assigned art-style documents or generated-image paths.
- **Skill:** Apply `$game-art-style` and `$imagegen`; use `$game-visual-blockout` when the decision depends on shape or massing rather than finish.

## Technology and implementation

### Technical director

- **Purpose:** Select architecture and production pipelines that preserve the design within platform, performance, and team constraints.
- **Use when:** A decision affects engine structure, rendering, asset pipelines, save/network models, tooling, or technical risk.
- **Inputs:** Design requirements, art constraints, repository architecture, platform targets, and measured bottlenecks.
- **Output:** Technical recommendation, alternatives, interfaces, risks, and a spike or verification plan.
- **Authority:** Read-only advisory unless assigned a narrowly scoped technical document or spike.
- **Avoid:** Replacing design requirements with preferred technology.

### Gameplay engineer

- **Purpose:** Implement and verify player-facing mechanics and supporting systems.
- **Use when:** A design contract is ready to build or a gameplay defect is confirmed.
- **Inputs:** Requirement IDs, owned paths, code conventions, tests, and acceptance criteria.
- **Output:** Working implementation, focused tests, verification evidence, and known limitations.
- **Authority:** Write-enabled only for named paths. Usually the sole writer in its batch.

### Content and level designer

- **Purpose:** Turn systems and aesthetic rules into representative encounters, levels, pacing, and reusable content patterns.
- **Use when:** The core loop exists and the milestone needs playable content or a vertical slice.
- **Inputs:** Mechanics, pacing targets, art rules, content budgets, editor/tool capabilities, and telemetry needs.
- **Output:** Content plan or implemented owned content, play path, tuning variables, and validation scenarios.
- **Authority:** Advisory by default; write-enabled only for named content paths.
- **Skill:** Apply `$game-visual-blockout` for spatial footprint, level greybox, encounter-flow, or modular-kit evidence.

### UX and accessibility lead

- **Purpose:** Make controls, information, flows, feedback, and recovery understandable and adaptable.
- **Use when:** Building onboarding, HUD, menus, settings, input, failure recovery, or interaction feedback.
- **Inputs:** Target platforms and inputs, player journey, screen flows, mechanic states, and accessibility goals.
- **Output:** Prioritized usability issues, accessible interaction contract, and acceptance tests.
- **Authority:** Read-only advisory unless assigned UI document or implementation paths.
- **Skill:** Apply `$game-interaction-contracts` when feedback, cancellation, input, accessibility, or failure recovery changes interaction behavior.

## Validation and release

### QA and test lead

- **Purpose:** Convert milestone promises into risk-based functional, systemic, and playtest coverage.
- **Use when:** A prototype, integration, vertical slice, or release candidate needs verification.
- **Inputs:** Acceptance criteria, changed behavior, diffs, build instructions, telemetry, and known risks.
- **Output:** Test matrix, reproduced failures, severity, evidence, and release recommendation.
- **Authority:** Read-only except for explicitly owned test files and reports.

### Performance and platform lead

- **Purpose:** Protect frame time, memory, loading, package size, input/device behavior, and platform compliance.
- **Use when:** The milestone introduces representative content, rendering cost, streaming, platform APIs, or a release target.
- **Inputs:** Platform budgets, profiling evidence, representative scenes, build settings, and technical changes.
- **Output:** Measured risks, budget status, bottleneck hypothesis, and prioritized optimization or compliance work.
- **Authority:** Read-only except for explicitly owned benchmarks or reports.
- **Avoid:** Optimizing without a measurement or representative workload.

### Milestone evaluator

- **Purpose:** Independently judge whether exit criteria are satisfied.
- **Use when:** The orchestrator is considering a gate pass or production commitment.
- **Inputs:** Original acceptance criteria, artifacts, diffs, test/build evidence, and unresolved-risk list.
- **Output:** `Pass`, `Revise`, `Stop`, or `Experiment`, criterion-by-criterion evidence, and the smallest missing work.
- **Authority:** Strictly read-only. Must not repair the work it evaluates.
- **Isolation:** Do not include a preferred verdict, producer pressure, or prior celebratory synthesis.

## Optional specialists

Add narrative, audio, economy, multiplayer/network, live-operations, localization, community, or platform-certification specialists only when the current decision materially depends on that discipline. Give each the same narrow contract and authority rules; do not keep them permanently active.

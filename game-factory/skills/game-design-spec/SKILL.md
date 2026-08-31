---
name: game-design-spec
description: Create, revise, critique, and maintain game design specifications that turn a game concept into scoped, testable requirements for design, engineering, art, audio, UX, and production. Use when Codex needs to write a game design document (GDD), concept brief, prototype brief, vertical-slice specification, mechanics or systems spec, content plan, UX flow, production scope, or design decision log; clarify a game idea; reconcile existing design documents with an implementation; or convert subjective design goals into measurable rules and acceptance criteria.
---

# Game Design Spec

Turn creative intent into a living specification that a team can implement and test. Preserve uncertainty as explicit assumptions or open questions instead of silently inventing settled decisions.

## Game Factory relationship

- **Consumes:** Concepts, research, existing implementation, production constraints, and accepted decisions.
- **Produces:** Pillars, loops, stable requirement IDs, scope boundaries, risks, and milestone acceptance criteria.
- **Hands off to:** `$game-interaction-contracts` for cross-system behavior, `$game-aesthetic` for emotional/world direction, and `$game-visual-blockout` for shape or spatial evidence.
- **Boundary:** Keep detailed state graphs, visual-production rules, and geometry in their owning skills; reference their IDs and paths instead of duplicating them here.

## Choose the design depth

Select the smallest mode that satisfies the request:

- **Concept brief:** Establish the player fantasy, audience, differentiator, pillars, core loop, and scope boundary. Copy `assets/concept-brief.md` when creating a file.
- **Prototype brief:** Define the riskiest design question, the minimum playable experiment, instrumentation, and success or stop criteria. Copy `assets/prototype-spec.md`.
- **Vertical-slice spec:** Define one production-quality, representative slice with locked boundaries and cross-discipline acceptance criteria. Copy `assets/vertical-slice-spec.md`.
- **Production spec:** Maintain the interconnected document set in `assets/production/`. Use this only when the team needs a durable source of truth for implementation and production.

Infer the mode from the user's goal and available artifacts. State the selected mode and any important assumption. Ask a question only when the answer would materially change the document's structure or committed scope; otherwise proceed and label the assumption.

## Build or revise the specification

1. **Inspect the source material.** Read relevant design files, code, issue trackers, build notes, and asset constraints. When revising, preserve useful structure and record meaningful decision changes. Do not overwrite unrelated user content.
2. **Frame the game.** Define the one-sentence concept, player fantasy, target player, platform, input method, session shape, design pillars, and non-goals. Make pillars discriminating enough to resolve later tradeoffs.
3. **Model the loops.** Describe the moment-to-moment loop, session loop, and long-term loop where applicable. Show a Mermaid state or flow diagram only when it makes a multi-step loop or state transition materially clearer.
4. **Specify systems.** For every important mechanic, define player intent, rules, inputs, state, outputs, tuning parameters, edge cases, dependencies, feedback, failure behavior, and acceptance criteria. Use the system contract in `references/design-quality.md`.
5. **Bound the content.** Quantify the MVP or slice: levels, characters, enemies, items, abilities, narrative beats, environments, UI screens, audio needs, and expected playtime. Separate `Must`, `Should`, `Could`, and `Out` scope.
6. **Cover the player journey.** Specify onboarding, controls, screen flow, feedback, failure and recovery, accessibility, saving, difficulty, and return-player experience as relevant.
7. **Expose production reality.** Record platform and performance targets, tool or engine constraints, dependencies, risks, telemetry needs, milestone exit criteria, and ownership when known.
8. **Check traceability.** Each pillar must affect at least one rule or scope choice. Each feature must support a loop or pillar. Each committed system must have testable acceptance criteria. Record unresolved choices in the decision log rather than scattering `TBD` markers.

Use `$game-interaction-contracts` when a mechanic needs structured, reusable metadata across multiple participants, state transitions, assets, scenes, implementation systems, or tests. Keep the design spec as the source of player intent and scope; reference interaction IDs instead of duplicating detailed behavioral rules.

Read `references/design-quality.md` before drafting a production spec, critiquing an existing spec, or translating subjective goals into measurable requirements.

## Write requirements that can be built

Keep desired experience separate from implementation-neutral rules and from suggested implementation. Do not present engine architecture as a design requirement unless a technical constraint makes it necessary.

Replace adjectives with observable behavior. For example, replace “dodging feels responsive” with explicit input buffering, startup, invulnerability, movement, recovery, resource cost, cancellation, feedback, and a playtest criterion. Mark proposed numbers as `Initial tuning` until validated.

Use stable identifiers for requirements in implementation-oriented specs:

```markdown
### COMBAT-DODGE-001 — Ground dodge

- Player intent: Escape a telegraphed attack without breaking combat flow.
- Rule: A valid press queues for up to 100 ms and begins when the current cancellable state ends.
- Initial tuning: 80 ms startup; 180 ms invulnerability; 250 ms recovery; 25 stamina.
- Edge cases: Ignore a second press while queued; reject when stamina is below 25.
- Feedback: Directional animation, short audio cue, and invulnerability flash.
- Acceptance: In a 60 fps test build, a press made within the buffer window starts on the first eligible frame.
- Supports: Pillar P2 — Readable, committed combat.
```

Use exact rules when known. When they are not known, include a bounded experiment, decision owner if known, and resolution criterion.

## Handle existing projects

When code and the design disagree, report the mismatch. Do not silently rewrite the intended design to match accidental implementation behavior. Classify each mismatch as one of:

- **Design changed:** Update the spec and record the decision.
- **Implementation defect:** Preserve the spec and create an actionable discrepancy.
- **Undecided:** Record both behaviors, impact, and the decision needed.

For a critique-only request, do not edit files. Rank findings by their effect on player experience, implementation ambiguity, scope risk, and testability; include a concrete repair for each material finding.

## Validate and hand off

Run the bundled structural checker after creating or materially revising Markdown specs:

```bash
python3 scripts/validate_spec.py <spec-file-or-directory> --mode auto
```

Use `--strict` before a milestone handoff so warnings also fail validation. Treat the checker as a structural aid, not a substitute for design judgment.

Finish with:

- selected design depth and artifact paths;
- assumptions and decisions made;
- unresolved questions that truly block implementation;
- major scope exclusions;
- validation performed and any remaining warnings;
- recommended next design or implementation step.

---
name: game-studio-orchestrator
description: Orchestrate a stage-gated, multi-agent game-development studio using GPT-5.6 Sol with ultra reasoning. Use when Codex needs to assemble and control a specialist game team; coordinate game design, player advocacy, scope, aesthetics, art style, technical direction, gameplay implementation, content, UX, QA, performance, or milestone review; decide which agents should participate in a game milestone; run independent parallel critiques; or synthesize specialist recommendations into one coherent game plan. Use this skill for multi-agent game work, not for a single isolated design or implementation task.
---

# Game Studio Orchestrator

Run a small, stage-appropriate game studio under one accountable orchestrator. Use specialists to expose tradeoffs and produce evidence; do not substitute a committee average for a clear decision.

## Route through Game Factory

Read `references/game-factory-map.md` before selecting skills for a multi-discipline milestone, resolving source-of-truth ownership, or evaluating downstream impact. Use the map's default routing and change-propagation rules; do not invoke every bundled skill by default.

## Establish the studio state

Inspect the game repository, existing design and visual documents, current build evidence, platform constraints, and prior decisions. Copy `assets/STUDIO_STATE.md` when the project lacks a durable studio state.

Record:

- the current milestone and stage gate;
- player fantasy, pillars, audience, platform, and scope ceiling;
- accepted decisions and non-negotiable constraints;
- source-of-truth paths for design, aesthetics, art style, code, builds, and tests;
- the decision that must be made next;
- files or directories that may be changed during this run.

Resolve only the context needed for the current gate. Do not make every specialist reread the whole repository.

## Select the smallest useful council

Read `references/agent-roster.md` and choose only roles whose distinct judgment is needed. Read the current gate in `references/stage-gates.md` before framing the milestone; its default council and required evidence are authoritative. Add a role only when the decision materially depends on that discipline, and record why.

Use the creative director to reconcile a genuinely cross-discipline conflict or establish the next milestone. Do not invoke it as decorative approval on every small task.

Specialists are advisory unless the user-authorized task and their assignment explicitly grant a bounded write scope. By default, only one implementation agent writes at a time. Two agents may write concurrently only when their target paths are disjoint, verified in advance, and integration ownership is explicit. Creating state files, reports, generated images, tests, or dependency files counts as writing.

## Pin and control subagents

Before spawning, inspect live agents and available capacity. Resolve required discipline skills to their installed name or absolute `SKILL.md` path and decide whether each is used as a read-only rubric or a write-enabled workflow. If a required skill is unavailable, report the missing dependency and either obtain approval for a documented downgrade or block that gate.

For each specialist spawn:

1. Set `model` to `gpt-5.6-sol` and `reasoning_effort` to `ultra` explicitly.
2. Use `fork_turns: "none"` for divergent reviewers and evaluators. Use it by default for every other specialist and pass a purpose-built evidence packet. A small positive recent-turn count is permitted only for a dependent implementation handoff after checking that it does not expose a verdict the role must judge independently. Do not use a full-history fork when the spawn interface requires inherited model settings for full-history forks.
3. Build every assignment from `assets/AGENT_ASSIGNMENT.md`. Include one role, one decision, an allowlist of inputs, explicit exclusions, tool and network rules, write authority, sibling-skill mode, and the required response contract. Instructions in the assignment override broader discipline-skill defaults when they are more restrictive.
4. Keep delegation depth at one. Specialists do not spawn further agents unless the user explicitly requests a hierarchy.
5. Batch independent, read-heavy work up to the available capacity while retaining the orchestrator. Freeze their shared input manifest before spawning, queue excess roles, and wait for the complete required batch before comparison. Never run an evaluator concurrently with writers.
6. If the requested model or effort is unavailable, report the failure. Do not silently downgrade without the user's approval.
7. Mark each role required or optional while framing. Retry a failed required spawn once with a smaller packet; if it or a required verification remains unavailable, the gate cannot pass.

Use this response contract for advisory agents:

```markdown
## Recommendation
One decisive recommendation.

## Evidence
Repository or artifact evidence supporting it.

## Tradeoffs and risks
What the recommendation costs or leaves uncertain.

## Gate impact
Pass, revise, stop, or experiment—and why.

## Next action
One concrete action, with an owner and output.
```

For write-enabled agents, add exact owned paths, verification commands, and a prohibition on unrelated edits. Snapshot repository status before the batch. An agent must inspect the current state of its owned files before changing them and preserve user changes. After the batch, inspect the complete diff or file change set and reject out-of-scope mutations. Do not install dependencies, perform git operations, generate images, or contact external services unless those actions are within the user's authorized task.

## Run the stage gates

Read `references/stage-gates.md` before orchestrating more than one gate or deciding whether a milestone may advance.

1. **Frame.** Define the milestone decision, evidence, observable exit thresholds, time/token/tool budget, contingency, accountable human owner, and required/optional council. Create a milestone packet from `assets/MILESTONE_PACKET.md` only when the user authorized durable artifacts; otherwise keep it in working context.
2. **Diverge.** Spawn independent specialists in parallel. Give each the same raw facts appropriate to its role; do not include another specialist's preferred verdict.
3. **Compare.** Normalize recommendations by player value, pillar fit, scope, implementation risk, testability, and reversibility. Separate factual disagreement from value judgment.
4. **Resolve.** The orchestrator makes the decision or asks the creative director to synthesize a cross-discipline conflict. Record a decision using `assets/DECISION_RECORD.md`.
5. **Build.** Assign one bounded writer, or disjoint writers, with acceptance criteria and verification. Advisory agents do not modify files.
6. **Verify.** Run relevant tests. Before every `Pass` or production commitment, spawn a fresh, read-only milestone evaluator that did not contribute to the work. Give it a frozen packet created from `assets/EVALUATION_PACKET.md`, excluding prior verdicts, other specialist conclusions, decision-record conclusions, and the Results section of the milestone packet.
7. **Gate.** Mark the milestone `Pass`, `Revise`, `Stop`, or `Experiment`. `Pass` requires evidence for every required criterion and evaluator support; a missing evaluator, failed required check, or unsupported required criterion prohibits `Pass`. Repair and re-evaluate with a fresh agent. If the accountable human has not delegated decision authority, report `Pass recommended` and request their decision rather than committing an irreversible choice.

The milestone evaluator receives the acceptance criteria, sanitized artifact manifest, diffs, and validation evidence. Do not reveal the desired verdict or ask it to ratify the team. Because agents share a filesystem, exclude conclusion-bearing files from its input allowlist and tell it not to inspect unlisted paths.

## Compose the game skills

Use the specialized skills as discipline playbooks when available. Preflight their paths before isolated spawns and pass the resolved skill path plus either `rubric-only` or `write-enabled` in the assignment:

- `$game-design-spec` for concept briefs, prototypes, vertical-slice specs, mechanics, and acceptance criteria;
- `$game-interaction-contracts` for reusable gameplay verbs, stateful exchanges, cross-asset behavior, flows, bindings, and interaction acceptance tests;
- `$game-aesthetic` for broad mood, emotional, thematic, and world-language exploration;
- `$game-art-style` after aesthetic direction is locked, for production-medium exploration and visual rules;
- `$game-visual-blockout` for silhouette, footprint, greybox, production-proxy, and AI asset-handoff evidence before finished content;
- relevant Blender game-development skills for 3D asset creation, review, and engine export.

The orchestrator owns sequencing, authority, and synthesis. The discipline skill owns the quality bar for its artifact but cannot expand an assignment's inputs, tools, or write scope. Never merge aesthetic exploration and production art-style selection merely to save a gate; they answer different questions. A project without an art-production owner may explore aesthetics and use placeholders, but it cannot pass production-art feasibility until an owner and representative pipeline test exist.

## Handle disagreement and failure

- When recommendations conflict, identify the contested assumption and design the smallest reversible experiment that can resolve it.
- When scope and quality conflict, protect the player-facing pillar and reduce breadth before silently weakening the experience.
- When the implementation contradicts a design document, classify it as a design change, implementation defect, or undecided discrepancy.
- When an agent returns generic advice, follow up once with the missing evidence or decision constraint. Replace the agent's conclusion with orchestrator judgment if it still cannot support it.
- When agents edit overlapping files, stop integration, inspect the diff, and resolve ownership before continuing. Never discard user changes.
- When evidence is insufficient for a gate, choose `Experiment` with a bounded question and stop criterion instead of pretending to pass.
- When using visual references, record provenance and permitted role; do not ask for imitation of a living artist. When collecting playtest or telemetry data, follow the project's consent, privacy, retention, and PII rules; if none exist, avoid collecting personal data until the accountable owner defines them.

## Finish the run

Return a compact studio report containing:

- milestone and gate result;
- specialists used, their model/effort, and whether each was advisory or write-enabled;
- decision made and strongest evidence;
- artifacts or code changed and validation performed;
- rejected alternatives and material risks;
- next milestone, owner, and exit criteria.

Update durable studio state and decision records only within the user-authorized mutation scope. A completed run must leave one coherent decision, not a pile of unranked agent opinions.

# Game design specification quality bar

Use this reference for production specs, design critiques, and system-level requirements.

## Contents

1. Source-of-truth rules
2. Design framing
3. System contract
4. Testable experience targets
5. Scope and content budgets
6. Cross-discipline coverage
7. Consistency review
8. Common failure modes

## Source-of-truth rules

- Give every document a clear purpose and avoid duplicating canonical rules.
- Link supporting documents from the overview and link requirements back to pillars.
- Distinguish `Confirmed`, `Initial tuning`, `Assumption`, `Experiment`, and `Open question`.
- Put unresolved decisions in one decision log with impact and resolution criteria.
- Record consequential changes with date, decision, rationale, and affected requirements.
- Treat shipped or observed behavior as evidence, not automatically as intended design.

## Design framing

A usable framing section answers:

- What does the player repeatedly do?
- What fantasy or emotional promise does that activity fulfill?
- Who is the intended player, on what platform, with what input method?
- How long is a typical interaction, session, and complete playthrough?
- What two to four pillars decide tradeoffs?
- Which attractive ideas are intentionally excluded?
- What comparable games establish vocabulary or expectations, and how is this game different?

A pillar must be specific enough to reject a feature. “Fun” and “immersive” are not pillars. “Every threat is readable before it becomes dangerous” can constrain animation, encounter density, audio, and camera behavior.

## System contract

Specify each committed system with the following fields. Omit a field only when it truly does not apply.

| Field | Question answered |
|---|---|
| Identifier and name | How can other documents refer to this rule reliably? |
| Player intent | Why would a player use or encounter it? |
| Preconditions | When is the action or system valid? |
| Inputs and triggers | What starts it? |
| Rules and state transitions | What happens, in what order? |
| Outputs | What changes in game state? |
| Initial tuning | Which adjustable values need starting bounds? |
| Resources and economy | What is consumed, produced, limited, or exchanged? |
| Feedback | How does the player perceive cause, state, and result? |
| Failure and recovery | How can it fail, and what happens next? |
| Edge cases | What happens at boundaries or during conflicting states? |
| Dependencies | Which content, systems, tools, or platform features are required? |
| Telemetry | What evidence would help validate or tune it? |
| Accessibility | Which alternate perception or input paths are needed? |
| Acceptance criteria | What observable evidence proves the rule works? |
| Traceability | Which loop, pillar, or requirement does it support? |

Avoid prescribing classes, nodes, components, tables, or network protocols unless the document is explicitly a combined design and technical specification.

## Testable experience targets

Subjective goals need observable proxies and a playtest method. Do not pretend that a proxy fully measures an emotion.

| Intent | Useful specification evidence |
|---|---|
| Responsive | Input buffer, worst-case latency target, cancellation rules, animation timing, test device |
| Fair | Telegraph duration, visibility and audio constraints, reaction window, deterministic damage rules |
| Strategic | Meaningful alternatives, information available before choice, counterplay, dominant-strategy checks |
| Replayable | Run variance, content combinations, decision density, repetition thresholds, seeded tests |
| Accessible | Remapping, timing alternatives, subtitle rules, contrast, non-color cues, assist options |
| Satisfying | Anticipation, impact feedback, state change, recovery timing, comparative playtest prompt |

Write acceptance criteria as observable outcomes under stated conditions. Prefer “Given/When/Then,” tables, or short test procedures. Avoid “works correctly,” “feels good,” and other circular criteria.

Treat all untested numeric values as initial tuning. Give a plausible range or experiment when a single value would imply false certainty.

## Scope and content budgets

Quantify scope by category and milestone. Useful units include:

- mechanics and upgrades;
- levels, rooms, encounters, or generated chunks;
- enemy families and behavioral variants;
- characters, dialogue scenes, quests, and narrative beats;
- items, recipes, cards, abilities, and status effects;
- animations, VFX, SFX, music states, and voice lines;
- UI screens, flows, tutorials, settings, and accessibility options;
- target playtime, session length, save slots, and supported player count;
- platforms, input devices, frame rate, memory, package size, and loading time.

Use `Must`, `Should`, `Could`, and `Out` for the relevant milestone. “Out” is a design tool: it protects the intended experience from accidental expansion. For procedural content, budget authored ingredients and validation combinations, not just theoretical outputs.

## Cross-discipline coverage

For each important feature, check the handoff needs of:

- **Design:** rules, tuning, content dependencies, failure behavior, telemetry.
- **Engineering:** state boundaries, persistence, determinism, platform constraints, performance target.
- **Art and animation:** required assets, readability, camera distance, states, transitions, budgets.
- **Audio:** events, priority, variation, mixing, spatial behavior, accessibility alternatives.
- **UX and writing:** entry points, labels, screen states, error cases, onboarding, localization.
- **QA:** acceptance criteria, debug controls, deterministic setup, boundary cases, regression risks.
- **Production:** owner, dependencies, estimate or complexity signal, milestone, cut strategy.

Do not invent owners or estimates. Mark them unknown and identify the decision that supplies them.

## Consistency review

Perform these passes after drafting:

1. **Promise:** Do pillars, loop, audience, and feature set describe the same game?
2. **Traceability:** Does each Must feature support a pillar or core loop? Does every pillar change a requirement?
3. **Rules:** Are state transitions, costs, rewards, failure, and recovery unambiguous?
4. **Economy:** Are sources, sinks, caps, pacing, and loss conditions internally compatible?
5. **Content:** Can the stated content budget deliver the promised duration and variety?
6. **UX:** Can a first-time player discover, understand, perform, and recover from each critical action?
7. **Production:** Are dependencies, platform budgets, tools, and milestone boundaries visible?
8. **Verification:** Can QA or a playtest produce evidence for each acceptance criterion?

## Common failure modes

- **Pitch disguised as specification:** Rich theme and story, but no precise player actions or rules.
- **Feature catalogue:** Many features without loops, priorities, dependencies, or exclusions.
- **False precision:** Exact numbers presented as final before prototypes or playtests exist.
- **Invisible edge cases:** Rules describe success but not invalid input, interruption, failure, or recovery.
- **Implementation leakage:** The design unnecessarily dictates engine architecture.
- **Unbounded content:** “Many levels” or “lots of items” without milestone budgets.
- **Scattered uncertainty:** `TBD` appears throughout instead of a decision log with impact.
- **Unverifiable feel:** Goals such as “epic” or “smooth” have no observable proxies or test method.
- **Contradictory sources:** The overview, system spec, UI flow, and build behavior disagree without a named authority.
- **Stale document:** Major decisions change without updating requirements, scope, and acceptance criteria.

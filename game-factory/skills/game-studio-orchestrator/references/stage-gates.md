# Stage-gated game studio workflow

Advance because evidence satisfies exit criteria, not because every role has produced a document. These gates are evidence states, not a mandatory linear waterfall. Route to the earliest gate whose evidence is missing for the requested milestone; earlier accepted evidence may be reused. A temporary-art first playable may reach Gate 4 before Gates 2–3, while production art cannot begin before those visual gates pass. Gate 6 is a reusable acceptance overlay for any consequential milestone or release.

During Frame, convert every required-evidence bullet for the selected gate into an observable criterion row with a pass threshold and evidence source. A gate passes only when every required row is supported by evidence and a fresh independent evaluator agrees.

## Gate 0 — Framed opportunity

**Question:** Is there a coherent opportunity worth specifying?

Required evidence:

- one-sentence game concept and player fantasy;
- target player, platform/input, and intended session shape;
- three or fewer discriminating design pillars;
- scope ceiling, non-goals, and highest-risk assumption.

Default council: game design lead, player advocate, scope producer.

Exit: a concept brief and a named prototype question. If the fantasy or audience remains incoherent, revise before visual exploration.

## Gate 1 — Prototype contract

**Question:** Can a minimum playable experiment answer the riskiest design question?

Required evidence:

- core-loop rules and minimum content;
- bounded prototype scope and explicit exclusions;
- instrumentation or observation plan;
- success, revise, and stop criteria;
- engineering and asset dependencies.

Default council: game design lead, technical director, scope producer.

Exit: a buildable prototype brief. A prototype is allowed to look temporary, but its feedback must be sufficient to judge the question.

## Gate 2 — Aesthetic direction

**Question:** What should the game world feel like across ordinary, aspirational, and dangerous moments?

Required evidence:

- locked or stable-enough player fantasy and pillars;
- comparable aesthetic territories using a controlled world anchor;
- scored range tests and a selected territory;
- palette roles, motifs, atmosphere, tone boundaries, and anti-anchors.

Default council: aesthetic director, player advocate. Use creative director only for a close cross-discipline conflict.

Exit: `AESTHETIC_DIRECTION.md`. Do not lock a production medium at this gate.

## Gate 3 — Production art style

**Question:** Which production visual system best expresses the aesthetic and survives real gameplay constraints?

Required evidence:

- locked aesthetic direction;
- representative gameplay views and content types;
- comparable style candidates evaluated for readability and production feasibility;
- technical range tests for characters, environments, effects, UI coexistence, and difficult cases;
- selected rules, anti-rules, asset tiers, and validation set.

Default council: art style director, technical director, performance/platform lead when platform budgets are tight.

Exit: `ART_STYLE_GUIDE.md` plus retained reference images and production constraints. Passing production feasibility requires a named art-production owner and a representative pipeline test; concept images alone are insufficient.

## Gate 4 — Playable prototype

**Question:** Does the core interaction create the intended player behavior and feeling?

For this skill, a **first playable** is the smallest reproducible build in which a player can complete the core loop once and generate valid evidence for the prototype hypothesis. It may use temporary assets and incomplete secondary systems.

Required evidence:

- executable build or reproducible play path;
- implemented core-loop contract;
- focused automated tests where useful;
- structured playtest observations against the prototype criteria;
- documented discrepancies and tuning variables.

Default council: gameplay engineer, UX/accessibility lead, QA/test lead.

Exit: pass the prototype hypothesis, revise it with a bounded next experiment, or recommend stopping the concept to the accountable owner. Fun is not proven by implementation completeness.

## Gate 5 — Vertical slice

**Question:** Can the team make one representative segment at target quality and cost?

Required evidence:

- integrated gameplay, content, art, UI, audio, and feedback representative of production;
- measured content throughput and named pipeline bottlenecks;
- target-platform performance evidence;
- onboarding and accessibility coverage appropriate to the slice;
- updated scope forecast based on actual production cost.

Default council: content/level designer, QA/test lead, performance/platform lead, scope producer.

Exit: a production plan grounded in measured throughput, or a reduction/rework decision.

## Gate 6 — Milestone or release acceptance

**Question:** Are all committed exit criteria met with acceptable residual risk?

Required evidence:

- criterion-by-criterion validation record;
- build, test, playtest, profiling, and compliance evidence as applicable;
- open defects classified by severity and player impact;
- rollback or recovery strategy for material risks;
- independent milestone evaluation.

Default council: QA/test lead, performance/platform lead, milestone evaluator.

Exit: `Pass`, `Revise`, `Stop`, or `Experiment`, with the next owner and milestone. If the accountable human has not delegated final authority, `Pass` and `Stop` remain recommendations awaiting their decision.

## Decision policy

Use the following order when tradeoffs cannot all be satisfied:

1. Protect safety, legal, platform, and data-integrity constraints.
2. Protect the player fantasy and discriminating pillars.
3. Protect the validity of the current experiment.
4. Reduce content breadth and secondary features.
5. Reduce polish that does not invalidate the test.
6. Move the date only when the user or accountable owner authorizes it.

Prefer reversible experiments for uncertain decisions. Treat sunk work as evidence of cost, not evidence that a direction should continue.

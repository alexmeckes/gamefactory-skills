# Game Factory skill map

Use this map to route work and preserve traceability across the plugin. Invoke only the skills needed for the current decision.

## Skill contracts

| Skill | Question it answers | Consumes | Produces | Primary handoff |
|---|---|---|---|---|
| `$game-studio-orchestrator` | Which specialists and evidence does this milestone need? | Objective, project state, constraints, existing artifacts | Council assignments, gate decision, decision record, next milestone | Every selected discipline |
| `$game-design-spec` | What game are we building, for whom, under which rules and scope? | Concept, research, implementation evidence, constraints | Pillars, loops, requirements, scope, prototype or slice criteria | Interaction, aesthetic, blockout, implementation |
| `$game-interaction-contracts` | How does a verb or stateful exchange behave across participants and systems? | Requirement IDs, player intent, system rules, implementation evidence | Contracts, flows, bindings, semantic hooks, acceptance cases | Blockout, UX, engineering, QA |
| `$game-aesthetic` | What should the world feel like? | Fantasy, themes, audience, tone boundaries, world facts | Aesthetic territories and locked aesthetic direction | Art style, narrative, audio, marketing |
| `$game-art-style` | How will the locked aesthetic be produced consistently and readably? | Aesthetic direction, camera, platform, team and content constraints | Production visual rules, asset tiers, pipeline and validation set | Blockout, asset production, rendering |
| `$game-visual-blockout` | Does the shape, scale, space, or gameplay footprint work before finish? | Requirements, interaction hooks, camera and optional art-style rules | Silhouettes, greyboxes, proxies, spatial evidence, AI construction handoffs | Asset/level production and interaction bindings |

## Default routing

1. Use `$game-design-spec` to establish the concept, pillars, loop, scope, and risky prototype question.
2. Use `$game-interaction-contracts` once a behavior spans participants, states, systems, scenes, or tests.
3. Use `$game-aesthetic` when the world's emotional and thematic language is unresolved.
4. Use `$game-art-style` only after aesthetic direction is stable enough to translate into a production method.
5. Use `$game-visual-blockout` as soon as shape or space needs evidence. It may run style-neutral before art-style selection, then receive production rules before L3 proxy handoff.
6. Use `$game-studio-orchestrator` across consequential milestones to frame, delegate, reconcile, verify, and gate the work.

Behavior and aesthetic exploration may proceed in parallel after the relevant design inputs stabilize. Art-style selection depends on aesthetic direction. A first playable may use temporary art and therefore does not require the art-style gate, but production asset commitments do.

## Shared identity and references

Use stable IDs and references instead of repeating rules:

- design requirements: discipline prefixes such as `COMBAT-DODGE-001`;
- interaction contracts: namespaced IDs such as `shop.appraise-cursed-item`;
- aesthetic candidates: `E01`, `E02`, and so on within their exploration;
- art-style candidates: `A01`, `A02`, and so on within their exploration;
- visual blockouts: `B01`, `B02`, and so on within their subject folder;
- milestone criteria and decisions: project-specific stable IDs.

Every downstream artifact records the upstream IDs and paths it implements. Keep player intent and scope in the design spec, behavior in interaction contracts, emotional meaning in aesthetic direction, representation rules in the art-style guide, and geometry/spatial evidence in blockouts.

## Sources of truth

- A design spec owns player goals, pillars, feature scope, and experience requirements.
- An interaction contract owns reusable behavioral rules and state transitions.
- An interaction binding owns context-specific prefab, socket, volume, animation, UI, audio, VFX, camera, input, and tuning mappings.
- An aesthetic direction owns mood, symbolism, palette intent, motifs, and tone boundaries.
- An art-style guide owns production representation, shape treatment, rendering, asset tiers, and visual budgets.
- A visual blockout owns validated dimensions, masses, negative spaces, clearances, collision intent, and construction geometry.
- A milestone decision record owns the accepted cross-discipline tradeoff and its evidence.

## Change propagation

- Design-rule changes trigger impact review for interaction contracts, flows, acceptance cases, blockouts, implementation, and tests.
- Interaction participant, state, timing, or semantic-hook changes trigger review of bindings, blockouts, animation, UX feedback, code, and QA.
- Aesthetic changes trigger art-style and downstream presentation review, but do not silently rewrite gameplay rules.
- Art-style changes trigger production-proxy, asset-pipeline, readability, performance, and handoff review. They change gameplay dimensions only through an explicit design decision.
- Blockout findings may expose an invalid design rule, interaction clearance, or art-production assumption. Classify the upstream change rather than hiding it in geometry.

## Plugin and future MCP boundary

Keep these workflows bundled as plugin skills. If Game Factory later adds an MCP server, use it for live project state, registries, generation jobs, build/playtest evidence, telemetry, or external actions. Do not move stable workflow instructions or their source-of-truth templates into opaque tool behavior. MCP-returned records should use the same stable IDs and paths described above.

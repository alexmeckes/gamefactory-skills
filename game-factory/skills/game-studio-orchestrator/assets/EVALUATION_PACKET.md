# Independent evaluation packet — [milestone]

This packet must be frozen before evaluator spawn and contain no preferred verdict, specialist conclusions, decision-record conclusion, or milestone Results.

## Evaluator contract

- Model: `gpt-5.6-sol`
- Reasoning effort: `ultra`
- Context fork: `none`
- Authority: strictly read-only
- Prior contributor to this work: `No`
- Allowed verdicts: `Pass | Revise | Stop | Experiment`

The evaluator must not inspect unlisted paths or repair the work. Every finding must cite supplied evidence. Any required criterion without evidence is unsupported and prohibits `Pass`.

## Gate and criteria

- Gate:

| ID | Required criterion and threshold | Evidence source |
|---|---|---|
| M-01 | | |

## Sanitized input allowlist

- [absolute artifact, diff, build log, test output, profile, or playtest record]

## Known evidence limitations

- [missing, stale, or non-representative evidence; do not include a desired conclusion]

## Required output

1. Verdict.
2. Criterion-by-criterion `Supported | Unsupported | Contradicted` table with evidence.
3. Residual risks.
4. Smallest work required before a fresh evaluation.

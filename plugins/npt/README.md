# npt — Natural Parallel Test

Stress-test a plan against nature by shared mechanism, not resemblance.

> Do not ask whether the plan *looks like* something in nature. Ask whether nature has
> solved the **same problem under comparable constraints**, and what mechanism allowed that
> solution to endure.

Full documentation, installation, and worked examples: [repository README](../../README.md).

## Components

| Type | Name | Purpose |
|------|------|---------|
| Skill | `natural-parallel-test` | The eight-step method. Fires automatically when a plan is being assessed or a nature analogy appears |
| Command | `/npt:test` | Full assessment — mechanisms, parallel search, audit, score, verdict |
| Command | `/npt:worksheet` | One page, one pass, no subagents |
| Command | `/npt:score` | Twelve-principle scorecard only |
| Command | `/npt:challenge` | Adversarial — assumes *Contrary* and tries to prove it |
| Command | `/npt:analogues` | Search only, all seven levels, for one problem |
| Agent | `analogue-scout` | Searches one assigned level. Dispatched in parallel, one per level |
| Agent | `analogy-auditor` | Refutes candidates. Separate model, `refuted` by default |

## Progressive disclosure

`SKILL.md` holds the procedure and a routing table. The heavy material loads only when the
relevant step is reached:

| Reference | Loaded at |
|-----------|-----------|
| `01-problem-statement.md` | Step 1 — restating the plan as a problem |
| `02-mechanisms.md` | Step 2 — the ten mechanisms |
| `03-analogue-library.md` | Steps 3 & 5 — ~35 catalogued systems across seven levels |
| `04-validity-tests.md` | Step 4 — the four tests |
| `05-scoring.md` | Steps 7 & 8 — anchors, bands, overrides |
| `06-limits-and-fallacies.md` | Step 6 — breaking points and the naturalistic fallacy |
| `07-report-template.md` | Step 8 — output shape |
| `08-worked-examples.md` | On demand — three full runs |

Always-on cost is roughly 530 tokens for the whole plugin.

## Agent model note

`analogy-auditor` declares `model: fable`. Refutation should not run on the model that
generated the candidate — a generated analogy audited by its generator is not audited.

Plugin agent `model` values are documented for `sonnet`, `opus`, `haiku`, and `inherit`.
`fable` sits outside that documented set but is verified resolving on Claude Code 2.1.220 —
the agent runs as Fable 5 at `effort: high`. If it stops resolving after an upgrade, change
the frontmatter to `model: opus` and keep `effort: high`; the auditor's value is in its
prompt and its separation from the generator, not in the specific model.

Note that `claude plugin validate` does **not** inspect agent `model` values at all, so a
wrong value there fails silently at runtime rather than at validation.
`scripts/validate-plugin.py` checks it instead.

## Conventions for contributors

Every analogue-library entry must carry:

- the problem solved, in nature's terms
- the mechanism, step by step — this is the part that transfers
- the constraints it operates under
- what its resilience comes from
- what makes it fail
- the transferable principle, **in non-biological language**
- **where the comparison stops being valid** — mandatory

Contested science must be flagged as contested. Entries without a stated limit will not be
merged: an entry quoted without its limit has been misused.

# CLAUDE.md — natural-parallel-test

Claude Code plugin implementing the Natural Parallel Test: a method for stress-testing plans
against nature by shared mechanism rather than resemblance.

## Repository shape

Marketplace at repo root; plugin nested under `plugins/npt/`. Inside the plugin,
`.claude-plugin/` contains **only** `plugin.json` — commands, agents, and skills sit at the
plugin root.

```
.claude-plugin/marketplace.json      # marketplace: natural-parallel-test
plugins/npt/
  .claude-plugin/plugin.json         # plugin: npt
  skills/natural-parallel-test/SKILL.md + references/01..08
  commands/{test,worksheet,score,challenge,analogues}.md
  agents/{analogue-scout,analogy-auditor}.md
```

## Working on this repo

**Validate after every manifest or frontmatter change:**

```bash
claude plugin validate ./plugins/npt --strict
claude plugin validate . --strict
```

**Reload after editing plugin files** — the installed copy is cached:

```bash
claude plugin marketplace update natural-parallel-test
```

**Command frontmatter**: `argument-hint` values must be **quoted**. Unquoted
`[a] [b]` is invalid YAML (two juxtaposed flow sequences) and the whole frontmatter block is
silently dropped at runtime. `--strict` catches this; the runtime does not.

**Agent `model` values are not validated by the CLI.** `claude plugin validate` checks
`plugin.json` only — a bogus `model:` in agent frontmatter passes validation and fails
silently at runtime. `scripts/validate-plugin.py` checks it instead.

`analogy-auditor` uses `model: fable` deliberately, so refutation never runs on the model
that generated the candidate. This is verified resolving on Claude Code 2.1.220 (the agent
reports running as Fable 5 at `effort: high`). Re-check after a Claude Code upgrade; if it
stops resolving, fall back to `model: opus` with `effort: high`.

## Editorial rules for the framework content

These are not style preferences. The framework's credibility depends on them.

1. **Every analogue-library entry carries a "Stops being valid when" line.** No exceptions.
   An entry quoted without its limit has been misused.
2. **Flag contested science as contested.** The library currently flags the mycorrhizal
   "wood-wide web" resource-sharing claims (E-23). The alpha wolf and the directing queen
   bee appear only as worked *failures*, never as entries.
3. **Transferable principles must contain no organism names.** "Be like mycelium" is not a
   principle. If a recommendation still names a species, it is unfinished.
4. **Never phrase a natural mechanism as an intention.** Rivers do not seek the sea;
   colonies do not choose. Dynamics, not goals.
5. **"Natural" is never an argument for desirability.** Nature sustains parasitism, cancer,
   and extinction. The framework uses nature as evidence about durability under constraint.
6. **Silence scores `0`, not `1`.** The scoring anchors in `05-scoring.md` are written to
   resist drift; do not soften them.
7. **Rejected analogues stay in reports.** They are the evidence the search happened.

## Keeping SKILL.md small

`SKILL.md` holds procedure and a routing table only. Anything table-shaped, enumerable, or
longer than a few lines belongs in `references/`. Always-on token cost is currently ~530 for
the whole plugin; check with `claude plugin details npt` after structural changes.

## Not present

No `evals/`. `claude plugin eval` is early-access and unavailable in this environment, so
the case/grader schema could not be verified. Adding an unverifiable eval suite would ship
config that fails silently — exactly what the framework's own Selection principle warns
against. Add it once the subcommand is generally available.

## Author

Babak Bandpey · bb@cocode.dk · https://cocode.dk

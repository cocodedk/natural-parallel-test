# Contributing to Natural Parallel Test

## Local Setup

```bash
git clone https://github.com/cocodedk/natural-parallel-test.git
cd natural-parallel-test
pip install pyyaml
./scripts/install-hooks.sh
```

`core.hooksPath` is per-checkout config and is not committed, so **every fresh clone must
run `./scripts/install-hooks.sh`** or no hooks are active.

## Local Git Setup

Run once after cloning:

```bash
git config pull.rebase true
git config core.autocrlf input        # 'true' on Windows
git config push.autoSetupRemote true
```

## Testing your changes

```bash
python3 scripts/validate-plugin.py    # manifests, frontmatter, editorial rules
python3 scripts/check-links.py        # relative markdown links
claude plugin validate ./plugins/npt --strict
claude plugin validate . --strict
```

Then install the plugin from your working copy and exercise it:

```bash
claude plugin marketplace add ./natural-parallel-test
claude plugin install npt@natural-parallel-test
claude plugin marketplace update natural-parallel-test   # after every edit
```

Run at least `/npt:worksheet` and `/npt:test` against a real plan before opening a PR. The
useful regression probe is a deliberately shallow analogy — feed it *"our company should
work like a beehive"* and confirm the output rejects the metaphor and asks for a mechanism
rather than elaborating it.

## Editorial rules

These are not style preferences. The framework's credibility rests on them, and the
validator enforces the first one automatically.

1. **Every analogue-library entry carries a "Stops being valid when" line.** No exceptions.
   An entry quoted without its limit has been misused. CI fails without it.
2. **Flag contested science as contested.** The alpha wolf, the directing queen bee, and
   trees generously sharing food through fungal networks are wrong or substantially
   disputed. They may appear as worked *failures*; they may not appear as entries.
3. **Transferable principles contain no organism names.** "Be like mycelium" is not a
   principle. If a recommendation still names a species, it is unfinished.
4. **Never phrase a natural mechanism as an intention.** Rivers do not seek the sea;
   colonies do not choose. Dynamics, not goals.
5. **"Natural" is never an argument for desirability.** Nature sustains parasitism, cancer,
   and extinction. The framework uses nature as evidence about durability under constraint.
6. **Silence scores `0`, not `1`.** The anchors in `05-scoring.md` resist drift; do not
   soften them.
7. **Rejected analogues stay in reports.** They are the evidence the search happened.

### Adding a library entry

Each entry needs all seven fields — problem solved, mechanism (step by step), constraints,
source of resilience, failure mode, transferable principle in non-biological language, and
where the comparison stops being valid. Add the entry ID to the routing table at the top of
`03-analogue-library.md`; the validator checks that the table and the entries agree.

Check the biology before writing the entry. Attractive analogies circulate on appeal rather
than evidence, and a wrong one entering a decision document is the failure mode this whole
project exists to prevent.

## Keeping SKILL.md small

`SKILL.md` holds procedure and a routing table only. Anything table-shaped, enumerable, or
longer than a few lines belongs in `references/`. Check the cost after structural changes:

```bash
claude plugin details npt
```

Always-on cost is currently ~530 tokens for the whole plugin. Treat a meaningful increase as
a design problem.

## Commits and branches

Conventional Commits, enforced by the `commit-msg` hook:

```
feat: add cosmic-level analogue entries
fix: correct the quorum threshold description in E-18
docs: expand the policy worked example
```

Types: `feat|fix|chore|docs|style|refactor|test|ci|build|perf|revert`

Branch names are kebab-case with a prefix matching the commit type: `feature/`, `fix/`,
`chore/`, `docs/`, `refactor/`, `ci/`. Never commit directly to `main` — always open a PR.

## Releasing

The release workflow does **not** bump the version. Bump it by PR first, in both
`plugins/npt/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` — the
workflow fails if they disagree — then run the `Release` workflow manually. It tags
`npt--v<version>` and creates the GitHub Release.

## PR Checklist

- [ ] `python3 scripts/validate-plugin.py` passes
- [ ] `python3 scripts/check-links.py` passes
- [ ] `claude plugin validate ./plugins/npt --strict` passes
- [ ] Plugin installed from the working copy and the changed command exercised
- [ ] Any new library entry has all seven fields including its limit
- [ ] Contested science flagged as contested
- [ ] No organism names in transferable principles

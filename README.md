# Natural Parallel Test

A Claude Code plugin that stress-tests plans against nature — by **shared mechanism**, not
by resemblance.

> Do not ask whether the plan *looks like* something in nature. Ask whether nature has
> solved the **same problem under comparable constraints**, and what mechanism allowed that
> solution to endure.

A company is not a forest. A software platform is not a nervous system. But they face the
same underlying problems: limited resources, uncertainty, coordination, competition,
failure, growth, and recovery. Those shared problems are the only legitimate basis for
comparison — and this plugin makes the comparison testable.

Point it at a plan, an architecture, an org design, or a policy. It decomposes the plan into
ten mechanisms, searches seven levels of nature for systems that solve the same problem
under the same constraints, sends every accepted candidate to an adversarial reviewer whose job is to
refute it, scores the plan on twelve durability principles, and returns one of four verdicts.

It also tells you which analogies **failed**, and why. That list is the point.

## Website

- [English](https://cocodedk.github.io/natural-parallel-test/)
- [فارسی (Persian)](https://cocodedk.github.io/natural-parallel-test/fa/)

---

## Installation

```
/plugin marketplace add cocodedk/natural-parallel-test
/plugin install npt@natural-parallel-test
```

That's it. Restart or `/reload-plugins` and the commands are available.

<details>
<summary>From the command line instead</summary>

```bash
claude plugin marketplace add cocodedk/natural-parallel-test
claude plugin install npt@natural-parallel-test
```
</details>

<details>
<summary>From a local clone (for development)</summary>

```bash
git clone https://github.com/cocodedk/natural-parallel-test.git
claude plugin marketplace add ./natural-parallel-test
claude plugin install npt@natural-parallel-test
```

The marketplace path must be given as a path — `./natural-parallel-test`, not
`natural-parallel-test` — or it is read as a GitHub `owner/repo`. Run
`claude plugin marketplace update natural-parallel-test` after editing plugin files.
</details>

<details>
<summary>Verifying and removing</summary>

```bash
claude plugin details npt          # component inventory and token cost
claude plugin validate ./plugins/npt --strict
claude plugin uninstall npt
claude plugin marketplace remove natural-parallel-test
```
</details>

**Requires** Claude Code v2.1.x or newer. The plugin adds roughly **530 tokens** to every
session; everything else loads only when invoked.

---

## Commands

| Command | What it does | When |
|---------|--------------|------|
| `/npt:test` | The full eight-step assessment: mechanisms, parallel analogue search, adversarial audit, twelve-principle score, verdict | Before committing to a plan |
| `/npt:worksheet` | One page, one pass, no subagents | A fast read, or deciding whether the full test is worth it |
| `/npt:score` | The twelve-principle scorecard alone, no analogue search | Comparing two plans, or re-checking after changes |
| `/npt:challenge` | Adversarial. Assumes the plan is *Contrary to natural patterns* and tries to prove it | When a plan was agreed too easily |
| `/npt:analogues` | Search only — all seven levels, for one problem | Thinking about a single mechanism |

Each takes a file path or a description. Quote multi-word arguments. With no argument, the
command asks for the plan's substance — it will not run on a title:

```
/npt:test docs/platform-strategy.md
/npt:test "one central team approves every automation across all countries"
/npt:challenge docs/five-year-plan.md
/npt:analogues "detect and stop a failing effort early" "no authority to cancel, political cost to admitting failure"
```

The skill also fires on its own when a nature analogy shows up in conversation.

---

## What it actually checks

**Ten mechanisms.** Resource flow · Information flow · Decision-making · Coordination ·
Adaptation · Growth · Repair · Selection · Boundaries · Renewal. Each is marked *Present*,
*Absent*, or *Not applicable* — and an absent mechanism is a finding, not a gap in the
search.

**Seven levels of nature**, searched in parallel so the answer cannot collapse into
"animals":

Physical systems · Cells · Organisms · Social species · Ecosystems · Evolution · Cosmic
systems

**Four validity tests**, of which any single failure rejects a candidate:

1. **Same problem** — genuinely the same function, not the same shape or vocabulary
2. **Similar constraints** — including who bears the cost of failure
3. **Comparable mechanism** — one this plan can actually instantiate
4. **Relevant scale** — size, speed, and timescale all compatible

**Twelve durability principles**, scored 0–2 against written anchors: Feedback · Adaptation
· Redundancy · Diversity · Modularity · Local autonomy · Coordination · Resource limits ·
Repair · Selection · Renewal · Environmental fit.

**Four classifications**: *Established natural pattern* · *Partial natural pattern* ·
*Novel but compatible* · *Contrary to natural patterns*.

**Five overrides that beat the score.** A plan depending on permanent control, unlimited
growth, perfect prediction, no failure, or no adaptation is *Contrary* whatever it scores.
Twelve generous readings should not outvote one structural dependency.

---

## Why it has an adversarial reviewer

The model that generates an analogy is the wrong one to judge it. Generation succeeds by
finding parallels; that is what it is for.

So candidate analogues go to a separate agent — `analogy-auditor`, running on a different
model with **`refuted` as its default verdict**. It checks the biology before it checks the
logic, because attractive analogies circulate on appeal rather than evidence:

- The **alpha wolf** comes from captive unrelated wolves. Wild packs are families; the
  researcher who popularised the term spent years trying to retract it.
- The **queen bee** directs nothing. She lays eggs. Colony decisions are distributed.
- **Trees generously sharing food** through fungal networks is substantially contested. The
  bilateral trade-and-sanction mechanism is supported; the cooperative-sharing story is not.

All three are widely repeated in strategy decks.

---

## An example

Given: *"One central team will approve and control every cybersecurity automation across
many countries."*

The plugin does **not** conclude "centralisation is unnatural" — organisms use central
control extensively. It finds something more useful. The best-fitting analogue is the
vertebrate reflex arc, and it argues against the plan as written:

> Reflexes act at the spinal cord in milliseconds without consulting the brain. The brain
> receives a copy, and can modulate, override, and learn from it — but it is not in the loop
> for the fast response. Thresholds for what counts as urgent are set centrally, long in
> advance.

Which becomes: set standards, thresholds, and prohibited actions centrally; let countries
execute inside them without asking; require a copy to the centre for learning; escalate only
exceptions.

And the limit, which is the most useful line in the report:

> Spinal neurons have no interests of their own. A country team choosing not to send the
> copy has interests — so the reporting step needs enforcement that the biological version
> never required.

Three of the four analogues that appeared to *support* central control turned out, on
inspection, to argue against it. The brain does not approve individual muscle contractions.

The full run, plus a software example and a policy example, is in
[`08-worked-examples.md`](plugins/npt/skills/natural-parallel-test/references/08-worked-examples.md).

---

## What this is not

It measures **structural durability under uncertainty**. It says nothing about whether a
plan is worth doing, affordable, legal, ethical, or wanted.

And "natural" does not mean good. Nature sustains parasitism, cancer, mass extinction, and
brutal inefficiency. This framework uses nature as evidence about what *endures* under
constraint — never as an argument that something is desirable. A plan that invokes
naturalness as justification gets that recorded as a defect in its reasoning.

---

## Repository layout

```
natural-parallel-test/
├── .claude-plugin/marketplace.json
└── plugins/npt/
    ├── .claude-plugin/plugin.json
    ├── skills/natural-parallel-test/
    │   ├── SKILL.md                    # the method
    │   └── references/                 # loaded on demand
    │       ├── 01-problem-statement.md
    │       ├── 02-mechanisms.md
    │       ├── 03-analogue-library.md  # ~35 entries across 7 levels
    │       ├── 04-validity-tests.md
    │       ├── 05-scoring.md
    │       ├── 06-limits-and-fallacies.md
    │       ├── 07-report-template.md
    │       └── 08-worked-examples.md
    ├── commands/                       # the 5 slash commands
    └── agents/                         # analogue-scout, analogy-auditor
```

Every entry in the analogue library carries a **"stops being valid when"** line. An entry
quoted without its limit has been misused.

---

## Contributing

New analogue-library entries are welcome. Each must state the problem solved, the mechanism
step by step, the constraints, the source of resilience, the failure mode, the transferable
principle in non-biological language, and where the comparison stops being valid. Entries
without a limit will not be merged, and contested science must be flagged as contested.

---

## Author

**Babak Bandpey** — [cocode.dk](https://cocode.dk) | [LinkedIn](https://linkedin.com/in/babakbandpey) | [GitHub](https://github.com/cocodedk)

Framework: the Natural Parallel Test, 2026.

## License

Apache-2.0 | © 2026 [Cocode](https://cocode.dk) | Created by [Babak Bandpey](https://linkedin.com/in/babakbandpey)

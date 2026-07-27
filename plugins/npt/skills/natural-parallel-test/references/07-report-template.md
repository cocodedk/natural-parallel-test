# Step 8 — Report Template

**Purpose**: a fixed output shape so two assessments of the same plan are comparable.
**Read this when**: scoring is complete.

Lead with the verdict. Someone reading only the first six lines should learn the
classification, the score, and the single most fragile mechanism.

---

## Complete report template

````markdown
# Natural Parallel Test — [Plan name]

**Plan**: [one-line description]
**Assessed**: [date]
**Horizon**: [timescale the plan must survive]
**Depth**: [worksheet | standard | deep]
**Assessor**: [agent or human]
**Framework version**: 0.1.0

## Verdict

**[Established natural pattern | Partial natural pattern | Novel but compatible | Contrary to natural patterns]**

**Score**: [N]/[denominator]
**Override fired**: [none | permanent control | unlimited growth | perfect prediction | no failure | no adaptation]
**Most fragile mechanism**: [name] — [one line on why]

[Two or three sentences. What this plan is trying to do, whether nature solves that problem
under comparable constraints, and the single change that would most improve durability.]

## 1. The problem, restated

> [The plan written as a problem, containing no solution nouns]

| # | Question | Answer |
|---|----------|--------|
| 1 | What must it achieve? | |
| 2 | What resources does it consume? | |
| 3 | What information does it need? | |
| 4 | What environment does it operate in? | |
| 5 | What can change unexpectedly? | |
| 6 | How long must it survive? | |
| 7 | What happens when one part fails? | |

[If the plan could not be stated without a solution noun, say so here — it is the first
finding.]

## 2. Mechanism map

| Mechanism | Mark | Note |
|-----------|------|------|
| Resource flow | Present / Absent / N/A | |
| Information flow | | |
| Decision-making | | |
| Coordination | | |
| Adaptation | | |
| Growth | | |
| Repair | | |
| Selection | | |
| Boundaries | | |
| Renewal | | |

**Absent mechanisms**: [list, or "none"]. Each is a gap in the plan, not a gap in the
search.

## 3. Accepted analogues

### A-01 · [System name] — [mechanism it addresses]

- **Level**: [physical | cells | organisms | social species | ecosystems | evolution | cosmic]
- **Problem it solves**: [in nature's terms]
- **Mechanism**: [step by step]
- **Validity**: same problem `[pass/partial]` · constraints `[pass/partial]` · mechanism `[pass/partial]` · scale `[pass/partial]`
- **Confidence**: [high | medium | low]
- **Transferable principle**: [written in the plan's vocabulary — no organism names]
- **Breaks down at**: [the specific differing property]

[Repeat per accepted analogue.]

## 4. Rejected analogues

Kept deliberately: these are the evidence that the search was real.

| ID | Candidate | Level | Failed test | Reason |
|----|-----------|-------|-------------|--------|
| A-0N | | | | |

## 5. Where the parallels break

[What the natural systems tolerate that this plan cannot. Answers to the six questions of
Step 6 that came back "yes, and we can't match it".]

[Any use of naturalness as justification found in the plan itself — a reasoning defect worth
recording independently.]

## 6. Scorecard

| # | Principle | Score | Evidence |
|---|-----------|-------|----------|
| 1 | Feedback | 0/1/2 | [passage, mechanism, or incident] |
| 2 | Adaptation | | |
| 3 | Redundancy | | |
| 4 | Diversity | | |
| 5 | Modularity | | |
| 6 | Local autonomy | | |
| 7 | Coordination | | |
| 8 | Resource limits | | |
| 9 | Repair | | |
| 10 | Selection | | |
| 11 | Renewal | | |
| 12 | Environmental fit | | |
| | **Total** | **[N]/[denom]** | |

**Weakest three**: [names]
**Unable to determine**: [principle — what evidence would resolve it]

A low score does not prove failure. It shows where the plan is fragile.

## 7. What to change

Ordered by the fragility they address, not by ease.

1. **[Change]** — from [analogue ID or principle]. Addresses [which mechanism/principle].
   [What specifically to do, in the plan's own vocabulary.]
2. …

## 8. Coverage log

```
resource-flow      walked  → N candidates (M accepted)
information-flow   walked  → N candidates (M accepted)
decision-making    walked  → N candidates (M accepted)
coordination       …
adaptation         skipped → [reason]
growth             …
repair             …
selection          …
boundaries         …
renewal            n/a     → [reason]
```

**Levels searched**: [list] — [count] of 7.

## Limits of this assessment

This test measures structural durability under uncertainty. It does not measure whether the
plan is worth doing, affordable, legal, ethical, or wanted. Nature is evidence about what
endures, not about what is good.

[Anything not assessed and why — missing environment description, unavailable incident
history, mechanisms not searched.]
````

---

## Worksheet output (depth: worksheet)

For `/npt:worksheet`. One page, no subagents, no full scorecard.

````markdown
# Natural Parallel Worksheet — [Plan name]

> We are trying to achieve **[function]** in an environment with **[constraints]**,
> using **[mechanism]**, over **[timescale]**.

**Where in nature does something solve a similar problem under similar constraints?**

### Candidate 1 — [system]

| | |
|---|---|
| What problem does it solve? | |
| What mechanism does it use? | |
| What makes it resilient? | |
| What causes it to fail? | |
| Which principle can we transfer? | |
| Where does the comparison stop being valid? | |

[Repeat for two or three candidates, from different levels.]

**Provisional read**: [classification] — [one line]. Run `/npt:test` for the full
assessment.
````

## Report rules

- **Lead with the verdict.** Never build up to it.
- **Keep rejected analogues.** A report with none did not search or did not test.
- **No organism names in the "what to change" section.** If a recommendation still says
  "like an immune system", it has not been translated.
- **State the denominator** whenever principles were N/A or unresolved. Never rebase
  silently.
- **Name which override fired**, if one did. "Contrary" without a named dependency is an
  insult rather than a finding.
- **Keep the limits section.** It is what separates this from a confident-sounding opinion.

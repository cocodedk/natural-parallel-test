# Worked Examples

Three complete runs across three domains, landing on three different classifications. Read
one before your first assessment.

| # | Domain | Plan | Verdict |
|---|--------|------|---------|
| 1 | Organisational | Central approval of all cybersecurity automation | Contrary to natural patterns |
| 1b | Organisational | The same plan, repaired | Partial natural pattern |
| 2 | Software / systems | Resilience-engineered service platform | Established natural pattern |
| 3 | Policy | Five-year predictive reskilling programme | Contrary to natural patterns |

Example 1 is the one to read first, and 1b immediately after it: together they show an
override firing and then being cleared, which is the single most common thing this framework
is asked to do.

---

# Example 1 — Central cybersecurity approval (organisational)

**As given**: *One central team will approve and control every cybersecurity automation
across many countries.*

## Verdict

**Contrary to natural patterns**

**Score**: 4/24
**Override fired**: **permanent control** *and* **no adaptation**
**Most fragile mechanism**: Decision-making — the information needed for every decision sits
in the countries, and the authority to decide does not.

Two structural dependencies fire independently of the score. Operation requires one central
team to be continuously available and the plan states no degraded mode for its absence
(Repair marked Absent). And no revision path exists at all (Adaptation marked Absent). Either
alone forces **Contrary**; the low total is corroboration, not the reason.

The conclusion is **not** that centralisation is unnatural — organisms use central control
extensively, and the best-fitting analogue found here is a vertebrate one. The finding is
narrower: nature combines central standards with local response, and this plan has taken
only the first half. Example 1b applies the changes below and clears both overrides.

## 1. The problem, restated

> We need to prevent a class of high-consequence mistakes across many units operating under
> different local conditions, when the people who understand each local condition are not
> the people who hold the authority to act.

| # | Question | Answer |
|---|----------|--------|
| 1 | Function | Prevent unreviewed automation from causing a security or availability incident, without stopping automation from happening |
| 2 | Resources | One central team; review time is the scarce resource and does not grow when country count does |
| 3 | Information | Local system context, local regulation, local risk appetite — all resident in the countries |
| 4 | Environment | Many jurisdictions, differing regulation, uneven local maturity, continuous change |
| 5 | Shocks | New regulation in one country; a vulnerability needing action in hours; the central team losing two people; automation volume tripling |
| 6 | Timescale | Multi-year, with volume growing throughout |
| 7 | One part fails | If the central team saturates or is unavailable, all countries stop — or proceed unreviewed. Both are failures |

Two facts are already visible: the information needed for the decision is structurally
distant from the authority to decide, and the scarce resource does not scale with demand.

## 2. Mechanism map

| Mechanism | Mark | Note |
|---|---|---|
| Resource flow | Present | Central review hours; fixed supply, growing demand, no buffer |
| Information flow | Present | Local context travels to the centre as written submissions; heavy filtering, days of delay |
| Decision-making | Present | Central team decides everything; no local decision rights |
| Coordination | Present | Achieved by routing every action through one point; cost grows with each country |
| Adaptation | **Absent** | No trigger, owner, or revision path stated |
| Growth | Present | "More countries"; review capacity does not grow with them |
| Repair | **Absent** | No stated behaviour when the central team is unavailable |
| Selection | **Absent** | No mechanism to stop a failing automation or retire the approval process |
| Boundaries | Present | The approval gate is the boundary; single, uniform, no fast path |
| Renewal | **Absent** | No retirement path for anything, including the approval process the Selection row says needs retiring |

Six Present, four Absent, none N/A. The absences — Adaptation, Repair, Selection, Renewal —
are the assessment before a single analogue has been considered, and two of them fire
overrides.

Note the Renewal row. An earlier draft marked it N/A on the grounds that the programme was
too new to have anything to retire. That was wrong, and it is exactly the error
`02-mechanisms.md` warns about: the Selection row two lines above says the approval process
itself needs retiring, so something *is* retirable and the mechanism is Absent, not
inapplicable. N/A shrinks the denominator and flatters the score — it has to be earned.

## 3. Accepted analogues

### A-01 · Reflex arcs alongside central integration (E-12) — decision-making, coordination

- **Level**: organisms
- **Problem it solves**: responding to urgent local events fast while keeping the whole body
  coherent
- **Mechanism**: reflexes act at the spinal cord in milliseconds without consulting the
  brain; the brain receives a copy and can modulate, override, and learn, but is not in the
  fast loop. Thresholds for "urgent" are set centrally, long in advance
- **Validity**: same problem `pass` · constraints `pass` · mechanism `pass` · scale `pass`
- **Confidence**: high
- **Transferable principle**: set standards, thresholds, and prohibited actions centrally;
  let countries execute inside them without asking; require a copy to the centre for
  learning; escalate only genuine exceptions
- **Breaks down at**: spinal neurons have no interests of their own. A country team choosing
  not to send the copy has interests, so the reporting step needs enforcement that the
  biological version never required

### A-02 · Innate and adaptive immunity (E-07) — information flow, boundaries

- **Level**: cells
- **Problem it solves**: defending a whole body against mostly-unknown threats faster than
  any central authority could respond
- **Mechanism**: fast local generic response requiring no permission, plus slow specific
  central response that generates diversity, selects what works, and remembers. Local
  detection triggers systemic escalation
- **Validity**: same problem `pass` · constraints `pass` · mechanism `partial` · scale `pass`
- **Confidence**: medium — `partial` on mechanism because "self versus non-self" is
  well-defined biologically and is precisely what is contested here
- **Transferable principle**: pair a fast local response needing no approval with a central
  function that analyses, remembers, and turns each incident into a reusable pattern — and
  budget explicitly for false positives, because a system that can escalate locally will
  over-escalate
- **Breaks down at**: autoimmunity has a direct analogue. Distributed authority to act
  against perceived threats will sometimes act against legitimate internal activity, and the
  damage is real

### A-03 · Layered proofreading and repair (E-10) — boundaries

- **Level**: cells
- **Validity**: same problem `pass` · constraints `partial` · mechanism `pass` · scale `pass`
- **Confidence**: medium
- **Transferable principle**: replace one perfect gate with several cheap independent checks
  — automated policy scanning, peer review in-country, sampled central audit. Multiplied
  error rates beat any single filter, and none of the layers needs to be a bottleneck
- **Breaks down at**: DNA repair works because an intact reference strand exists. There is
  no ground-truth "correct automation" to repair against; correctness here is judgement, so
  the layers reduce error rate without ever guaranteeing it

## 4. Rejected analogues

| ID | Candidate | Level | Failed test | Reason |
|----|-----------|-------|-------------|--------|
| A-04 | Brain as central controller | Organisms | Comparable mechanism | The brain does not approve individual muscle contractions; it sets policy and delegates execution. The analogue actually argues against the plan |
| A-05 | Queen bee directing the colony | Social species | Same problem | Factually wrong. Queens lay eggs; they direct nothing. The colony's decisions are distributed (E-18) |
| A-06 | Immune system as *central* clearing house | Cells | Comparable mechanism | Immunity's speed comes from local action. An immune system that required central approval per response would be lethal — the analogue inverts the plan |
| A-07 | Ant pheromone trails | Social species | Relevant scale | Requires thousands of reinforcement cycles to converge. This programme makes tens of decisions per quarter, three orders of magnitude short |

Note that three of the four rejections come from analogues that at first appear to *support*
central control, and on inspection argue against it.

## 5. Where the parallels break

- Every accepted analogue depends on local actors whose interests are aligned with the whole.
  Spinal neurons and immune cells have no agenda; country teams do. Each transferred
  mechanism needs an enforcement or verification step its biological version never needed.
- Immunity works because a false positive costs tissue. Here a false positive costs a
  blocked business action, and the pressure to suppress the response is political rather
  than physiological.
- The plan is not using naturalness as justification anywhere — no fallacy finding.

## 6. Scorecard

| # | Principle | Score | Evidence |
|---|---|---|---|
| 1 | Feedback | 0 | Approval decisions are logged — that is activity, not outcome. Nothing measures whether incidents fell |
| 2 | Adaptation | 0 | No revision trigger, owner, or path stated |
| 3 | Redundancy | 0 | Central team is a single point of failure with no alternate |
| 4 | Diversity | 0 | Exactly one approval route |
| 5 | Modularity | 1 | Country operations are separable, but every one is coupled through the gate |
| 6 | Local autonomy | 0 | No local decision rights of any kind |
| 7 | Coordination | 1 | Routing everything through one point does produce consistency, but by central inspection rather than by construction, and the mechanism map records that its cost grows with every country added |
| 8 | Resource limits | 1 | Team size stated; no statement of behaviour at saturation |
| 9 | Repair | 0 | No recovery path when the central team is unavailable |
| 10 | Selection | 0 | No mechanism to stop a failing automation or retire the process |
| 11 | Renewal | 0 | No retirement path; the approval process itself cannot be retired |
| 12 | Environmental fit | 1 | Jurisdictions described; assumption of uniform applicability not stated as an assumption |
| | **Total** | **4/24** | |

**Weakest three**: Local autonomy, Repair, Selection — though seven principles score `0`.

Both the band (`0–5` → Contrary) and the overrides agree here. They usually do not, which is
why the overrides exist; see the note under the verdict.

## 6a. Why the override decides this, not the score

Worth stating explicitly, because it is the step most often skipped.

Suppose the plan were improved everywhere except availability — richer feedback, real
diversity, better environmental characterisation — and scored `20/24`. It would still be
**Contrary to natural patterns**, because operation would still require one team to be
continuously available with no defined degraded mode. `05-scoring.md` is unambiguous:
*"regardless of total"*.

The temptation is to soften that: the plan does define boundaries, it does achieve
consistency, the fix looks structural rather than foundational. None of those is an
exemption, and no exemption exists. Reaching for one is the *"we're a special case"*
rationalization from `06-limits-and-fallacies.md`, applied by the assessor rather than by
the plan's author.

## 7. What to change

1. **Split standards from execution** (A-01). Centre defines prohibited actions, mandatory
   controls, and escalation thresholds. Countries execute within them without asking.
2. **Add a fast local path with no approval** (A-02) for actions inside the defined
   envelope, with mandatory notification to the centre. This converts the centre from a gate
   into a learning function and removes the scaling wall.
3. **Replace the single gate with layered checks** (A-03): automated policy scanning, local
   peer review, sampled central audit weighted by risk.
4. **Define degraded operation** — Repair scores `0` because nobody has written what happens
   when the centre is unavailable. Silence means countries will improvise, unevenly.
5. **Add a stopping mechanism** — Selection scores `0`. Name the signal that says an
   automation is failing, and who may stop it without escalation.
6. **Name the revision trigger and owner** — Adaptation scores `0`. Without this, the plan
   cannot respond to the volume growth it predicts for itself.

## 8. Coverage log

```
resource-flow      walked  → 1 candidate  (0 accepted)   A-07
information-flow   walked  → 1 candidate  (1 accepted)   A-02
decision-making    walked  → 3 candidates (1 accepted)   A-01, A-04, A-05
coordination       walked  → 1 candidate  (0 accepted)   A-06
adaptation         skipped → mechanism marked Absent; recorded as gap, not searched
growth             walked  → 0 candidates (0 accepted)   nothing at any level fit the
                             constraint that review capacity is fixed while demand grows
repair             skipped → mechanism marked Absent
selection          skipped → mechanism marked Absent
boundaries         walked  → 1 candidate  (1 accepted)   A-03
renewal            skipped → mechanism marked Absent
```

Seven candidates, three accepted, four rejected — and every one of the seven appears in
section 3 or section 4 by ID. **The log must reconcile with the report.** A log claiming
more candidates than the report shows is either a search that was not recorded or a count
that was invented; both make the coverage claim worthless, and the ID column is what makes
the reconciliation checkable.

**Levels searched**: physical, cells, organisms, social species, ecosystems, evolution — 6
of 7. Cosmic omitted; *reason: no mechanism at that level addresses decision latency or
authority distribution at this timescale.* Physical, ecosystems and evolution were swept and
produced nothing worth carrying forward — recorded here so that absence is visible as a
search result rather than as an omission.

---

# Example 1b — The same plan, repaired (organisational)

**As revised**: *The centre publishes prohibited actions, mandatory controls, and escalation
thresholds. Countries execute inside that envelope without seeking approval, and notify the
centre within 24 hours. Actions outside the envelope escalate. Automated policy scanning runs
in every country, with sampled central audit weighted by risk. If the centre is unreachable
for more than 48 hours, countries continue under the standing envelope and the notification
queue drains on recovery. The envelope is reviewed when an incident occurs or a jurisdiction
changes its rules, whichever comes first; the named owner is the central team lead. A country
security lead may halt any automation in their jurisdiction without escalation.*

Only the mechanisms changed. The intent — prevent unreviewed automation from causing an
incident — is identical.

## Verdict

**Partial natural pattern**

**Score**: 15/24
**Override fired**: none
**Most fragile mechanism**: Diversity — one envelope, one scanning tool, one audit method.

## What changed, and what it bought

| Change | Mechanism | Principle | Was | Now |
|---|---|---|---|---|
| Standards central, execution local | Decision-making | Local autonomy | 0 | 2 |
| Notify within 24h, escalate exceptions | Information flow | Feedback | 0 | 1 |
| Envelope makes actions compatible by construction | Coordination | Coordination | 1 | 2 |
| Continue under standing envelope if centre unreachable | Repair | Repair | 0 | 2 |
| Review on incident or rule change, named owner | Adaptation | Adaptation | 0 | 2 |
| Country lead may halt without escalation | Selection | Selection | 0 | 2 |
| Layered checks replace the single gate | Boundaries | Redundancy | 0 | 1 |
| Envelope is versioned and reviewable | Renewal | Renewal | 0 | 1 |

Unchanged: Diversity `0`, Modularity `1`, Resource limits `1` — the plan still does not say
what happens when audit capacity saturates — and Environmental fit `1`.

**Both overrides clear.** Permanent control no longer fires because a degraded mode is now
*stated*: countries continue under the standing envelope. No adaptation no longer fires
because a revision trigger and a named owner exist. Neither required abandoning central
control — the centre still sets every boundary that matters. What changed is that it stopped
being in the path of every action.

This is the general shape of the repair. An override is almost never cleared by
decentralising; it is cleared by writing down what happens when the centre is unavailable,
and by naming who may change the rule and when.

**Why still Partial and not Established**: three mechanisms have accepted analogues at high
or medium confidence, but Diversity remains `0` — one envelope, one tool, one method, all
failing for the same reason (see E-27). The upgrade guard also requires analogues from more
than one level, which this run satisfies, and fewer than three Absent mechanisms, which it
now satisfies.

---

# Example 2 — Resilience-engineered service platform (software / systems)

**As given**: *Services deploy independently behind versioned APIs. Every release goes out
as a canary to 1% of traffic with automatic rollback on error-rate regression. Calls between
services carry circuit breakers and timeouts. Each service owns an error budget; exceeding
it freezes feature work until reliability is restored. Failure injection runs weekly in
production. Services are retired on a published deprecation calendar.*

## Verdict

**Established natural pattern**

**Score**: 21/24
**Override fired**: none
**Most fragile mechanism**: Diversity — every failure response is real, but they share one
deployment pipeline and one region.

Detail, guard checks and coverage log follow the scorecard below.

## The problem, restated

> We need many independently-changing components to keep serving users correctly while
> individual components fail unpredictably and change continuously.

**Horizon**: indefinite, with continuous growth in both component count and traffic.

## Mechanism map

All ten Present. Growth is the weakest: the plan describes how components change, not what
breaks as component count rises.

## Accepted analogues

| ID | Analogue | Level | Mechanism | Confidence |
|---|---|---|---|---|
| A-01 | Homeostasis by negative feedback (E-13) | Organisms | Adaptation, feedback | High |
| A-02 | Innate + adaptive immunity (E-07) | Cells | Repair, boundaries | High |
| A-03 | Layered proofreading (E-10) | Cells | Selection | High |
| A-04 | Modularity and evolvability (E-31) | Evolution | Modularity | High |
| A-05 | Apoptosis (E-09) | Cells | Renewal | Medium |

**A-01 · Homeostasis → error budgets.** Sense the variable, compare to a set point, drive a
response opposing deviation, with graded effectors recruited in order. Error budgets are
this mechanism exactly: an explicit set point, continuous sensing, and a graduated response
ending in a feature freeze. *Breaks down at*: homeostasis fails when sensing delay exceeds
response time, producing oscillation. If the error-budget window is long relative to the
deploy cadence, the freeze arrives after the causing change has been buried under twenty
others. **Check the window against the cadence** — this is the finding.

**A-02 · Immunity → circuit breakers.** Fast local generic response acting without
permission, isolating the affected region before the cause is understood. *Breaks down at*:
autoimmunity. A circuit breaker tuned tight will isolate a healthy dependency during a
traffic spike and convert a slowdown into an outage. The false-positive budget must be
explicit, exactly as in the biological case.

**A-03 · Layered proofreading → canary plus rollback.** Several cheap independent checks
with multiplying error rates, against a preserved reference. Canary-at-1% is the proofreading
step; the previous version is the intact reference strand. *Breaks down at*: DNA repair fails
on double-strand breaks, where no intact reference remains. The equivalent is a migration
that alters persistent state irreversibly — rollback restores the code and not the data. The
mechanism offers no protection there, and the plan should say so.

**A-04 · Modularity and evolvability → versioned APIs.** Stable interfaces, variable
internals, change as recombination rather than redesign. *Breaks down at*: deeply conserved
interfaces become nearly impossible to change precisely because everything depends on them.
Expect the most successful API to become the most permanent constraint.

**A-05 · Apoptosis → deprecation calendar.** Removal is orderly, scheduled, and does not
damage neighbours. *Breaks down at*: in the cell, **removal is the default** — survival must
be continuously earned by receiving signals. A deprecation calendar **defaults to
retention**: something must be actively proposed for removal, and proposing it costs someone
political capital. That inversion is why services accumulate, and reversing it — services
expire unless renewed — would be the stronger version. (Note the polarity carefully: E-09
describes the same fact as "survival is default-off". Say which thing is defaulted, never
just "default-on", or the recommendation inverts.)

## Rejected analogues

| ID | Candidate | Failed test | Reason |
|---|---|---|---|
| A-06 | Service mesh as mycelium (E-23) | Constraints, mechanism, scale | Resemblance is purely visual; see the worked failure in `04-validity-tests.md` |
| A-07 | Chaos testing as natural selection (E-28) | Comparable mechanism | Selection requires *heritable variation* — surviving variants must propagate their differences. Failure injection tests robustness; it does not generate or inherit variation. Useful practice, wrong analogue |

A-07 matters: the plan's own documentation calls chaos testing "evolutionary". It is not,
and the mislabel invites the expectation that the system will improve on its own.

## Scorecard

| # | Principle | Score | Evidence |
|---|---|---|---|
| 1 | Feedback | 2 | Error rate sensed continuously, routed to the owning team, acts within the deploy cycle |
| 2 | Adaptation | 2 | Error budget is a named trigger with a named owner and a bounded response |
| 3 | Redundancy | 2 | Circuit breakers plus independent deployability; alternates verified weekly by injection |
| 4 | Diversity | 1 | Multiple failure responses exist, but one deployment pipeline and one cloud region — correlated failure unaddressed (E-27) |
| 5 | Modularity | 2 | Versioned APIs; services demonstrably change independently |
| 6 | Local autonomy | 2 | Teams deploy without central approval inside the error budget |
| 7 | Coordination | 2 | API versioning makes local action compatible by construction; cost does not grow super-linearly |
| 8 | Resource limits | 1 | Error budget bounds reliability spend; no stated limit on component count or on the platform team's review capacity |
| 9 | Repair | 2 | Automatic rollback, exercised weekly in production |
| 10 | Selection | 2 | Error budget freeze is a defined signal with a named owner, and it has fired |
| 11 | Renewal | 1 | Deprecation calendar exists but is default-off; nothing expires on its own |
| 12 | Environmental fit | 2 | Load profile characterised; assumptions stated with falsifying conditions |
| | **Total** | **21/24** | |

## Verdict

**Established natural pattern** — 21/24. No override fired.

**Upgrade guard checked**: high-confidence accepted analogue for the dominant mechanism
(information flow / repair) ✓ · six of seven levels searched ✓ (see coverage log) · zero
Absent mechanisms ✓ · analogues drawn from three levels ✓ (more than one is the requirement).

## Coverage log

```
resource-flow      walked  → 1 candidate  (0 accepted)
information-flow   walked  → 2 candidates (1 accepted)   A-01
decision-making    walked  → 1 candidate  (0 accepted)
coordination       walked  → 1 candidate  (0 accepted)   A-06 rejected
adaptation         walked  → 1 candidate  (1 accepted)   A-01 (shared)
growth             walked  → 0 candidates (0 accepted)   no analogue for component-count growth
repair             walked  → 2 candidates (2 accepted)   A-02, A-03
selection          walked  → 2 candidates (1 accepted)   A-03 (shared), A-07 rejected
boundaries         walked  → 1 candidate  (1 accepted)   A-02 (shared)
renewal            walked  → 1 candidate  (1 accepted)   A-05
```

**Levels searched**: physical, cells, organisms, social species, ecosystems, evolution — 6
of 7. Cosmic omitted; *reason: nothing at that level operates at millisecond cycle times.*
Accepted analogues come from three levels — cells, organisms, evolution.

**Most fragile**: Diversity (1). Every failure response is real, but they share a
deployment pipeline and a region. E-27 is explicit: redundancy pays only when the copies
fail for *different* reasons. Three replicas behind one pipeline are one replica.

**What to change**, in order: audit alternates for shared dependencies (E-27); check the
error-budget window against deploy cadence for oscillation (E-13); state that rollback does
not cover irreversible state migrations (E-10); invert the deprecation default so services
expire unless renewed (E-09); stop calling failure injection "evolutionary" (A-07).

---

# Example 3 — Five-year predictive reskilling programme (policy)

**As given**: *A national programme forecasts which occupational skills will be in demand in
five years, and funds training places accordingly. Allocations are set at programme start
and held stable to give providers planning certainty.*

## The problem, restated

> We need to commit large fixed resources now to build capabilities that will only be usable
> years from now, in a labour market whose future composition nobody can observe.

**Horizon**: five years. **Shocks**: technology shifts, sectoral collapse, migration,
recession, a competing national programme.

## Verdict

**Contrary to natural patterns**

**Score**: 4/24
**Override fired**: **perfect prediction** *and* **no adaptation**
**Most fragile mechanism**: Information flow — nothing in the plan would detect that its
central forecast was wrong.

Reasoning follows below.

## Mechanism map

| Mechanism | Mark |
|---|---|
| Resource flow | Present — fixed allocations, no reallocation path |
| Information flow | **Absent** — no mechanism senses whether the forecast is proving right |
| Decision-making | Present — decided once, at the start |
| Coordination | Present — central allocation to providers |
| Adaptation | **Absent** — stability is stated as a design goal |
| Growth | N/A — *fixed programme size* |
| Repair | **Absent** |
| Selection | **Absent** — no mechanism to stop a stream training for a collapsed occupation |
| Boundaries | Present — eligibility criteria |
| Renewal | **Absent** |

Five mechanisms Absent. The assessment is essentially complete before any analogue is
considered.

## Analogues

**Rejected — A-01 · Circadian anticipation (E-17).** The plan's implicit analogue: prepare
in advance for a predictable change. Fails **Test 2 (constraints)**. Circadian anticipation
works because the environmental cycle is genuinely reliable — the sun has risen on schedule
for billions of years — and the clock re-entrains when cues shift. A five-year labour market
is neither reliably cyclic nor re-entraining. As E-17 puts it: anticipation applied to a
non-cycle is bias with a schedule.

### Absent-mechanism critiques

Adaptation, Selection, Renewal and Information flow are all marked Absent, so no analogue
here *supports* the plan. The two below are `applied as critique` — they show what the
missing mechanism would have to do. Per `02-mechanisms.md` they are labelled, reported
separately, and excluded from the accepted count in the coverage log.

**A-02 · Variation, selection, inheritance (E-28) — applied as critique (Adaptation,
Selection, both Absent).** Where the environment is not modellable, nature does not forecast. It runs many variants
against reality simultaneously and lets outcomes select. This is the mechanism that solves
the plan's actual problem, and the plan does the opposite: one prediction, committed, held
stable. *Breaks down at*: evolution needs cheap survivable failure and many iterations.
Trainees are not disposable variants — a failed training place is a person's two years. So
the transfer is **not** "run reskilling like natural selection"; it is narrower: allocate in
tranches, measure placement outcomes per stream, and shift subsequent tranches toward what
is placing. The variation is in the *allocation*, not in the people.

**Accepted — A-03 · Response diversity and the portfolio effect (E-27).** Aggregate function
stays steady when components respond *differently* to the same disturbance. Funding a
spread of skill types whose demand is uncorrelated protects the programme's aggregate
outcome without requiring any forecast to be right. *Breaks down at*: this is deliberately
inefficient in the expected case, and pays only across the distribution of futures — a
political cost, not a technical one.

**A-04 · Bone remodelling (E-16) — applied as critique (Information flow, Absent).**
Capacity follows measured strain; unused capacity is reclaimed. The plan has no equivalent
sensing at all, which is what this critique exposes. *Breaks down at*: bone remodels over
months, and its signal is present strain, so unloaded-but-critical and unloaded-and-obsolete
are identical inputs — a skill in a temporary downturn would be dismantled. Protection for
strategically important but currently-idle streams has to be explicit.

## Scorecard

| # | Principle | Score | Evidence |
|---|---|---|---|
| 1 | Feedback | 0 | No mechanism senses whether the forecast is proving correct |
| 2 | Adaptation | 0 | Stability is stated as a design goal; no revision path |
| 3 | Redundancy | 0 | One forecast, no alternate scenario funded |
| 4 | Diversity | 0 | Allocation follows a single predicted demand curve |
| 5 | Modularity | 1 | Streams are separable in principle; allocations are locked together |
| 6 | Local autonomy | 0 | Providers cannot vary intake against local demand |
| 7 | Coordination | 2 | Central allocation does produce consistent national coverage |
| 8 | Resource limits | 1 | Budget stated; no statement of what happens if placement rates collapse |
| 9 | Repair | 0 | No recovery path for a stream training into a collapsed occupation |
| 10 | Selection | 0 | Nothing can be stopped mid-programme |
| 11 | Renewal | 0 | No retirement path for obsolete streams |
| 12 | Environmental fit | 0 | The plan assumes a forecastable five-year labour market; the assumption is not stated as one |
| | **Total** | **4/24** | |

## Verdict

**Contrary to natural patterns** — 4/24.

**Override fired: perfect prediction.** The programme's correctness rests entirely on a
five-year forecast, with no revision path when it is wrong and no mechanism that would even
detect that it was wrong. A second override, **no adaptation**, also fires — Adaptation was
marked Absent.

The band alone would have said Contrary here anyway. The override matters because it would
still say Contrary if the plan scored 20: a plan with excellent coordination, clear
boundaries, and strong provider relationships that still cannot notice its central forecast
failing is not a durable plan. It is a well-run bet.

**What to change**: allocate in tranches rather than once (E-28); fund a spread of
uncorrelated skill types instead of the single predicted curve (E-27); measure placement
outcomes per stream and let subsequent tranches follow measured demand (E-16); name who may
stop a stream, and on what signal (E-09/E-28); state the forecast as an assumption with the
conditions that would falsify it — that one comes from the Environmental fit anchor in
`05-scoring.md`, not from any analogue in this run.

None of these requires abandoning the programme. They require moving the commitment point
later and making the allocation responsive to evidence the programme is already positioned
to collect.

## Coverage log

```
resource-flow      walked  → 2 candidates (0 accepted)   fixed allocation, no reallocation
                             path — nothing transferable found
information-flow   skipped → mechanism marked Absent; A-04 recorded as critique
decision-making    walked  → 1 candidate  (0 accepted)   A-01 rejected at Test 2
coordination       walked  → 1 candidate  (0 accepted)
adaptation         skipped → mechanism marked Absent; A-02 recorded as critique
growth             n/a     → fixed programme size, stated at the outset
repair             skipped → mechanism marked Absent
selection          skipped → mechanism marked Absent; A-02 covers it as critique
boundaries         walked  → 1 candidate  (1 accepted)   A-03
renewal            skipped → mechanism marked Absent
```

One accepted analogue (A-03); one rejected (A-01); two critiques (A-02, A-04) excluded from
the accepted count. Five mechanisms skipped as Absent — which is the finding, not a gap in
the search.

**Levels searched**: physical, cells, organisms, social species, ecosystems, evolution — 6
of 7. Cosmic omitted; *reason: no mechanism at that level addresses the present mechanisms
at this timescale.*

## Limits of this assessment

This test measured structural durability under uncertainty. It says nothing about whether
the programme is worth funding, whether reskilling is the right instrument, or whether the
occupations chosen are the right ones. A programme can be **Contrary to natural patterns**
and still be the correct thing to do — the finding is that it will not notice if it is
wrong, not that it is wrong.

Not assessed: actual placement data (none supplied), provider capacity, and the political
constraints that produced the fixed-allocation design in the first place. The last of these
is likely the real reason the plan looks like this, and it is outside what this test can see.

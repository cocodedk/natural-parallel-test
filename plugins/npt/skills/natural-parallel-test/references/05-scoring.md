# Step 7 & 8 — Scoring and Classification

**Purpose**: turn the assessment into a repeatable score and one of four classifications.
**Output**: twelve principles scored 0–2 with cited evidence, a total, and a classification.
**Read this when**: analogues have been tested and breaking points written.

## Scoring rules

Score `0` absent · `1` partially present · `2` clearly present. Maximum 24.

**Evidence rule**: score from evidence only.

- `2` requires a **specific named mechanism** in the plan — who, what trigger, what action.
- `1` requires a stated intention *without* a mechanism, or a mechanism covering only part
  of the system.
- `0` is the default when the plan is silent. **Silence is `0`, not `1`.**

**Insufficient evidence rule**: if you cannot cite a passage, mechanism, or prior incident
supporting a score, do not guess. Record "unable to determine — insufficient evidence" and
state what evidence would resolve it. An unresolved principle is excluded from the total and
the total is reported as `n/22` (or whatever the denominator becomes), never silently
rebased to look complete.

**N/A**: if a principle genuinely does not apply, mark N/A with a one-line reason and
reduce the denominator. Reserve this; most N/A claims are really `0`.

**Cite every score.** One line: the passage, the mechanism, or the prior incident. A score
without a citation is an opinion wearing a number.

## The twelve principles with anchors

### 1. Feedback — *can the system detect the results of its actions?*

| | |
|---|---|
| `0` | No measurement of outcomes. Activity may be tracked; results are not |
| `1` | Outcomes measured, but the measurement does not reach anyone able to act, or arrives too late to matter |
| `2` | Outcomes measured, routed to someone with authority to respond, within a stated interval shorter than the response it should trigger |

*Common error: counting activity metrics as feedback. Tickets closed is activity; incidents
prevented is feedback.*

### 2. Adaptation — *can it change without being completely redesigned?*

| | |
|---|---|
| `0` | No revision path. Changing the plan means replacing it |
| `1` | Review exists but is calendar-driven only, or requires re-approval by the original authority |
| `2` | Named triggers, a named owner empowered to revise, and a bounded scope of change that does not require rebuilding |

### 3. Redundancy — *can one component fail without destroying everything?*

| | |
|---|---|
| `0` | At least one component whose failure stops the whole plan, unmitigated |
| `1` | Backups exist for some critical components, or exist on paper but are untested |
| `2` | Every identified critical component has a tested alternate, and the alternates do not share a dependency (see E-27) |

*Duplicate components that fail for the same reason score `1`, not `2`.*

### 4. Diversity — *are there multiple ways to solve the same problem?*

| | |
|---|---|
| `0` | Exactly one approach, method, supplier, or route |
| `1` | Alternatives exist but are not resourced, or are variants of one underlying approach |
| `2` | Genuinely different approaches run concurrently with resources, and they fail for different reasons |

### 5. Modularity — *can one part change without destabilising the whole?*

| | |
|---|---|
| `0` | Changes anywhere require coordinated change elsewhere; no stable interfaces |
| `1` | Boundaries exist but are crossed routinely, or interfaces change with implementations |
| `2` | Explicit interfaces, versioned or otherwise stabilised, with parts demonstrably changed independently |

### 6. Local autonomy — *can local parts respond without waiting for central permission?*

| | |
|---|---|
| `0` | All actions require central approval; no local decision rights |
| `1` | Local action permitted within limits that are informal, undocumented, or routinely overridden |
| `2` | Written scope of local authority, an emergency path that does not require permission, and a defined escalation exception |

*This principle and #7 must be scored together. High autonomy with low coordination is
fragmentation; low autonomy with high coordination is the bottleneck.*

### 7. Coordination — *can local actions still support the larger system?*

| | |
|---|---|
| `0` | Local actions can conflict with no mechanism to detect or resolve it |
| `1` | Coordination by meeting, goodwill, or shared documents — cost grows with every added part |
| `2` | Shared standards, signals, or interfaces that make local actions compatible by construction, at a cost that does not grow super-linearly |

### 8. Resource limits — *does the plan recognise finite energy, money, and attention?*

| | |
|---|---|
| `0` | No stated limits, or limits stated only in money while attention and capacity are treated as unbounded |
| `1` | Budget stated; the binding constraint — usually senior attention or a specialist team's hours — is not identified |
| `2` | The binding constraint is named with a magnitude, its growth versus demand is stated, and behaviour at saturation is defined |

*Very few plans score `2`. The test is whether the plan says what happens when the scarce
resource runs out.*

### 9. Repair — *can damaged parts be restored or replaced?*

| | |
|---|---|
| `0` | No recovery path for any identified failure |
| `1` | Recovery described but untested, unowned, or dependent on the same people running normal operations with no slack |
| `2` | Recovery path per identified failure, owned, exercised, with capacity that does not fully displace normal work — and the system can run degraded |

### 10. Selection — *can failing ideas be stopped?*

| | |
|---|---|
| `0` | No stopping mechanism. Things end by exhaustion, reorganisation, or not at all |
| `1` | Stopping is possible but requires escalation, or costs the proposer politically, so it rarely happens |
| `2` | Defined failure signals, a named person able to stop, and evidence of something actually having been stopped |

*The most commonly absent of the twelve. Ask for an example of something stopped in the last
year; if there is none, the answer is `0` regardless of policy.*

### 11. Renewal — *can old structures be retired safely?*

| | |
|---|---|
| `0` | No retirement path; old structures accumulate |
| `1` | Retirement possible but ad hoc, or requires the system to stop |
| `2` | Defined retirement path exercised without halting operation, with someone accountable for noticing obsolescence |

### 12. Environmental fit — *is the plan suited to the conditions where it will operate?*

| | |
|---|---|
| `0` | Environment not characterised, or the plan assumes conditions that do not hold |
| `1` | Environment described but the plan's assumptions about it are not stated as assumptions |
| `2` | Environment characterised with the plan's assumptions written explicitly, including what would falsify them |

## Bands and classification

Bands set the **default**. The overrides below outrank them.

| Total (of 24) | Default classification |
|---|---|
| 19–24 | Established natural pattern |
| 12–18 | Partial natural pattern |
| 6–11 | Partial natural pattern, fragile — name the three weakest principles in the verdict |
| 0–5 | Contrary to natural patterns |

Adjust the denominator for N/A and unresolved principles and report the fraction, e.g.
`14/22`. Do not convert to a percentage; it implies precision the method does not have.

**Never compare a reduced total to the raw table.** When the denominator is below 24,
compute `round(total × 24 / denominator)` and read *that* against the bands, stating both
figures — e.g. `12/16 → 18 equivalent → Partial natural pattern`. Without this a plan with
six N/A principles scoring a perfect `12/12` would read as *Partial*, and a plan scoring
`5/16` would read as *Contrary*, purely from the size of the denominator.

### The four classifications

**Established natural pattern** — a close analogue exists for the plan's dominant
mechanisms, with similar constraints and a mechanism the plan can actually instantiate.
Requires at least one `accepted` analogue at high or medium confidence for the dominant
mechanism, not merely a high score.

**Partial natural pattern** — some mechanisms have strong analogues; others are unsupported
or absent. The most common result. The report's value here is the *list of unsupported
mechanisms*, not the score.

**Novel but compatible** — no close analogue was found, but the plan follows durable
natural principles. Legitimate and not a lesser result. Requires an honest search across at
least five levels with the coverage log to show it. Distinguish carefully from "we did not
look hard enough".

**Contrary to natural patterns** — the plan depends on something nature does not sustain.
Gets the strongest challenge and the plainest wording.

### Overrides — these beat the band

Classify **Contrary to natural patterns** regardless of total if any of these hold. Name
which one triggered it.

| Dependency | Test |
|---|---|
| **Permanent control** | Operation requires a specific central authority to be continuously available, with no defined degraded mode when it is not |
| **Unlimited growth** | Growth is planned against a resource with no stated limit, or the binding constraint does not grow with demand and this is unaddressed |
| **Perfect prediction** | Correctness depends on a forecast being right, with no revision path when it is wrong |
| **No failure** | No component is permitted to fail; there is no failure mode analysis and no degraded operation |
| **No adaptation** | No revision path exists at all — the Adaptation mechanism was marked Absent |

A plan scoring 20/24 that cannot operate when one team is unavailable is **Contrary**, not
Established. The override exists because twelve generous readings should never outvote one
structural dependency.

### Upgrade guard

Do **not** classify **Established** when any of these hold, whatever the total:

- No `accepted` analogue at high or medium confidence for the plan's dominant mechanism.
- The coverage log shows fewer than five levels searched.
- Three or more mechanisms marked Absent.
- Every analogue came from a single level.

## Reporting the score

State the total, the denominator, the classification, whether an override fired, and the
three weakest principles by name. Then the sentence that matters:

> A low score does not prove failure. It shows where the plan is fragile.

Score inflation is the standard failure of this step. If a run produces a higher score than
the previous run of the same plan and the plan did not change, the scoring drifted — re-read
the anchors. Every principle at `1` is a signature of scoring by impression rather than
evidence; `1` should be the *least* common score, not the most.

## Handoff

Assemble the report using [`07-report-template.md`](07-report-template.md).

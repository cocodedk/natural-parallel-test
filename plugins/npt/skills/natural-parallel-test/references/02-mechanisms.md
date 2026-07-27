# Step 2 — Decompose the Plan Into Mechanisms

**Purpose**: split the plan into parts that can each be searched separately.
**Output**: the ten mechanisms, each marked present / absent / not applicable, with the
probing answers that justify the mark.
**Read this when**: the problem statement from Step 1 is written.

## Why decompose

A plan almost never has one natural parallel. It has a strong parallel for how information
moves, a weak one for how decisions are made, and none at all for how old parts are
retired. A single global analogy — "the company is an organism" — averages those together
and hides exactly the mechanism that will fail.

Decomposing also prevents the most common cheat in this method: finding one satisfying
analogy and declaring the plan natural.

## The ten mechanisms

For each, the framework question, the probes that make it answerable, and what a missing
answer usually means.

### 1. Resource flow

> How do energy, money, people, or materials move?

- Where do resources enter the system, and who decides that?
- What path do they take to the point of use? How many hops?
- Can resources move *toward* demand, or only along fixed allocations?
- What happens to surplus? What happens to a shortfall mid-period?
- Is there any storage or buffer, or is it flow-to-consumption?

*No buffer and no reallocation path is the signature of a plan that works only while
demand is predictable.*

### 2. Information flow

> How does the system detect what is happening?

- What is sensed, where, and by whom?
- How far does a signal travel before it reaches someone who can act on it?
- What is the delay between an event and its detection?
- Is any signal aggregated or filtered on the way, and who chooses the filter?
- What information exists locally but never leaves?

*Distance between sensing and acting is the most predictive single measurement in this
framework. Record it explicitly.*

### 3. Decision-making

> Who decides, and using what information?

- Name the decider for each class of decision.
- Do they hold the information from mechanism 2, or a summary of it?
- What is the decision latency, worst case?
- What happens to decisions when the decider is absent or saturated?
- Are there decisions nobody owns?

### 4. Coordination

> How do separate parts work together?

- What makes independent parts act compatibly — shared standard, shared signal, shared
  schedule, direct negotiation, or central instruction?
- Is coordination continuous or episodic?
- What is the cost of coordination per added part? Does it grow linearly or worse?
- Can two parts conflict without anyone noticing?

### 5. Adaptation

> How does the plan change when reality changes?

- What triggers a change — a threshold, a review date, an incident, someone's judgement?
- Who is allowed to change what, without permission?
- How long from "reality changed" to "plan changed"?
- Is there a version of the plan, or does it change silently?

### 6. Growth

> How does it expand without collapsing?

- What is the intended growth path, and what breaks first as it grows?
- Which costs scale super-linearly with size — coordination, review, communication?
- Is there a size beyond which the plan is known not to work? Is that written down?
- Does growth consume the resource that enables it?

### 7. Repair

> How does it recover from damage?

- What is the recovery path for each named failure from Step 1 question 7?
- Who performs repair, and are they the same people running normal operations?
- Is there spare capacity for repair, or does repair displace normal work?
- Can the system operate degraded, or only fully working / fully stopped?

### 8. Selection

> How are bad ideas removed and good ones retained?

- What is the mechanism for stopping something that is failing?
- Who is allowed to stop it, and what does stopping cost them personally?
- Is there a defined signal for "this is not working", or only opinion?
- How long can a failing effort continue before something forces the issue?

*A plan with no stopping mechanism accumulates commitments until the resource base fails.
This is the most commonly absent mechanism of the ten.*

### 9. Boundaries

> What keeps harmful things outside?

- What is inside the system, what is outside, and what crosses?
- What is filtered at the boundary, and by what?
- Is the boundary uniform, or are there privileged paths through it?
- What happens when the boundary is breached — detection, containment, neither?

### 10. Renewal

> How are old parts replaced?

- What is the retirement path for a component, process, or role?
- Is anything currently un-retirable, and why?
- Who notices that something is obsolete?
- Does renewal require the system to stop?

## Marking each mechanism

Three marks, and the distinction matters because scoring depends on it:

| Mark | Meaning | Consequence |
|---|---|---|
| **Present** | The plan specifies this mechanism, even poorly | Search for analogues; score on the anchors |
| **Absent** | The mechanism is needed but the plan is silent | Do **not** search for analogues. Record as a gap. Related principles score `0` |
| **Not applicable** | The mechanism genuinely does not arise for this plan | State a one-line reason. Excluded from scoring as N/A |

**Absent is not the same as not applicable.** A plan with no Selection mechanism is not a
plan that does not need one. Reserve *not applicable* for genuine cases — a
three-month fixed-scope migration may legitimately have no Growth mechanism — and require
a written reason every time. If the reason takes more than one line, it is Absent.

**Do not search for analogues for an Absent mechanism.** Finding a beautiful natural
parallel for a mechanism the plan does not have produces a report describing a plan that
does not exist. Record the gap and move on.

**One exception: critique.** An analogue may be searched for an Absent mechanism when it is
used to show *what the missing mechanism would have to do* — that is an argument about the
gap, not a description of the plan. Label it `applied as critique`, report it in a separate
section, and exclude it from the accepted count in the coverage log. Without the label it
reads as support for a mechanism that is not there.

## Mechanism → principle mapping

Which of the twelve scored principles each mechanism supplies evidence for. Used in Step 7;
one mechanism can inform several principles.

| Mechanism | Principles it primarily informs |
|---|---|
| Resource flow | Resource limits, Redundancy |
| Information flow | Feedback, Local autonomy |
| Decision-making | Local autonomy, Coordination, Feedback |
| Coordination | Coordination, Modularity |
| Adaptation | Adaptation, Feedback |
| Growth | Resource limits, Environmental fit, Modularity |
| Repair | Repair, Redundancy |
| Selection | Selection, Diversity |
| Boundaries | Modularity, Environmental fit |
| Renewal | Renewal, Adaptation |

## Worked decomposition

The central cybersecurity approval plan from `01`:

| Mechanism | Mark | Note |
|---|---|---|
| Resource flow | Present | Central team's review hours; fixed supply, growing demand; no buffer, no reallocation |
| Information flow | Present | Local context must travel to the centre as a written submission; heavy filtering, days of delay |
| Decision-making | Present | Central team decides everything; no local decision rights of any kind |
| Coordination | Present | Achieved by making every action pass one point — coordination cost grows with every country added |
| Adaptation | **Absent** | No trigger, no owner, no revision path stated |
| Growth | Present | Growth path is "more countries"; review capacity does not grow with it |
| Repair | **Absent** | No stated behaviour when the central team is unavailable |
| Selection | **Absent** | No mechanism to stop a failing automation or to retire the approval process itself |
| Boundaries | Present | The approval gate *is* the boundary; single, uniform, no privileged fast path |
| Renewal | N/A | No components old enough to retire within the stated horizon — *reason: programme is new* |

Six present, three absent, one N/A. The three absences — Adaptation, Repair, Selection —
are the assessment before a single analogue has been considered.

## Handoff to Step 3

Carry forward: the present mechanisms with their probe answers and constraints, and the
absent ones as gaps. Search only the present ones, using
[`03-analogue-library.md`](03-analogue-library.md).

# Step 1 — State the Problem, Not the Solution

**Purpose**: stop the proposed solution from controlling the search for analogues.
**Output**: a one-paragraph problem statement plus answers to seven defining questions.
**Read this when**: starting any assessment. This step is mandatory and cannot be skipped.

## Why this step exists

If the plan is described as *"we need a central management platform"*, every analogue found
afterwards will be an argument for central management platforms. The brain will come up.
The queen bee will come up — wrongly, since a queen does not direct a colony. The search
becomes a justification exercise.

Described as a problem — *"we need to coordinate many independent actors while conditions
keep changing"* — the same search yields immune systems, ant pheromone trails, market price
signals, mycorrhizal networks, and vertebrate nervous systems, each with a different
mechanism and a different failure mode. Some will beat the platform. That is the point.

## The rewrite

Write one sentence containing **no nouns naming a solution**. Banned from the problem
statement: platform, team, committee, dashboard, framework, board, process, service,
policy, tool, hub, layer, pipeline, standard, portal.

| Solution form (wrong) | Problem form (right) |
|---|---|
| We need a central management platform. | We need to coordinate many independent actors while conditions keep changing. |
| We'll create a governance board to approve all AI use. | We need to prevent a class of high-consequence mistakes across units we do not directly observe. |
| We'll build a service mesh. | We need many independently-deployed components to find each other and keep talking as membership changes constantly. |
| We need a quarterly planning process. | We need to commit finite resources ahead of information we do not yet have, and revise as it arrives. |
| We'll hire a Head of Platform. | We need one point of accountability for shared infrastructure whose costs are spread across teams that do not pay for it. |
| We need a data lake. | We need information generated in one place to be usable in another, later, by people who did not produce it. |

If you cannot write the sentence without a solution noun, the plan may be a solution in
search of a problem. Record that as the first finding.

## The seven defining questions

Answer all seven. Each one supplies constraints that later steps test analogues against; an
unanswered question weakens every validity test downstream.

### 1. What must the plan achieve?

The function, stated as an outcome in the world, not as an activity. "Approve automations"
is an activity. "Prevent unreviewed automation from causing an incident" is a function.

### 2. What resources does it consume?

Money, headcount, attention, compute, goodwill, political capital. Give magnitudes in the
plan's own units. "Two FTE and about 15 hours of senior attention per month" tests
differently from "a team of forty".

Attention is the resource most often omitted and most often the binding one.

### 3. What information does it need?

What must the plan *know* to work, where does that knowledge live, and how far is it from
where the decision is made? Distance between information and decision is the single most
predictive constraint in this whole framework.

### 4. What environment does it operate in?

Market, regulator, org size, geography, load, culture, competitors. Is the environment
stable, cyclical, or turbulent? Analogues admissible in a stable environment are not
admissible in a turbulent one.

### 5. What can change unexpectedly?

List concrete shocks, not "change" in the abstract: a regulation lands, a key person
leaves, traffic goes up 10×, a supplier fails, a budget is cut mid-year, a competitor
launches. These become the test cases for Adaptation, Repair, and Redundancy.

### 6. How long must it survive?

A quarter, a fiscal year, five years, a decade. This sets scale admissibility. Evolutionary
analogues require many generations of selection; a two-quarter plan cannot borrow from them
and should not pretend to.

### 7. What happens when one part fails?

Not *if*. Trace one concrete failure end to end. If the honest answer is "everything stops",
that is a Redundancy `0` and probably a Modularity `0`, established before scoring begins.

## Worked rewrite

**As given**

> One central team will approve and control every cybersecurity automation across many
> countries.

**As a problem**

> We need to prevent a class of high-consequence mistakes across many units operating under
> different local conditions, when the people who understand each local condition are not
> the people who hold the authority to act.

**The seven answers**

| # | Question | Answer |
|---|---|---|
| 1 | Function | Prevent unreviewed automation from causing a security or availability incident, without stopping automation from happening |
| 2 | Resources | One central team; their review time is the scarce resource, and it does not grow when the number of countries does |
| 3 | Information | Local system context, local regulation, local risk appetite — all of which live in the countries, not in the central team |
| 4 | Environment | Many jurisdictions, differing regulation, uneven local maturity, continuous change in the automation itself |
| 5 | Shocks | A new regulation in one country; a critical vulnerability needing action in hours; the central team losing two people; automation volume tripling |
| 6 | Timescale | Multi-year, and the volume grows throughout |
| 7 | One part fails | If the central team is saturated or unavailable, **all** countries stop, or they proceed unreviewed. Both are failures |

Notice what the problem form exposes before any analogue is considered: the information
needed for the decision is structurally distant from the authority to decide, and the
scarce resource does not scale with demand. Those two facts drive the entire assessment.

## Common failures in this step

| Failure | How to spot it | Fix |
|---|---|---|
| Solution smuggled in as a noun | The banned-word list hits | Rewrite until it does not |
| Function stated as activity | "Manage", "oversee", "coordinate" with no outcome | Ask "so that what?" until an outcome appears |
| Resources omitted | No numbers anywhere | Demand magnitudes; approximate is fine, absent is not |
| Environment stated as "the business" | No regulator, load, or competitor named | Ask what would have to change for the plan to become wrong |
| Timescale left open | "Ongoing" | Force a horizon; it gates which analogues are admissible |
| Failure question answered "it won't" | Confidence instead of a trace | Trace one specific component failing and follow it |

## Handoff to Step 2

Carry forward: the problem sentence, the seven answers, and any finding already visible
from the answers themselves. Then decompose into mechanisms using
[`02-mechanisms.md`](02-mechanisms.md).

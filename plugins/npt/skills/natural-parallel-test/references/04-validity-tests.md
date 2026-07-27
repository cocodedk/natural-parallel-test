# Step 4 — Test Whether the Analogy Is Real

**Purpose**: reject analogues that resemble the plan without sharing its mechanism.
**Output**: each candidate marked `pass` / `partial` / `fail` on four tests, with an overall
`accepted` or `rejected` verdict and a written reason.
**Read this when**: candidates have been gathered in Step 3.

Most candidates should fail here. A run that accepts everything it found did not test
anything.

## The four tests

### Test 1 — Same problem

> Does the natural system solve a genuinely similar problem?

Compare the **function**, from Step 1 question 1 — not the domain, not the shape, not the
vocabulary.

| Verdict | Condition |
|---|---|
| `pass` | Both systems solve the same functional problem, stated in the same terms without either being stretched |
| `partial` | Overlapping problems where one is a subset of the other, or the match holds only for part of the plan's function |
| `fail` | The problems differ once the metaphor is stripped, or the "similarity" is a shared word |

**Disqualifiers — automatic `fail`:**
- The similarity is structural appearance: branching, layering, a hub, a hierarchy.
- The similarity is vocabulary: both are called "networks", "cells", "ecosystems".
- The natural system's problem can only be made to match by restating it in the plan's
  business terms.

### Test 2 — Similar constraints

> Does it operate under scarcity, uncertainty, delay, competition, or failure?

Check each constraint the plan faces, from Step 1 questions 2–5, against the natural
system. List them; do not assess in the aggregate.

| Verdict | Condition |
|---|---|
| `pass` | The major constraints are shared in kind and roughly in severity |
| `partial` | Most are shared but at least one important constraint differs materially |
| `fail` | The natural system operates without a constraint that dominates the plan, or vice versa |

**The constraint most often missed** is who bears the cost of failure. A natural mechanism
that works because failed units simply die is operating under a constraint the plan almost
certainly does not share — and that difference usually invalidates the transfer.

**Disqualifiers — automatic `fail`:**
- The natural system has unlimited time and the plan has a deadline.
- The natural system tolerates total loss of individual units and the plan cannot.
- The natural system's mechanism **depends on** participants having aligned interests, and
  the plan cannot add a verification or enforcement step to substitute for that alignment.

That last one needs care, because misapplied it rejects almost every social-species and
cellular analogue. Aligned interests are extremely common in nature and rare in
organisations. The question is not *"are the interests aligned?"* but *"does the mechanism
stop working once they are not, and can the plan buy the alignment back?"* If naming a
verification or enforcement step restores the mechanism, score `partial` and record the
required enforcement in `breaks_down_at`. If no such step exists, it is a `fail`.

### Test 3 — Comparable mechanism

> Does it solve the problem through a mechanism your plan can actually use?

This is where most candidates die. Write out the natural mechanism step by step, then write
what the plan would have to do to instantiate it.

| Verdict | Condition |
|---|---|
| `pass` | The mechanism can be instantiated with means available to the plan, and you can name them |
| `partial` | Part of the mechanism transfers; the rest requires something unavailable |
| `fail` | The mechanism depends on a property the plan cannot have — genetic relatedness, physical law, millions of participants, disposable units |

**Disqualifiers — automatic `fail`:**
- The mechanism depends on the participants being genetically near-identical.
- It depends on a physical property with no organisational equivalent.
- It requires population sizes or generation counts outside the plan's reach.
- It relies on a signal that cannot be faked in nature but can be trivially faked here.
- Instantiating it requires exactly the thing the plan was supposed to provide — circular.

### Test 4 — Relevant scale

> Does the pattern still work at your plan's size, speed, and timescale?

Three dimensions, all three must hold.

| Dimension | Ask |
|---|---|
| Size | How many units does the mechanism need? Within an order of magnitude or two of the plan's? |
| Speed | What is the mechanism's cycle time versus the plan's required response time? |
| Timescale | How long must the mechanism run to produce its benefit, versus the plan's horizon from Step 1 question 6? |

| Verdict | Condition |
|---|---|
| `pass` | All three dimensions are compatible |
| `partial` | Two hold; one is stretched but arguably workable — state which |
| `fail` | Any one is off by enough to change the mechanism's behaviour |

**Disqualifiers — automatic `fail`:**
- The mechanism needs thousands of iterations and the plan runs for four quarters.
- The mechanism works at colony scale (10⁴–10⁶) and the plan has twelve people.
- The mechanism's response time is months and the plan needs hours.

## Scoring the verdict

| Pattern | Verdict |
|---|---|
| Four `pass` | **accepted** — high confidence |
| Three `pass`, one `partial` | **accepted** — medium confidence; name the weak test in the report |
| Two `pass`, two `partial` | **accepted** — low confidence; usable as a prompt for thinking, not as support for a decision |
| One `pass`, three `partial` | **rejected** — too little of the mechanism survives to transfer. Record which single test passed |
| Four `partial` | **rejected** — re-run the disqualifier lists first; a candidate partial on all four tests almost always has an unexamined `fail` |
| Any `fail` | **rejected**, regardless of the others |

**One `fail` rejects the candidate.** A candidate that matches beautifully on three tests
and fails the fourth is the most dangerous kind, because the three matches make the failure
feel like a detail. It is not.

Rejected candidates stay in the report with their failing test and reason. They are the
evidence that the search was real.

## Worked failure 1 — "Our company should work like a beehive"

**As offered**: no mechanism, no constraint, no scale. Not yet a candidate — there is
nothing to test. This is the state most nature analogies arrive in.

| Test | Verdict | Reason |
|---|---|---|
| Same problem | `fail` | No problem has been stated. "Like a beehive" names an image |

**Repair**: replace the image with a mechanism from E-18:

> Bees use distributed sensing. Individual scouts assess sites independently and advertise
> in proportion to assessed quality; the colony commits when a quorum forms at one site, not
> when the queen decides and not by unanimity.

Now it can be tested:

| Test | Verdict | Reason |
|---|---|---|
| Same problem | `pass` | Committing a group to one irreversible choice nobody has fully evaluated — genuinely the same problem as a major architecture or market decision |
| Similar constraints | `partial` | Shared: time limit, distributed information, high cost of a bad choice. Differs: bees make one such decision per swarm, irreversibly; firms revisit |
| Comparable mechanism | `partial` | Independent assessment before aggregation transfers directly. Quality-proportional advertising transfers only if advocacy can be weighted by assessment rather than seniority — possible, but it is the whole difficulty |
| Relevant scale | `pass` | Hundreds of scouts, dozens to hundreds of staff. Days for both |

**Verdict: accepted, low confidence.** Transferable principle: have people assess
independently *before* anyone hears the others, weight advocacy by assessed quality, and
commit at an explicit quorum rather than consensus.

**Breaks down at**: every scout shares one colony fate on a one-shot, irreversible choice —
there is no outcome in which a scout does better than the swarm — so its signal has nothing
to gain by lying. Human advocacy usually does have a separate payoff, and the compounding
that makes the mechanism work amplifies a dishonest signal just as efficiently as an honest
one. The transfer is only safe with an independent-assessment stage protected from
influence.

Note the distance between the offered version and the tested one. The first says nothing;
the second yields one concrete practice and one concrete warning.

## Worked failure 2 — "Teams should have an alpha, like a wolf pack"

| Test | Verdict | Reason |
|---|---|---|
| Same problem | `fail` | **The premise is factually wrong.** The "alpha wolf" comes from studies of unrelated captive wolves forced together. Wild wolf packs are families; the "alphas" are the breeding parents, and their position comes from parentage, not from dominance contests. The researcher whose work popularised the term spent years trying to retract it |

**Rejected at Test 1.** Two lessons: the analogue must be factually checked before it is
tested, and an analogy that flatters an existing preference deserves more scrutiny, not
less. This one survived for decades because people liked it.

## Worked failure 3 — "Our microservice mesh is like mycelium"

| Test | Verdict | Reason |
|---|---|---|
| Same problem | `partial` | Both connect many parties for exchange, but mycelium trades *substances* between organisms that cannot move; a mesh routes requests between components that can be redeployed freely |
| Similar constraints | `fail` | Fungal networks operate over months against partners who cannot relocate or renegotiate. A mesh operates in milliseconds with fully reconfigurable membership. Timescale and mobility both differ decisively |
| Comparable mechanism | `fail` | The actual mechanism is bilateral reciprocal allocation with sanctioning of poor partners. A service mesh has no equivalent — services do not choose partners by returned value |
| Relevant scale | `fail` | Milliseconds versus months |

**Rejected on three tests.** The resemblance is entirely visual: both are drawn as
branching networks. Note also that the popular version of this analogue — trees generously
sharing resources — is itself contested (E-23), so the appealing version was never
available.

## Common ways this step gets skipped

| Symptom | What it means |
|---|---|
| Every candidate accepted | The tests were applied as narrative, not as tests. Re-run with the disqualifier lists |
| No rejected candidates in the report | Either the search was too narrow or the testing did not happen |
| All four verdicts `partial` | Almost always an unexamined `fail`. Find which test the candidate genuinely fails |
| Verdicts assigned before the mechanism is written out | Test 3 cannot be assessed without the step-by-step. Write it |
| Reason field restates the verdict | "Fails because it is not comparable" is not a reason. Name the specific property |

## Handoff to Steps 5 & 6

Accepted candidates go to Step 5 — rewrite each transferable principle in the plan's own
vocabulary, using the table at the end of
[`03-analogue-library.md`](03-analogue-library.md).

Every accepted candidate then goes to Step 6,
[`06-limits-and-fallacies.md`](06-limits-and-fallacies.md), to have its breaking point
written out. An accepted analogue without a stated limit is not finished.

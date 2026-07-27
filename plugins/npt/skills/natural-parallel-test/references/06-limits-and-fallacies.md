# Step 6 — Find Where the Analogy Breaks

**Purpose**: state the limit of every accepted analogue, and guard against the reasoning
errors this method invites.
**Output**: a `breaks_down_at` line for each accepted candidate, plus any fallacy findings.
**Read this when**: candidates have been accepted in Step 4.

**An accepted analogue without a stated limit is not finished.** The limit is the most
useful part of the finding, because it says where the borrowed principle stops applying —
which is exactly where a plan built on it will fail.

## The six questions

Ask all six of every accepted analogue. Any "yes" that the plan cannot match is the
breaking point.

### 1. What does the natural system tolerate that we cannot?

Usually loss. Ecosystems tolerate local extinctions; immune systems tolerate collateral
tissue damage; evolution tolerates the overwhelming majority of variants dying. If the
mechanism's function *depends* on losses the plan cannot absorb, the transfer is invalid
however well it matched.

### 2. Does it depend on death, waste, or extreme competition?

Many of the most attractive natural mechanisms are powered by elimination. Apoptosis is
death. Selection is death. Self-limiting star formation is waste. Ask whether the
organisational version has an equivalent — and whether that equivalent is acceptable. It is
usually acceptable for projects and processes, and not for people.

### 3. Does it work only because millions of failures are acceptable?

Check the numbers. Evolution's search works because populations are enormous and generations
are cheap. A plan with four experiments a year is not running evolution; it is guessing with
extra vocabulary. State the required iteration count and compare it to what the plan can
actually afford.

### 4. Does it optimise survival rather than fairness or human welfare?

Natural selection optimises reproductive success. Not welfare, not fairness, not efficiency,
not justice. Any mechanism borrowed from it carries that objective unless it is deliberately
replaced — and the replacement must be stated, because the mechanism will otherwise keep
optimising what it evolved to optimise.

### 5. Does it take thousands of generations to improve?

Compare cycle times explicitly. Bone remodels over months. Succession runs for decades.
Evolutionary adaptation needs many generations. If the plan's horizon is shorter than the
mechanism's cycle time, the mechanism will not have acted before the plan is judged.

### 6. Does it have a goal, or are we projecting one onto it?

This one catches the most errors. Rivers do not seek the sea. Evolution does not seek
complexity. Ecosystems do not seek balance. Immune systems do not "want" to protect you.
These systems have dynamics, not intentions. Any transferred principle phrased as an
intention — "the network *decides*", "the colony *chooses*", "the system *wants*" — has
imported a goal that is not there, and the imported goal will do the reasoning work that
evidence should have done.

Rewrite every principle in mechanism terms before it enters the report.

## The naturalistic fallacy

> **"Natural" does not mean good.**

This method uses nature as evidence about **durability under constraint** — what survives,
and why. It says nothing about desirability. The two are routinely confused, and the
confusion is what makes nature analogies persuasive beyond their evidential worth.

Nature produces, durably and at scale:

- **Parasitism** — stable, ancient, extremely successful, and purely extractive.
- **Cancer** — the direct result of a cell escaping the selection mechanism that governs it.
- **Mass extinction** — repeated, and each one an efficient reset of accumulated structure.
- **Brutal inefficiency** — most organisms produced die before reproducing; that waste is
  the mechanism, not a flaw in it.
- **Extreme inequality** — accretion (E-32) concentrates from negligible initial
  differences, with no relationship to merit.
- **Arms races that consume everything and settle nothing** — Red Queen dynamics (E-30).

So:

| Invalid | Valid |
|---|---|
| "This is how nature does it, so we should do it." | "This mechanism has endured under constraints resembling ours, so it is worth understanding." |
| "Hierarchy is natural, therefore justified." | "Hierarchy appears where decision latency matters more than local knowledge; here is what it costs." |
| "Competition is natural, so internal competition is healthy." | "Competition selects effectively when losers can actually be stopped. Can they, here?" |
| "Our restructuring is like natural selection." | Selection requires that failures actually stop, that variants differ genuinely, and that reality does the judging. Do all three hold? |

**Record a finding** whenever a plan uses naturalness as justification rather than as
evidence. That move is itself a defect in the plan's reasoning, independent of whether the
plan is any good.

## Structural dependencies to hunt

These are the override conditions from `05-scoring.md`. Step 6 is where they are actively
looked for rather than noticed by accident.

| Dependency | Where it hides |
|---|---|
| **Permanent control** | "All X must be approved by Y." Ask what happens at 3am, during holidays, when Y is saturated, when Y disagrees with itself |
| **Unlimited growth** | Growth targets with no stated saturation point. Ask which resource runs out first and at what volume |
| **Perfect prediction** | Any plan whose correctness rests on a forecast. Ask what happens if the forecast is wrong by 2×, and who notices |
| **No failure** | Absent failure-mode analysis. Ask for the degraded mode; if there is none, there is no partial failure — only total |
| **No adaptation** | No revision trigger and no owner. Ask who is allowed to change this, and what would make them |

A plan can contain a dependency without stating it. Trace, do not read.

## Rationalizations to resist

| Rationalization | Reality |
|---|---|
| "It's just a metaphor, it doesn't need to be exact." | Then it carries no information and does not belong in a decision document. Metaphor for communication is fine; metaphor as evidence is not |
| "Nature does it, so it must work." | Nature does parasitism. Durability is not endorsement |
| "We're a special case, natural constraints don't apply." | Scarcity, delay, and failure apply to every plan. Claiming exemption is itself a finding |
| "We'll add the feedback loop later." | An unbuilt mechanism scores `0`. "Later" has no owner and no date, or it would have one now |
| "Central control is unnatural." | Organisms use central control. The finding is that *pure* central control is slow and fragile — nature combines central standards with local response |
| "There's no natural parallel, so this framework doesn't apply." | Absence of a parallel is a result: *Novel but compatible*, assessed on principles |
| "The score is low but the plan is fine." | Possibly true. Name the specific fragility being accepted and why, rather than dismissing the total |
| "Our people are our immune system." | Then say what the fast local response is, who may trigger it without permission, and what the false-positive budget is. Otherwise this is a compliment, not a mechanism |
| "We're building an ecosystem." | Ecosystems have no controller, no shared goal, and no guarantee of stability. Check that this is what is meant |

## Writing the breaking point

One or two sentences, naming the specific property that differs. Not "the analogy is
imperfect" — every analogy is imperfect. Name what breaks and where.

| Weak | Strong |
|---|---|
| "The comparison isn't perfect." | "Every scout shares one colony fate on a one-shot choice, so its signal has nothing to gain by lying. Advocacy here has a separate payoff, and the compounding that makes the mechanism work amplifies a dishonest signal just as efficiently." |
| "Scale is different." | "Ant foraging needs thousands of trips to converge. This team makes roughly forty routing decisions a quarter — three orders of magnitude short of where the mechanism produces its result." |
| "Organisations aren't organisms." | "Reflex arcs work because spinal neurons have no interests of their own. A country team choosing not to escalate has interests, so the 'send the centre a copy' step needs enforcement that the biological version never required." |

## Handoff

Every accepted candidate now has a filled `breaks_down_at` field. Any naturalness-as-
justification findings go into the report's *Where the parallels break* section. Score using
[`05-scoring.md`](05-scoring.md).

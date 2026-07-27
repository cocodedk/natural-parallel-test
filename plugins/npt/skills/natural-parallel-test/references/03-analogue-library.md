# Step 3 & 5 — The Analogue Library

**Purpose**: a starting catalogue of natural systems described at mechanism level, so the
search does not default to whatever comes to mind first.
**Output**: candidate analogues per mechanism, carried into Step 4 for validity testing.
**Read this when**: mechanisms are marked Present and their constraints are written down.

## How to use this file

1. Take one **Present** mechanism and its constraints from Step 2.
2. Use the routing table to find candidates — **from at least three different levels**.
3. Read those entries, not the whole file.
4. Carry each candidate into [`04-validity-tests.md`](04-validity-tests.md). Most will fail.
   That is the expected outcome, not a problem with the search.

This library is a starting point, not a closed set. Nature is larger than any catalogue.
If you find a better analogue outside it, use that — and apply the same four tests, with
the same suspicion.

**Every entry carries a "Stops being valid when" line. It is not optional garnish. An
entry quoted without its limit has been misused.**

## Routing table — mechanism to candidates

| Mechanism | Candidate entries |
|---|---|
| Resource flow | E-01, E-03, E-08, E-15, E-16, E-23, E-32, E-36 |
| Information flow | E-01, E-07, E-12, E-19, E-22, E-35 |
| Decision-making | E-11, E-12, E-13, E-18, E-22, E-25 |
| Coordination | E-11, E-12, E-17, E-18, E-19, E-21, E-22, E-35 |
| Adaptation | E-07, E-13, E-16, E-17, E-27, E-28, E-30, E-31 |
| Growth | E-02, E-15, E-24, E-32, E-33, E-34 |
| Repair | E-10, E-14, E-20, E-29 |
| Selection | E-09, E-10, E-25, E-28, E-30 |
| Boundaries | E-06, E-07, E-26, E-33 |
| Renewal | E-09, E-14, E-16, E-24, E-29 |

Two rows that cut across the ten mechanisms and are worth reading whatever you are
searching for:

| Concern | Entries |
|---|---|
| Redundancy and correlated failure | E-10, E-27, E-29 |
| Capacity limits and what stability costs | E-04, E-05, E-15, E-33, E-36 |

---

# Level 1 — Physical systems

### E-01 · Diffusion down a concentration gradient

- **Problem solved**: distributing a substance evenly with no distributor and no map.
- **Mechanism**: random local motion; net flow is automatically from high to low
  concentration. No component knows the global state.
- **Constraints**: no central control, no addressing, no energy input.
- **Resilience from**: having no coordinating component that can fail.
- **Fails when**: distances are large — diffusion time scales with the *square* of distance,
  so it is hopeless beyond small scales. Real organisms bolt on circulation instead.
- **Transferable principle**: for local, small-scale distribution, a gradient plus local
  action beats a router. Above a size threshold it stops working entirely, and the correct
  response is to add transport, not more gradient.
- **Stops being valid when**: the thing distributed must arrive at a *specific* place, or
  within a deadline. Diffusion has no destinations and no schedule.

### E-02 · Nucleation and crystal growth

- **Problem solved**: forming large ordered structure from disordered material without a
  blueprint.
- **Mechanism**: growth cannot start until a seed exceeds a critical size; below it,
  clusters dissolve. Past it, growth is fast and self-propagating along existing structure.
- **Constraints**: energy barrier to start; growth only at existing surfaces.
- **Resilience from**: order is enforced locally by the geometry of what is already there.
- **Fails when**: growth is too fast — defects, inclusions, and grain boundaries get locked
  in. They are removable only by a separate high-energy reprocessing step (annealing,
  recrystallisation, zone refining), which generally costs more than growing slowly would
  have. Slow growth gives quality; fast growth gives flaws plus a reprocessing bill.
- **Transferable principle**: initiatives have a critical mass below which they reliably
  dissolve; seeding many sub-critical efforts wastes everything invested. And growth speed
  trades directly against structural quality — defects introduced during fast growth are
  not repaired later.
- **Stops being valid when**: the desired structure is heterogeneous. Crystals make one
  repeating unit; most plans need differentiated parts.

### E-03 · River drainage networks

- **Problem solved**: collecting dispersed input across a large area and moving it to an
  outlet, with no design.
- **Mechanism**: flow erodes its own channel, so paths that carry more flow become easier
  to flow along — positive feedback producing a branching hierarchy.
- **Constraints**: gravity only, no pumps, highly variable input.
- **Resilience from**: branching redundancy upstream; the network re-forms after disruption.
- **Fails when**: input exceeds channel capacity. Then it floods — and the flood plain is
  part of the system, not a failure of it. Channelised rivers with no flood plain fail
  catastrophically instead of gracefully.
- **Transferable principle**: usage should be allowed to carve the path, and capacity
  planning must include an explicit overflow area that is expected to be used. A system
  with no designed overflow does not avoid overflow; it just fails badly at one.
- **Stops being valid when**: flow must go uphill or be prioritised. Rivers cannot route by
  importance, only by elevation.

### E-04 · Laminar-to-turbulent transition

- **Problem solved**: nothing — this is a constraint, not a solution. Included because it
  describes how capacity limits actually behave.
- **Mechanism**: below a critical range, flow is smooth and predictable; above it the flow
  becomes intermittently and then fully turbulent, and resistance jumps. The transition is
  not a single number — it depends on how large the disturbances are, it is hysteretic, and
  it announces itself first as **intermittency**: brief turbulent episodes inside otherwise
  smooth flow.
- **Constraints**: fixed geometry, fluid properties.
- **Resilience from**: n/a — the value here is the shape of the failure.
- **Fails when**: disturbances grow past what the smooth regime absorbs. Extrapolating the
  smooth trend misses the transition entirely, because the trend contains no sign of it.
- **Transferable principle**: capacity limits are frequently regime changes, not gradual
  degradations — so extrapolating current smooth performance is the wrong method for finding
  them. Watch instead for intermittency: brief episodes of the bad regime inside otherwise
  normal operation. Those are the warning, they arrive before the transition, and they are
  visible only if someone is looking for episodes rather than averages.
- **Stops being valid when**: used to claim a specific threshold. It says thresholds exist
  and are abrupt, not where yours is.

### E-05 · Static versus dynamic equilibrium

- **Problem solved**: nothing — this is a *distinction*, and it is the one most often got
  wrong when people reason about stability.
- **Mechanism**: two different things look identical from outside. **Static** equilibrium —
  a stone arch, a column of fluid — is a genuine resting state. No work is done without
  displacement, so it costs nothing to maintain and an arch holds for two thousand years at
  zero running cost. **Dynamic** equilibrium looks equally unchanging but is two
  continuously-supplied opposing processes cancelling, and it stops the moment supply stops
  (see E-36).
- **Constraints**: from outside, the two are indistinguishable by observation of the state
  alone. Only the flows distinguish them.
- **Resilience from**: in the static case, from geometry — nothing is being consumed. In the
  dynamic case, from continued throughput, and from nothing else.
- **Fails when**: the two are confused. Treating a dynamic equilibrium as static is how
  maintenance goes unfunded; treating a static one as dynamic is how effort is spent holding
  up something that was standing by itself. Note also that only *stable* equilibria
  self-correct — unstable and neutral ones exist, and a displaced unstable equilibrium keeps
  going.
- **Transferable principle**: for anything that appears steady, ask what is being consumed
  to hold it there. If the answer is nothing, it is structural and free. If the answer is
  attention, goodwill, key-person effort, or deferred maintenance, it is dynamic and the
  budget must show it. Do not assume either.
- **Stops being valid when**: the opposing forces are strategic actors who can change
  behaviour. Physical forces do not anticipate, and an equilibrium between parties who model
  each other can move without either being displaced.

---

# Level 2 — Cells

### E-06 · Selective membrane permeability

- **Problem solved**: maintaining an internal state different from the environment while
  still exchanging with it.
- **Mechanism**: a barrier impermeable to **ions and to large or charged polar solutes**,
  crossed by specific, individually-regulated channels and pumps. Small nonpolar molecules —
  O₂, CO₂, N₂ — still cross freely by diffusion and are not gated at all.
- **Constraints**: continuous energy cost to maintain gradients; environment is hostile
  and does not cooperate.
- **Resilience from**: default-deny *for the traffic that matters*. The number of controlled
  ways in is small, enumerable, and each is separately governed.
- **Fails when**: energy fails — gradients collapse and the boundary equalises with the
  outside. Also when a pathogen mimics a legitimate channel's key.
- **Transferable principle**: boundaries should be default-closed with a small enumerated
  set of controlled crossings, each independently governed — and maintaining a boundary is
  a continuous operating cost, not a one-time build. Then identify the traffic your boundary
  does *not* gate, because every real default-deny boundary has a class that passes freely,
  and knowing which class that is matters more than the stated policy.
- **Stops being valid when**: applied to information rather than substance. Information
  copies; it does not obey conservation, so "controlling the channels" does not control the
  content the way it does for molecules.

### E-07 · Innate and adaptive immunity

- **Problem solved**: defending against threats that are mostly unknown in advance, across
  a whole body, faster than any central authority could respond.
- **Mechanism**: two layers. Innate — fast, local, pattern-based, acts immediately; its
  learning is coarse and short-lived (weeks to a couple of years, non-specific) rather than
  absent, which is the trained-immunity finding. Adaptive — slow first time, generates
  enormous receptor diversity randomly,
  selects what binds, and **remembers**. Local tissue signals escalate; the response is
  raised locally and amplified systemically.
- **Constraints**: threat is novel and adversarial; response must be fast; the sensing
  happens everywhere and the resources are finite.
- **Resilience from**: layering (fast-generic plus slow-specific), distributed detection,
  and memory that makes the second encounter cheap.
- **Fails when**: it misidentifies self as foreign — autoimmunity — or over-responds and
  the response causes more damage than the threat. Both are common and sometimes fatal.
  Distributed detection with amplification is *intrinsically* prone to this.
- **Transferable principle**: pair a fast generic local response that needs no permission
  with a slower specific central one that learns and remembers; let local detection trigger
  escalation rather than requiring central detection. Then budget explicitly for the
  false-positive cost, because a system that can escalate locally *will* over-escalate.
- **Stops being valid when**: what counts as legitimate is itself contested. Immunity has a
  physical reference for what belongs — imperfect, which is why autoimmunity and tumour
  tolerance happen at all — whereas in an organisation the definition of a legitimate action
  is exactly what is being argued about, and there is no body to refer to.

### E-08 · ATP as a common energy currency

- **Problem solved**: letting hundreds of unrelated processes trade energy without each
  pair negotiating its own exchange.
- **Mechanism**: most energy-releasing reactions converge on a small set of intermediates
  dominated by one, and most energy-consuming reactions draw on it. (Others exist — NADH,
  NADPH, acetyl-CoA, the proton-motive force — and several are not freely interconvertible.)
  `N` processes need `N` interfaces, not `N²`.
- **Constraints**: conversion is lossy; the pool is small and must turn over constantly.
- **Resilience from**: decoupling — producers and consumers need not know each other.
- **Fails when**: the common currency is a single point of failure, and its small pool
  means a supply interruption is felt within seconds, everywhere.
- **Transferable principle**: a single shared interchange standard converts `N²`
  integrations into `N`. Accept the conversion overhead deliberately. Then treat the
  standard as critical infrastructure, because everything now depends on it.
- **Stops being valid when**: the things exchanged are not fungible. Energy is
  interchangeable; people, attention, and trust are not, and a common currency for them
  destroys the information that made them different.

### E-09 · Apoptosis — programmed cell death

- **Problem solved**: removing components that are damaged, obsolete, or no longer needed,
  before they harm the whole.
- **Mechanism**: in many cell types the death machinery is pre-assembled and held in check
  only by continuously-received survival signals, so survival is conditional rather than
  automatic. Removal is orderly and does not trigger inflammation. Neighbours can also
  instruct death.
- **⚠ Contested**: how generally "death by default" holds is not established. It is well
  supported for developing neurons and lymphocytes, but its universality is disputed, and
  much cell death runs instead through the extrinsic pathway, which requires an *active*
  death signal — the opposite arrangement. Both exist.
- **Constraints**: must be decisive and irreversible; must not damage surroundings.
- **Resilience from**: survival is default-off. Nothing continues on inertia; continuation
  must be continuously earned.
- **Fails when**: the mechanism is disabled in a cell that keeps dividing — evasion of it is
  one of the recognised hallmarks of cancer. **The absence of this mechanism, not its
  presence, is the pathology.** Conversely, over-firing causes degenerative disease.
- **Transferable principle**: make continuation require renewed justification rather than
  making termination require justification. Build the removal path *before* you need it,
  and make it non-punitive so it can actually be used.
- **Stops being valid when**: the components are people. Cells have no interests; the
  metaphor has an ugly history when applied to humans and should not be transferred to
  headcount. Transfer it to projects, services, processes, and commitments.

### E-10 · DNA proofreading and repair

- **Problem solved**: keeping error rates survivably low in a process that copies billions
  of units and is intrinsically error-prone.
- **Mechanism**: three independent layers — polymerase selectivity, immediate proofreading
  that excises a wrong base as it is added, and post-replication mismatch repair that finds
  errors later using the intact strand as reference. Each layer catches roughly what the
  previous one missed; the error rates multiply down.
- **Constraints**: errors are inevitable; perfection is unaffordable; speed matters.
- **Resilience from**: independent layers with a preserved reference copy to repair against.
- **Fails when**: no second copy is available. Double-strand breaks are far more dangerous
  than single-strand damage — but not because the reference is inherently gone. When a
  sister chromatid exists the break is repaired accurately against it; when it does not, the
  fallback mechanism joins the ends with no template at all and loses information every
  time. The danger is the absence of a *second* copy, not the loss of a strand. Repair
  capacity is also finite and saturates under heavy damage.
- **Transferable principle**: stack several cheap independent checks rather than one perfect
  gate; multiplied error rates beat any single filter. Always keep an intact reference to
  repair against, and treat simultaneous loss of the working copy and the reference as the
  failure mode that actually matters — that is the state in which recovery stops being
  restoration and becomes guesswork.
- **Stops being valid when**: there is no ground truth to repair against. Genetic repair
  works because the correct answer is physically present. Where correctness is a judgement,
  this mechanism has nothing to offer.

### E-11 · Quorum sensing in bacteria

- **Problem solved**: acting only when enough participants are present for the action to be
  worth its cost, without anyone counting.
- **Mechanism**: each cell emits a signal molecule continuously and senses ambient
  concentration. Concentration is a proxy for population density; past a threshold, the
  whole population switches behaviour together.
- **Constraints**: no counting, no addressed messages, no leader.
- **Resilience from**: no census-taker to fail — the threshold is a property of the
  receptor, not of anyone's judgement.
- **Fails when**: the environment traps or disperses the signal, giving a false density
  reading — a single cell in a confined space can trigger as if a crowd were present. Also
  exploitable by cheaters who sense but do not emit.
- **Transferable principle**: gate expensive collective action behind an ambient measure of
  participation rather than a headcount or a vote. Then check what could make the ambient
  measure lie, because it can.
- **Stops being valid when**: participants have divergent interests. Bacterial signalling is
  cheap and mostly honest; where signalling is strategic, expect the signal to be gamed.

---

# Level 3 — Organisms

### E-12 · Reflex arcs alongside central integration

- **Problem solved**: responding to urgent local events fast, while still keeping the whole
  body coherent.
- **Mechanism**: a two-tier nervous system. Reflex arcs act at the spinal cord in
  milliseconds without consulting the brain — the withdrawal happens before the pain is
  felt. The brain receives a *copy* and can modulate, override, or learn from it, but is not
  in the loop for the fast response. Reflex thresholds are fixed by the wiring itself and
  adjusted only slowly by descending modulation — the fast path's calibration is not
  renegotiated per event, and the response itself is local.
- **Constraints**: signal transmission is slow relative to the danger; the brain is a
  bottleneck; damage is irreversible.
- **Resilience from**: separating the *time-critical* path from the *judgement-heavy* path
  rather than trading one against the other.
- **Fails when**: the reflex is wrong for the situation — reflexes cannot be contextual, and
  they will pull a hand off a hot surface even when holding on matters more. Also, spinal
  injury leaves reflexes intact but unmodulated, which is not a good state.
- **Transferable principle**: set standards, thresholds, and boundaries centrally; execute
  locally without asking; send the centre a copy for learning and let it escalate
  exceptionally. Neither pure central control nor pure autonomy — both, at different
  latencies.
- **Stops being valid when**: local actors' incentives diverge from the whole. Spinal
  neurons have no agenda; a subsidiary does.

### E-13 · Homeostasis by negative feedback

- **Problem solved**: holding a critical variable near a set point despite continuous
  external disturbance.
- **Mechanism**: sense the variable, compare against a set point, drive a response opposing
  the deviation. Multiple redundant effectors — for temperature: vasodilation, sweating,
  shivering, behaviour — with different costs and speeds, recruited in order.
- **Constraints**: disturbances are continuous and unpredictable; deviation is expensive;
  sensing has delay.
- **Resilience from**: correction proportional to error, plus graded effectors so cheap
  responses are used first.
- **Fails when**: delay exceeds the response time — then feedback drives oscillation and
  makes things worse. Also when the set point itself is wrong: the loop corrects toward a
  bad set point as forcefully as toward a good one, and nothing inside the loop can detect
  the difference.
- **Transferable principle**: define the variable, the set point, the sensing interval, and
  a graduated ladder of responses in advance. Check that sensing delay is short relative to
  the response, or the control loop will amplify the problem. Review the set point
  separately from the control loop — nothing inside the loop can question it.
- **Stops being valid when**: the goal is to move rather than to hold. Homeostasis actively
  resists change, including intended change.

### E-14 · Wound healing

- **Problem solved**: restoring function after damage, while continuing to operate.
- **Mechanism**: strict phases — haemostasis (stop the loss, seconds), inflammation (clear
  debris and pathogens, days), proliferation (rebuild fast and badly, weeks), remodelling
  (replace the rushed repair with proper structure, months to years). The fast repair is
  explicitly temporary and is expected to be replaced.
- **Constraints**: cannot pause operation; damage is unpredictable; repair competes for
  resources with everything else.
- **Resilience from**: sequencing. Stopping the bleeding is not confused with rebuilding,
  and each phase has an exit condition.
- **Fails when**: remodelling never happens — the temporary repair becomes permanent scar
  tissue, which is mechanically inferior and permanently reduces function. Also when
  inflammation fails to resolve and becomes chronic, causing ongoing damage by itself.
- **Transferable principle**: separate stop-the-bleeding from rebuild-properly, and put a
  scheduled, owned exit condition on the temporary fix. Unremodelled emergency repair is
  scar tissue: it holds, it never gets better, and it accumulates. Also budget for the
  resolution of the response, not just its initiation.
- **Stops being valid when**: the damage is to the repair mechanism itself. Healing assumes
  an otherwise-functioning body.

### E-15 · Metabolic scaling and allometry

- **Problem solved**: staying viable across enormous changes in size.
- **Mechanism**: metabolic rate scales sub-linearly with body mass, so larger organisms need
  proportionally less energy per unit mass — but supply networks must branch more, transport
  distances grow, and structure must be redesigned. Large animals are not scaled-up small
  ones: bone proportions, circulation, and thermoregulation all change qualitatively.
- **⚠ Contested**: the exponent and its explanation are unsettled. Measured values cluster
  between 2/3 and 3/4, and neither a universal value nor the fractal-branching account of it
  is established. Note that the pure surface-to-volume argument predicts **2/3** — the
  interest of Kleiber's law is precisely that the data tend to *exceed* that prediction, so
  do not cite the geometry as if it produced 3/4. What is not contested is the direction and
  the structural consequence, which is all the principle below needs.
- **Constraints**: geometry sets the floor — volume grows as the cube of length, surface
  area as the square, so supply is a surface problem while demand is a volume problem.
- **Resilience from**: redesigning form at each scale rather than scaling the same design.
- **Fails when**: a design is scaled without redesign. There are hard size limits for every
  body plan, and they are approached rapidly.
- **Transferable principle**: efficiency per unit can improve with size while the *structure*
  must change qualitatively at thresholds. Name in advance the size at which the current
  design stops working, and expect a redesign there rather than an extension.
- **Stops being valid when**: the design can be replaced wholesale rather than grown. An
  organism must stay viable at every intermediate size, which is what forces redesign in
  place; a system that can be rebuilt from scratch at the target scale is not under that
  constraint and can skip the intermediate forms entirely. Also never quote the efficiency
  gain without the structural break — they arrive together.

### E-16 · Bone remodelling under load

- **Problem solved**: placing structural capacity where it is actually needed, when the
  needs are not known in advance and keep changing.
- **Mechanism**: bone continuously deposits material where mechanical strain is high and
  resorbs it where strain is low, driven by local strain sensing in embedded cells. The
  skeleton is fully replaced roughly every decade. No plan; the load pattern writes the
  structure.
- **Constraints**: material is expensive to carry; loads change over a lifetime; no
  designer.
- **Resilience from**: capacity tracks demand automatically, and unused capacity is
  reclaimed rather than paid for indefinitely.
- **Fails when**: load disappears — bone is lost quickly in disuse and in microgravity,
  producing fragility exactly when reloading eventually occurs. The signal is present
  strain, so unloaded-but-critical and unloaded-and-obsolete are identical inputs.
- **Transferable principle**: let measured demand drive capacity allocation, and actively
  reclaim capacity that measurement shows is unused. Then guard the failure mode: something
  temporarily idle but critical will be dismantled by this mechanism unless explicitly
  protected.
- **Stops being valid when**: demand is spiky and the response is slow. Bone remodels over
  months; it is a terrible model for anything needing to absorb a sudden peak.

### E-17 · Circadian anticipation

- **Problem solved**: being ready for a predictable change *before* it arrives, rather than
  reacting after.
- **Mechanism**: an internal oscillator, free-running at roughly 24 hours, entrained by
  external cues. Physiology is pre-positioned ahead of dawn instead of responding to light.
- **Constraints**: the environmental cycle is reliable; sensing alone would be too slow.
- **Resilience from**: it keeps running when cues are absent, and re-synchronises when they
  return.
- **Fails when**: the environment shifts faster than entrainment — jet lag, shift work —
  producing sustained internal desynchrony with real health costs. Anticipation of a cycle
  that has changed is worse than reaction.
- **Transferable principle**: where a cycle is genuinely reliable, pre-position resources
  ahead of it rather than reacting to it, and keep the schedule running when signals are
  missing. Re-entrainment is slow, so a plan that changes its own rhythm frequently pays a
  compounding cost.
- **Stops being valid when**: the cycle is assumed rather than measured. Anticipation
  applied to a non-cycle is just bias with a schedule.

---

# Level 4 — Social species

### E-18 · Honeybee nest-site selection

- **Problem solved**: committing an entire group to one irreversible choice among options
  that no individual has evaluated all of.
- **Mechanism**: scouts inspect sites independently and advertise by dancing, with dance
  duration proportional to assessed quality. Better sites recruit more scouts, which
  compounds. Scouts at competing sites deliver inhibitory stop-signals to each other.
  Commitment triggers on a **quorum** at one site, not on unanimity and not by the queen —
  who has no decision role whatsoever.
- **Constraints**: one-shot, irreversible, time-limited, no individual has global
  information, and the cost of a bad choice is colony death.
- **Resilience from**: independent assessment before aggregation, weighting by assessed
  quality, and cross-inhibition that prevents deadlock between two good-enough options.
- **Fails when**: scouts are not independent — if they copy each other rather than assess,
  the compounding amplifies an early accident into a decision. Speed-accuracy is a real
  trade-off, and a swarm that commits sooner commits to worse sites on average.
- **Transferable principle**: have people assess independently before anyone hears the
  others' views; weight advocacy by assessed quality rather than by seniority or volume;
  commit at an explicit quorum instead of demanding consensus. Protect the independence of
  the assessment stage — it is where the value is, and it is what meetings destroy first.
- **Stops being valid when**: participants can do better than the group does. Every scout
  shares one colony fate on a one-shot, irreversible choice — there is no outcome in which a
  scout wins while the swarm loses — so its signal has nothing to gain by lying. (Kinship is
  the weaker argument here and is often overstated: queens mate with many drones, so
  nestmates average well below supersister relatedness. Shared fate, not shared genes, is
  what makes the signal honest.) Human advocacy usually does have a separate payoff, and the
  compounding that makes this mechanism work amplifies a dishonest signal just as
  efficiently as an honest one.

### E-19 · Ant pheromone foraging (stigmergy)

- **Problem solved**: finding and exploiting resources, and abandoning them when exhausted,
  with no individual holding a map of the resource landscape and no addressed messages. The
  memory is not in any ant; it is in the environment, and it decays.
- **Mechanism**: ants deposit trail pheromone when returning with food; others
  probabilistically follow stronger trails and reinforce them. Pheromone **evaporates**, so
  a trail not continuously reinforced disappears. Coordination happens entirely through
  modification of the shared environment, not through messages.
- **Constraints**: no individual has a global view; resources appear and vanish. (Ants are
  not as simple as the popular version suggests — many species navigate by path integration
  and landmarks, and they do communicate directly. What the trail supplies is the *shared,
  externalised* record that no individual holds.)
- **Resilience from**: evaporation. Forgetting is the active ingredient — it is what lets
  the colony abandon a depleted source and re-explore.
- **Fails when**: reinforcement outruns evaporation and the colony locks onto a mediocre
  path. Ant mills — a circular trail that traps a column until it dies — are the pathological
  case of the same mechanism.
- **Transferable principle**: coordinate through shared, visible, *decaying* state rather
  than through messages. Then set the decay rate deliberately: signals that never expire
  become lock-in, and documentation, dashboards, and processes that nothing removes are the
  pathological case: a self-reinforcing loop that consumes effort, produces nothing, and
  persists only because nothing expires.
- **Stops being valid when**: the shared medium is not honest. Pheromone cannot be faked
  cheaply; a metric can, and a stigmergic system on a gameable signal optimises the signal.

### E-20 · Termite mound ventilation

- **Problem solved**: maintaining a stable internal atmosphere for millions of individuals
  with no active machinery and no controller.
- **Mechanism**: mound geometry drives gas exchange passively, without machinery.
  Construction is stigmergic — termites respond to local structure and local gradients,
  building without a plan. The infrastructure does the regulation; nobody manages it.
- **⚠ Contested**: *which external driver does the work is not settled, and differs by
  species.* Turner and Soar argue that African *Macrotermes* mounds work as a lung driven by
  **wind-induced pressure fluctuations** through the surface complex — explicitly not a
  thermosiphon. Ocko, King, Mahadevan et al. (PNAS 2015) argue for **diurnal thermal
  convection**, on evidence from a South Asian *Odontotermes* species. The older Lüscher
  thermosiphon model was refuted. Use only the well-supported claims: that the regulation is
  structural, and that construction is stigmergic. Do not build an argument on the driver.
- **Constraints**: no energy budget for active ventilation; huge population; a large,
  persistent external driver of some kind.
- **Resilience from**: the regulation lives in the structure, so it cannot fail
  operationally. Damage is repaired continuously by the same local rules that built it.
- **Fails when**: the external driver the geometry is matched to changes. Construction is
  also slow — a mound cannot be reconfigured quickly.
- **Transferable principle**: prefer regulation built into structure over regulation
  performed by an operator; structural regulation has no on-call rota. Accept in exchange
  that it adapts slowly and silently encodes an assumption about the environment — write
  that assumption down, because the structure will not tell you what it is.
- **Stops being valid when**: the regulated variable is contested. Gas exchange has one
  measurable target; where the target itself is argued over, freezing it into structure
  freezes the current winner of that argument and makes it very expensive to revisit.

### E-21 · Starling murmuration

- **Problem solved**: keeping a large group cohesive and responsive to threats with no
  leader and no global communication.
- **Mechanism**: each bird tracks a fixed *number* of nearest neighbours — about seven —
  not everything within a radius. Topological rather than metric interaction keeps the
  network connectivity constant as the flock's density changes, so a disturbance propagates
  across the whole flock faster than any individual bird moves.
- **Constraints**: no leader, limited attention per individual, predators attack suddenly.
- **Resilience from**: fixed per-individual load regardless of flock size, and no
  distinguished individual to remove.
- **Fails when**: a destination is required. No destination is represented anywhere in the
  system — cohesion and evasion are what the interaction rules produce, and direction simply
  is not among the outputs.
- **Transferable principle**: bound each participant's coordination load to a fixed number
  of relationships rather than to the size of the organisation, and cohesion will scale
  without a hub. Do not expect strategy to emerge from it — pair it with a mechanism that
  sets direction.
- **Stops being valid when**: participants can be individually addressed. Topological
  interaction is a workaround for having no addressing at all; where you *can* reach a named
  person directly, capping everyone at seven neighbours discards capability rather than
  buying scale.

### E-22 · Division of labour by response threshold

- **Problem solved**: allocating individuals across many tasks with changing demand, with no
  assigner.
- **Mechanism**: on the most-used model of this — response thresholds; competing accounts
  exist — individuals differ in their stimulus threshold for each task. Low-threshold
  individuals act first; if a task goes undone its stimulus rises until higher-threshold
  individuals engage. Performing a task lowers its threshold further, producing
  specialisation from what began as small variation.
- **⚠ Contested**: reinforced-threshold theory competes with foraging-for-work,
  spatial-fidelity, and social-inhibition accounts, and empirical support is partial and
  species-dependent.
- **Constraints**: no manager, no global view of demand, demand fluctuates.
- **Resilience from**: automatic reallocation under surge, plus graceful degradation — a
  reserve exists without anyone designating it.
- **Fails when**: the threshold distribution is too narrow — everyone responds to
  everything, or nobody does. Specialisation can also over-run, leaving too few generalists
  when demand shifts.
- **Transferable principle**: variation in willingness-to-engage is a *feature* that
  produces automatic surge capacity and specialisation without assignment. Preserve the
  spread deliberately; standardising everyone to the same response destroys the reserve.
- **Stops being valid when**: tasks require specific credentials or access. Threshold
  allocation assumes anyone *could* do the task; permissions break it entirely.

---

# Level 5 — Ecosystems

### E-23 · Mycorrhizal networks

- **Problem solved**: exchanging resources between organisms that cannot move, across
  distances they cannot bridge alone.
- **Mechanism**: fungal hyphae connect plant roots and trade mineral nutrients for plant
  carbon, with partner-specific reciprocal exchange — plants preferentially allocate carbon
  to fungi delivering more nutrients, and vice versa.
- **Constraints**: neither partner can obtain what the other has; both can cheat.
- **Resilience from**: bilateral sanctioning. Reciprocal preferential allocation makes
  cheating expensive without any enforcement authority.
- **Fails when**: one partner can defect without losing access. Some plants are full
  parasites on these networks, contributing no carbon at all.
- **⚠ Contested**: the popular "wood-wide web" account — trees deliberately sharing
  resources with needy neighbours through a cooperative network — has been substantially
  challenged in recent literature as running well ahead of the field evidence. The
  bilateral trade-and-sanction mechanism is well supported; **collective altruistic sharing
  is not**. Use only the trade mechanism, and say so.
- **Transferable principle**: sustained exchange between parties who cannot compel each
  other rests on the ability to *preferentially reallocate* to better partners. Build the
  reallocation lever, not a cooperation agreement.
- **Stops being valid when**: it is invoked as a story about generous sharing. That version
  is not established, and using it imports a conclusion the evidence does not support.

### E-24 · Ecological succession

- **Problem solved**: reaching a complex, productive state from bare ground, when the
  complex state cannot establish directly.
- **Mechanism**: pioneer species tolerate harsh conditions, are fast and low-quality, and
  **modify the environment** — building soil, providing shade. In some systems those changes
  favour their successors (facilitation); in others the pioneers actively *inhibit*
  successors and are replaced only by disturbance. Where facilitation operates, each stage
  alters conditions in ways that happen to favour a different set of species.
- **⚠ Contested**: facilitation is only one of three recognised mechanisms — the others are
  tolerance and **inhibition**, and inhibition is common. The directional, deterministic
  climax model is largely abandoned in favour of non-equilibrium dynamics, alternative
  stable states, and priority effects. **Whether succession has a predictable endpoint is
  disputed.** The staged-enabling principle below survives this; a claim that the sequence
  must arrive somewhere does not.
- **Constraints**: the end state cannot establish in the starting conditions; decades to
  centuries.
- **Resilience from**: staged progression, and the fact that disturbance resets only part of
  the sequence, leaving a mosaic of stages.
- **Fails when**: an early stage is preserved past its role — arrested succession — or when
  disturbance is so frequent that no stage completes.
- **Transferable principle**: build the enabling stage explicitly and design it to be
  replaced. The first version's job is to create the conditions for the second, and holding
  onto it because it works is the standard failure. Say at the outset what the pioneer stage
  is and what will displace it.
- **Stops being valid when**: the target state can be built directly. Succession is forced
  on ecosystems because the climax community physically cannot establish on bare rock; where
  the end state *can* be stood up from the start, staging is a choice to be justified on
  other grounds, not a necessity. And do not let the pattern excuse indefinite delay: each
  stage has an exit condition, so "we're still in the pioneer phase" three years in is
  arrested succession, not progress.

### E-25 · Keystone species and trophic cascades

- **Problem solved**: nothing — this describes a *structural property*: some components have
  influence wildly disproportionate to their size.
- **Mechanism**: a predator suppresses a dominant competitor, and that suppression allows
  many other species to persist. In the cases where this has been demonstrated, removing it
  collapses diversity through cascading indirect effects. Influence flows through the
  interaction network, not through mass.
- **⚠ Contested**: how commonly this structure occurs, and whether "keystone" can be defined
  operationally before the removal, has been criticised since the early 1990s. Effects are
  strongly context-dependent. Treat it as a shape to look for, not a category to assign.
- **Constraints**: effects are indirect and delayed, often by years.
- **Resilience from**: none inherent — this is a *fragility*, described.
- **Fails when**: keystones are identified only after removal. Their importance is
  systematically invisible in inventories of size, cost, or headcount.
- **Transferable principle**: some components hold the structure open for everything else
  and will not show up in any list ordered by cost or size. Look for what *suppresses* a
  would-be dominant — the review nobody likes, the constraint everyone wants relaxed — and
  test removals in a way that can be reversed.
- **Stops being valid when**: used to grant something keystone status by assertion. The
  claim needs the interaction chain traced, not the label applied.

### E-26 · Mutualism and the parasitism gradient

- **Problem solved**: obtaining a capability you cannot build, from a party with its own
  interests.
- **Mechanism**: partners exchange complementary services. Stability requires that
  defection be detectable and punishable — through partner choice, sanctions, or
  vertical transmission that binds the partner's fate to the host's.
- **Constraints**: interests are only partially aligned; cheating is always available and
  usually profitable short-term.
- **Resilience from**: alignment of *fate*, not goodwill. The most stable mutualisms are the
  ones where the partner cannot survive the host's failure.
- **Fails when**: the enforcement weakens. Mutualism and parasitism are the same
  relationship at different enforcement levels, and lineages shift between them repeatedly.
- **Transferable principle**: when depending on an outside party, ask what makes defection
  expensive *for them*. If the honest answer is "our good relationship", the arrangement is
  one budget cycle from parasitism. Align fate where possible; build detection and exit
  where not.
- **Stops being valid when**: the benefit to each party is a byproduct of pursuing its own
  interest. Those mutualisms are stable with no enforcement at all, and importing sanctions
  into one wastes effort. Where the benefit is *not* a byproduct, the default is drift toward
  exploitation whenever enforcement lapses — so establish which kind you have before
  designing for it.

### E-27 · Response diversity and the portfolio effect

- **Problem solved**: keeping aggregate function steady when individual components respond
  unpredictably to disturbance.
- **Mechanism**: multiple species perform a similar function but respond *differently* to
  the same disturbance. When one declines, another compensates. Aggregate variance falls
  because the responses are uncorrelated — the same statistics as a diversified portfolio.
- **Constraints**: disturbances are unpredictable in kind; redundancy costs resources.
- **Resilience from**: uncorrelated responses, not from redundancy alone. Duplicate
  components that fail identically provide none of this.
- **Fails when**: the diversity is superficial — components look different but share a
  hidden dependency, so a single disturbance takes them all. Correlated failure is the way
  this mechanism is usually lost without anyone noticing.
- **Transferable principle**: redundancy is only worth its cost when the copies fail for
  *different* reasons. Audit alternates for shared dependencies; three suppliers on one
  shipping lane, or three regions in one cloud provider, are one supplier.
- **Stops being valid when**: the disturbance distribution is known and narrow. The
  portfolio effect pays for *unknown* kinds of disturbance; against one well-characterised
  threat, a single well-chosen defence beats diversification and costs less. It is also
  deliberately inefficient in the ordinary case, so it must be justified across the
  distribution of futures rather than the expected one.

---

# Level 6 — Evolution

### E-28 · Variation, selection, inheritance

- **Problem solved**: producing designs fitted to an environment nobody has modelled, with
  no designer and no foresight.
- **Mechanism**: generate variation blindly, test every variant against the real
  environment simultaneously, retain what survives, and inherit it. Search happens in
  parallel across the whole population, and the environment — not a predictor — does the
  evaluating.
- **Constraints**: no foresight, no goal, only local moves from what already exists.
- **Resilience from**: parallelism and the use of reality rather than a model as the fitness
  test.
- **Fails when**: it is slow, wasteful, and finds local optima it leaves only slowly and by
  accident. It optimises only what reproduces — never fairness, welfare, or intent. And it
  requires the failures: the mechanism *is* the deaths.
- **Transferable principle**: where the environment is not modellable, run many small real
  tests in parallel and let outcomes select, rather than predicting and committing. This
  demands three things most organisations lack: variants must be genuinely different, the
  test must be reality rather than review, and losing variants must actually be stopped.
- **Stops being valid when**: individual failures are unaffordable, or the cycle time is too
  long for the horizon. Evolution assumes cheap, plentiful, survivable failure — if a failed
  variant means a lost customer segment or a safety incident, this mechanism is unavailable
  and reaching for it anyway is how "fail fast" becomes negligence.

### E-29 · Gene duplication and divergence

- **Problem solved**: acquiring genuinely new capability without losing existing function.
- **Mechanism**: a gene is duplicated; one copy continues the original job under selection,
  freeing the other to accumulate changes that would otherwise be fatal. Most redundant
  copies decay into nothing; occasionally one acquires a new function.
- **Constraints**: existing function cannot be interrupted; most experiments fail.
- **Resilience from**: redundancy first, experimentation second. The safe copy is what makes
  the risky copy affordable.
- **Fails when**: the duplicate is not actually free — if both copies remain constrained,
  nothing can diverge. But note the standing objection: a *fully* freed copy is invisible to
  selection and usually decays into a pseudogene long before it innovates, which is why
  subfunctionalisation and amplification-then-divergence models exist. The routes that
  actually work generally keep both copies under some selection while they specialise.
- **Transferable principle**: to change something load-bearing, duplicate it and diverge the
  copy while the original keeps serving — the incremental-replacement migration pattern. Its
  natural version comes with a warning the engineering version usually omits: **most
  duplicates decay without ever becoming anything**, and they decay precisely because
  nothing depends on them. A duplicate needs an owner, a deadline, and preferably real
  traffic, or it becomes dead weight.
- **Stops being valid when**: running two copies is unaffordable, or the copies must stay
  synchronised. Divergence is the entire mechanism; a synchronised duplicate is just cost.

### E-30 · Red Queen dynamics

- **Problem solved**: nothing — this describes a *condition*: continuous adaptation that
  yields no lasting advantage.
- **Mechanism**: in a co-evolutionary arms race, each party's improvement degrades the
  others' relative position, so all must keep improving to maintain the same standing.
- **Constraints**: opponents adapt; the environment includes strategic actors.
- **Resilience from**: n/a — this is the treadmill, described.
- **Fails when**: n/a as a mechanism — the dynamic does not fail, it continues. What fails
  is a participant who treats their position as permanent, or who stops while others do not.
- **Transferable principle**: against adaptive opponents — competitors, attackers,
  regulators-and-avoiders — expect improvement to buy position, not progress, and budget for
  it permanently. A security or competitive plan with a completion date has misread the
  problem as static. Ask whether the race can be left rather than won.
- **Stops being valid when**: the environment is not adaptive. Against a fixed problem this
  reasoning justifies indefinite spending on a race nobody is running.

### E-31 · Modularity and evolvability

- **Problem solved**: nothing — this describes an observed **structural property**, and its
  origin is disputed. Systems that persist tend to be modular, and modular ones change more
  cheaply. Evolution has no foresight (E-28), so it cannot have solved the problem of
  remaining changeable later.
- **Mechanism**: biological systems are organised into semi-independent modules with
  conserved interfaces. Regulatory changes rearrange when and where modules are deployed
  without redesigning their internals — the same body-plan toolkit generates enormously
  different forms.
- **⚠ Contested**: whether selection can favour evolvability *as such* is genuinely
  disputed. The competing accounts are that modularity arises from developmental constraint,
  from drift, or as a byproduct of selection for robustness. The observation is solid; the
  explanation is not, and the principle below does not depend on which is right.
- **Constraints**: change must never break the currently-working organism.
- **Resilience from**: stable interfaces with variable internals and variable composition.
- **Fails when**: interfaces themselves must change. Deeply conserved interfaces are
  conserved precisely because everything depends on them, and they become nearly impossible
  to alter — evolutionary technical debt with no refactor available.
- **Transferable principle**: put the stability in the interfaces and the variation behind
  them; then most change becomes recombination rather than redesign. Choose those interfaces
  carefully, because the ones that succeed become permanent.
- **Stops being valid when**: the module boundaries were drawn wrong. Modularity around the
  wrong seams is worse than none, and the constraint hardens over time.

---

# Level 7 — Cosmic systems

### E-32 · Gravitational accretion

- **Problem solved**: nothing — this describes *positive feedback in resource
  concentration*.
- **Mechanism**: a region slightly denser than its surroundings attracts more matter,
  increasing its density and its attraction. Small initial differences amplify into
  enormous ones. Structure forms from noise.
- **Constraints**: attraction scales with accumulated mass. Opposing effects do exist —
  cosmic expansion, thermal pressure below the Jeans mass, angular momentum — but each acts
  at a particular scale, so they set a ceiling on how far concentration runs rather than
  preventing it. This is why structure has a characteristic size instead of everything
  ending up in one object.
- **Resilience from**: n/a — this describes concentration, and it is why voids stay empty.
- **Fails when**: taken as a model for anything that should stay distributed. Left alone,
  accretion produces extreme inequality from negligible initial differences — the outcome is
  not evidence of merit in the seed.
- **Transferable principle**: any process where success increases the ability to succeed
  will concentrate, and early random differences will be amplified beyond recognition.
  Budget allocation, attention, and platform adoption all behave this way. If concentration
  is not wanted, an opposing mechanism must be built deliberately — and it will have a
  characteristic scale, so expect it to cap concentration rather than to oppose it
  everywhere.
- **Stops being valid when**: used to justify a concentrated outcome as natural. It is
  natural, and that is an argument about dynamics, not about desert.

### E-33 · Stellar hydrostatic equilibrium

- **Problem solved**: remaining stable for billions of years under two opposed forces that
  never rest.
- **Mechanism**: inward gravity is balanced by outward **thermal gas pressure**, sustained
  by the heat of fusion — radiation pressure matters structurally only in the most massive
  stars. The loop is self-correcting: compression raises temperature, raising fusion rate,
  raising pressure, re-expanding the star.
- **Constraints**: fuel is finite; the balance must hold continuously.
- **Resilience from**: the negative feedback is intrinsic to the physics, not imposed by a
  regulator.
- **Fails when**: fuel runs out. In massive stars the balance then fails catastrophically;
  in smaller ones the core contracts while the envelope expands and the structure
  reorganises into a different, colder equilibrium over a very long time. Either way the old
  steady state ends, and it ends by reorganisation rather than by gentle decline.
- **Transferable principle**: long stability can rest entirely on a resource whose depletion
  is invisible from the outside, and the ending is a collapse rather than a decline. Ask
  what is being consumed to hold the current steady state — goodwill, key-person knowledge,
  deferred maintenance — and how much is left.
- **Stops being valid when**: the balancing force can be replenished. Stars cannot refuel;
  most organisations can, if they notice in time.

### E-34 · Self-limiting star formation

- **Problem solved**: nothing — this describes **negative feedback generated by the
  consumption itself**.
- **Mechanism**: forming stars heat and disperse the surrounding gas through radiation and
  winds, suppressing further formation nearby. Growth generates the conditions that stop
  growth, so a cloud converts only a small fraction of its gas.
- **Constraints**: shared finite reservoir; no coordinating authority.
- **Resilience from**: the brake is intrinsic and requires no enforcement.
- **Fails when**: the feedback is too weak or too strong — runaway consumption on one side,
  sterilisation on the other. Tuning is not chosen; it is a property of the physics.
- **Transferable principle**: the durable brake on consuming a shared resource is one
  generated by the consumption itself, not one administered by a committee. Make growth
  bear its own cost at the point of growth — internal chargeback, cost visible to the team
  spending it — rather than policing it externally.
- **Stops being valid when**: the feedback can be externalised. Gas clouds cannot make
  someone else absorb the heat; organisations do this constantly, and the mechanism fails
  the moment the cost lands somewhere other than the growing part.

### E-35 · Orbital resonance

- **Problem solved**: many independent bodies remaining in a stable configuration
  indefinitely with no communication.
- **Mechanism**: orbital periods settle into small integer ratios, so encounters recur at
  the same relative geometry. In protective configurations that geometry is one of maximum
  separation — Pluto's 3:2 with Neptune holds because Pluto is never near perihelion when
  Neptune is at the same longitude — and the repeated nudges cancel over a cycle. In others
  the same repetition adds up. Coordination emerges from timing alone.
- **Constraints**: no communication channel, no controller, must hold for billions of years.
- **Resilience from**: phase protection — the ratio guarantees *when* encounters happen, so
  the perturbations arrive where they cancel rather than accumulating randomly.
- **Fails when**: the ratio is one of the destabilising ones. The same repetition that
  cancels in a protective resonance pumps eccentricity in others until bodies are ejected —
  the Kirkwood gaps in the asteroid belt are where resonance cleared material out. The
  specific ratio, not the fact of resonance, decides which happens.
- **Transferable principle**: aligning cycles — planning, release, review, reporting — to
  simple integer ratios lets independent groups coordinate through timing rather than
  messages. Mismatched cycles accumulate drift and force meetings. Check the specific
  ratio, though: some alignments amplify rather than damp.
- **Stops being valid when**: the work is not cyclic. Resonance coordinates repetition; it
  offers nothing for one-off dependencies.

### E-36 · Dissipative structures

- **Problem solved**: maintaining organised structure in a universe that tends toward
  disorder.
- **Mechanism**: ordered structures — convection cells, cyclones, life — form and persist
  only while energy flows *through* them. Local order is paid for by exporting entropy to
  the surroundings; total entropy still rises. Stop the flow and the structure dissolves,
  quickly.
- **Constraints**: order is never free and never static; it requires continuous throughput.
- **Resilience from**: the structure is a *process*, not an object, so it reforms readily
  while the flow continues.
- **Fails when**: the gradient driving the flow is exhausted or the exported disorder cannot
  leave — a system that cannot dump entropy to its surroundings degrades internally.
- **Transferable principle**: organisation is a running cost, not a completed asset. Any
  ordered arrangement — a clean codebase, a functioning process, a healthy team — dissolves
  when the energy maintaining it stops, and it dissolves faster than it formed. Also ask
  where the disorder is being exported: order maintained here at the cost of chaos next door
  is the normal case, not an exception.
- **Stops being valid when**: used to excuse any expenditure as "maintaining order". The
  mechanism says throughput is required; it does not say the current throughput is
  well-spent.

---

## Step 5 — Extract the principle, not the shape

Every "Transferable principle" line above is written as a rule, not as an image. When
carrying one into a report, rewrite it again in the plan's own vocabulary.

| Shape (useless) | Principle (usable) |
|---|---|
| "The organisation should be like a tree." | Distribute through multiple paths; place capacity near demand; grow incrementally; remove damaged parts; maintain roots before expanding the crown. |
| "Our platform should work like a nervous system." | Handle latency-critical responses locally against centrally-set thresholds; send the centre a copy for learning; escalate only exceptions. |
| "We need an immune system for security." | Fast generic local response requiring no permission, plus slow specific central analysis that retains memory — and an explicit budget for false positives. |
| "Be like an ant colony." | Coordinate through shared visible state that decays unless reinforced; set the decay rate deliberately. |
| "Adopt a startup mindset." | Run several genuinely different variants against reality in parallel, and actually terminate the losers. |

If the principle still contains the name of the organism, it is not finished.

## Handoff to Step 4

Carry each candidate forward in the YAML schema from `SKILL.md`, with `validity` left
blank. Fill it in using [`04-validity-tests.md`](04-validity-tests.md).

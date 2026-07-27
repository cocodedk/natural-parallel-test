---
description: Search all seven levels of nature for systems solving a given problem under given constraints
argument-hint: "[\"problem or mechanism\"] [\"constraints\"] [\"timescale\"]"
---

Search for natural analogues to: $ARGUMENTS

That text describes the problem or mechanism. If it was supplied as separate quoted
segments, the second is the constraints it operates under and the third is the timescale. If
it was not quoted, treat the whole text as the problem — do **not** read stray words as
constraints.

Search only. No scoring, no classification, no plan assessment — this returns tested
candidates with their transferable principles and their limits. Use it when you have one
mechanism to think about rather than a whole plan.

Use the `natural-parallel-test` skill; references at
`${CLAUDE_PLUGIN_ROOT}/skills/natural-parallel-test/references/`.

## 1. Make the request searchable

If the request names a solution rather than a problem — "a governance board", "an event bus" —
rewrite it as a problem first, using `references/01-problem-statement.md`. Show the rewrite.
A solution-shaped request returns analogues that justify the solution.

If no constraints were given, ask once: scarcity, uncertainty, delay, competition,
failure, and who bears the cost of failure. Test 2 cannot be applied without them, and
without Test 2 this is just a list of interesting animals.

## 2. Search all seven levels

Read `references/03-analogue-library.md` and use the routing table.

Cover every level. Dispatch `analogue-scout` subagents in parallel, one per level:

**Physical** · **Cells** · **Organisms** · **Social species** · **Ecosystems** ·
**Evolution** · **Cosmic**

Report at least one candidate per level or state explicitly why that level has nothing to
offer this problem. "Nothing at this level" is a legitimate and informative answer;
silently skipping a level is not.

Start with physical and cellular. They are least susceptible to storytelling and most
likely to yield a mechanism you can actually inspect.

The library is a starting point. Better candidates found outside it are welcome, tested the
same way — and check the biology before testing it, because attractive analogies survive on
appeal (see the alpha-wolf case in `references/04-validity-tests.md`).

## 3. Test each candidate

Apply the four tests from `references/04-validity-tests.md`: same problem, similar
constraints, comparable mechanism, relevant scale. Any single `fail` rejects the candidate.

Then run the `analogy-auditor` over the accepted ones.

## Output

Group by level. For each candidate:

| | |
|---|---|
| **System** | |
| **Problem it solves** | in nature's terms |
| **Mechanism** | step by step — this is the part that transfers |
| **Constraints it operates under** | |
| **Resilience comes from** | |
| **Fails when** | |
| **Validity** | same problem / constraints / mechanism / scale |
| **Verdict** | accepted (high/medium/low confidence) or rejected + failing test |
| **Transferable principle** | in the requester's vocabulary — no organism names |
| **Stops being valid when** | mandatory |

Close with a short comparison: where the accepted candidates agree, and where they
disagree. Disagreement is not noise — nature solves most problems more than one way, and
two mechanisms pointing in different directions is a real finding about the trade-off you
are facing. Say what each one costs.

Then note that this was a search, not an assessment, and that `/npt:test` applies these
findings to a specific plan with the twelve-principle score and a verdict.

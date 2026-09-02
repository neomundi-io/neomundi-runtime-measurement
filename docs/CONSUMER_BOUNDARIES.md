# Consumer Boundaries

```text
Measurement
    ≠
Interpretation
    ≠
Policy
    ≠
Execution
```

NeoMundi produces the measurement. Everything after that line is the consuming system's responsibility.

## The four layers

1. **Measurement** — what NeoMundi observes and emits. Defined by the [Measurement Contract](./MEASUREMENT_CONTRACT.md).
2. **Interpretation** — what can legitimately be inferred from a measurement, given its documented meaning and limits. Supported by the [Measurement Interpretation Table](./MEASUREMENT_INTERPRETATION_TABLE.md).
3. **Consumer policy** — what an external system chooses to do with a measurement, given its own risk tolerance, regulatory environment, and operational context. This belongs entirely to the consuming system.
4. **Execution** — the action eventually performed on or around the AI system. Also entirely the consuming system's responsibility.

```text
AI generation
     │
     ▼
NeoMundi measurement
     │
     ▼
Runtime signals
     │
     ▼
Consumer interpretation / policy
     │
     ▼
CONTINUE / VERIFY / STOP / REGENERATE / REROUTE / ABSTAIN / other action
```

NeoMundi is a runtime measurement layer, not a universal policy engine.

## What a measurement is not

```text
high stability ≠ factual correctness
FLAG ≠ proven error
ALLOW ≠ proven truth
```

A NeoMundi signal is a measurement signal — not, by itself, a verdict about truth, safety, legality, or business acceptability. This holds for every signal in the [Measurement Contract](./MEASUREMENT_CONTRACT.md): `risk_signal` never automatically means `ALLOW`, `BLOCK`, `COMPLIANT`, `SAFE`, or any of their opposites; a measurement never by itself establishes truth, safety, authority, downstream permission, or execution admissibility.

## Actions that belong to consumer policy, not to NeoMundi

A consuming system MAY use a NeoMundi measurement as input to decide, among other things, to:

- **continue** normally;
- **verify** — perform additional or external validation;
- request **human review**;
- **reroute** the request;
- **regenerate** the output;
- **stop** or interrupt the workflow;
- **abstain** — decline to decide and transfer control to another path (fallback policy, safe default, human review);
- log, audit, or feed a compliance or evidence workflow.

This list is illustrative and non-exhaustive, drawn directly from the source material. **None of these actions is implemented by NeoMundi, and none of them is the intrinsic meaning of a measurement.** This repository does not implement an actionability layer — see the "Future architecture" section of the [top-level README](../README.md).

## Consumer authority

```text
NeoMundi
   ↓
measurement
   ↓
consumer C
   ↓
policy decision
   ↓
system B
```

A NeoMundi signal may cause a consuming system to select a different computational path — but this happens because the consuming system defines that policy, not because the measurement itself carries universal execution authority.

## Missing, malformed, partial and stale signals — consumer responsibilities

These rules are drawn from the pre-freeze consumption-rules material; they describe sound handling practice rather than a frozen contract, but the underlying boundary they protect (measurement ≠ decision) is the same one the normative Measurement Contract states directly.

- **Missing signal**: must be treated as "measurement unavailable", never silently converted into `0`, `ALLOW`, `STABLE`, "safe", or "verified".
- **Malformed payload**: must not be interpreted as a valid measurement, and must never silently produce `ALLOW`. Reject, log, retain provenance, and apply your own fallback policy.
- **Partial payload** (e.g. in streaming): a partial runtime observation must be distinguished from a final measurement; fields representing final aggregation or classification must not be assumed valid before the schema-defined completion event.
- **Stale signal**: a measurement is temporally bound to the generation/turn it was produced from. A signal from turn `t-1` must not automatically govern turn `t` without an explicit, separately defined longitudinal consumer policy.

## No inferred thresholds

No consumer should derive official NeoMundi thresholds from exploratory research findings. Values such as `∆G < -0.05`, `∆G < -0.10`, or `∆G < -0.15` have been used in exploratory studies but are explicitly **not** official NeoMundi thresholds. A context-specific threshold, if a consumer defines one for their own policy, should at minimum identify: `metric_version`, `normalizer_version`, provider/model scope, task/context scope, the threshold value, and its semantics. Absent these, treat any such threshold as non-authoritative.

## Conflict resolution belongs to the consumer

Conflicting signals (e.g. high stability alongside a poor factual signal) are expected in a multidimensional measurement system and are not necessarily an internal contradiction — they may reveal exactly the kind of situation multi-signal measurement is meant to surface (e.g. "deceptive stability": stable generation with factual weakness). NeoMundi does not reduce every signal conflict to a single universal scalar verdict. Consumer-specific precedence rules must be explicit and must not be reverse-engineered from incidental correlations in research datasets.

## Summary

**Measurement ≠ Policy ≠ Execution.**

NeoMundi provides the independent runtime measurement layer. The surrounding infrastructure remains in control of interpretation, policy, and action.

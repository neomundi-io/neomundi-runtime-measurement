# Measurement Contract

**Status: Draft v0.0** (condensed from the NeoMundi Metric Contract, English version dated 2026-08-16 — the more recent and more tightly audited of the two source-language versions; see [source-notes/SOURCE_STATUS.md](../source-notes/SOURCE_STATUS.md)).

This document explains what NeoMundi measurements and signals mean, their limits, and what conclusions may or may not be drawn from them. It does not define policy, execution authorization, or operational action.

> **The Metric Contract MUST NOT define a policy decision, execution authorization or operational action as the intrinsic meaning of a NeoMundi measurement.**
>
> **NeoMundi measures. The consuming system retains authority over decisions and actions.**

## Normative language

- **MUST / MUST NOT** — a binding semantic requirement.
- **SHOULD / SHOULD NOT** — a recommended requirement an implementation may depart from with justification.
- **MAY** — permitted but non-mandatory behaviour.

This contract's normative scope is limited to **meaning, interpretation and semantic boundaries**. Exact field names, JSON locations, enums, serialization, transport and version negotiation are not normative here — they belong to the interoperable measurement contract layer (see [INTEROPERABILITY.md](./INTEROPERABILITY.md)).

## Current operational anchor

Draft v0.0 is anchored in the structure of the observation payload currently exposed by the NeoMundi API:

```json
{
  "schema_version": "neomundi_observation_payload_v0.1",
  "observation_id": "nm-syn-001",
  "generated_at": "2026-06-28T06:42:47Z",
  "synthetic": true,
  "source": {},
  "measurement": {},
  "known_limitations": [],
  "measurement_boundary": []
}
```

This is an **operational reference example, not a complete normative JSON Schema**. Example values, identifiers and observed enums are non-normative. `synthetic: true` marks this specific example as synthetic — a synthetic observation MUST NOT be represented as a production observation.

## Fundamental concepts

- **Observation** — a runtime event or set of runtime executions under declared conditions from which one or more measurements may be produced. A measurement MUST remain attributable to the observation it belongs to.
- **Metric** — an observable property NeoMundi measures, together with the semantics required to interpret its values.
- **Measurement** — a result obtained from an observation via a declared method. It does not, by itself, constitute an external decision.
- **Metrological state** — an optional classification of a measurement per a declared, versioned taxonomy. It describes an observed condition, not a policy decision or execution authorization.

```text
Observation → measurement or signal → optional metrological interpretation → external consumption
```
The resulting decision or action is outside this contract.

## Source context

Information not explicitly present or declared in the observation context MUST NOT be silently inferred as measured or known. In particular, a model alias alone is not proof of provider identity, exact model version, or execution configuration.

## Interpreting in context

A value or signal MUST NOT be interpreted independently of applicable limitations and measurement boundaries when those materially affect its meaning. The presence of a numerical value does not, by itself, imply that all measurement dimensions were assessed.

## Measurement status and coverage

An observation may be complete, partial, not assessed, or otherwise limited.

- A partial observation MUST NOT be represented as complete.
- A value present within a partial observation MUST NOT imply that all measurement dimensions were assessed.
- Known incomplete coverage MUST remain distinguishable from complete coverage.

## Signal definitions

### `stability_score`

Describes a level of observed behavioural stability under the declared measurement conditions.

> **`stability_score` MUST NOT be interpreted as a measure of factual truth.**

It MUST NOT, by itself, establish safety, compliance, admissibility, execution authorization, or the overall quality of a system. High stability MAY coexist with a factually incorrect output.

> **Stability is not truth.**

### `coherence_score`

Describes an observed coherence property. It MUST NOT, by itself, be interpreted as factual validation, safety validation, a compliance determination, or execution authorization. It may be consumed together with other signals; this contract does not prescribe the consumer's resulting policy.

### `factual_validity_signal`

Represents information produced within the limits of its associated measurement method. A signal based only on runtime-available evidence MUST NOT be presented as independent verification of truth when no independent validation has been performed. A `null`, `unknown` or `not_assessed` value MUST NOT be interpreted as factual validation, absence of error, or zero factual risk. Observed taxonomies/enums remain descriptive until explicitly stabilized and versioned.

### `semantic_variability_signal`

Describes semantic variability observed under the applicable conditions. Low variability MUST NOT be interpreted as evidence of factual correctness. Elevated variability MUST NOT, by itself, identify the cause of the variation, identify which output is correct, or constitute proof of error.

### Latency and cost

NeoMundi may expose latency/cost measurements or bands. Draft v0.0 does not freeze definitive enums, exact thresholds, band boundaries, or routing consequences. An explicitly unknown latency or cost value MUST NOT be silently interpreted as a measured value.

### `risk_signal`

A measurement or interpretation signal within the declared limits of the metric. It MUST NOT automatically mean `ALLOW`, `BLOCK`, `ACCEPT`, `REJECT`, `COMPLIANT`, `NON_COMPLIANT`, `SAFE`, `UNSAFE`, `ADMISSIBLE`, or `NON_ADMISSIBLE`. A consuming system MAY use it as an input to its own policy; the resulting decision is outside this contract. Currently observed risk levels/types are not automatically normative categories in Draft v0.0.

## Known limitations

Any limitation that materially affects interpretation of a measurement MUST remain semantically associated with that measurement when interpreted or transmitted to support a decision. Exact format, location and serialization of limitations belong to interoperability.

## Measurement boundary

A NeoMundi measurement describes an observable property within a declared scope. It does not automatically constitute a general conclusion about the observed system.

> **A NeoMundi measurement MUST NOT, by itself, be interpreted as establishing truth, safety, authority, downstream permission or execution admissibility, unless a future explicitly versioned metric defines otherwise.**

This is one of the contract's fundamental normative boundaries. See also [CONSUMER_BOUNDARIES.md](./CONSUMER_BOUNDARIES.md).

## Separation between measurement and decision

NeoMundi is responsible for the declared semantics of its measurements. The consuming system remains responsible for the policy or operational action it derives from those measurements. External infrastructures MAY, for example, use a measurement to log, verify, regenerate, reroute, escalate, request human supervision, interrupt a workflow, support a compliance process, or produce/enrich an evidence artifact. This list is illustrative and non-exhaustive; none of these actions is the intrinsic meaning of the measurement.

## Infrastructure neutrality

This contract MUST NOT impose one downstream use as the unique interpretation of a measurement. The same measurement MAY be consumed by multiple infrastructures, within multiple architectures, for multiple purposes. Infrastructure-specific policy logic stays outside this contract.

## Unknown, null and non-assessed values

Measured value, unavailable value, `null`, `unknown`, and `not_assessed` are **not** semantically equivalent.

- `null` MUST NOT be interpreted as zero.
- `unknown` MUST NOT be interpreted as a measured, low, or high category.
- `not_assessed` MUST NOT be interpreted as absence of risk or successful validation.

The distinction MUST be preserved semantically. **`not measured` must never be read as `no issue detected`, and a partial measurement must never be read as a complete one.**

## Partial measurements

A partial observation MUST NOT be represented as complete. A value available within a partial observation MUST NOT imply that all measurement dimensions were assessed. Consuming systems SHOULD consider declared coverage when interpreting partial measurements.

## Traceability

The current representation may include identifiers such as `observation_id`, `source_batch_id`, `trace_id`, a timestamp, and version references. A measurement SHOULD remain attributable to its originating observation. Draft v0.0 does not yet freeze the mandatory traceability structure; requirements for hashes, signatures, receipts, mandatory identifiers, and cryptographic integrity belong to the interoperable measurement contract or dedicated specifications.

## Confidentiality and non-exposed data

This contract describes the data and measurements exposed by the measurement interface. It does not imply access to an AI system's internal computation data. Current synthetic examples may not expose raw prompts, raw model outputs, certain provider information, customer data, or proprietary structures — this observation does not constitute a universal normative prohibition in Draft v0.0. Confidentiality, security, and data-exposure requirements must be defined in dedicated specifications.

## Boundary with the interoperable measurement contract

This contract defines the **semantics** of measurements and signals. The interoperable measurement contract defines, or will define, **how** the corresponding objects are exchanged and consumed between systems (machine-readable structures, required fields, types, enums, serialization, compatibility, version negotiation, integration constraints). This contract MUST NOT freeze transport or interoperability details that have not yet been validated.

```text
AI execution → NeoMundi observation → NeoMundi measurement or signal → interoperability → consuming system → external decision or action
```

## Semantic versioning

A material change in the meaning of a measurement or signal MUST be explicitly versioned. This includes changes materially affecting the measured property, semantic definition, interpretation domain, fundamental limitations, or the meaning of a value/signal. Historical observations SHOULD remain interpretable according to the semantic version under which they were produced. Structural or serialization changes that do not alter meaning MAY be handled exclusively through schema/interoperability versioning. See also [VERSIONING.md](../VERSIONING.md).

## Explicitly deferred elements

Draft v0.0 does **not** yet freeze: the definitive JSON Schema; the definitive list of required fields; definitive field names; definitive enums; the transport protocol; version negotiation; cryptographic receipts; signatures and hashes; evidence packaging; provider disclosure rules; exact threshold values; exact band boundaries; automatic routing rules; automatic stop rules; compliance determination; admissibility determination; execution authorization.

These may belong to the interoperable measurement contract, evidence specifications, product configuration, consuming-system policy, or future explicitly versioned specifications.

## Normative core v0.0

1. A measurement **MUST** remain attributable to its observation.
2. A synthetic observation **MUST NOT** be represented as a production observation.
3. Undeclared information **MUST NOT** be silently inferred as measured or known.
4. A partial measurement **MUST NOT** be represented as complete.
5. Stability **MUST NOT** be interpreted as factual truth.
6. Coherence **MUST NOT**, by itself, be interpreted as factual validation.
7. A runtime factual signal **MUST NOT** be presented as independent verification of truth when it is not based on independent validation.
8. Semantic variability **MUST NOT** be treated as proof of factual correctness or as identification of the correct output.
9. A risk signal **MUST NOT** automatically become a policy or execution decision.
10. Material measurement limitations **MUST** remain semantically associated with interpretation.
11. A NeoMundi measurement **MUST NOT**, by itself, establish truth, safety, authority, downstream permission or execution admissibility.
12. Unknown, null or non-assessed states **MUST NOT** be silently converted into measured values.
13. Any material semantic change **MUST** be explicitly versioned.
14. This contract **MUST NOT** freeze unvalidated transport or interoperability details.
15. The consuming system retains authority over the decisions and actions it derives from NeoMundi measurements.

## Fundamental principle

**NeoMundi provides contextualized measurements and signals about observable AI-system behaviour within declared runtime boundaries.** These measurements may be consumed by multiple systems, infrastructures and use cases without transferring downstream decision authority to NeoMundi.

> **Measured by NeoMundi.**
> **Used according to the authority of the consuming system.**

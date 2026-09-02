# Versioning

NeoMundi's sources describe versioning at two levels that must not be confused: a conceptual triad described in the pre-freeze consumption-rules material, and the version fields actually observed in the one real signed contract example available. **These two are not fully reconciled in the current sources** — see the discrepancy noted below and in [source-notes/SOURCE_STATUS.md](./source-notes/SOURCE_STATUS.md).

## The conceptual triad (pre-freeze)

The Signal Interpretation & Consumption Rules material (status: experimental / pre-freeze) describes three distinct version identifiers a production-grade measurement should expose:

| Version | Refers to | Example use |
|---|---|---|
| `schema_version` | Serialization and payload structure. | Whether a consumer's parser can read the payload shape at all. |
| `metric_version` | Definition and semantics of the metric itself. | Whether `stability_score` still means what it meant last time it was consumed. |
| `normalizer_version` | The transformation/calibration applied to the raw or intermediate measurement. | Whether two `stability_score` values from different periods are comparable. |

**These are not interchangeable.** A change in one must not silently masquerade as a change in another — for example, a re-calibration of the normalizer is not a change in what the metric means, and must not be reported only as a `schema_version` bump.

## What the real signed contract example actually carries

The real signed RGC v0.1 example in [API_INTEGRATION_GUIDE.md §5](./API_INTEGRATION_GUIDE.md) does not use this exact triad. It carries:

- `identity.schema_version` (e.g. `"0.1.0"`) — payload/serialization version.
- `provenance.measurement_version` (e.g. `"3.0.0"`) — closer in role to the conceptual `metric_version` above, but under a different name.
- `provenance.normalizer_version` (e.g. `"1.0.0"`) — matches the conceptual `normalizer_version`.

There is no field named `metric_version` in the real example. **This repository does not assume `measurement_version` and `metric_version` are the same thing** — they occupy a similar conceptual role across two different, not-yet-reconciled sources, and only a future versioned specification can state whether they are meant to be identical, related, or distinct.

## Compatibility rule

Regardless of exact field names, the rule stated across the sources is consistent:

> A consumer MUST NOT silently consume an unknown measurement version as if it were semantically identical to a known one. Unknown or incompatible versions should enter fallback handling rather than best-effort interpretation.

**Always check `identity.schema_version` (or the equivalent version field for a given payload shape) before interpreting a contract.** Never apply one version's semantics to a payload carrying a different version identifier — this applies, for instance, between the documented RGC v0.1 and v0.2 shapes (v0.2 adds per-signal `signal_status`, absent from v0.1).

## What is not yet defined

Exact schema compatibility rules, version negotiation, and a canonical compatibility table are explicitly deferred by the Measurement Contract to future interoperability work. This repository does not invent them.

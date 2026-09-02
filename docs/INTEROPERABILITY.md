# Interoperability

**The interoperable contract defines the structure, representation and interpretation rules of runtime measurements produced by NeoMundi.**

This is a distinct layer from the [Measurement Contract](./MEASUREMENT_CONTRACT.md): the Measurement Contract defines what a signal *means*; this document is about how a measurement is *structured, versioned, carried, and independently checked* once it leaves NeoMundi.

> **Naming note.** The concrete implementation of this layer is internally identified as "RGC" in schema `$id`s and API paths (`/v1/rgc/...`). The authoritative interoperability specification itself deliberately does not put that acronym first — it calls itself the **NeoMundi Measurement Interoperability Contract**. This document follows that choice: **Interoperable Measurement Contract** / **NeoMundi Measurement Interoperability Contract** is the general term used throughout; "RGC" appears only where a concrete field, schema path, or endpoint requires it.

## The core principle

> **Absence of evidence is only meaningful over the measured domain.**

This is the governing rule behind everything else in this document. A contract must always keep three things distinguishable:

```text
MEASURED + NO SIGNAL          (a real measurement found nothing notable)
NOT MEASURED                  (no measurement was attempted or produced)
INSUFFICIENT COVERAGE         (a measurement was attempted but not enough evidence was available)
```

An unmeasured or insufficiently covered signal must never be represented by an invented reassuring numeric value. This is enforced at the schema level from v0.2 onward (see "Per-signal measurement status" below), not left to convention.

## Public interface, private implementation

> **Open interface ≠ open implementation.**

The interoperability contract standardizes the **interface between measurement and consumption**. It does not standardize, disclose, or require:

- NeoMundi's internal measurement implementation or formulas;
- a consumer's policy engine, thresholds, routing logic, or enforcement mechanisms;
- disclosure of partner-specific governance architecture or intellectual property.

```text
NeoMundi measurement
        ↓
PUBLIC INTEROPERABILITY LAYER
signed contract · schema · validation · verification
        ↓
──────────────── consumer boundary ────────────────
        ↓
PRIVATE / PARTNER-SPECIFIC LAYER
interpretation · policy · thresholds · decision · action
```

## Meaning vs. serialization vs. exchange vs. interpretation

- **Meaning** — what a signal represents (`stability_score` describes stability, not truth). Defined by the [Measurement Contract](./MEASUREMENT_CONTRACT.md).
- **Serialization** — how a measurement is encoded as data (field names, JSON structure, types). Defined by the JSON Schemas in [schema/](../schema/).
- **Exchange** — how a measurement moves between systems (which endpoint returns it, how it is fetched, how its integrity is checked in transit). Defined below.
- **Interpretation** — what a specific consuming system concludes from a measurement, and what it does next. The consumer's responsibility, not NeoMundi's — see [CONSUMER_BOUNDARIES.md](./CONSUMER_BOUNDARIES.md).

## Contract structure

Every contract has five sections:

```text
identity      — who/when/what produced this contract
provenance    — technical provenance of the measurement
observation   — the runtime measurement observation itself
governance    — non-binding advisory information
integrity     — independent-verification material
```

### `identity`

Correlates the observation across systems: schema version, request identifier, a W3C-Trace-Context-shaped trace identifier, timestamp, system identifier, mode, and a **pseudonymized** model identifier. The model field is schema-constrained to either the literal `local` or the pattern `model-[0-9a-f]{12}` — raw provider/model identifiers cannot validate against the schema.

### `provenance`

Measurement version, normalizer version, number of checks emitted, source batch identifier, canonicalization method. Does not expose raw conversational or business content.

### `observation`

Measurement status, measurement coverage, the observed signal values and their per-signal status (v0.2), an observation classification, confidence, limitations, and the measurement boundary statement. **A NeoMundi observation is a bounded measurement signal, not a universal verdict on the observed system.**

### `governance`

Non-binding advisory information only. A review recommendation is not an execution authorization, does not replace the consumer's policy, and does not automatically trigger any NeoMundi-imposed action. Schema-enforced invariant: `governance_boundary.execution_permission_changed` is always `false` — a NeoMundi signal never grants or revokes execution permission.

### `integrity`

SHA-256 payload fingerprint, canonicalization method, Ed25519/JWS signature, signer identity, and `key_id`.

## Versioning

Two schema versions currently exist, both included in this repository under [schema/](../schema/): `contract-v0.1.schema.json` and `contract-v0.2.schema.json`, with published `$id`s `https://schemas.neomundi.io/rgc/0.1.0/contract.schema.json` and `.../0.2.0/...`.

- **RGC v0.1** — historical. Signed v0.1 observations remain unchanged; their original semantics are preserved as historical facts, even where later found imprecise (see "A known historical inconsistency" below).
- **RGC v0.2** — introduces the corrected epistemic semantics described in this document. Introduced as a *new* version rather than a silent rewrite of v0.1, to preserve falsifiability, historical reproducibility, and cryptographic integrity of existing signed artifacts.

**A consumer must never validate or interpret a contract under a schema version other than the one it declares in `identity.schema_version`.** A `v0.2` contract checked against the `v0.1` schema (or vice versa) must be rejected before interpretation.

This is a different, non-interchangeable set of fields from the conceptual `schema_version` / `metric_version` / `normalizer_version` triad described in the pre-freeze consumption-rules material — see [VERSIONING.md](../VERSIONING.md) for that discrepancy, which remains open.

## Per-signal measurement status (RGC v0.2)

Each observed signal carries an explicit status:

```text
measured                — a valid numeric measurement was actually produced
not_measured             — the signal was not measured
insufficient_coverage    — available evidence was insufficient to produce a valid measurement
```

This is schema-enforced, not just documented: a signal whose status is `measured` **must** carry a numeric value; a signal whose status is anything else **must** carry `null`. `null` must never be interpreted as `0.0`, "safe", "normal", "within_bounds", or "no risk". See [schema/contract-v0.2.schema.json](../schema/contract-v0.2.schema.json) for the exact conditional rule.

## Measurement coverage (RGC v0.2)

The relationship between observation status and coverage is schema-enforced from v0.2 onward:

```text
measurement_status = complete   requires   measurement_coverage = 1.0
measurement_status = partial    requires   measurement_coverage < 1.0
```

Coverage is the fraction of the **declared measurement boundary** covered — it must not be read as the percentage of individual signal fields populated.

### A known historical inconsistency, preserved as-is

The real signed v0.1 example `within-bounds-no-review` (see [schema/examples/](../schema/examples/)) has `measurement_status: "complete"` together with `measurement_coverage: 0.6` — a combination the v0.2 schema now forbids. The source specification documents this itself as the ambiguity that motivated v0.2, and states explicitly that the signed v0.1 record must remain unchanged: modifying it would invalidate its hash and signature. This repository preserves that inconsistency rather than silently correcting it.

## Meaning of `observation_class` values

- **`within_bounds`** means only: *no threshold-crossing signal was detected within the measured domain.* It does **not** mean every dimension was measured, that the system is globally safe, or that unmeasured signals equal zero.
- **`flagged`** — measured evidence within the covered domain supports a flagged classification. A partially covered observation can legitimately still be `flagged`: partial coverage limits the *scope of inference*, not the ability to report evidence actually observed.
- **`not_assessed`** *(v0.2 only)* — the available measured evidence is insufficient to support either `within_bounds` or `flagged`. This prevents insufficient measurement from being silently converted into a reassuring classification. Not present in the v0.1 schema's `observation_class` enum.

## Temporal boundary

A record with `runtime_scope: "single_request"` describes exactly one observation. It cannot by itself establish frequency, persistence, recurrence, trend, or drift — those properties require comparison across a series of observations. A single-request record must never be interpreted as evidence of temporal behaviour it does not measure.

## Timestamping

`identity.timestamp` is one of the claims signed by the JWS (see Integrity below), so it is tamper-evident once the contract is signed.

## Integrity and independent verification

1. A canonical JSON object is built from exactly four sections — `identity`, `provenance`, `observation`, `governance` (`integrity` is excluded from its own hash).
2. That object is serialized with sorted keys and no whitespace, then hashed with SHA-256 → `integrity.payload_hash`.
3. The hash (plus `hash_algorithm`, `schema_version`, `request_id`, `timestamp`) is signed as a compact Ed25519 JWS (`alg=EdDSA`) → `integrity.signature`. There is no hash-only fallback: if a valid signature cannot be produced, a valid production contract must not be emitted.

A party that does not trust NeoMundi's infrastructure can verify a contract independently, using only the public schema and public keys (no API key required):

```bash
curl https://api.neomundi.io/v1/rgc/schema
curl https://api.neomundi.io/v1/rgc/jwks
```

**This has been independently re-verified while building this repository**: both real signed v0.1 examples in [schema/examples/](../schema/examples/) were checked end-to-end (SHA-256 recomputation + Ed25519/JWS signature verification against the bundled public test key) and both passed (`hash_match=True`, `signature_valid=True`), and all four RGC examples validated against their declared schema version with zero errors. The exact verification steps are in [API_INTEGRATION_GUIDE.md §6](../API_INTEGRATION_GUIDE.md); a reference implementation is in [reference/python/](../reference/python/).

## Data sovereignty

The contract is designed to avoid transporting raw conversational or business content. It does not contain raw user prompts, raw model responses, or raw provider/model identifiers (schema-enforced via the `identity.model` pattern). It also does not require disclosure of a consumer's proprietary policies, thresholds, decision rules, or enforcement mechanisms.

## Exchange / consumer workflow

```text
1. Receive
2. Match schema version      — contract.identity.schema_version == schema.version
3. Validate                  — against the matching JSON Schema in schema/
4. Check sovereignty boundaries
5. Verify integrity          — SHA-256 + Ed25519/JWS
6. Interpret                 — bounded by the measured domain
7. Apply consumer policy     — belongs entirely to the consumer, not to NeoMundi
8. Retain an auditable receipt
```

The contract is fetched via a dedicated endpoint (`POST /v1/rgc/contracts/{request_id}`), separate from the measurement call itself (`POST /v1/govern`) — retrieving the signed contract is explicitly optional relative to obtaining the measurement.

## Standards used

- **JSON Schema Draft 2020-12** — structural and semantic validation.
- **W3C Trace Context** — the shape of `identity.trace_id`, for cross-system correlation; this does not replace a platform's own internal tracing.
- **SHA-256** — canonical payload fingerprint (detects modification; not itself the signature).
- **JWS (RFC 7515) / Ed25519 / JWK** — signature and public-key representation.
- **CloudEvents** — the structure reuses general principles around identity, source, time, and event type, while keeping NeoMundi-specific field names. NeoMundi does not claim full CloudEvents envelope compliance.

## What this contract does not do

It does not grant or revoke execution authorization, replace a consumer's policy engine, decide on behalf of a third-party infrastructure, certify third-party data or an AI system as globally safe, make claims beyond the measured domain, convert unmeasured evidence into reassuring values, infer drift from a single observation, require access to NeoMundi's internal code or formulas, transport raw prompts or responses, or require disclosure of a partner's policy, thresholds, or enforcement logic.

## What is not yet frozen

The exact relationship between this interoperability layer's signal vocabulary (`stability_score`, `coherence_score`, `factual_hallucination_score`, `semantic_instability_score`, `semantic_risk`) and the Measurement Contract's own vocabulary (`stability_score`, `coherence_score`, `factual_validity_signal`, `semantic_variability_signal`, `risk_signal`) is not stated by any source — see [source-notes/SOURCE_STATUS.md](../source-notes/SOURCE_STATUS.md). The exact mechanism for retrieving multiple historical schema versions from a live API should be treated as its own versioned API contract and must not be assumed by a consumer implementation.

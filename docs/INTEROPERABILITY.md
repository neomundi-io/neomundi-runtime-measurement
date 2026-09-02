# Interoperability

**The interoperable contract defines the structure, representation and interpretation rules of runtime measurements produced by NeoMundi.**

This is a distinct layer from the [Measurement Contract](./MEASUREMENT_CONTRACT.md): the Measurement Contract defines what a signal *means*; this document is about how a measurement is *structured, versioned, carried, and — where applicable — independently checked* once it leaves NeoMundi.

> **Internal naming note.** The concrete implementation of this layer currently observed in the API is referred to internally as "RGC" (see [API_INTEGRATION_GUIDE.md](../API_INTEGRATION_GUIDE.md)). This document uses **Interoperable Measurement Contract** as the general term. Where a concrete example is shown, it is the RGC structure, because that is what is actually implemented today — not because the name "RGC" is the intended public term.

## Meaning vs. serialization vs. exchange vs. interpretation

Four different things are easy to conflate; the sources keep them separate:

- **Meaning** — what a signal represents (`stability_score` describes stability, not truth). Defined by the [Measurement Contract](./MEASUREMENT_CONTRACT.md).
- **Serialization** — how a measurement is encoded as data (field names, JSON structure, types). This is what the interoperable contract defines.
- **Exchange** — how a measurement moves between systems (which endpoint returns it, how it is fetched, how its integrity is checked in transit).
- **Interpretation** — what a specific consuming system concludes from a measurement, and what it does next. This is the consumer's responsibility, not NeoMundi's — see [CONSUMER_BOUNDARIES.md](./CONSUMER_BOUNDARIES.md).

The Measurement Contract explicitly refuses to freeze serialization or exchange details until they are validated as part of interoperability work. That work is, per the sources, still in progress.

## Structure

The one real, signed example available (RGC v0.1, reproduced in full in [API_INTEGRATION_GUIDE.md §5](../API_INTEGRATION_GUIDE.md)) is organized into five sections:

- `identity` — schema version, request/trace identifiers, timestamp, system and model identifiers, mode.
- `provenance` — measurement and normalizer versions, number of checks emitted, batch identifier, canonicalization method.
- `observation` — runtime scope, measurement status and coverage, the observed signals themselves, known limitations, and the measurement boundary statement.
- `governance` — an advisory block only (see below); in the real example, `governance_boundary.authorization_status` is `"not_applicable"` and `execution_permission_changed` is `false`.
- `integrity` — the payload hash, hash algorithm, canonicalization method, signature, signer identity, key id, confidentiality class, and retention reference.

A separate, simpler illustrative structure appears in the Measurement Contract itself (`schema_version`, `observation_id`, `generated_at`, `synthetic`, `source`, `measurement`, `known_limitations`, `measurement_boundary`). **These are two different examples from two different source documents, not two views of one frozen schema** — see [source-notes/SOURCE_STATUS.md](../source-notes/SOURCE_STATUS.md) for why they are not yet reconciled.

## Versioning

The real RGC example carries `identity.schema_version` (e.g. `"0.1.0"`) and `provenance.measurement_version` / `provenance.normalizer_version`. This is a different set of version fields from the `schema_version` / `metric_version` / `normalizer_version` triad described conceptually in the pre-freeze consumption-rules material (see [VERSIONING.md](../VERSIONING.md) for the full discussion, including this naming discrepancy). In both cases the underlying rule is the same: **a consumer must never apply one version's semantics to a payload carrying a different version identifier.**

## Provenance

The `provenance` block records what produced the measurement (measurement/normalizer version, number of checks emitted) and how it can be traced back (`source_batch_id`, canonicalization method). The Measurement Contract does not yet freeze a mandatory traceability structure beyond this; requirements for stronger guarantees (hashes, signatures, receipts) are exactly what the `integrity` block below already implements in the real example, ahead of a fully versioned specification.

## Timestamping

Every layer of the real example carries a timestamp (`identity.timestamp`), and the JWS signature (see Integrity below) signs that timestamp as one of its claims — so the timestamp itself is tamper-evident once the contract is signed.

## Integrity

The real example is hashed and signed:

1. A canonical JSON object is built from exactly four sections — `identity`, `provenance`, `observation`, `governance` (the `integrity` block is excluded from its own hash).
2. That object is serialized with sorted keys and no whitespace, then hashed with SHA-256 → `integrity.payload_hash`.
3. The hash (plus `hash_algorithm`, `schema_version`, `request_id`, `timestamp`) is signed as a JWS using `EdDSA` (Ed25519), producing `integrity.signature`.

This is described at the level needed to know *that* independent verification is possible and *what* it checks — not as a cryptography tutorial. The exact verification steps (for implementers) are in [API_INTEGRATION_GUIDE.md §6](../API_INTEGRATION_GUIDE.md), and a working reference implementation is in [reference/python/](../reference/python/).

## Exchange / machine consumption

The contract is fetched via a dedicated endpoint (`POST /v1/rgc/contracts/{request_id}`), separate from the measurement call itself (`POST /v1/govern`) — retrieving the signed contract is explicitly optional relative to obtaining the measurement. Public endpoints (`GET /v1/rgc/schema`, `GET /v1/rgc/jwks`) require no API key, so that a third party can verify a contract without needing NeoMundi credentials at all.

## Independent verification, where applicable

Because the hash and signature cover only declared sections of the payload, and the public key material is fetchable without authentication, a party that does not trust NeoMundi's infrastructure can still check that a specific contract (a) has not been altered since it was signed, and (b) was in fact signed by the claimed NeoMundi signing key. This is "where applicable" because it currently applies to the v0.1 RGC contract structure as documented; it is not yet described as a general property of every NeoMundi measurement.

## What is not yet frozen

Per the Measurement Contract's own explicit deferral list: the definitive JSON Schema, the definitive required-field list, definitive enums, the transport protocol, version negotiation rules, and evidence-packaging rules are **not** frozen by Draft v0.0. The complete RGC JSON Schema files referenced by the API guide (`schema/contract-v0.1.schema.json`, `schema/contract-v0.2.schema.json`) were not supplied to this repository — see [source-notes/SOURCE_STATUS.md](../source-notes/SOURCE_STATUS.md).

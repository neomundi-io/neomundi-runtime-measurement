# NeoMundi Runtime Measurement Layer

[🇬🇧 English](./README.md) ·
[🇫🇷 Français](./README_FR.md)

## The missing measurement context for interpreting AI behavior

NeoMundi measures the behavioral state of an AI system at a specific
point in time, within a defined measurement framework.

Through a universal connector, this independent, timestamped and
comparable measurement signal provides the context needed to interpret:

- observations;
- detections;
- audits;
- diagnoses;
- comparisons;
- insurance assessments;
- evidence records.

NeoMundi provides this context without replacing the infrastructure,
rules or decision mechanisms of the system consuming it.

**Integrate once. Strengthen multiple downstream uses.**

> **Your system. Your decisions. Our measurement signal.**

### Activate the layer and obtain your first measurement

[**Follow the Quickstart guide →**](./QUICKSTART.md)

**One API call · Universal connector · Infrastructure preserved**

**Privacy by design · Bring your own keys**

~~~text
AI System
    │
    ▼
NeoMundi Runtime Measurement Layer
    │
    ▼
Measurement Signals
    │
    ▼
Interoperable Measurement Contract
    │
    ▼
Customer or Integrator System
~~~

---

## What NeoMundi does

### Runtime measurement

NeoMundi observes the behavior of an AI system during or after its
execution, under declared conditions.

The measurement describes what was observed in a specific context. It
does not define an absolute or permanent state of the system.

### Behavioral and operational signals

The layer can produce different signals, including:

- `stability_score`;
- `coherence_score`;
- `factual_validity_signal`;
- `semantic_variability_signal`;
- `risk_signal`.

The definition, scope and limits of each signal are documented in the
[measurement contract](./docs/MEASUREMENT_CONTRACT.md).

### Defined semantics

Each signal is accompanied by an explicit definition.

The documentation specifies:

- what the signal measures;
- the conditions under which it was produced;
- how it may be interpreted;
- what cannot be concluded from it.

The corresponding rules are available in the
[measurement interpretation table](./docs/MEASUREMENT_INTERPRETATION_TABLE.md).

### Reproducibility

The measurement conditions, protocol and applicable versions are
declared.

A measurement can therefore be:

- reproduced;
- compared;
- verified;
- independently challenged.

### Comparability over time

Measurements include explicit version information.

This makes it possible to distinguish:

- the schema version;
- the metric version;
- the normalizer version.

Historical observations therefore remain interpretable as the contract
evolves.

See the
[versioning documentation](./VERSIONING.md).

### Traceability

Identifiers, timestamps and provenance information connect each
measurement to the observation that produced it.

### Interoperability

Measurements are exposed as structured, machine-readable records.

The interoperable contract allows customer infrastructures to receive,
store, exchange and use the signal without becoming NeoMundi systems.

See the
[interoperability documentation](./docs/INTEROPERABILITY.md).

### Independent verifiability

When these elements are produced, the record may contain:

- a cryptographic hash of the content;
- a verifiable signature;
- the information required to verify its integrity.

A third party can therefore verify the integrity of a record without
having to trust NeoMundi’s infrastructure.

---

## What NeoMundi produces

NeoMundi produces measured behavioral context that is structured and
machine-readable.

### Measurement signals

The signals describe the observed behavior of the AI system under the
declared conditions.

They may include information about:

- stability;
- coherence;
- factual validity;
- semantic variability;
- observed risk.

### Structured records

Each measurement can be linked to:

- a request;
- an observation;
- a system;
- a specific point in time;
- a declared protocol.

### Version information

The record distinguishes between schema, metric and normalization
mechanism versions.

### Provenance information

Provenance indicates what produced the measurement and under which
protocol.

### Integrity information

The record may contain a content hash and a verifiable cryptographic
signature.

### An interoperable JSON contract

Measurements can be exposed in a structured, versioned and
machine-readable format.

The schemas are available in the
[`schema`](./schema/)
directory.

---

## Why this context matters

A raw observation is not always enough to understand the behavioral
state of the system that produced it.

NeoMundi adds the measurement context needed to interpret that
observation at a specific point in time.

The same measurement primitive can support multiple downstream uses:

- observability;
- drift detection;
- audit;
- diagnosis;
- comparison;
- governance;
- insurance;
- optimization;
- orchestration;
- control;
- creation of evidence records.

These uses are built and operated by the consuming system.

NeoMundi provides the measurement signal. The consuming system retains
its architecture, rules and decision authority.

> **One measurement primitive. Multiple applications.**
>
> **Multiple infrastructures, without replacing them.**

---

## How to integrate NeoMundi

Integration relies on a common interface that allows different
infrastructures to consume the same measurement contract.

### Quickstart

[**Activate the layer and obtain your first measurement →**](./QUICKSTART.md)

The Quickstart guide presents the shortest path for connecting a system
and obtaining a first measurement.

### API integration guide

The
[API integration guide](./API_INTEGRATION_GUIDE.md)
describes:

- endpoints;
- payloads;
- headers;
- authentication;
- error handling;
- response processing.

### Measurement contract

The
[measurement contract](./docs/MEASUREMENT_CONTRACT.md)
defines the meaning, scope and limits of the signals.

### Interpretation table

The
[measurement interpretation table](./docs/MEASUREMENT_INTERPRETATION_TABLE.md)
indicates what may and may not be concluded from a signal.

### Interoperability contract

The
[interoperability documentation](./docs/INTEROPERABILITY.md)
describes the structure, versioning, provenance and exchange of the
measurement.

---

## Architectural boundary

> **NeoMundi measures.**
>
> **The consuming system interprets, governs and acts.**

**Measurement ≠ Interpretation ≠ Policy ≠ Execution**

The NeoMundi Runtime Measurement Layer is not:

- an AI governance platform;
- a compliance engine;
- a policy engine;
- a decision engine;
- a monitoring dashboard;
- a business application;
- an autonomous blocking or authorization mechanism.

NeoMundi does not decide:

- `ALLOW`;
- `BLOCK`;
- `STOP`;
- `ROUTE`;
- or any other operational consequence.

A NeoMundi measurement does not, by itself, constitute proof of truth,
safety, compliance or admissibility.

It provides independent, timestamped, traceable and comparable
behavioral context that can strengthen the systems responsible for
these functions.

See the documentation on
[consumer boundaries](./docs/CONSUMER_BOUNDARIES.md).

---

## Integration principles

### Infrastructure preserved

NeoMundi integrates with existing infrastructure without requiring its
replacement.

### Responsibility preserved

The consuming system retains:

- its rules;
- its thresholds;
- its policies;
- its decisions;
- its actions.

### Privacy by design

The integration is designed to limit exchanges to the elements required
for measurement.

### Bring your own keys

The consuming system retains control over its keys and provider access.

### Independent consumption

The same signal can be consumed by multiple infrastructures without
imposing a shared governance model or interpretation.

---

## Documentation

### Get started

[QUICKSTART.md](./QUICKSTART.md)

Activate the layer and obtain a first measurement.

### Integrate the API

[API_INTEGRATION_GUIDE.md](./API_INTEGRATION_GUIDE.md)

Understand the endpoints, payloads, headers and error-handling
mechanisms.

### Understand the measurements

[docs/MEASUREMENT_CONTRACT.md](./docs/MEASUREMENT_CONTRACT.md)

Understand the meaning, scope and limits of each measurement.

### Interpret the signals

[docs/MEASUREMENT_INTERPRETATION_TABLE.md](./docs/MEASUREMENT_INTERPRETATION_TABLE.md)

Identify what may and may not be concluded from a signal.

### Consume the interoperable contract

[docs/INTEROPERABILITY.md](./docs/INTEROPERABILITY.md)

Understand the structure, versioning, provenance and exchange of
measurements.

### Respect the usage boundaries

[docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md)

Distinguish measurement, interpretation, policy and execution.

### Understand versioning

[VERSIONING.md](./VERSIONING.md)

Distinguish between schema, metric and normalizer versions.

### Review product changes

[CHANGELOG.md](./CHANGELOG.md)

Review the product’s change history.

---

## Product architecture

This repository contains only the NeoMundi measurement primitive.

Layers that interpret the measurement or act on the signal are
intentionally separated.

~~~text
neomundi-runtime-measurement
              │
              ▼
      neomundi-actionability
              │
              ▼
      Specialized Applications
~~~

These applications may include:

- compliance;
- insurance;
- governance;
- orchestration;
- diagnosis;
- decision support;
- change assurance.

This separation protects the neutrality of the measurement and allows
multiple infrastructures to consume the same signal according to their
own rules.

---

## Founding principle

> **One measurement primitive. Multiple applications.**
>
> **Your system. Your decisions. Our measurement signal.**

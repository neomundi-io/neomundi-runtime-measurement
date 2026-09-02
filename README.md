# NeoMundi Runtime Measurement Layer

[🇬🇧 English](./README.md) · [🇫🇷 Français](./README_FR.md)

**NeoMundi is a runtime measurement layer for AI systems.**

It observes the runtime behaviour of an AI system's execution and produces structured, versioned, interoperable measurements about that behaviour. It does not decide what should happen as a result.

> **NeoMundi measures. The consuming system interprets, governs and acts.**

---

## How it fits together

```text
AI System
   │
   ▼
NeoMundi Runtime Measurement API
   │
   ▼
Runtime Measurement
   │
   ▼
Interoperable Measurement Contract
   │
   ▼
Customer / Integrator Systems
   (interpretation, policy, action)
```

NeoMundi sits between an AI system's execution and the infrastructure that consumes information about that execution. It does not sit downstream of the decision.

## The four central elements

1. **NeoMundi API** — the interface through which an AI execution is observed and measured. See [API_INTEGRATION_GUIDE.md](./API_INTEGRATION_GUIDE.md).
2. **Runtime measurement** — the structured output describing observed behaviour (stability, coherence, factual-validity and risk signals, among others) under declared conditions and limitations. See [docs/MEASUREMENT_CONTRACT.md](./docs/MEASUREMENT_CONTRACT.md).
3. **Interoperable measurement contract** — the versioned, machine-consumable, independently verifiable representation of a measurement, designed to be exchanged and consumed across systems. See [docs/INTEROPERABILITY.md](./docs/INTEROPERABILITY.md).
4. **Official integration documentation** — this repository: the API guide, the measurement contract, the interpretation table and the consumer boundaries that together define correct usage.

A fifth, necessary layer sits alongside these: **documentation of interpretation**. A measurement is only usable correctly if its meaning, and the limits of that meaning, are documented at the same time it is produced. [docs/MEASUREMENT_INTERPRETATION_TABLE.md](./docs/MEASUREMENT_INTERPRETATION_TABLE.md) and [docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md) exist for this reason — they are part of what makes the measurement layer usable, not a governance or compliance layer in themselves.

## What NeoMundi does

- Observes the runtime execution of an AI system under declared conditions.
- Produces versioned runtime measurements and signals (e.g. `stability_score`, `coherence_score`, `factual_validity_signal`, `semantic_variability_signal`, `risk_signal`).
- Documents the meaning, limitations and boundaries of each measurement.
- Exposes those measurements through an interoperable contract that can be consumed, exchanged, and where applicable independently verified, by external systems.
- Distinguishes explicitly between what is measured, what is unknown, and what is not assessed.

## What NeoMundi does not do

- It is not a dashboard.
- It is not a `.exe` application.
- It is not a governance engine.
- It is not a compliance engine.
- It is not a policy engine.
- It is not an actionability layer.
- It is not a business application.
- It does not decide `ALLOW`, `BLOCK`, `STOP`, or any other operational or execution consequence. It measures; the consuming system decides.
- It does not itself constitute proof of truth, safety, compliance or admissibility. See [docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md).

## Documentation map

| Document | Purpose |
|---|---|
| [QUICKSTART.md](./QUICKSTART.md) | Get a first measurement in a few minutes |
| [API_INTEGRATION_GUIDE.md](./API_INTEGRATION_GUIDE.md) | Endpoints, payloads, headers, error handling |
| [docs/MEASUREMENT_CONTRACT.md](./docs/MEASUREMENT_CONTRACT.md) | What each measurement and signal means, and its limits |
| [docs/MEASUREMENT_INTERPRETATION_TABLE.md](./docs/MEASUREMENT_INTERPRETATION_TABLE.md) | Quick-reference table: signal → meaning → what it does not mean |
| [docs/INTEROPERABILITY.md](./docs/INTEROPERABILITY.md) | Structure, versioning, provenance and exchange of the measurement contract |
| [docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md) | The boundary between measurement, interpretation, policy and execution |
| [VERSIONING.md](./VERSIONING.md) | `schema_version`, `metric_version`, `normalizer_version` |
| [CHANGELOG.md](./CHANGELOG.md) | Change history |
| [schema/](./schema/) | Known payload examples, labelled by status (real signed / illustrative / pre-freeze) |
| [reference/python/](./reference/python/) | Minimal, non-normative reference integration starter |
| [source-notes/SOURCE_STATUS.md](./source-notes/SOURCE_STATUS.md) | What is normative, experimental, pre-freeze, or contradictory in the sources behind this repository |

## Status

This repository documents a measurement layer whose contract is still partly in **Draft** and, for some signals, explicitly **experimental / pre-freeze**. Every document below states its own status. Nothing here should be read as a finalized, frozen specification unless it says so explicitly.

## Future architecture

This repository is the measurement primitive only. Layers that act on the measurement — actionability, compliance evidence, insurance evidence, change assurance, and other applications — are intentionally kept out of this repository and will live in separate, dependent repositories.

```text
neomundi-runtime-measurement
        ↑
        │ dependency
neomundi-actionability
        ↑
        │
solution-specific layers
        ├── compliance evidence
        ├── insurance evidence
        ├── change assurance
        └── other applications
```

**One measurement primitive. Multiple applications.**

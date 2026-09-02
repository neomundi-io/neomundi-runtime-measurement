# NeoMundi Runtime Measurement Layer

[🇬🇧 English](./README.md) · [🇫🇷 Français](./README_FR.md)

**Measure, characterize and trace AI behavior in production.**

Produce reproducible, machine-readable and independently verifiable measurement evidence for monitoring, audit, governance, assurance and optimization.

**Defined semantics · Comparable over time · Structured JSON · Timestamped · Versioned · Hash & signature verifiable**

> **NeoMundi measures. The consuming system interprets, governs and acts.**

```text
AI System
   │
   ▼
NeoMundi Runtime Measurement Layer
   │
   ▼
Runtime Signals
   │
   ▼
Interoperable Measurement Contract
   │
   ▼
Customer / Integrator Systems
```

---

## What it does

- **Runtime measurement** — observes the behaviour of an AI system during or after execution, under declared conditions.
- **Behavioural and operational signals** — e.g. `stability_score`, `coherence_score`, `factual_validity_signal`, `semantic_variability_signal`, `risk_signal`. See [docs/MEASUREMENT_CONTRACT.md](./docs/MEASUREMENT_CONTRACT.md).
- **Defined semantics** — each signal's meaning, limits, and what it does *not* mean are documented at the same time it is produced, not left to inference. See [docs/MEASUREMENT_INTERPRETATION_TABLE.md](./docs/MEASUREMENT_INTERPRETATION_TABLE.md).
- **Reproducibility** — measurement conditions, protocol, and versions are declared, so a measurement can be reproduced or independently challenged.
- **Comparison over time** — signals carry explicit version information so historical observations remain interpretable as the contract evolves. See [VERSIONING.md](./VERSIONING.md).
- **Traceability** — identifiers, timestamps, and provenance connect a measurement back to the observation that produced it.
- **Interoperable measurement records** — measurements are exposed through a structured, machine-consumable, independently verifiable contract. See [docs/INTEROPERABILITY.md](./docs/INTEROPERABILITY.md).

"Characterize" means a NeoMundi measurement comes with defined semantics, declared scope, versioning, and interpretation rules. It does **not** mean NeoMundi universally diagnoses root causes — see [docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md).

## What it produces

- **Runtime signals** describing observed behaviour (stability, coherence, factual-validity, semantic-variability, risk — among others).
- **Structured measurement records**, timestamped and identifiable back to the observation and request that produced them.
- **Version information** distinguishing schema, metric, and normalizer versions — see [VERSIONING.md](./VERSIONING.md).
- **Provenance** — what produced the measurement and under which protocol.
- **Integrity information** — a payload hash and, where produced, a cryptographic signature that a third party can verify independently, without needing to trust NeoMundi's infrastructure.
- **Interoperable, machine-readable JSON**, where supported by the interoperability layer — see [schema/](./schema/) and [docs/INTEROPERABILITY.md](./docs/INTEROPERABILITY.md). The interoperable measurement contract defines the structure, representation and interpretation rules of runtime measurements produced by NeoMundi.

## Why it matters

The same measurement layer can support downstream:

- monitoring
- audit
- governance
- assurance
- optimization

These are downstream uses of the measurement, built and operated by the consuming system — **this repository does not implement any of them**. One measurement primitive can feed several different downstream infrastructures without those infrastructures needing to become NeoMundi systems.

## How it integrates

- [QUICKSTART.md](./QUICKSTART.md) — get a first measurement in a few minutes.
- [API_INTEGRATION_GUIDE.md](./API_INTEGRATION_GUIDE.md) — endpoints, payloads, headers, error handling.
- [docs/MEASUREMENT_CONTRACT.md](./docs/MEASUREMENT_CONTRACT.md) — what each measurement and signal means, and its limits.
- [docs/MEASUREMENT_INTERPRETATION_TABLE.md](./docs/MEASUREMENT_INTERPRETATION_TABLE.md) — quick-reference table: signal → meaning → what it does not mean.
- [docs/INTEROPERABILITY.md](./docs/INTEROPERABILITY.md) — structure, versioning, provenance and exchange of the measurement contract.

## Architectural boundary

> **NeoMundi measures.**
> **The consuming system interprets, governs and acts.**

**Measurement ≠ Interpretation ≠ Policy ≠ Execution**

The NeoMundi Runtime Measurement Layer is not:

- an AI governance platform;
- a compliance engine;
- a policy engine;
- a decision engine;
- a monitoring dashboard;
- a `.exe` application;
- a business application.

Monitoring, audit, governance, assurance, and optimization are downstream uses of the measurement — not this product. NeoMundi does not decide `ALLOW`, `BLOCK`, `STOP`, or any other operational or execution consequence, and a NeoMundi measurement does not itself constitute proof of truth, safety, compliance, or admissibility. See [docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md).

---

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

This repository documents a measurement layer whose contract is still partly in **Draft** and, for some signals, explicitly **experimental / pre-freeze**. Every document above states its own status. Nothing here should be read as a finalized, frozen specification unless it says so explicitly.

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

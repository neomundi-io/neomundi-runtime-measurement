<div align="center">

<sub><b>English</b> · <a href="README_FR.md">Français</a></sub>

[Station — Observe & Experiment](https://github.com/neomundi-io/neomundi-station-public) · **[Runtime Measurement — Measure & Integrate](README.md)** · [Use Cases — Applications, Pilots & Evidence](https://github.com/neomundi-io/neomundi-use-cases) · [Create an Account — ControlTower](https://controltower.neomundi.io/welcome)

<sub>[NeoMundi GitHub organization](https://github.com/neomundi-io)</sub>

# NeoMundi Runtime Measurement

## Turn AI behavior into measurable signals.

**Independent AI measurement infrastructure for your existing systems.**

[![Layer: runtime measurement](https://img.shields.io/badge/layer-runtime_measurement-475569?style=flat-square)](#how-it-works)
[![REST: primary path](https://img.shields.io/badge/REST-primary_path-0f766e?style=flat-square)](QUICKSTART.md)
[![SSE: alternative](https://img.shields.io/badge/SSE-alternative_path-2563eb?style=flat-square)](API_INTEGRATION_GUIDE.md)
[![Interop: v0.1 signed](https://img.shields.io/badge/Interop-v0.1_signed-0f766e?style=flat-square)](docs/INTEROPERABILITY.md)
[![SDK and MCP: see status](https://img.shields.io/badge/SDK_%26_MCP-see_status-a16207?style=flat-square)](#integration-status)

**[Start here](START_HERE.md)** · [First measurement](QUICKSTART.md) · [API guide](API_INTEGRATION_GUIDE.md) · [Signals](docs/MEASUREMENT_CONTRACT.md) · [Interop](docs/INTEROPERABILITY.md) · [Limits](#known-limitations)

> **Your system. Your decisions. Our measurement signal.**

</div>

---

NeoMundi measures an AI execution under declared conditions and returns a structured, timestamped measurement record. Your system can retain the record, compare compatible observations, or request a signed interoperability contract for independent verification.

NeoMundi does **not** decide whether your application should allow, block, reroute or approve anything. Interpretation, policy and execution remain with the consuming system.

```text
Measurement ≠ Interpretation ≠ Policy ≠ Execution
```

## Choose your path

| Goal | Path | Start |
|---|---|---|
| Measure an answer you already produced | REST `POST /v1/govern` | [Quickstart](QUICKSTART.md) |
| Generate through NeoMundi and receive streamed events | SSE `POST /v1/govern/stream` | [API guide](API_INTEGRATION_GUIDE.md#3-step-1--v1governstream-get-the-model-response) |
| Integrate from Python | Python SDK | [SDK](https://github.com/neomundi-io/neomundi-python-sdk) |
| Measure from an agent | MCP connector | [MCP](https://github.com/neomundi-io/neomundi-measurement-mcp) |
| Validate a portable record | JSON Schema + signature verification | [Interoperability](docs/INTEROPERABILITY.md) |
| Use the hosted instrument | NeoMundi Station | [Station](https://github.com/neomundi-io/neomundi-station-public) |

## Get your first measurement

The primary path measures an execution you already hold. It does not ask NeoMundi to generate the answer and does not require a provider API key.

```bash
curl -X POST "https://api.neomundi.io/v1/govern" \
  -H "X-API-Key: YOUR_NEOMUNDI_KEY" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
    "source_type": "llm",
    "mode": "OBS",
    "llm_prompt": "What is the capital of France?",
    "llm_response": "Paris.",
    "raw_metrics": {"token_count": 1, "latency_ms": 120}
  }'
```

The `token_count: 1` and `latency_ms: 120` values above are illustrative placeholders, not measured data and not values captured from a live observation.

The route and request fields are confirmed by existing integration material. No response values are shown because this documentation change did not perform a new live API call. Preserve the raw response, its versions, and every partial or unavailable state; never replace a missing value with zero.

[**Follow the complete REST path →**](QUICKSTART.md)

## What NeoMundi measures

NeoMundi reports bounded behavioral and operational signals for one observation. Depending on the deployed measurement version and available checks, records may expose signals related to stability, coherence, factuality, semantic variability or risk.

The Metric Contract vocabulary, experimental `G`/`g_score`/`∆G` material and RGC fields are distinct vocabularies. No undocumented mapping is implied. Read the [Measurement Contract](docs/MEASUREMENT_CONTRACT.md) and [Interpretation Table](docs/MEASUREMENT_INTERPRETATION_TABLE.md).

## How it works

```text
Your AI execution
       ↓
NeoMundi Measurement API
       ↓
Versioned measurement record
       ├──── optional signed interoperability contract
       ↓
Your storage, interpretation, policy and action
```

The API includes a historical field named `governance.decision`. Values such as `ALLOW`, `FLAG`, `REROUTE`, `HUMAN_REVIEW` or `STOP` are measurement-layer signals—not permissions, commands or actions executed by NeoMundi. The interoperability schema constrains `execution_permission_changed` to `false`.

## What your system receives

A response may include an identifier and timestamp, version and provenance information, measured values, status and coverage, limitations, and advisory fields. For portable exchange, request a versioned JSON contract, validate it against the matching schema, and verify its SHA-256 fingerprint and Ed25519/JWS signature.

## Integration status

Checked against the linked repositories on **30 October 2026**.

| Path | Status | Evidence and limit |
|---|---|---|
| REST API | **Available; examples qualified** | Route and fields are confirmed. Response values remain illustrative until captured live. |
| SSE API | **Available alternative** | NeoMundi calls the provider and receives its credential for that call. Not required for an existing execution. |
| Python SDK 2.0.0 | **Implemented; live V2 qualification pending** | REST/SSE implemented and offline tests pass; installed V2 live qualification remains pending. |
| Local MCP plugin 0.2.0 | **Pilot-evaluated** | One bounded REST/SSE live qualification completed on 26 October 2026. |
| MCP 0.3.0-rc.1 source | **Release candidate** | Response-schema validation added; companion backend deployment and fresh qualification required. |
| Hosted MCP | **Transport validated; contract pending** | Local plugin evidence does not qualify the separate hosted server. |
| Interop v0.1 | **Historical, signed, re-verified** | Two bundled examples pass schema, hash and signature checks. |
| Interop v0.2 | **Schema available; examples illustrative** | Fixtures validate structurally but are explicitly unsigned and are not live observations. |

## Data, privacy and provenance

Keep three boundaries separate:

1. **Data submitted for measurement.** REST may include prompt and response text. SSE sends generation arguments and a configured provider credential upstream.
2. **Internal processing.** Submitted material may be processed by enabled evaluators and services. Retention and destinations depend on the deployment.
3. **Interoperability disclosure.** The signed exchange contract excludes raw prompts, responses and provider/model identifiers by schema design.

An export without raw text does not prove no raw text was processed upstream. Review [Data and confidentiality](https://github.com/neomundi-io/neomundi-io-data-protection).

## Evidence

- Two historical v0.1 contracts were independently re-verified for schema, SHA-256 hash and Ed25519/JWS signature.
- v0.2 schemas enforce explicit partial and unavailable states.
- v0.2 fixtures are unsigned illustrations, not production observations.
- The Python verifier was cross-checked on the signed v0.1 examples.
- End-to-end example code is not qualified as a production client.

See [source status](source-notes/SOURCE_STATUS.md) for provenance and evidentiary weight.

## Architectural boundaries

NeoMundi does not provide a universal truth verdict, safety certification, compliance determination, policy engine or automatic enforcement mechanism.

```text
high stability ≠ factual correctness
FLAG ≠ proven error
ALLOW ≠ proven truth or permission
single observation ≠ drift
```

## Documentation

| Document | Purpose |
|---|---|
| [START_HERE.md](START_HERE.md) | Select an integration path. |
| [QUICKSTART.md](QUICKSTART.md) | Obtain a REST measurement and optional contract. |
| [API_INTEGRATION_GUIDE.md](API_INTEGRATION_GUIDE.md) | REST, SSE, errors and verification. |
| [Measurement Contract](docs/MEASUREMENT_CONTRACT.md) | Signal meanings and limits. |
| [Interoperability](docs/INTEROPERABILITY.md) | Contract, versions and verification. |
| [Consumer Boundaries](docs/CONSUMER_BOUNDARIES.md) | Measurement versus policy and action. |
| [VERSIONING.md](VERSIONING.md) | Version schemes and unresolved differences. |
| [schema/](schema/) | Authoritative v0.1 and v0.2 schemas. |
| [reference/python/](reference/python/) | Pedagogical integration and verifier. |

## Known limitations

- API response values are illustrative unless identified as real signed examples.
- No official mapping reconciles the Metric Contract, experimental `G` vocabulary and RGC fields.
- `metric_version` and `measurement_version` are not reconciled.
- A signed v0.1 example combines `complete` with coverage `0.6`; preserve it as history, not a v0.2 template.
- One observation establishes neither trend nor drift.
- Deployment-wide evaluator destinations, retention and deletion guarantees are not established here.
- SDK, local MCP and hosted MCP have different qualification states.

---

**One measurement primitive. Multiple applications.**

> **Your system. Your decisions. Our measurement signal.**

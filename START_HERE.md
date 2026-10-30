# Start here

[English](START_HERE.md) · [Français](START_HERE_FR.md) · [Runtime Measurement](README.md)

NeoMundi Runtime Measurement is the developer entry point for measuring an AI execution and consuming the resulting signal in your own infrastructure.

## Choose your path

| You want to… | Start here | Current status |
|---|---|---|
| Measure an answer you already have | [REST Quickstart](QUICKSTART.md) | Primary path |
| Generate through NeoMundi and consume SSE | [API guide §3](API_INTEGRATION_GUIDE.md#3-step-1--v1governstream-get-the-model-response) | Alternative path |
| Integrate from Python | [Python SDK](https://github.com/neomundi-io/neomundi-python-sdk) | V2 implemented; installed live qualification pending |
| Connect an agent through MCP | [MCP connector](https://github.com/neomundi-io/neomundi-measurement-mcp) | Local 0.2.0 pilot-evaluated; source 0.3.0-rc.1 |
| Validate a portable contract | [Interoperability](docs/INTEROPERABILITY.md) | v0.1 signed examples; v0.2 unsigned fixtures |
| Understand signal meaning | [Measurement Contract](docs/MEASUREMENT_CONTRACT.md) | Draft v0.0 semantic contract |
| Use the hosted instrument | [NeoMundi Station](https://github.com/neomundi-io/neomundi-station-public) | Access granted case by case |

## Primary path

```text
Your existing prompt and response
            ↓
      POST /v1/govern
            ↓
 Versioned measurement response
            ↓
 Optional interoperability contract
            ↓
 Your interpretation, policy and action
```

NeoMundi measures. It does not execute `ALLOW`, `STOP`, `REROUTE` or any other operational consequence. The historical field `governance.decision` remains advisory signal output.

## Before sending data

REST may include the prompt and response. SSE additionally sends generation arguments and a configured provider credential to NeoMundi. The interoperability export excludes raw prompt, response and provider/model identifiers, but that export boundary does not describe all upstream processing or retention.

Read [Data and confidentiality](https://github.com/neomundi-io/neomundi-io-data-protection) before submitting sensitive material.

## Read in this order

1. [Quickstart](QUICKSTART.md)
2. [API integration guide](API_INTEGRATION_GUIDE.md)
3. [Measurement Contract](docs/MEASUREMENT_CONTRACT.md)
4. [Consumer Boundaries](docs/CONSUMER_BOUNDARIES.md)
5. [Interoperability](docs/INTEROPERABILITY.md)
6. [Versioning](VERSIONING.md)
7. [Source status](source-notes/SOURCE_STATUS.md)

## Interpretation safeguards

```text
high stability ≠ factual correctness
missing signal ≠ zero
ALLOW ≠ permission or proven truth
single observation ≠ drift
v0.1 semantics ≠ v0.2 semantics
```

No official mapping reconciles the Metric Contract vocabulary, experimental `G`/`g_score`/`∆G` material and RGC fields.

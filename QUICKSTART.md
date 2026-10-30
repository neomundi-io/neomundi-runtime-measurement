# Quickstart — first REST measurement

[English](README.md) · [Français](README_FR.md) · [Choose another path](START_HERE.md)

Measure an AI execution you already produced, then optionally retrieve its portable interoperability contract.

> Route and request field names below are confirmed by existing integration code. This guide deliberately does not invent a response example: no new live API call was made for this documentation release. See [source status](source-notes/SOURCE_STATUS.md).

## Before you start

You need a NeoMundi API key and a prompt/response pair you are authorized to submit. This REST path does **not** require a provider API key and does not ask NeoMundi to generate an answer.

Do not put credentials or unrelated personal data in the prompt or response. Review [Data and confidentiality](https://github.com/neomundi-io/neomundi-io-data-protection).

## 1. Measure the execution

```bash
curl -X POST "https://api.neomundi.io/v1/govern" \
  -H "X-API-Key: YOUR_NEOMUNDI_KEY" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
    "source_type": "llm",
    "mode": "OBS",
    "llm_prompt": "What is the capital of France?",
    "llm_response": "Paris.",
    "raw_metrics": {
      "token_count": 1,
      "latency_ms": 120
    }
  }'
```

Use actual observed token count and latency when available. Do not invent operational values merely to fill a field.

Preserve the complete JSON response, including:

- the request identifier returned by this REST call;
- version and provenance fields;
- measurement status and coverage;
- numeric values **and** null/unavailable states;
- the raw envelope for later review.

Do not treat a missing signal as `0`, “safe” or “within bounds”.

### About `governance.decision`

The API may return a historical signal field named `governance.decision`, with values such as `ALLOW`, `FLAG`, `REROUTE`, `HUMAN_REVIEW` or `STOP`.

This is advisory measurement output—not an authorization, command or action executed by NeoMundi. Your system remains responsible for interpretation, policy and execution. See [Consumer Boundaries](docs/CONSUMER_BOUNDARIES.md).

## 2. Optionally request the interoperability contract

Use the `request_id` returned by the REST measurement:

```bash
curl -X POST \
  "https://api.neomundi.io/v1/rgc/contracts/REQUEST_ID_FROM_REST" \
  -H "X-API-Key: YOUR_NEOMUNDI_KEY"
```

The measurement already exists without this step. Request the contract when you need a portable record another system can validate and verify independently.

Before interpreting it:

1. read `identity.schema_version`;
2. select the exact matching schema in [`schema/`](schema/);
3. validate the JSON;
4. verify the payload hash and Ed25519/JWS signature;
5. inspect coverage, signal states, limitations and measurement boundary;
6. apply only your own explicitly defined consumer policy.

Never validate a v0.1 contract under v0.2 semantics or the reverse.

## 3. Understand the evidence status

- **v0.1:** two bundled historical examples are genuinely signed and were independently re-verified.
- **v0.2:** the schema enforces corrected partial-measurement semantics; bundled examples are explicitly unsigned fixtures, not live observations.
- **API examples:** field paths are documented, but illustrative values are not evidence of a new live measurement.

Read [Interoperability](docs/INTEROPERABILITY.md) and the [schema examples](schema/examples/README.md) before using a contract as audit evidence.

## Alternative: generate through SSE

If you want NeoMundi to call an AI provider and stream the answer, use `POST /v1/govern/stream`. That path sends generation arguments and the configured provider credential to NeoMundi. It is separate from measuring an execution you already hold.

Follow [API Integration Guide §3](API_INTEGRATION_GUIDE.md#3-step-1--v1governstream-get-the-model-response).

## Next steps

- [API integration guide](API_INTEGRATION_GUIDE.md) — payloads, SSE, errors and verification.
- [Measurement Contract](docs/MEASUREMENT_CONTRACT.md) — what signals mean.
- [Interpretation Table](docs/MEASUREMENT_INTERPRETATION_TABLE.md) — what they do not mean.
- [Interoperability](docs/INTEROPERABILITY.md) — schemas, signatures and consumer workflow.
- [Python reference starter](reference/python/) — pedagogical code, not a production-qualified client.

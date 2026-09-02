# Quickstart

Get a runtime measurement and its interoperable contract in three calls.

> Field paths, endpoints and headers below are confirmed by production client code. Example response *values* are illustrative unless a step explicitly says "real signed example". See [source-notes/SOURCE_STATUS.md](./source-notes/SOURCE_STATUS.md) for provenance.

## 1. Call NeoMundi around your model call

```bash
curl -N -X POST "https://api.neomundi.io/v1/govern/stream" \
  -H "X-API-Key: YOUR_NEOMUNDI_KEY" \
  -H "Accept: text/event-stream" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
    "prompt": "Explain why runtime stability should not be confused with factual correctness.",
    "model": "gpt-4o-2024-11-20",
    "provider": "openai",
    "provider_api_key": "YOUR_PROVIDER_KEY"
  }'
```

NeoMundi calls the provider on your behalf and streams the generated text back to you as Server-Sent Events, terminated by `data: [DONE]`.

Reconstruct the full generated text from the stream before moving to step 2. Do **not** reuse the `request_id` returned at this step for step 3 — see [API_INTEGRATION_GUIDE.md, §3](./API_INTEGRATION_GUIDE.md) for why.

## 2. Get the runtime measurement

```bash
curl -X POST "https://api.neomundi.io/v1/govern" \
  -H "X-API-Key: YOUR_NEOMUNDI_KEY" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
    "source_type": "llm",
    "mode": "OBS",
    "llm_prompt": "Explain why runtime stability should not be confused with factual correctness.",
    "llm_response": "THE_FULL_TEXT_RECONSTRUCTED_IN_STEP_1",
    "raw_metrics": { "token_count": 42, "latency_ms": 640 }
  }'
```

This returns the runtime measurement, including a `request_id` — **this** is the identifier to use in step 3. It also returns a `governance.decision` signal (`ALLOW` / `FLAG` / `REROUTE` / `HUMAN_REVIEW` / `STOP`). This is a measurement-layer signal, not an executed action — NeoMundi does not block, reroute or modify your flow on your behalf.

## 3. Get the interoperable measurement contract

```bash
curl -X POST "https://api.neomundi.io/v1/rgc/contracts/REQUEST_ID_FROM_STEP_2" \
  -H "X-API-Key: YOUR_NEOMUNDI_KEY"
```

This step is optional relative to steps 1–2 — the measurement already exists without it — but recommended whenever you need an audit trail that a third party can verify independently of NeoMundi's own infrastructure. See [docs/INTEROPERABILITY.md](./docs/INTEROPERABILITY.md).

## Where to read what a field means

Do not guess. Every signal returned above has a documented meaning and, just as importantly, a documented **non**-meaning:

- [docs/MEASUREMENT_CONTRACT.md](./docs/MEASUREMENT_CONTRACT.md) — full semantic definitions and limits.
- [docs/MEASUREMENT_INTERPRETATION_TABLE.md](./docs/MEASUREMENT_INTERPRETATION_TABLE.md) — one-line-per-signal quick reference.
- [docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md) — what you, as the consuming system, are responsible for deciding.

A working, minimal end-to-end example (Python) is in [reference/python/](./reference/python/).

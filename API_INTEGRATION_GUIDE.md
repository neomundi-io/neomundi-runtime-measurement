# NeoMundi API — Integration Guide

> **Provenance note.** This guide is derived from the NeoMundi client integration reference material, from the request/response handling implemented in NeoMundi's reference client code, and from the NeoMundi Measurement Interoperability repository (schemas, real signed examples, and reference verifier). Endpoint names, headers, request payload structure, and the field paths that production code reads (e.g. `governance.decision`, `identity.request_id`) are confirmed by that code. Response *example values* for `/v1/govern/stream` and `/v1/govern` are illustrative — they have not been captured from a live call — and are marked as such below. The RGC v0.1 contract example in §5 is a real signed example, independently re-verified (hash + Ed25519/JWS signature) while building this repository; the v0.2 example in §5.1 is an illustrative fixture, explicitly marked as unsigned in its source. See [source-notes/SOURCE_STATUS.md](./source-notes/SOURCE_STATUS.md) for full provenance.

## 1. Overview

```text
Your backend (chatbot, agent, AI service)
        │
        │  1. POST /v1/govern/stream   → NeoMundi calls the provider on your behalf
        ▼
   api.neomundi.io
        │
        │  streamed model response
        ▼
Your backend receives the generated text
        │
        │  2. POST /v1/govern          → full measurement + signal
        ▼
   api.neomundi.io
        │
        │  decision, stability_score, r_score, request_id...
        ▼
Your backend receives the measurement
        │
        │  3. POST /v1/rgc/contracts/{request_id}   → signed, portable proof
        ▼
   api.neomundi.io
        │
        │  signed JSON contract (SHA-256 + Ed25519/JWS)
        ▼
Your backend stores the proof, independently verifiable
```

**Core principle**: your backend never talks directly to the provider (OpenAI, Anthropic, etc.). You give NeoMundi your provider key for that one call in step 1, and NeoMundi calls the provider on your behalf, then relays the response to you. This is what allows NeoMundi to measure what was actually generated.

**What NeoMundi does not do**: NeoMundi never automatically blocks, reroutes, or modifies your flow. The returned `decision` (`ALLOW`/`FLAG`/`REROUTE`/`HUMAN_REVIEW`/`STOP`) is a signal — it is **your** backend that decides whether and how to act on it. NeoMundi measures. You decide.

---

## 2. Prerequisites

| Item | Where to get it |
|---|---|
| NeoMundi API key | provided by NeoMundi, sent as `X-API-Key` on every call |
| Provider API key (OpenAI, Anthropic, etc.) | yours, from the relevant provider |
| `base_url` | `https://api.neomundi.io` (default, rarely needs changing) |

**Security**: your provider key travels in the body of the `/v1/govern/stream` request (see §3). Always use HTTPS (never a `http://` base URL), and never log this key on the client side.

---

## 3. Step 1 — `/v1/govern/stream`: get the model response

### Request

```
POST https://api.neomundi.io/v1/govern/stream
```

**Headers**

| Header | Value |
|---|---|
| `X-API-Key` | your NeoMundi key |
| `Accept` | `text/event-stream` |
| `Content-Type` | `application/json; charset=utf-8` |

**Body (JSON)**

```json
{
  "prompt": "The message sent to the model.",
  "model": "gpt-4o-2024-11-20",
  "provider": "openai",
  "provider_api_key": "sk-..."
}
```

| Field | Type | Description |
|---|---|---|
| `prompt` | string | The user message / request sent to the model. |
| `model` | string | Model identifier at the provider (e.g. `gpt-4o-2024-11-20`). |
| `provider` | string | One of the supported providers — see §3.1. |
| `provider_api_key` | string | Your API key at that provider. Sent to NeoMundi for this call only; not stored by NeoMundi according to the documented policy of the reference client. |

**Observed operational rule**: do not send `temperature`, `top_p` or `seed` — each provider is measured under its native default generation policy. If your use case needs these parameters, confirm with NeoMundi before adding them to the payload.

### 3.1 Supported providers

Per the production mapping (`resolve_provider_key()` in the reference client):

```text
openai · anthropic · google (alias gemini) · mistral · cohere · deepseek
xai (alias grok) · perplexity · together · qwen · apertus · euria
```

### Response

An SSE stream (`text/event-stream`). Each useful line starts with `data: ` followed by a JSON object (or may be a raw JSON object, depending on the event). The stream ends with `data: [DONE]`.

**⚠️ Illustrative — field structure confirmed by code, values not captured live:**

```text
data: {"content": "Here", "request_id": "req_abc123..."}
data: {"content": " is the"}
data: {"content": " model's answer."}
data: {"response_text": "Here is the model's answer.", "token_count": 42, "latency_ms": 640.2, "request_id": "req_abc123...", "decision": "ALLOW", "stability_score": 0.91, "r_score": 0.04}
data: [DONE]
```

Reference client code reads, in this priority order, several possible shapes for each piece of information (tolerant of field-shape variants):

| Information | Accepted paths (first match wins) |
|---|---|
| Current chunk text | `content`, `delta.content`, `text`, `chunk` |
| Final full text | `response_text`, `llm_response`, `output_text`, `response`, `provider_response.text` |
| Token count | `token_count`, `total_tokens`, `tokens_so_far`, `usage.total_tokens`, `usage.output_tokens`, `provider_usage.total_tokens`, `provider_usage.output_tokens`, `token_position` |
| Latency | `latency_ms`, `processing_time_ms` (otherwise measured client-side) |

**⚠️ Important — two different `request_id`s exist in this flow:**

The `request_id` returned here by `/v1/govern/stream` (the *stream request_id*) is **not** the one to use in step 3 to retrieve the RGC contract. Production tooling stores it in a separate column from the final `request_id`. Use only the reconstructed full text (`response_text`) for step 2 — ignore this step's `request_id` for everything else.

---

## 4. Step 2 — `/v1/govern`: the full measurement

### Request

```
POST https://api.neomundi.io/v1/govern
```

**Headers**

| Header | Value |
|---|---|
| `X-API-Key` | your NeoMundi key |
| `Content-Type` | `application/json; charset=utf-8` |

**Body (JSON)**

```json
{
  "source_type": "llm",
  "mode": "OBS",
  "llm_prompt": "The same prompt sent in step 1.",
  "llm_response": "The full text reconstructed in step 1.",
  "raw_metrics": {
    "token_count": 42,
    "latency_ms": 640
  }
}
```

| Field | Type | Description |
|---|---|---|
| `source_type` | string | `"llm"` for a language-model output measurement. |
| `mode` | string | `"OBS"` (observation) currently in production. |
| `llm_prompt` | string | The prompt sent in step 1. |
| `llm_response` | string | The full generated text reconstructed in step 1. |
| `raw_metrics.token_count` | int | Token count (measured or estimated in step 1). |
| `raw_metrics.latency_ms` | int | Latency in milliseconds, rounded to an integer. |

### Response

**⚠️ Illustrative — field paths confirmed by production tooling, values not captured live:**

```json
{
  "request_id": "gov_9f8e7d6c5b4a...",
  "timestamp": "2026-08-29T14:32:10.114Z",
  "system_id": "controltower-api",
  "governance": {
    "decision": "ALLOW",
    "reasons": []
  },
  "quality": {
    "stability_score": 0.91
  },
  "runtime": {
    "r_score": 0.04
  }
}
```

**Use the `request_id` from THIS response** — not step 1's — in step 3 to retrieve the signed RGC contract for this measurement.

`governance.decision` can be: `ALLOW`, `FLAG`, `REROUTE`, `HUMAN_REVIEW`, `STOP`. As above: NeoMundi only emits this signal — it is your backend that decides, if it chooses to, what to do with it.

---

## 5. Step 3 — `/v1/rgc/contracts/{request_id}`: the signed, portable proof

This step is **optional** relative to steps 1–2 (the measurement already exists without it), but recommended whenever you need an audit trail that can be verified independently of NeoMundi's own infrastructure — by a third party, a regulator, or an end customer, without having to trust NeoMundi's infrastructure itself.

### Request

```
POST https://api.neomundi.io/v1/rgc/contracts/{request_id}
```

Replace `{request_id}` with the `request_id` received in **step 2** (not step 1's — see the note in §3).

**Headers**

| Header | Value |
|---|---|
| `X-API-Key` | your NeoMundi key |

### Response — real example (signed RGC v0.1 contract, taken as-is from the reference repository)

```json
{
  "identity": {
    "schema_version": "0.1.0",
    "request_id": "c735fe2c-b88f-488a-ab27-aa456e43a556",
    "trace_id": "00-149519e750f0b7e901942da66c9f4693-53f5b5783400c854-01",
    "timestamp": "2026-08-17T21:04:45.245605Z",
    "system_id": "controltower-api",
    "model": "local",
    "mode": "OBS"
  },
  "provenance": {
    "measurement_version": "3.0.0",
    "normalizer_version": "1.0.0",
    "checks_emitted": 3,
    "source_batch_id": null,
    "canonicalization_method": "sorted-json-utf8"
  },
  "observation": {
    "runtime_scope": "single_request",
    "observation_window": null,
    "measurement_status": "complete",
    "measurement_coverage": 0.6,
    "observed_signals": {
      "stability_score": 0.923077,
      "coherence_score": 1.0,
      "factual_hallucination_score": 0.0,
      "semantic_instability_score": 0.0,
      "semantic_risk": 0.0,
      "observation_class": "within_bounds",
      "confidence": 1.0
    },
    "limitations": [
      "Measurement reflects a single runtime observation window; it is not a certification of third-party content.",
      "The governance signal is advisory only — it does not grant, refuse, suspend, or modify any execution permission.",
      "Provider/model identity is pseudonymized in this contract and cannot be reversed to the original value."
    ],
    "measurement_boundary": "This contract measures a single observed runtime signal. It does not evaluate ground truth, does not certify third-party data, and carries no execution authority."
  },
  "governance": {
    "governance_boundary": {
      "authorization_status": "not_applicable",
      "execution_permission_changed": false
    },
    "advisory": {
      "review_recommendation": "not_indicated",
      "review_trigger": [],
      "recommended_review_type": [],
      "interpretation_policy": {
        "policy_id": "rgc-piste-b-advisory",
        "policy_version": "0.1.0"
      }
    }
  },
  "integrity": {
    "payload_hash": "746c8e82e28b3048ab6a070901c648fe89a3df7a33324a25fd4a2b16ae96402d",
    "hash_algorithm": "sha256",
    "canonicalization": "sorted-json-utf8",
    "signature": "eyJhbGciOiJFZERTQSIsImtpZCI6Im5lb211bmRpLXJnYy0yMDI2LTAxIiwidHlwIjoiSldUIn0.eyJwYXlsb2FkX2hhc2giOiI3NDZjOGU4MmUyOGIzMDQ4YWI2YTA3MDkwMWM2NDhmZTg5YTNkZjdhMzMzMjRhMjVmZDRhMmIxNmFlOTY0MDJkIiwiaGFzaF9hbGdvcml0aG0iOiJzaGEyNTYiLCJzY2hlbWFfdmVyc2lvbiI6IjAuMS4wIiwicmVxdWVzdF9pZCI6ImM3MzVmZTJjLWI4OGYtNDg4YS1hYjI3LWFhNDU2ZTQzYTU1NiIsInRpbWVzdGFtcCI6IjIwMjYtMDgtMTdUMjE6MDQ6NDUuMjQ1NjA1WiJ9.0Co6a9EN4xRRvfLV_8MCiJO5AWJ1F9SEF84Ck7YP5X5d6NAIGMuaQj2kENIyKHoBOmBQonsupgK1k2pT3Bw5DA",
    "signer_identity": "neomundi-controltower-rgc",
    "key_id": "neomundi-rgc-2026-01",
    "confidentiality_class": "controlled",
    "retention_reference": "governance_logs:c735fe2c-b88f-488a-ab27-aa456e43a556"
  }
}
```

This is the complete, untruncated signature — it has been independently re-verified (SHA-256 hash match and Ed25519/JWS signature valid against the published test key; see [schema/examples/](./schema/examples/)). A second real signed example (`flagged` classification) is also available there.

Note that this contract's `governance` block itself states `authorization_status: "not_applicable"` and `execution_permission_changed: false` — the advisory signal does not grant, refuse, suspend or modify execution permission. This is consistent with the boundary in [docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md): the `governance` naming in this payload is an object/field name in the current API, not a claim that NeoMundi performs governance.

### 5.1 Under RGC v0.2 — explicit partial measurement

Since v0.2, each measured signal carries an individual status (`measured` / `not_measured` / `insufficient_coverage`) under `observation.observed_signals.signal_status`. This is now **schema-enforced** by [schema/contract-v0.2.schema.json](./schema/contract-v0.2.schema.json): a signal with status `measured` must carry a numeric value; any other status must carry `null` — never silently replaced by a reassuring default. v0.2 also adds a third `observation_class` value, `not_assessed`, for when measured evidence is insufficient to support either `within_bounds` or `flagged`.

**Status: the schema rule is normative; the specific example values below remain an illustrative fixture** — the full fixture (not just this fragment) is in [schema/examples/rgc-v0.2-flagged-partial-measurement-illustrative.json](./schema/examples/rgc-v0.2-flagged-partial-measurement-illustrative.json), and is explicitly marked `"signature": "illustrative.fixture.not-signed"` in the source — it is not a captured real contract. A second fixture demonstrating `not_measured` and `insufficient_coverage` values is in [schema/examples/rgc-v0.2-within-bounds-partial-measurement-illustrative.json](./schema/examples/rgc-v0.2-within-bounds-partial-measurement-illustrative.json). Example shape:

```json
"observed_signals": {
  "stability_score": 0.615385,
  "coherence_score": 1.0,
  "factual_hallucination_score": 1.0,
  "semantic_instability_score": 0.0,
  "semantic_risk": 0.0,
  "signal_status": {
    "stability_score": "measured",
    "coherence_score": "measured",
    "factual_hallucination_score": "measured",
    "semantic_instability_score": "measured",
    "semantic_risk": "measured"
  },
  "observation_class": "flagged",
  "confidence": 1.0
}
```

**Always check `identity.schema_version`** before interpreting a contract — never apply v0.2 semantics to a v0.1 contract, or vice versa.

### 5.2 If this call fails

Recommendation: do not fail the whole observation if step 3 fails (network issue, contract not yet available server-side, etc.). The measurements from steps 1–2 remain valid without a signed proof for that particular observation — log the failure and continue.

---

## 6. Step 4 — Independently verify the RGC contract's signature

This is what makes the proof useful to a third party who does not trust NeoMundi: they can verify it themselves, without calling the NeoMundi API for the measurement itself — only to fetch the schema and public keys, once.

### 6.1 Required public endpoints (no API key required)

```
GET https://api.neomundi.io/v1/rgc/schema
GET https://api.neomundi.io/v1/rgc/jwks
```

### 6.2 Verification algorithm (as implemented by NeoMundi's published reference verifier)

1. **Recompute the SHA-256 hash.** Rebuild the canonical object from **only** these four sections of the contract (`integrity` is excluded from its own hash):
   ```json
   {
     "identity": { ... },
     "provenance": { ... },
     "observation": { ... },
     "governance": { ... }
   }
   ```
   Serialize as JSON with sorted keys and no whitespace (`sort_keys=True, separators=(",", ":")`), encode as UTF-8, compute the hex SHA-256. Compare against the received `integrity.payload_hash` — they **must be strictly identical**.

2. **Retrieve the public key.** Look up the key in the fetched JWKS whose `kid` matches `integrity.key_id`.

3. **Verify the JWS signature.** Expected algorithm: `EdDSA` (Ed25519). If the JWS header carries a `kid`, it must match `integrity.key_id`.

4. **Verify the signed claims.** The JWS must contain, and they must exactly match the received contract:
   ```text
   payload_hash    == integrity.payload_hash
   hash_algorithm  == integrity.hash_algorithm
   schema_version  == identity.schema_version
   request_id      == identity.request_id
   timestamp       == identity.timestamp
   ```

5. **The contract is valid only if both layers (1) and (3–4) pass.** One without the other is not sufficient.

---

## 7. Code examples

A minimal, working Python example implementing steps 1–4 is provided in [reference/python/](./reference/python/). It is illustrative and pedagogical — see that folder's own README for what it deliberately omits (retry logic, a control/policy layer).

**Node.js note (not independently verified against a real signed contract)**: a JavaScript implementation of the recursive key-sort used in the hash canonicalization step must exactly reproduce Python's `json.dumps(sort_keys=True, separators=(",", ":"))` behaviour, including floating-point number representation, or the recomputed hash will not match. This has not been validated end-to-end and should be checked before production use.

---

## 8. Error handling — recommendations from production experience

Per the retry logic used in production tooling:

| Situation | Recommended behaviour |
|---|---|
| Network error (timeout, DNS, connection reset) | Retry with linear backoff (e.g. `10s × attempt`), up to ~5 attempts. |
| HTTP 5xx | Treat as transient, same retry logic as above. |
| HTTP 429 / body mentioning `rate_limit_exceeded` or `rate_limit_error` | Wait significantly longer before retrying (60s observed in production) — not the same cadence as 5xx errors. |
| Other 4xx codes (400, 401, 403...) | **Do not retry** — this is a malformed request or an invalid key; waiting will not help. Fix the request or the key. |
| Step 3 failure specifically (`/v1/rgc/contracts/...`) | Do not fail the whole observation — the measurement from steps 1–2 remains valid without a signed proof. |

---

## 9. Out of scope for this document

- Full field-by-field schema validation rules — the complete RGC JSON Schemas are included at [schema/contract-v0.1.schema.json](./schema/contract-v0.1.schema.json) and [schema/contract-v0.2.schema.json](./schema/contract-v0.2.schema.json); see [docs/INTEROPERABILITY.md](./docs/INTEROPERABILITY.md) for how to use them.
- Thresholds, routing policies, or decision logic specific to your infrastructure — NeoMundi provides the signal; your backend owns the interpretation. See [docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md).
- Authentication / lifecycle management of your own NeoMundi API key (rotation, permissions) — to be documented separately if needed.

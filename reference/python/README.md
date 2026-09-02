# Reference Integration Starter (Python)

A minimal, pedagogical script showing:

```text
API call  →  runtime measurement  →  interoperable contract retrieval
```

## What this is

`reference_integration.py` calls `/v1/govern/stream`, then `/v1/govern`, then optionally fetches and independently verifies the signed interoperable contract via `/v1/rgc/contracts/{request_id}`. It is adapted from the request/response handling logic in NeoMundi's client integration reference material — see [API_INTEGRATION_GUIDE.md](../../API_INTEGRATION_GUIDE.md) for the fully annotated version of this same flow.

## What this deliberately is not

- **No policy engine.** The script prints the `governance.decision` signal; it does not act on it.
- **No compliance engine.** It does not decide compliance, admissibility, or safety.
- **No automated governance.** No thresholds, no automatic stop/reroute/escalation logic.
- **No actionability layer.** See [docs/CONSUMER_BOUNDARIES.md](../../docs/CONSUMER_BOUNDARIES.md) for why this is out of scope for the measurement layer.
- **No retry logic.** [API_INTEGRATION_GUIDE.md §8](../../API_INTEGRATION_GUIDE.md) documents recommended retry/backoff behaviour; this script does not implement it, to keep the example minimal and easy to read end-to-end.

## Status

This code has not been run against a live NeoMundi API — the source guide it is adapted from notes that response values are illustrative. Treat it as a starting point to adapt, not a drop-in production client.

Its verification logic (`verify_rgc_contract`) has, however, been independently cross-checked: it implements the same SHA-256 + Ed25519/JWS algorithm as NeoMundi's own published reference verifier (found in the NeoMundi Measurement Interoperability repository), and that exact algorithm was used to successfully re-verify both real signed examples now bundled in [schema/examples/](../../schema/examples/) (see [source-notes/SOURCE_STATUS.md](../../source-notes/SOURCE_STATUS.md)).

A fuller reference consumer implementation exists upstream in that same interoperability repository — separate modules for schema validation, data-sovereignty checks, signature verification, an example consumer-defined routing policy, and receipt storage. It was not duplicated into this repository to keep this starter minimal; its schemas and examples are, however, included in [schema/](../../schema/).

## Usage

```bash
pip install -r requirements.txt

export NEOMUNDI_API_KEY="your_neomundi_key"
export NEOMUNDI_BASE_URL="https://api.neomundi.io"   # optional, this is the default
export OPENAI_API_KEY="your_openai_key"

python reference_integration.py
```

Never commit real API keys. Keys are read from environment variables only.

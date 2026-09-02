"""
Reference Integration Starter — NeoMundi Runtime Measurement Layer.

Shows the minimal end-to-end path:

    API call  ->  runtime measurement  ->  interoperable contract retrieval

This is pedagogical reference code, not a production client. It deliberately
contains no policy engine, no compliance engine, no automated governance, and
no actionability logic — see reference/python/README.md for the full list of
what is intentionally left out and why.

Adapted from the NeoMundi client integration reference material
(see ../../API_INTEGRATION_GUIDE.md for the full, annotated version of this
flow, including error-handling recommendations not implemented here).
"""

import base64
import hashlib
import json
import os

import requests
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
import jwt  # PyJWT

NEOMUNDI_BASE_URL = os.getenv("NEOMUNDI_BASE_URL", "https://api.neomundi.io")
NEOMUNDI_API_KEY = os.getenv("NEOMUNDI_API_KEY")


def call_stream(prompt, model, provider, provider_api_key):
    """Step 1 — get the model's response via NeoMundi."""
    url = f"{NEOMUNDI_BASE_URL}/v1/govern/stream"
    headers = {
        "X-API-Key": NEOMUNDI_API_KEY,
        "Accept": "text/event-stream",
        "Content-Type": "application/json; charset=utf-8",
    }
    body = {
        "prompt": prompt,
        "model": model,
        "provider": provider,
        "provider_api_key": provider_api_key,
    }

    response = requests.post(url, headers=headers, json=body, stream=True, timeout=120)
    response.raise_for_status()

    response_text = ""
    token_count = None
    latency_ms = None

    for raw_line in response.iter_lines(decode_unicode=True):
        if not raw_line or not raw_line.startswith("data:"):
            continue
        payload_text = raw_line[5:].strip()
        if payload_text == "[DONE]":
            continue
        event = json.loads(payload_text)

        chunk = event.get("content") or event.get("text") or event.get("chunk")
        if chunk:
            response_text += str(chunk)

        complete = event.get("response_text") or event.get("output_text")
        if complete:
            response_text = str(complete)

        if "token_count" in event:
            token_count = event["token_count"]
        if "latency_ms" in event:
            latency_ms = event["latency_ms"]

    return response_text, token_count or max(1, len(response_text) // 4), latency_ms or 0


def call_govern(prompt, response_text, token_count, latency_ms):
    """Step 2 — full measurement. Returns the request_id to use for the interoperable contract."""
    url = f"{NEOMUNDI_BASE_URL}/v1/govern"
    headers = {
        "X-API-Key": NEOMUNDI_API_KEY,
        "Content-Type": "application/json; charset=utf-8",
    }
    body = {
        "source_type": "llm",
        "mode": "OBS",
        "llm_prompt": prompt,
        "llm_response": response_text,
        "raw_metrics": {
            "token_count": int(token_count),
            "latency_ms": int(round(latency_ms)),
        },
    }
    response = requests.post(url, headers=headers, json=body, timeout=120)
    response.raise_for_status()
    return response.json()


def fetch_rgc_contract(request_id):
    """Step 3 — retrieve the signed interoperable contract for this measurement (optional)."""
    url = f"{NEOMUNDI_BASE_URL}/v1/rgc/contracts/{request_id}"
    headers = {"X-API-Key": NEOMUNDI_API_KEY}
    response = requests.post(url, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()


def verify_rgc_contract(contract):
    """Step 4 — independent verification (no API key required for this step)."""
    schema = requests.get(f"{NEOMUNDI_BASE_URL}/v1/rgc/schema", timeout=10).json()
    jwks = requests.get(f"{NEOMUNDI_BASE_URL}/v1/rgc/jwks", timeout=10).json()

    if contract["identity"]["schema_version"] != schema.get("version"):
        return False, "schema_version mismatch"

    sections = {
        "identity": contract["identity"],
        "provenance": contract["provenance"],
        "observation": contract["observation"],
        "governance": contract["governance"],
    }
    canonical = json.dumps(sections, sort_keys=True, separators=(",", ":"))
    recomputed_hash = hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    hash_match = recomputed_hash == contract["integrity"]["payload_hash"]

    key_id = contract["integrity"]["key_id"]
    keys = {k["kid"]: k for k in jwks.get("keys", []) if "kid" in k}
    signature_valid = False

    if key_id in keys:
        jwk = keys[key_id]
        x = jwk["x"]
        raw = base64.urlsafe_b64decode(x + "=" * (-len(x) % 4))
        public_key = ed25519.Ed25519PublicKey.from_public_bytes(raw)
        pem = public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)

        try:
            header = jwt.get_unverified_header(contract["integrity"]["signature"])
            if header.get("alg") == "EdDSA" and header.get("kid", key_id) == key_id:
                claims = jwt.decode(
                    contract["integrity"]["signature"],
                    pem,
                    algorithms=["EdDSA"],
                    options={"verify_aud": False},
                )
                expected = {
                    "payload_hash": contract["integrity"]["payload_hash"],
                    "hash_algorithm": contract["integrity"]["hash_algorithm"],
                    "schema_version": contract["identity"]["schema_version"],
                    "request_id": contract["identity"]["request_id"],
                    "timestamp": contract["identity"]["timestamp"],
                }
                signature_valid = all(claims.get(k) == v for k, v in expected.items())
        except Exception:
            signature_valid = False

    return (hash_match and signature_valid), {
        "hash_match": hash_match,
        "signature_valid": signature_valid,
    }


if __name__ == "__main__":
    if not NEOMUNDI_API_KEY:
        raise SystemExit("Missing environment variable: NEOMUNDI_API_KEY")

    provider_key = os.getenv("OPENAI_API_KEY")
    if not provider_key:
        raise SystemExit("Missing environment variable: OPENAI_API_KEY")

    prompt = "Explain why runtime stability should not be confused with factual correctness."

    text, tokens, latency = call_stream(prompt, model="gpt-4o-2024-11-20", provider="openai", provider_api_key=provider_key)
    measurement = call_govern(prompt, text, tokens, latency)

    print("Decision:", measurement.get("governance", {}).get("decision"))

    contract = fetch_rgc_contract(measurement["request_id"])
    valid, details = verify_rgc_contract(contract)
    print("Contract valid:", valid, details)

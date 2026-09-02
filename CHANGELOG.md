# Changelog

All notable changes to this repository are documented here.

## [Unreleased] — 2026-09-03

Integrated the NeoMundi Measurement Interoperability repository (`neomundi-measurement-interoperability-main`) as an additional, authoritative source for the interoperability layer, and added a French README.

Added:

- `schema/contract-v0.1.schema.json`, `schema/contract-v0.2.schema.json` — authoritative JSON Schemas (previously not supplied).
- `schema/examples/rgc-v0.1-within-bounds-no-review-real-signed.json`, `rgc-v0.1-flagged-review-required-real-signed.json` — two real signed RGC v0.1 examples, both independently re-verified (SHA-256 + Ed25519/JWS) during this update.
- `schema/examples/rgc-v0.1-public-jwks-test-key.json` — the public test key used for that verification.
- `schema/examples/rgc-v0.2-within-bounds-partial-measurement-illustrative.json`, `rgc-v0.2-flagged-partial-measurement-illustrative.json` — full illustrative v0.2 fixtures (replacing a partial fragment), both schema-validated with zero errors.
- `README_FR.md` — French README, same positioning as `README.md`, with language navigation added to both.

Removed (superseded): `schema/examples/rgc-v0.1-real-signed-example.json` (truncated signature), `schema/examples/rgc-v0.2-illustrative-partial-fragment.json` (fragment only, replaced by full fixtures).

Substantially rewrote `docs/INTEROPERABILITY.md` around the interoperability repository's own governing principle ("Absence of evidence is only meaningful over the measured domain"), its five-section contract structure, per-signal measurement status, coverage/status consistency rules, data sovereignty, and standards used. Updated `docs/MEASUREMENT_INTERPRETATION_TABLE.md`, `API_INTEGRATION_GUIDE.md`, `QUICKSTART.md`, `schema/README.md`, and `source-notes/SOURCE_STATUS.md` accordingly — including a newly documented historical inconsistency in the real v0.1 example (`measurement_status: complete` with `measurement_coverage: 0.6`) that v0.2's schema-enforced rule now forbids, preserved unchanged per the source's own instruction.

## [Unreleased] — 2026-09-02

Initial assembly of the NeoMundi Runtime Measurement Layer product repository, built from local source material:

- `NEOMUNDI_API_INTEGRATION_GUIDE.md` (working draft, client-integration reference material)
- `neomundi-metric-contract-main` (Metric Contract Draft v0.0, Measurement Reference Framework Draft v0.1, Signal Interpretation & Consumption Rules v0.1 experimental/pre-freeze, and their internal normative audit)
- `neomundi-continuous-control-launcher-main` (experimental MVP reference client)

Added:

- `README.md`, `QUICKSTART.md`, `API_INTEGRATION_GUIDE.md`, `VERSIONING.md`
- `docs/MEASUREMENT_CONTRACT.md`, `docs/MEASUREMENT_INTERPRETATION_TABLE.md`, `docs/INTEROPERABILITY.md`, `docs/CONSUMER_BOUNDARIES.md`
- `schema/examples/` — labelled JSON examples (real signed / illustrative / pre-freeze)
- `reference/python/` — minimal, non-normative reference integration starter
- `source-notes/SOURCE_STATUS.md` — full provenance and contradiction audit

This is the first version of this repository. No prior version exists to diff against.

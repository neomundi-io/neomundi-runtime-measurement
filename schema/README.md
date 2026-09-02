# Schema

**Authoritative JSON Schemas for the interoperable measurement contract are now included: `contract-v0.1.schema.json` and `contract-v0.2.schema.json`.**

Both are JSON Schema Draft 2020-12 documents, sourced verbatim from the NeoMundi Measurement Interoperability repository, with published `$id`s:

- `https://schemas.neomundi.io/rgc/0.1.0/contract.schema.json`
- `https://schemas.neomundi.io/rgc/0.2.0/contract.schema.json`

Every JSON example in [examples/](./examples/) that claims conformance to one of these schemas has been validated against it with zero errors — see [examples/README.md](./examples/README.md) for the per-file status and validation notes.

## What is authoritative vs. still open

The schema files define structure, types, required fields, and — as of v0.2 — several conditional/normative rules enforced at the schema level:

- `observation.measurement_status = "complete"` requires `observation.measurement_coverage = 1.0`; `"partial"` requires `< 1.0`.
- Each entry in `observation.observed_signals.signal_status` (`measured` / `not_measured` / `insufficient_coverage`) constrains the corresponding signal value: `measured` requires a numeric value; anything else requires `null`.
- `identity.model` is schema-constrained to `local` or a pseudonymized `model-[0-9a-f]{12}` form — raw provider/model identifiers cannot validate.
- `governance.governance_boundary.execution_permission_changed` is schema-constrained to always be `false`.

What the schemas do **not** freeze: which of `stability_score`, `coherence_score`, etc. is authoritative outside the RGC interoperability layer (the Measurement Contract in [docs/MEASUREMENT_CONTRACT.md](../docs/MEASUREMENT_CONTRACT.md) uses a related but not identical vocabulary — see [source-notes/SOURCE_STATUS.md](../source-notes/SOURCE_STATUS.md)); how a consumer should map `observed_signals` onto its own policy; and any threshold or band. The interoperability layer defines transport/structure; the Measurement Contract defines meaning; the two are still not fully reconciled — this is documented, not resolved, in `SOURCE_STATUS.md`.

Do not treat this directory as covering every field NeoMundi may ever expose — it covers exactly what the two versioned RGC schemas declare, nothing more.

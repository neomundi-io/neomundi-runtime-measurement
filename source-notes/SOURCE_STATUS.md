# Source Status

This document records what local sources were used to build this repository, their normative weight, known contradictions between them, and what was deliberately left out. It exists so that a future contributor does not have to re-derive this analysis, and so that no statement elsewhere in this repository is mistaken for more authoritative than its source actually is.

## Sources used

| Source | Role | Status as declared by the source itself |
|---|---|---|
| `NEOMUNDI_API_INTEGRATION_GUIDE.md` | API / integration reference | Working draft — explicitly marked as needing review before publication. Endpoints, headers, request payloads and field paths are stated to be confirmed by production client code; response *values* are stated to be illustrative/unverified except the RGC v0.1 example. |
| `metric-contract-v0.0.en.md` | Metric Contract, semantics | Draft v0.0, dated 2026-08-16. Reflects the tightened normative core produced by the internal normative audit (see below). |
| `metric-contract-v0.0.fr.md` | Metric Contract, semantics (French) | Draft v0.0, dated 2026-08-13 — **three days older than the English version and structurally different (865 lines vs. 584)**. Predates the audit's tightened normative core. Treated as **stale relative to the English version**, not as an equally authoritative mirror. |
| `audit_normatif.md` | Internal audit of normative language in the Metric Contract | Explicitly "Working document — Non-normative." Used here only to understand *why* the English Metric Contract reads the way it does, not as a source of new rules. |
| `measurement_reference_framework_en.md` / `_fr.md` | Methodological framework (reproducibility, portability, traceability, falsifiability) | Draft v0.1. FR/EN identical in length (508 lines each) — no discrepancy found here. |
| `signal_interpretation_and_consumption_rules.en.md` / `.fr.md` | Signal semantics and consumption rules, including a much larger concrete signal vocabulary | **Explicitly "Experimental / pre-freeze", "Standardization status: Work in progress."** Dated 2026-08-19. FR/EN differ slightly in length (1540 vs. 1567 lines) — not verified line-by-line for content parity; treated as pre-freeze regardless. |
| `neomundi-continuous-control-launcher-main/*` (README, QUICKSTART, `docs/SIGNALS.md`, `launcher.py`, `config.example.json`, `example_request.json`, `.env.example`, `requirements.txt`) | Old reference client ("Continuous Control Launcher") | Self-described "Experimental MVP — under active development." |

## What is normative vs. experimental vs. pre-freeze

- **Normative**: the English Metric Contract (`metric-contract-v0.0.en.md`), specifically its "Normative core v0.0" (15 numbered MUST/MUST NOT statements). This repository treats this as the closest thing to an authoritative semantic boundary currently available.
- **Experimental / pre-freeze**: everything in `signal_interpretation_and_consumption_rules.*` — including the entire `G` / `g_score` / `∆G` / `delta_profile` (DROP/FLAT/V_SHAPE) / binary `ALLOW`/`FLAG` `decision` / `regime` (STABLE) vocabulary. The source document says so about itself; this repository does not upgrade any of it to normative status.
- **Working draft, not yet publication-ready**: the API Integration Guide. Its structural facts (endpoints, headers, payload shape, field paths, the verification algorithm) are stated by the source as confirmed by code; illustrative example *values* are marked as such throughout this repository's derived `API_INTEGRATION_GUIDE.md`.
- **Real, not illustrative**: the RGC v0.1 signed contract example in the API guide (§5) and reproduced in `schema/examples/rgc-v0.1-real-signed-example.json`. This is the one payload in all the sources that is explicitly described as a genuine captured example rather than a constructed illustration.

## Contradictions encountered

1. **Three non-reconciled signal vocabularies.**
   - The normative Metric Contract uses: `stability_score`, `coherence_score`, `factual_validity_signal`, `semantic_variability_signal`, `risk_signal`.
   - The pre-freeze consumption-rules document uses: `G`/`g_score`, `∆G`, `delta_profile` (`DROP`/`FLAT`/`V_SHAPE`), a **binary** `decision` (`ALLOW`/`FLAG`), `regime` (`STABLE`), `hallucination_score`, `g_final`.
   - The API guide's real RGC example uses: `stability_score`, `coherence_score`, `factual_hallucination_score`, `semantic_instability_score`, `semantic_risk`, `r_score`, and a **five-value** `governance.decision` (`ALLOW`/`FLAG`/`REROUTE`/`HUMAN_REVIEW`/`STOP`).
   
   No source states these three vocabularies are equivalent, and this repository does not invent a mapping between them. `docs/MEASUREMENT_INTERPRETATION_TABLE.md` lists them in three separate sections rather than merging them.

2. **FR/EN divergence on the Metric Contract.** The French `metric-contract-v0.0.fr.md` predates the normative audit that produced the current English version and has a substantially different structure and length. This repository's `docs/MEASUREMENT_CONTRACT.md` is derived from the English version only. The French source was not corrected or resynchronized as part of this work — that remains a task for whoever maintains the original `neomundi-metric-contract` source repository.

3. **Two non-reconciled version-field schemes.**
   - The pre-freeze consumption-rules document describes a conceptual `schema_version` / `metric_version` / `normalizer_version` triad.
   - The real RGC v0.1 example instead carries `identity.schema_version`, `provenance.measurement_version`, and `provenance.normalizer_version` — no `metric_version` field exists in the real example.
   
   This repository does not assume `measurement_version` and `metric_version` mean the same thing. See `VERSIONING.md`.

4. **Two non-reconciled illustrative payload shapes.** The Metric Contract's own illustrative reference payload (`schema_version: "neomundi_observation_payload_v0.1"`, top-level `source`/`measurement`/`known_limitations`/`measurement_boundary`) does not match the structure of the real RGC v0.1 contract (`identity`/`provenance`/`observation`/`governance`/`integrity`). The Metric Contract itself states its payload is non-normative, which is consistent with a more complex real structure existing elsewhere — but no source explicitly states these two are the same object at different maturity stages, so this repository presents them as two separate examples rather than merging them.

5. **Naming tension between "governance" and the product's non-governance positioning.** The real API endpoints are named `/v1/govern` and `/v1/govern/stream`, and the response field is `governance.decision`. Read in isolation this could suggest NeoMundi performs governance. However, the actual documented behaviour is consistent with a measurement-only product: the real signed RGC example's own `governance` block states `governance_boundary.authorization_status: "not_applicable"` and `execution_permission_changed: false`, and the API guide states outright that NeoMundi "never automatically blocks, reroutes, or modifies your flow." This repository preserves the real field/endpoint names (they cannot be renamed without breaking API accuracy) while explicitly noting, wherever `governance` appears, that it names a signal object in the current API, not a governance function of the product. See `docs/INTEROPERABILITY.md` and `docs/CONSUMER_BOUNDARIES.md`.

6. **The old launcher's framing overstates what its own code does.** The launcher's README and QUICKSTART describe a "control policy" layer reading `control_policy.json` and producing `control_decision.json`. Its actual code (`launcher.py`) implements neither — it only calls the two API endpoints and journals the result. `config.example.json` contains no thresholds or policy rules. This repository's `reference/python/` starter reflects what the code actually does (call + journal-equivalent print), not what the launcher's documentation claimed it would eventually do.

## Elements explicitly not integrated

- The "10 default provider profiles" list and the external `controltowerai-docs` providers documentation link from the launcher's README — unverifiable from local sources, and not required to describe the measurement layer itself.
- The launcher's naming and framing as a "Continuous Control Launcher" / "runtime measurement and governance infrastructure" — superseded by the current product positioning (measurement layer, not governance/control product).
- Any threshold value found only in exploratory/experimental material (e.g. `∆G < -0.05`, `-0.10`, `-0.15`), per the sources' own explicit statement that these are not official NeoMundi thresholds.
- The complete RGC JSON Schema files (`contract-v0.1.schema.json`, `contract-v0.2.schema.json`) and the `verify.py` reference verifier — referenced by the API guide as existing in a separate `neomundi-measurement-interoperability` repository, but not present among the local files supplied for this work. `schema/README.md` states this gap explicitly rather than fabricating the missing schema.
- Any license text. The old launcher shipped under Apache-2.0; this repository does not assume the same license applies to the new product without an explicit decision, so no `LICENSE` file was added.
- The Node.js code sample from the API guide — the guide itself flags it as untested against a real signed contract, particularly around floating-point hash-canonicalization behaviour; it was not carried into `reference/` to avoid presenting untested cryptographic code as a working reference.

## Parts that still require a future freeze

Per the Metric Contract's own "Explicitly deferred elements" list and the pre-freeze status of the consumption-rules document:

- The definitive JSON Schema, required-field list, and enums for a NeoMundi measurement and for the interoperable contract.
- The exact relationship among `G`, `g_score`, `g_final`, `stability_score`, and `∆G` — not specified by any source supplied here.
- Official numerical thresholds and band boundaries (latency, cost, ∆G degradation), if any are ever made official.
- A reconciled version-field scheme (see contradiction 3 above).
- A reconciled payload structure between the Metric Contract's illustrative example and the real RGC structure (see contradiction 4 above).
- Resynchronization of the French and English Metric Contract documents (see contradiction 2 above).
- Whether, and how, the `DROP ⇔ FLAG` empirical correspondence observed in specific replication campaigns is ever promoted from empirical observation to a normative rule.

## Human validation still needed

- The API Integration Guide's illustrative response examples (§3–4 in `API_INTEGRATION_GUIDE.md`) should be checked against a real, live API call before this repository's documentation is treated as fully verified.
- A decision on public vs. private repository visibility and license terms, if this repository is ever intended for external/public distribution beyond its current private scope.
- A decision on whether "RGC" should remain the internal implementation name or be renamed to align with the "Interoperable Measurement Contract" terminology used in this repository's public-facing docs.

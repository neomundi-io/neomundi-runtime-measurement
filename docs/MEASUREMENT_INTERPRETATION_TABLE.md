# Measurement Interpretation Table

Quick-reference only. **This table does not replace [MEASUREMENT_CONTRACT.md](./MEASUREMENT_CONTRACT.md) or [CONSUMER_BOUNDARIES.md](./CONSUMER_BOUNDARIES.md)** — read those for full definitions and normative force.

No threshold, numeric band, or enum in this table is invented. Where sources do not define one, this table says so explicitly rather than filling the gap.

**Contract status legend**

- **Normative** — defined in the Measurement Contract Draft v0.0.
- **Normative (RGC schema-enforced)** — defined and structurally enforced by the published JSON Schema in [schema/](../schema/) (`contract-v0.1.schema.json` / `contract-v0.2.schema.json`), independently re-validated while building this repository (zero schema errors on all bundled examples). This is a different normative source from the Measurement Contract — see [INTEROPERABILITY.md](./INTEROPERABILITY.md) for how the two relate.
- **Experimental / pre-freeze** — defined only in the Signal Interpretation & Consumption Rules document, itself explicitly labelled "Experimental / pre-freeze, work in progress."
- **Illustrative (real field)** — the field path appears in a real API response structure (confirmed by production client code or a real signed contract example), but is not yet covered by normative semantic text of its own beyond what's listed here.

## Core signals

| Signal / State | Meaning | Does not mean | Consumer guidance | Contract status |
|---|---|---|---|---|
| `stability_score` | A level of observed behavioural stability of the generation, under the declared measurement conditions. Documented range `0.0`–`1.0`; higher = more measured stability. | Factual correctness, correctness probability, safety probability, compliance probability, overall system quality. | Do not use alone to validate an answer. May coexist with a factually incorrect output ("deceptive stability" / "misleading stability" in source material). | Normative |
| `coherence_score` | An observed coherence property (semantic/structural) of the generation. | Factual validation, safety validation, a compliance determination, execution authorization. | Consume together with other signals; do not collapse into a single "quality" score. | Normative |
| `factual_validity_signal` | Information about factual validity produced within the limits of its measurement method. | Independent verification of truth, when not independently validated. | A `null`/`unknown`/`not_assessed` value must not be read as "no factual risk" or "validated". | Normative |
| `semantic_variability_signal` | Observed variability in the semantic content of generations under the applicable conditions. | Proof of factual correctness (low variability) or proof of error / identification of the correct output (high variability). | Treat as one input among several, not a verdict. | Normative |
| `risk_signal` | A measurement/interpretation signal within the declared limits of the metric. | Any of: `ALLOW`, `BLOCK`, `ACCEPT`, `REJECT`, `COMPLIANT`, `NON_COMPLIANT`, `SAFE`, `UNSAFE`, `ADMISSIBLE`, `NON_ADMISSIBLE`. | May be used as one input to your own policy. The resulting decision is yours, not NeoMundi's. | Normative |
| latency / cost bands | May be exposed as measurements or bands. | A frozen enum, an official threshold, or a routing rule — none are defined yet. | An explicitly unknown value must not be silently treated as a measured value. | Normative (existence only) — thresholds/bands explicitly **not frozen** |

## Signals documented only in the experimental / pre-freeze consumption-rules material

These names appear in `signal_interpretation_and_consumption_rules` (status: "Experimental / pre-freeze, work in progress") and are **not** part of the normative Measurement Contract's current vocabulary. Their exact mathematical relationship to the normative signals above (e.g. how `G` relates to `stability_score`) is explicitly **not specified** by the sources — do not assume equivalence or conversion.

| Signal / State | Meaning | Does not mean | Consumer guidance | Contract status |
|---|---|---|---|---|
| `G` / `g_score` | A runtime property related to stability, regularity or coherence of the generative process. | A direct factual-truth score. | High `G` may coexist with an incorrect answer ("deceptive stability"). Do not infer "`G` up ⇒ factual correctness up". | Experimental / pre-freeze |
| `∆G` / `delta_g` | Change in the runtime stability signal over the course of generation. | A frozen, portable numeric threshold. | Consumers must not invent their own ∆G from unrelated fields; no official stopping threshold exists — values like `∆G < -0.05/-0.10/-0.15` seen in exploratory studies are explicitly non-official. | Experimental / pre-freeze |
| `delta_profile`: `DROP` | Degradation of the stability signal without sufficient subsequent recovery. | A factual judgment or confirmed error. | Read together with other signals; a `DROP` + `FLAG` combination is a stronger attention zone than either alone. | Experimental / pre-freeze |
| `delta_profile`: `FLAT` | A largely stable trajectory, no substantial degradation/recovery pattern. | Factual validation. | Informational only. | Experimental / pre-freeze |
| `delta_profile`: `V_SHAPE` | Degradation followed by partial recovery. | Proof that the issue fully resolved. | Distinguish from persistent degradation (`DROP`). | Experimental / pre-freeze |
| `decision`: `ALLOW` (binary form) | The runtime measurement did not classify the generation as requiring a `FLAG` under the applicable configuration. | True, safe, approved, compliant, factually verified, or that no external validation is needed. | Do not treat as sufficient on its own where factual correctness matters. | Experimental / pre-freeze |
| `decision`: `FLAG` (binary form) | The runtime measurement identified a generation deserving attention. | Automatic proof that the output is wrong. | May trigger verification, escalation, human review, regeneration, rerouting, early stopping, logging — as a matter of **your** policy. | Experimental / pre-freeze |
| `regime`: `STABLE` | A synthetic description of runtime context. | Absence of hallucination, absence of `FLAG`/`DROP`, or authorization to skip verification, on its own. | Interpret together with other signals, never alone as an operational trigger. | Experimental / pre-freeze |
| `DROP ⇔ FLAG` relationship | A very strong / near-perfect correspondence was observed in specific replication campaigns. | A universal invariant. | Explicitly classified **EMPIRICAL** in the source material — do not assume it holds outside tested conditions unless a versioned contract promotes it to normative. | Experimental — empirical observation, not a rule |

## Fields defined by the RGC interoperability schema

These field names come from the NeoMundi Measurement Interoperability Contract, now included as authoritative JSON Schemas in [schema/](../schema/) (`contract-v0.1.schema.json`, `contract-v0.2.schema.json`) — see [INTEROPERABILITY.md](./INTEROPERABILITY.md). They are not yet given standalone semantic text of their own in the abstract Measurement Contract; treat their meaning as adjacent to the closest normative signal above, not identical to it, unless a future versioned contract states equivalence.

| Field | Meaning | Does not mean | Consumer guidance | Contract status |
|---|---|---|---|---|
| `governance.decision` (5-value form: `ALLOW`/`FLAG`/`REROUTE`/`HUMAN_REVIEW`/`STOP`, seen in `/v1/govern` responses) | A measurement-layer signal. | An executed action — the real signed RGC examples' own `governance_boundary.authorization_status` is `"not_applicable"` and `execution_permission_changed` is schema-enforced `false`. | Treat as advisory input to your own policy, exactly like `risk_signal`. | Illustrative (`/v1/govern` field path confirmed by production code) |
| `r_score` | A runtime-related numeric score returned alongside `stability_score`. | Not defined further in any source supplied to this repository. | Do not assume a formula or relationship to `stability_score` or `G` — none is documented. | Illustrative (real field), meaning **not specified** |
| `factual_hallucination_score` | An observed signal in `observation.observed_signals`. | Confirmed proof of hallucination by itself. | Treat as the RGC-side counterpart of `factual_validity_signal`'s boundary — not independent truth verification. | Normative (RGC schema-enforced); real value confirmed in two cryptographically verified v0.1 examples |
| `semantic_instability_score`, `semantic_risk` | Observed signals in `observation.observed_signals`. | A single unified "quality" score when combined with the others. | Read as separate dimensions, per the Measurement Contract's stance on `semantic_variability_signal`. | Normative (RGC schema-enforced) |
| `observation_class`: `within_bounds` | No threshold-crossing signal was detected **within the measured domain**. | Every dimension was measured; the system is globally safe; unmeasured signals equal zero. | Never extend beyond the declared measurement boundary. | Normative (RGC schema-enforced, v0.1 and v0.2) |
| `observation_class`: `flagged` | Measured evidence within the covered domain supports a flagged classification. | Proof extending to unmeasured dimensions — a partially covered observation can still legitimately be `flagged`. | Partial coverage limits scope of inference, not the ability to report what was actually observed. | Normative (RGC schema-enforced, v0.1 and v0.2) |
| `observation_class`: `not_assessed` | Available measured evidence is insufficient to support either `within_bounds` or `flagged`. | A safe default — this is a deliberate third state, not an omission. | Do not silently treat as `within_bounds`. | Normative (RGC schema-enforced) — **v0.2 only**, not a valid value under the v0.1 schema |
| `signal_status`: `measured` / `not_measured` / `insufficient_coverage` | Per-signal coverage status. Schema-enforced: `measured` requires a numeric value; the other two require `null`. | `not_measured` must never be read as "no issue" — its value is always `null`, never a reassuring default. | Check `signal_status` before trusting any individual signal value. | Normative (RGC v0.2 schema-enforced) — **v0.2 only**, absent from the v0.1 schema |

## Measurement status states

| State | Meaning | Does not mean | Consumer guidance | Contract status |
|---|---|---|---|---|
| `complete` | All declared measurement dimensions for this observation were assessed. Under RGC v0.2, this value requires `measurement_coverage = 1.0` — schema-enforced. | — | Safe to interpret coverage as full for this observation, under v0.2. **Under v0.1, this guarantee did not hold** — see the historical inconsistency note below. | Normative (RGC v0.2 schema-enforced); Normative but not schema-enforced under v0.1 |
| `partial` | Some but not all declared measurement dimensions were assessed. Under RGC v0.2, this value requires `measurement_coverage < 1.0` — schema-enforced. | Complete coverage. The presence of a numeric value does not imply every dimension was assessed. | Consider declared coverage before drawing conclusions. | Normative (RGC v0.2 schema-enforced) |
| `insufficient coverage` | Coverage is too low to support the intended interpretation. | — | Do not treat as equivalent to a "no issue" result. | Normative (concept) — exact coverage thresholds not frozen |
| `not measured` / missing signal | The signal was not produced for this observation. | **"No issue detected."** A missing signal must never be silently converted into `0`, `ALLOW`, `STABLE`, "safe", or "verified". | Treat as "measurement unavailable" and apply your own fallback policy explicitly. | Normative |
| malformed payload | The payload failed to parse or validate as a NeoMundi measurement. | A valid measurement of any kind. | Must not silently produce `ALLOW`; reject, log, and apply your fallback policy. | Experimental / pre-freeze (consumption-rules material) |

**Historical inconsistency, preserved as-is**: the real signed RGC v0.1 example `within-bounds-no-review` (see [schema/examples/](../schema/examples/)) has `measurement_status: "complete"` together with `measurement_coverage: 0.6` — a combination the v0.2 schema now forbids. The source material documents this itself as the ambiguity that motivated v0.2's schema-enforced consistency rule, and the signed v0.1 record is kept unchanged (modifying it would invalidate its hash and signature). Do not use this v0.1 example as a template for a new integration; use v0.2 semantics for new work.

## What this table does not do

- It does not reduce all signals to one composite quality score — the sources explicitly prohibit this ("stability", "factuality" and "semantic coherence" are separate axes that must not be silently collapsed).
- It does not introduce thresholds, band boundaries, or routing rules that are not already present in the sources.
- It does not upgrade any "Experimental / pre-freeze" or "Illustrative" row to normative status. Only a future explicitly versioned Measurement Contract can do that.

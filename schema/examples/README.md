# Example status

Every example below is reproduced exactly from a source document (byte-for-byte for JSON content, aside from formatting), with no invented fields or values. Status determines how much weight the example should carry.

| File | Status | Source |
|---|---|---|
| `rgc-v0.1-real-signed-example.json` | **Real signed example.** A genuine signed RGC v0.1 contract, reproduced as-is. Its hash/signature fields are real and could in principle be checked against the original signing key (see [API_INTEGRATION_GUIDE.md §6](../../API_INTEGRATION_GUIDE.md)). | Reference interoperability repository, via API Integration Guide §5 |
| `rgc-v0.2-illustrative-partial-fragment.json` | **Illustrative fixture, pre-freeze.** A fragment only (`observed_signals`, not a full contract). Not a captured real contract. | Reference interoperability repository fixture, via API Integration Guide §5.1 |
| `metric-contract-reference-payload-illustrative.json` | **Illustrative, explicitly synthetic** (`synthetic: true` in the payload itself). The Metric Contract itself labels this "an operational reference example — not a complete normative JSON Schema." | Metric Contract Draft v0.0 |
| `govern-response-illustrative.json` | **Illustrative — field paths confirmed by production code, values not captured from a live call.** | API Integration Guide §4 |
| `govern-stream-final-event-illustrative.json` | **Illustrative — field paths confirmed by production code, values not captured from a live call.** | API Integration Guide §3 |
| `consumption-rules-conceptual-payload-prefreeze.json` | **Illustrative and non-authoritative, explicitly pre-freeze.** Placeholder version strings (`"1.x"`) are from the source verbatim — not real version numbers. | Signal Interpretation & Consumption Rules (experimental / pre-freeze) |
| `delta-series-conceptual-prefreeze.json` | **Conceptual representation only, explicitly pre-freeze.** The source states the authoritative serialization must be defined by a future versioned schema. | Signal Interpretation & Consumption Rules (experimental / pre-freeze) |

None of these examples should be used as a target for schema validation in production. See [../README.md](../README.md).

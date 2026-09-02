# NeoMundi Runtime Measurement Layer

[🇬🇧 English](./README.md) · [🇫🇷 Français](./README_FR.md)

**NeoMundi est une couche de mesure runtime pour les systèmes d'IA.**

NeoMundi mesure le comportement runtime des systèmes d'IA. Elle observe le comportement runtime de l'exécution d'un système d'IA et produit des mesures structurées, versionnées et interopérables sur ce comportement. Elle ne décide pas de ce qui doit en résulter.

> **NeoMundi mesure. Le système consommateur interprète, gouverne et agit.**

---

## Comment cela s'articule

```text
Système d'IA
   │
   ▼
API NeoMundi de mesure runtime
   │
   ▼
Mesure runtime
   │
   ▼
Contrat interopérable de mesure
   │
   ▼
Systèmes clients / intégrateurs
   (interprétation, politique, action)
```

NeoMundi se situe entre l'exécution d'un système d'IA et l'infrastructure qui consomme l'information sur cette exécution. NeoMundi ne se situe pas en aval de la décision.

## Les quatre éléments centraux

1. **API NeoMundi** — l'interface par laquelle une exécution d'IA est observée et mesurée. Voir [API_INTEGRATION_GUIDE.md](./API_INTEGRATION_GUIDE.md).
2. **Mesure runtime** — la sortie structurée décrivant le comportement observé (stabilité, cohérence, signaux de validité factuelle et de risque, entre autres) dans des conditions et des limites déclarées. Voir [docs/MEASUREMENT_CONTRACT.md](./docs/MEASUREMENT_CONTRACT.md).
3. **Contrat interopérable de mesure** — la représentation versionnée, consommable par machine et vérifiable indépendamment d'une mesure, conçue pour être échangée et consommée entre systèmes. Le contrat interopérable définit la structure, la représentation et les règles d'interprétation des mesures runtime produites par NeoMundi. Voir [docs/INTEROPERABILITY.md](./docs/INTEROPERABILITY.md).
4. **Documentation d'intégration officielle** — ce dépôt : le guide API, le contrat de mesure, la table d'interprétation et les frontières consommateur qui définissent ensemble un usage correct.

Une cinquième couche, nécessaire, accompagne ces quatre éléments : **la documentation d'interprétation**. Une mesure n'est utilisable correctement que si sa signification, et les limites de cette signification, sont documentées en même temps qu'elle est produite. [docs/MEASUREMENT_INTERPRETATION_TABLE.md](./docs/MEASUREMENT_INTERPRETATION_TABLE.md) et [docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md) existent pour cette raison — elles font partie de ce qui rend la couche de mesure utilisable, elles ne constituent pas en elles-mêmes une couche de gouvernance ou de conformité.

## Ce que NeoMundi fait

- Observe l'exécution runtime d'un système d'IA dans des conditions déclarées.
- Produit des mesures et signaux runtime versionnés (par ex. `stability_score`, `coherence_score`, `factual_validity_signal`, `semantic_variability_signal`, `risk_signal`).
- Documente la signification, les limitations et les frontières de chaque mesure.
- Expose ces mesures via un contrat interopérable qui peut être consommé, échangé et, le cas échéant, vérifié indépendamment par des systèmes externes.
- Distingue explicitement ce qui est mesuré, ce qui est inconnu, et ce qui n'est pas évalué.

## Ce que NeoMundi ne fait pas

- Ce n'est pas un tableau de bord.
- Ce n'est pas une application `.exe`.
- Ce n'est pas un moteur de gouvernance.
- Ce n'est pas un moteur de conformité.
- Ce n'est pas un policy engine.
- Ce n'est pas une couche d'actionnabilité.
- Ce n'est pas une application métier.
- NeoMundi ne décide pas `ALLOW`, `BLOCK`, `STOP`, ni aucune autre conséquence opérationnelle ou d'exécution. NeoMundi mesure ; le système consommateur décide.
- NeoMundi ne constitue pas en soi une preuve de vérité, de sécurité, de conformité ou d'admissibilité. Voir [docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md).

**Mesure ≠ Interprétation ≠ Politique ≠ Exécution**

## Carte de la documentation

| Document | Objet |
|---|---|
| [QUICKSTART.md](./QUICKSTART.md) | Obtenir une première mesure en quelques minutes |
| [API_INTEGRATION_GUIDE.md](./API_INTEGRATION_GUIDE.md) | Endpoints, payloads, headers, gestion des erreurs |
| [docs/MEASUREMENT_CONTRACT.md](./docs/MEASUREMENT_CONTRACT.md) | Ce que signifie chaque mesure et signal, et ses limites |
| [docs/MEASUREMENT_INTERPRETATION_TABLE.md](./docs/MEASUREMENT_INTERPRETATION_TABLE.md) | Table de référence rapide : signal → signification → ce qu'il ne signifie pas |
| [docs/INTEROPERABILITY.md](./docs/INTEROPERABILITY.md) | Structure, versionnement, provenance et échange du contrat de mesure |
| [docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md) | La frontière entre mesure, interprétation, politique et exécution |
| [VERSIONING.md](./VERSIONING.md) | `schema_version`, `metric_version`, `normalizer_version` |
| [CHANGELOG.md](./CHANGELOG.md) | Historique des changements |
| [schema/](./schema/) | Exemples de payload connus, étiquetés par statut (signé réel / illustratif / pre-freeze) |
| [reference/python/](./reference/python/) | Starter d'intégration de référence minimal, non normatif |
| [source-notes/SOURCE_STATUS.md](./source-notes/SOURCE_STATUS.md) | Ce qui est normatif, expérimental, pre-freeze, ou contradictoire dans les sources de ce dépôt |

## Statut

Ce dépôt documente une couche de mesure dont le contrat est encore partiellement en **Draft** et, pour certains signaux, explicitement **expérimental / pre-freeze**. Chaque document ci-dessus indique son propre statut. Rien ici ne doit être lu comme une spécification finalisée et figée, sauf mention explicite contraire.

## Architecture future

Ce dépôt est uniquement la primitive de mesure. Les couches qui agissent sur la mesure — actionnabilité, preuve de conformité, preuve assurantielle, assurance de changement, et autres applications — sont volontairement exclues de ce dépôt et vivront dans des dépôts séparés et dépendants.

```text
neomundi-runtime-measurement
        ↑
        │ dépendance
neomundi-actionability
        ↑
        │
couches spécifiques à la solution
        ├── preuve de conformité
        ├── preuve assurantielle
        ├── assurance de changement
        └── autres applications
```

**Une primitive de mesure. Plusieurs applications.**

# NeoMundi Runtime Measurement Layer

[🇬🇧 English](./README.md) · [🇫🇷 Français](./README_FR.md)

**Mesurer, caractériser et tracer le comportement des systèmes d'IA en production.**

Produire des preuves de mesure reproductibles, lisibles par machine et vérifiables indépendamment pour le monitoring, l'audit, la gouvernance, l'assurance et l'optimisation.

**Sémantique définie · Comparable dans le temps · JSON structuré · Horodaté · Versionné · Hash & signature vérifiables**

> **NeoMundi mesure. Le système consommateur interprète, gouverne et agit.**

```text
Système d'IA
   │
   ▼
NeoMundi Runtime Measurement Layer
   │
   ▼
Signaux runtime
   │
   ▼
Contrat interopérable de mesure
   │
   ▼
Systèmes clients / intégrateurs
```

---

## Ce que ça fait

- **Mesure runtime** — observe le comportement d'un système d'IA pendant ou après son exécution, dans des conditions déclarées.
- **Signaux comportementaux et opérationnels** — par ex. `stability_score`, `coherence_score`, `factual_validity_signal`, `semantic_variability_signal`, `risk_signal`. Voir [docs/MEASUREMENT_CONTRACT.md](./docs/MEASUREMENT_CONTRACT.md).
- **Sémantique définie** — la signification de chaque signal, ses limites, et ce qu'il ne signifie pas, sont documentées en même temps qu'il est produit, non laissées à l'interprétation. Voir [docs/MEASUREMENT_INTERPRETATION_TABLE.md](./docs/MEASUREMENT_INTERPRETATION_TABLE.md).
- **Reproductibilité** — les conditions de mesure, le protocole et les versions sont déclarés, de sorte qu'une mesure puisse être reproduite ou contestée de façon indépendante.
- **Comparaison dans le temps** — les signaux portent une information de version explicite afin que les observations historiques restent interprétables à mesure que le contrat évolue. Voir [VERSIONING.md](./VERSIONING.md).
- **Traçabilité** — identifiants, horodatages et provenance relient une mesure à l'observation qui l'a produite.
- **Enregistrements de mesure interopérables** — les mesures sont exposées via un contrat structuré, consommable par machine et vérifiable indépendamment. Voir [docs/INTEROPERABILITY.md](./docs/INTEROPERABILITY.md).

« Caractériser » signifie qu'une mesure NeoMundi est accompagnée d'une sémantique définie, d'un périmètre déclaré, d'un versionnement et de règles d'interprétation. Cela ne signifie **pas** que NeoMundi diagnostique universellement des causes racines — voir [docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md).

## Ce que ça produit

- **Des signaux runtime** décrivant le comportement observé (stabilité, cohérence, validité factuelle, variabilité sémantique, risque — entre autres).
- **Des enregistrements de mesure structurés**, horodatés et identifiables jusqu'à l'observation et la requête qui les ont produits.
- **Une information de version** distinguant les versions de schéma, de métrique et de normaliseur — voir [VERSIONING.md](./VERSIONING.md).
- **De la provenance** — ce qui a produit la mesure et sous quel protocole.
- **De l'information d'intégrité** — une empreinte de hash et, lorsqu'elle est produite, une signature cryptographique qu'un tiers peut vérifier indépendamment, sans avoir à faire confiance à l'infrastructure de NeoMundi.
- **Du JSON interopérable, lisible par machine**, là où la couche d'interopérabilité le prend en charge — voir [schema/](./schema/) et [docs/INTEROPERABILITY.md](./docs/INTEROPERABILITY.md). Le contrat interopérable de mesure définit la structure, la représentation et les règles d'interprétation des mesures runtime produites par NeoMundi.

## Pourquoi c'est utile

La même couche de mesure peut alimenter, en aval :

- le monitoring
- l'audit
- la gouvernance
- l'assurance
- l'optimisation

Ce sont des usages en aval de la mesure, construits et exploités par le système consommateur — **ce dépôt n'implémente aucun d'entre eux**. Une seule primitive de mesure peut alimenter plusieurs infrastructures en aval différentes sans que celles-ci n'aient besoin de devenir des systèmes NeoMundi.

## Comment s'intégrer

- [QUICKSTART.md](./QUICKSTART.md) — obtenir une première mesure en quelques minutes.
- [API_INTEGRATION_GUIDE.md](./API_INTEGRATION_GUIDE.md) — endpoints, payloads, headers, gestion des erreurs.
- [docs/MEASUREMENT_CONTRACT.md](./docs/MEASUREMENT_CONTRACT.md) — ce que signifie chaque mesure et signal, et ses limites.
- [docs/MEASUREMENT_INTERPRETATION_TABLE.md](./docs/MEASUREMENT_INTERPRETATION_TABLE.md) — table de référence rapide : signal → signification → ce qu'il ne signifie pas.
- [docs/INTEROPERABILITY.md](./docs/INTEROPERABILITY.md) — structure, versionnement, provenance et échange du contrat de mesure.

## Frontière architecturale

> **NeoMundi mesure.**
> **Le système consommateur interprète, gouverne et agit.**

**Mesure ≠ Interprétation ≠ Politique ≠ Exécution**

Le NeoMundi Runtime Measurement Layer n'est pas :

- une plateforme de gouvernance de l'IA ;
- un moteur de conformité ;
- un policy engine ;
- un moteur de décision ;
- un tableau de bord de monitoring ;
- une application `.exe` ;
- une application métier.

Le monitoring, l'audit, la gouvernance, l'assurance et l'optimisation sont des usages en aval de la mesure — pas ce produit. NeoMundi ne décide pas `ALLOW`, `BLOCK`, `STOP`, ni aucune autre conséquence opérationnelle ou d'exécution, et une mesure NeoMundi ne constitue pas en soi une preuve de vérité, de sécurité, de conformité ou d'admissibilité. Voir [docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md).

---

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

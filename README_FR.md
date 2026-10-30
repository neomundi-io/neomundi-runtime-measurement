<div align="center">

<sub><a href="README.md">English</a> · <b>Français</b></sub>

# NeoMundi Runtime Measurement

## Transformez le comportement de l’IA en signaux mesurables.

**Une infrastructure indépendante de mesure de l’IA pour vos systèmes existants.**

[![Couche : mesure pendant l'exécution](https://img.shields.io/badge/couche-mesure_pendant_l'exécution-475569?style=flat-square)](#fonctionnement)
[![REST : parcours principal](https://img.shields.io/badge/REST-parcours_principal-0f766e?style=flat-square)](QUICKSTART.md)
[![SSE : alternatif](https://img.shields.io/badge/SSE-parcours_alternatif-2563eb?style=flat-square)](API_INTEGRATION_GUIDE.md)
[![Interop : v0.1 signée](https://img.shields.io/badge/Interop-v0.1_signée-0f766e?style=flat-square)](docs/INTEROPERABILITY.md)
[![SDK et MCP : voir statuts](https://img.shields.io/badge/SDK_%26_MCP-voir_statuts-a16207?style=flat-square)](#statut-des-intégrations)

**[Commencer](START_HERE_FR.md)** · [Première mesure](QUICKSTART.md) · [Guide API](API_INTEGRATION_GUIDE.md) · [Signaux](docs/MEASUREMENT_CONTRACT.md) · [Interopérabilité](docs/INTEROPERABILITY.md) · [Limites](#limites-connues)

> **Votre système. Vos décisions. Notre signal de mesure.**

</div>

---

NeoMundi mesure une exécution d’IA dans des conditions déclarées et renvoie un enregistrement structuré et horodaté. Votre système peut le conserver, comparer des observations compatibles ou demander un contrat d’interopérabilité signé.

NeoMundi ne décide **pas** si votre application doit autoriser, bloquer, rediriger ou approuver quoi que ce soit. L’interprétation, la politique et l’exécution restent sous l’autorité du système consommateur.

```text
Mesure ≠ Interprétation ≠ Politique ≠ Exécution
```

## Choisissez votre parcours

| Objectif | Parcours | Point de départ |
|---|---|---|
| Mesurer une réponse déjà produite | REST `POST /v1/govern` | [Quickstart](QUICKSTART.md) |
| Générer via NeoMundi et recevoir un flux | SSE `POST /v1/govern/stream` | [Guide API](API_INTEGRATION_GUIDE.md#3-step-1--v1governstream-get-the-model-response) |
| Intégrer depuis Python | SDK Python | [SDK](https://github.com/neomundi-io/neomundi-python-sdk) |
| Mesurer depuis un agent | Connecteur MCP | [MCP](https://github.com/neomundi-io/neomundi-measurement-mcp) |
| Valider un enregistrement portable | JSON Schema et signature | [Interopérabilité](docs/INTEROPERABILITY.md) |
| Utiliser l’instrument hébergé | NeoMundi Station | [Station](https://github.com/neomundi-io/neomundi-station-public/blob/main/README.fr.md) |

## Obtenez votre première mesure

Le parcours principal mesure une exécution que vous détenez déjà. Il ne demande pas à NeoMundi de générer la réponse et ne nécessite aucune clé API de fournisseur.

```bash
curl -X POST "https://api.neomundi.io/v1/govern" \
  -H "X-API-Key: YOUR_NEOMUNDI_KEY" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
    "source_type": "llm",
    "mode": "OBS",
    "llm_prompt": "Quelle est la capitale de la France ?",
    "llm_response": "Paris.",
    "raw_metrics": {"token_count": 1, "latency_ms": 120}
  }'
```

La route et les champs sont confirmés par les documents d’intégration existants. Aucune valeur de réponse n’est affichée, car cette refonte n’a effectué aucun nouvel appel live. Conservez la réponse brute, ses versions et tous les états partiels ou indisponibles ; ne remplacez jamais une valeur absente par zéro.

[**Suivre le parcours REST complet →**](QUICKSTART.md)

## Ce que mesure NeoMundi

NeoMundi produit des signaux comportementaux et opérationnels bornés pour une observation. Selon la version déployée et les contrôles disponibles, ils peuvent concerner la stabilité, la cohérence, la factualité, la variabilité sémantique ou le risque.

Le vocabulaire du Metric Contract, les travaux expérimentaux `G`/`g_score`/`∆G` et les champs RGC sont distincts. Aucun mapping non documenté n’est sous-entendu. Consultez le [contrat de mesure](docs/MEASUREMENT_CONTRACT.md) et la [table d’interprétation](docs/MEASUREMENT_INTERPRETATION_TABLE.md).

## Fonctionnement

```text
Votre exécution d’IA
       ↓
API de mesure NeoMundi
       ↓
Enregistrement de mesure versionné
       ├──── contrat d’interopérabilité signé facultatif
       ↓
Votre stockage, interprétation, politique et action
```

L’API contient un champ historique nommé `governance.decision`. Les valeurs `ALLOW`, `FLAG`, `REROUTE`, `HUMAN_REVIEW` ou `STOP` sont des signaux de mesure—ni permissions, ni commandes, ni actions exécutées par NeoMundi. Le schéma impose `execution_permission_changed: false`.

## Ce que reçoit votre système

Une réponse peut contenir un identifiant, un horodatage, des versions, la provenance, des valeurs mesurées, l’état, la couverture, les limites et des champs consultatifs. Pour un échange portable, demandez un contrat JSON versionné, validez-le avec le schéma correspondant et vérifiez son empreinte SHA-256 et sa signature Ed25519/JWS.

## Statut des intégrations

Statuts vérifiés le **30 octobre 2026**.

| Parcours | Statut | Preuve et limite |
|---|---|---|
| API REST | **Disponible ; exemples qualifiés** | Route et champs confirmés. Valeurs illustratives jusqu’à leur capture live. |
| API SSE | **Alternative disponible** | NeoMundi appelle le fournisseur et reçoit son identifiant pour cet appel. |
| SDK Python 2.0.0 | **Implémenté ; qualification live V2 en attente** | REST/SSE implémentés et tests hors ligne réussis. |
| Plugin MCP local 0.2.0 | **Évalué en pilote** | Qualification REST/SSE bornée le 26 octobre 2026. |
| Source MCP 0.3.0-rc.1 | **Release candidate** | Déploiement backend compagnon et nouvelle qualification requis. |
| MCP hébergé | **Transport validé ; contrat en attente** | Les preuves locales ne qualifient pas le serveur séparé. |
| Interop v0.1 | **Historique, signée, revérifiée** | Deux exemples passent schéma, empreinte et signature. |
| Interop v0.2 | **Schéma disponible ; exemples illustratifs** | Fixtures valides mais explicitement non signées et non live. |

## Données, confidentialité et provenance

Distinguez trois frontières :

1. **Données envoyées à la mesure.** REST peut inclure l’invite et la réponse. SSE transmet les paramètres et un identifiant fournisseur configuré.
2. **Traitements internes.** Le contenu peut être traité par les évaluateurs et services activés. Conservation et destinations dépendent du déploiement.
3. **Divulgation d’interopérabilité.** Le contrat signé exclut par conception les invites, réponses et identifiants bruts de fournisseur ou modèle.

Un export sans texte brut ne prouve pas qu’aucun texte brut n’a été traité en amont. Consultez [Données et confidentialité](https://github.com/neomundi-io/neomundi-io-data-protection/blob/main/README_FR.md).

## Preuves

- Deux contrats historiques v0.1 ont été revérifiés pour le schéma, l’empreinte SHA-256 et la signature Ed25519/JWS.
- Les schémas v0.2 imposent des états partiels et indisponibles explicites.
- Les fixtures v0.2 sont des illustrations non signées, pas des observations de production.
- Le vérificateur Python a été contrôlé avec les exemples signés v0.1.
- Le code d’exemple de bout en bout n’est pas qualifié comme client de production.

## Limites architecturales

NeoMundi ne fournit ni verdict universel de vérité, ni certification de sécurité, ni détermination de conformité, ni moteur de politique, ni exécution automatique.

```text
stabilité élevée ≠ exactitude factuelle
FLAG ≠ erreur prouvée
ALLOW ≠ vérité ou permission prouvée
observation unique ≠ dérive
```

## Documentation

| Document | Objet |
|---|---|
| [START_HERE_FR.md](START_HERE_FR.md) | Choisir un parcours d’intégration. |
| [QUICKSTART.md](QUICKSTART.md) | Obtenir une mesure REST et un contrat facultatif. |
| [Guide API](API_INTEGRATION_GUIDE.md) | REST, SSE, erreurs et vérification. |
| [Contrat de mesure](docs/MEASUREMENT_CONTRACT.md) | Sens et limites des signaux. |
| [Interopérabilité](docs/INTEROPERABILITY.md) | Contrat, versions et vérification. |
| [Limites consommateur](docs/CONSUMER_BOUNDARIES.md) | Mesure, politique et action. |
| [VERSIONING.md](VERSIONING.md) | Versions et différences non résolues. |
| [schema/](schema/) | Schémas v0.1 et v0.2 faisant autorité. |

## Limites connues

- Les valeurs de réponse sont illustratives sauf mention d’un exemple réel signé.
- Aucun mapping officiel ne réconcilie Metric Contract, vocabulaire `G` et champs RGC.
- `metric_version` et `measurement_version` ne sont pas réconciliés.
- Un exemple signé v0.1 combine `complete` et une couverture `0.6` ; il reste historique, pas modèle v0.2.
- Une observation unique n’établit ni tendance ni dérive.
- Les garanties globales de destination, conservation et effacement ne sont pas établies ici.
- SDK, MCP local et MCP hébergé ont des états de qualification différents.

---

**Une primitive de mesure. Plusieurs applications.**

> **Votre système. Vos décisions. Notre signal de mesure.**

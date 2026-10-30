# Commencer ici

[English](START_HERE.md) · [Français](START_HERE_FR.md) · [Runtime Measurement](README_FR.md)

NeoMundi Runtime Measurement est le point d’entrée développeur pour mesurer une exécution d’IA et consommer le signal obtenu dans votre propre infrastructure.

## Choisissez votre parcours

| Vous souhaitez… | Point de départ | Statut actuel |
|---|---|---|
| Mesurer une réponse existante | [Quickstart REST](QUICKSTART.md) | Parcours principal |
| Générer via NeoMundi et consommer SSE | [Guide API §3](API_INTEGRATION_GUIDE.md#3-step-1--v1governstream-get-the-model-response) | Parcours alternatif |
| Intégrer depuis Python | [SDK Python](https://github.com/neomundi-io/neomundi-python-sdk) | V2 implémentée ; qualification live en attente |
| Connecter un agent avec MCP | [Connecteur MCP](https://github.com/neomundi-io/neomundi-measurement-mcp) | 0.2.0 local évalué ; source 0.3.0-rc.1 |
| Valider un contrat portable | [Interopérabilité](docs/INTEROPERABILITY.md) | Exemples v0.1 signés ; fixtures v0.2 non signées |
| Comprendre les signaux | [Contrat de mesure](docs/MEASUREMENT_CONTRACT.md) | Contrat sémantique Draft v0.0 |
| Utiliser l’instrument hébergé | [NeoMundi Station](https://github.com/neomundi-io/neomundi-station-public/blob/main/README.fr.md) | Accès au cas par cas |

## Parcours principal

```text
Votre invite et votre réponse existantes
                 ↓
           POST /v1/govern
                 ↓
     Réponse de mesure versionnée
                 ↓
 Contrat d’interopérabilité facultatif
                 ↓
 Votre interprétation, politique et action
```

NeoMundi mesure. Il n’exécute ni `ALLOW`, ni `STOP`, ni `REROUTE`, ni aucune autre conséquence opérationnelle. Le champ historique `governance.decision` reste consultatif.

## Avant d’envoyer des données

REST peut inclure l’invite et la réponse. SSE transmet en plus les paramètres de génération et un identifiant fournisseur configuré à NeoMundi. L’export exclut l’invite, la réponse et les identifiants bruts, mais ne décrit pas tous les traitements ou toutes les conservations en amont.

Consultez [Données et confidentialité](https://github.com/neomundi-io/neomundi-io-data-protection/blob/main/README_FR.md).

## Ordre de lecture conseillé

1. [Quickstart](QUICKSTART.md)
2. [Guide d’intégration API](API_INTEGRATION_GUIDE.md)
3. [Contrat de mesure](docs/MEASUREMENT_CONTRACT.md)
4. [Limites du consommateur](docs/CONSUMER_BOUNDARIES.md)
5. [Interopérabilité](docs/INTEROPERABILITY.md)
6. [Versionnement](VERSIONING.md)
7. [Statut des sources](source-notes/SOURCE_STATUS.md)

## Garde-fous d’interprétation

```text
stabilité élevée ≠ exactitude factuelle
signal absent ≠ zéro
ALLOW ≠ permission ou vérité prouvée
observation unique ≠ dérive
sémantique v0.1 ≠ sémantique v0.2
```

Aucun mapping officiel ne réconcilie le vocabulaire du Metric Contract, les travaux expérimentaux `G`/`g_score`/`∆G` et les champs RGC.

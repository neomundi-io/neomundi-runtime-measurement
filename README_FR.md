# Couche de mesure à l’exécution NeoMundi

[🇬🇧 English](./README.md) · [🇫🇷 Français](./README_FR.md)

## Le contexte de mesure manquant pour interpréter le comportement des IA à l’exécution

NeoMundi mesure l’état comportemental d’un système d’IA à un instant précis, au sein d’un cadre de mesure défini.

Grâce à un connecteur universel, ce signal de mesure indépendant, horodaté et comparable apporte le contexte nécessaire pour interpréter :

- une observation ;
- une détection ;
- un audit ;
- un diagnostic ;
- une comparaison ;
- une évaluation assurantielle ;
- un élément de preuve.

NeoMundi apporte ce contexte sans remplacer l’infrastructure, les règles ou les mécanismes de décision du système qui le consomme.

**Une seule intégration. De multiples usages renforcés en aval.**

> **Votre système. Vos décisions. Notre signal de mesure.**

### Activer la couche et obtenir une première mesure

[**Suivre le guide de démarrage rapide →**](./QUICKSTART.md)

**Un appel API · Connecteur universel · Aucun remplacement d’infrastructure · Confidentialité dès la conception · Vos propres clés**

```text
Système d’IA
    │
    ▼
Couche de mesure à l’exécution NeoMundi
    │
    ▼
Signaux de mesure
    │
    ▼
Contrat de mesure interopérable
    │
    ▼
Infrastructure du client ou de l’intégrateur
```

---

## Ce que fait NeoMundi

### Mesure à l’exécution

NeoMundi observe le comportement d’un système d’IA pendant ou après son exécution, dans des conditions déclarées.

La mesure décrit ce qui a été observé dans un contexte donné. Elle ne prétend pas définir un état absolu ou permanent du système.

### Signaux comportementaux et opérationnels

La couche peut produire différents signaux, notamment :

- `stability_score` ;
- `coherence_score` ;
- `factual_validity_signal` ;
- `semantic_variability_signal` ;
- `risk_signal`.

La définition, le périmètre et les limites de chaque signal sont documentés dans le [contrat de mesure](./docs/MEASUREMENT_CONTRACT.md).

### Sémantique définie

Chaque signal est accompagné d’une définition explicite.

La documentation précise :

- ce que le signal mesure ;
- dans quelles conditions il a été produit ;
- comment il peut être interprété ;
- ce qu’il ne permet pas de conclure.

Les règles correspondantes sont disponibles dans la [table d’interprétation de la mesure](./docs/MEASUREMENT_INTERPRETATION_TABLE.md).

### Reproductibilité

Les conditions de mesure, le protocole utilisé et les versions applicables sont déclarés.

Une mesure peut ainsi être :

- reproduite ;
- comparée ;
- vérifiée ;
- discutée indépendamment.

### Comparabilité dans le temps

Les mesures comportent des informations de version explicites.

Cela permet de distinguer :

- la version du schéma ;
- la version de la métrique ;
- la version du normaliseur.

Les observations historiques restent ainsi interprétables lorsque le contrat évolue.

Consulter la documentation sur le [versionnement](./VERSIONING.md).

### Traçabilité

Les identifiants, horodatages et informations de provenance relient chaque mesure à l’observation qui l’a produite.

### Interopérabilité

Les mesures sont exposées sous la forme d’enregistrements structurés et lisibles par machine.

Le contrat interopérable permet aux infrastructures clientes de recevoir, stocker, échanger et exploiter le signal sans devenir des systèmes NeoMundi.

Consulter la documentation sur l’[interopérabilité](./docs/INTEROPERABILITY.md).

### Vérifiabilité indépendante

Lorsque ces éléments sont produits, l’enregistrement peut contenir :

- une empreinte cryptographique du contenu ;
- une signature vérifiable ;
- les informations nécessaires au contrôle de l’intégrité.

Un tiers peut ainsi vérifier l’intégrité d’un enregistrement sans devoir faire confiance à l’infrastructure NeoMundi.

---

## Ce que produit NeoMundi

NeoMundi produit un contexte comportemental mesuré, structuré autour de plusieurs éléments.

### Des signaux de mesure

Les signaux décrivent le comportement observé du système d’IA dans les conditions déclarées.

Ils peuvent notamment porter sur :

- la stabilité ;
- la cohérence ;
- la validité factuelle ;
- la variabilité sémantique ;
- le risque observé.

### Des enregistrements structurés

Chaque mesure peut être reliée :

- à une requête ;
- à une observation ;
- à un système ;
- à un instant précis ;
- à un protocole déclaré.

### Des informations de version

L’enregistrement distingue les versions du schéma, des métriques et des mécanismes de normalisation.

### Des informations de provenance

La provenance indique ce qui a produit la mesure et selon quel protocole.

### Des informations d’intégrité

L’enregistrement peut contenir une empreinte du contenu et une signature cryptographique vérifiable.

### Un contrat JSON interopérable

Les mesures peuvent être exposées sous une forme structurée, versionnée et exploitable par machine.

Les schémas sont disponibles dans le dossier [`schema`](./schema/).

---

## Pourquoi ce contexte est utile

Une observation brute ne suffit pas toujours à comprendre l’état comportemental du système qui l’a produite.

NeoMundi ajoute le contexte de mesure nécessaire pour interpréter plus solidement cette observation à un instant donné.

Une même primitive de mesure peut alimenter plusieurs usages en aval :

- observabilité ;
- détection de dérive ;
- audit ;
- diagnostic ;
- comparaison ;
- gouvernance ;
- assurance ;
- optimisation ;
- orchestration ;
- contrôle ;
- constitution d’éléments de preuve.

Ces usages sont construits et exploités par le système consommateur.

NeoMundi fournit le signal de mesure. Le système consommateur conserve son architecture, ses règles et son pouvoir de décision.

> **Une primitive de mesure. Plusieurs applications. Plusieurs infrastructures.**

---

## Comment intégrer NeoMundi

L’intégration repose sur une interface commune permettant à différentes infrastructures de consommer le même contrat de mesure.

### Démarrage rapide

[**Activer la couche et obtenir une première mesure →**](./QUICKSTART.md)

Le guide de démarrage rapide présente le chemin le plus court pour connecter un système et obtenir un premier résultat de mesure.

### Guide d’intégration API

Le [guide d’intégration API](./API_INTEGRATION_GUIDE.md) décrit notamment :

- les points d’accès ;
- les charges utiles ;
- les en-têtes ;
- l’authentification ;
- la gestion des erreurs ;
- le traitement des réponses.

### Contrat de mesure

Le [contrat de mesure](./docs/MEASUREMENT_CONTRACT.md) définit la signification, le périmètre et les limites des signaux.

### Table d’interprétation

La [table d’interprétation](./docs/MEASUREMENT_INTERPRETATION_TABLE.md) indique ce qui peut être conclu à partir d’un signal et ce qui ne peut pas l’être.

### Contrat d’interopérabilité

La documentation sur l’[interopérabilité](./docs/INTEROPERABILITY.md) décrit la structure, le versionnement, la provenance et les modalités d’échange de la mesure.

---

## Frontière architecturale

> **NeoMundi mesure. Le système consommateur interprète, gouverne et agit.**

**Mesure ≠ Interprétation ≠ Politique ≠ Exécution**

La couche de mesure à l’exécution NeoMundi n’est pas :

- une plateforme de gouvernance de l’IA ;
- un moteur de conformité ;
- un moteur de politiques ;
- un moteur de décision ;
- un tableau de bord de supervision ;
- une application métier ;
- un mécanisme autonome de blocage ou d’autorisation.

NeoMundi ne décide pas :

- `AUTORISER` ;
- `BLOQUER` ;
- `ARRÊTER` ;
- `ACHEMINER` ;
- ou toute autre conséquence opérationnelle.

Une mesure NeoMundi ne constitue pas, à elle seule, une preuve de vérité, de sécurité, de conformité ou de recevabilité.

Elle fournit un contexte comportemental indépendant, horodaté, traçable et comparable pouvant renforcer les systèmes chargés de ces fonctions.

Consulter la documentation sur les [frontières de consommation](./docs/CONSUMER_BOUNDARIES.md).

---

## Principes d’intégration

### Infrastructure préservée

NeoMundi s’intègre à l’infrastructure existante sans imposer son remplacement.

### Responsabilité préservée

Le système consommateur conserve :

- ses règles ;
- ses seuils ;
- ses politiques ;
- ses décisions ;
- ses actions.

### Confidentialité dès la conception

L’intégration est conçue pour limiter les échanges aux éléments nécessaires à la mesure.

### Vos propres clés

Le système consommateur conserve la maîtrise de ses clés et de ses accès fournisseurs.

### Consommation indépendante

Le même signal peut être consommé par plusieurs infrastructures sans leur imposer une gouvernance ou une interprétation commune.

---

## Cartographie de la documentation

### Commencer

[QUICKSTART.md](./QUICKSTART.md)

Activer la couche et obtenir une première mesure.

### Intégrer l’API

[API_INTEGRATION_GUIDE.md](./API_INTEGRATION_GUIDE.md)

Comprendre les points d’accès, charges utiles, en-têtes et mécanismes de gestion des erreurs.

### Comprendre les mesures

[docs/MEASUREMENT_CONTRACT.md](./docs/MEASUREMENT_CONTRACT.md)

Comprendre la signification, le périmètre et les limites de chaque mesure.

### Interpréter les signaux

[docs/MEASUREMENT_INTERPRETATION_TABLE.md](./docs/MEASUREMENT_INTERPRETATION_TABLE.md)

Identifier ce qu’un signal permet ou ne permet pas de conclure.

### Consommer le contrat interopérable

[docs/INTEROPERABILITY.md](./docs/INTEROPERABILITY.md)

Comprendre la structure, le versionnement, la provenance et l’échange des mesures.

### Respecter les frontières d’usage

[docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md)

Distinguer la mesure, l’interprétation, la politique et l’exécution.

### Comprendre le versionnement

[VERSIONING.md](./VERSIONING.md)

Distinguer les versions du schéma, des métriques et du normaliseur.

### Consulter les évolutions

[CHANGELOG.md](./CHANGELOG.md)

Consulter l’historique des modifications du produit.

---

## Architecture produit

Ce dépôt contient exclusivement la primitive de mesure NeoMundi.

Les couches qui interprètent la mesure ou agissent à partir du signal sont volontairement séparées.

```text
neomundi-runtime-measurement
              │
              ▼
      neomundi-actionability
              │
              ▼
      Applications spécialisées
```

Ces applications peuvent notamment concerner :

- la conformité ;
- l’assurance ;
- la gouvernance ;
- l’orchestration ;
- le diagnostic ;
- l’aide à la décision ;
- la garantie de changement.

Cette séparation protège la neutralité de la mesure et permet à plusieurs infrastructures de consommer le même signal selon leurs propres règles.

---

## Principe fondateur

> **Une primitive de mesure. Plusieurs applications.**

> **Votre système. Vos décisions. Notre signal de mesure.**

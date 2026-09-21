# NeoMundi Runtime Measurement Layer

[🇬🇧 English](./README.md) ·
[🇫🇷 Français](./README_FR.md)

## Mesurez le comportement de l’IA avec un contexte réutilisable

NeoMundi mesure l’état comportemental observable d’un système d’IA à un
instant donné et renvoie un signal de mesure structuré, horodaté et comparable.

Ce signal contextualise les observations, détections, audits, diagnostics,
comparaisons, évaluations assurantielles et éléments de preuve, sans remplacer
l’infrastructure, les règles ni les mécanismes de décision du système qui le
consomme.

**Intégrez une fois. Renforcez plusieurs usages en aval.**

> **Votre système. Vos décisions. Notre signal de mesure.**

### Obtenez votre première mesure

1. **Créez votre compte et votre clé API NeoMundi**  
   [Ouvrir la plateforme NeoMundi →](https://controltower.neomundi.io/welcome)

2. **Connectez votre système à l’API de mesure**  
   Commencez par le [Quickstart](./QUICKSTART.md), puis consultez le
   [guide d’intégration API](./API_INTEGRATION_GUIDE.md) pour les endpoints,
   l’authentification, les payloads et la gestion des erreurs.

3. **Recevez et conservez la mesure**  
   Conservez l’identifiant renvoyé et l’enregistrement de mesure. Lorsqu’un autre
   système doit consommer le signal, utilisez la
   [documentation d’interopérabilité](./docs/INTEROPERABILITY.md) et les schémas
   JSON versionnés du répertoire [`schema/`](./schema/).

**Une API de mesure · Infrastructure existante préservée · Sortie lisible par machine**

**Privacy by design · Les clés NeoMundi et fournisseur restent distinctes**

En mode d’observation directe, votre système appelle son fournisseur d’IA et
transmet l’exécution observée à NeoMundi pour la mesurer. Un parcours de streaming
distinct est disponible lorsque NeoMundi orchestre la génération du fournisseur.

~~~text
Système d’IA
    │
    ▼
API de mesure NeoMundi
    │
    ▼
Signal de mesure structuré
    │
    ▼
Contrat JSON interopérable
    │
    ▼
Système client ou partenaire
~~~

---

## Ce que fait NeoMundi

### Mesure en cours d’exécution

NeoMundi observe le comportement d’un système d’IA pendant ou après son
exécution, dans des conditions déclarées.

La mesure décrit ce qui a été observé dans un contexte précis. Elle ne définit
pas un état absolu ou permanent du système.

### Signaux comportementaux et opérationnels

La couche peut produire différents signaux, notamment :

- `stability_score` ;
- `coherence_score` ;
- `factual_validity_signal` ;
- `semantic_variability_signal` ;
- `risk_signal`.

La définition, la portée et les limites de chaque signal sont documentées dans
le [contrat de mesure](./docs/MEASUREMENT_CONTRACT.md).

### Sémantique définie

Chaque signal est accompagné d’une définition explicite.

La documentation précise :

- ce que le signal mesure ;
- les conditions dans lesquelles il a été produit ;
- la manière dont il peut être interprété ;
- ce qui ne peut pas en être conclu.

Les règles correspondantes sont disponibles dans la
[table d’interprétation des mesures](./docs/MEASUREMENT_INTERPRETATION_TABLE.md).

### Reproductibilité

Les conditions de mesure, le protocole et les versions applicables sont
déclarés.

Une mesure peut donc être :

- reproduite ;
- comparée ;
- vérifiée ;
- contestée de manière indépendante.

### Comparabilité dans le temps

Les mesures incluent des informations de version explicites.

Il est ainsi possible de distinguer :

- la version du schéma ;
- la version de la métrique ;
- la version du normaliseur.

Les observations historiques restent donc interprétables à mesure que le
contrat évolue.

Consultez la
[documentation sur le versionnement](./VERSIONING.md).

### Traçabilité

Les identifiants, horodatages et informations de provenance relient chaque
mesure à l’observation qui l’a produite.

### Interopérabilité

Les mesures sont exposées sous forme d’enregistrements structurés et lisibles
par machine.

Le contrat interopérable permet aux infrastructures clientes de recevoir,
conserver, échanger et utiliser le signal sans devenir des systèmes NeoMundi.

Consultez la
[documentation d’interopérabilité](./docs/INTEROPERABILITY.md).

### Vérifiabilité indépendante

Lorsque ces éléments sont produits, l’enregistrement peut contenir :

- une empreinte cryptographique du contenu ;
- une signature vérifiable ;
- les informations nécessaires pour vérifier son intégrité.

Un tiers peut ainsi vérifier l’intégrité d’un enregistrement sans avoir à faire
confiance à l’infrastructure de NeoMundi.

---

## Ce que produit NeoMundi

NeoMundi produit un contexte comportemental mesuré, structuré et lisible par
machine.

### Signaux de mesure

Les signaux décrivent le comportement observé du système d’IA dans les
conditions déclarées.

Ils peuvent inclure des informations sur :

- la stabilité ;
- la cohérence ;
- la validité factuelle ;
- la variabilité sémantique ;
- le risque observé.

### Enregistrements structurés

Chaque mesure peut être reliée à :

- une requête ;
- une observation ;
- un système ;
- un instant précis ;
- un protocole déclaré.

### Informations de version

L’enregistrement distingue les versions du schéma, de la métrique et du
mécanisme de normalisation.

### Informations de provenance

La provenance indique ce qui a produit la mesure et selon quel protocole.

### Informations d’intégrité

L’enregistrement peut contenir une empreinte du contenu et une signature
cryptographique vérifiable.

### Un contrat JSON interopérable

Les mesures peuvent être exposées dans un format structuré, versionné et
lisible par machine.

Les schémas sont disponibles dans le répertoire
[`schema`](./schema/).

---

## Pourquoi ce contexte est important

Une observation brute ne suffit pas toujours à comprendre l’état
comportemental du système qui l’a produite.

NeoMundi ajoute le contexte de mesure nécessaire pour interpréter cette
observation à un instant précis.

Une même primitive de mesure peut servir à plusieurs usages en aval :

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
- création d’éléments de preuve.

Ces usages sont construits et exploités par le système consommateur.

NeoMundi fournit le signal de mesure. Le système consommateur conserve son
architecture, ses règles et son autorité de décision.

> **Une primitive de mesure. Plusieurs applications.**
>
> **Plusieurs infrastructures, sans les remplacer.**

---

## Comment intégrer NeoMundi

L’intégration repose sur l’API NeoMundi et sur un contrat d’interopérabilité
versionné qui permettent à différentes infrastructures de consommer le même
signal de mesure.

### Quickstart

[**Activez la couche et obtenez votre première mesure →**](./QUICKSTART.md)

Le guide Quickstart présente le chemin le plus court pour connecter un système
et obtenir une première mesure.

### Guide d’intégration API

Le
[guide d’intégration API](./API_INTEGRATION_GUIDE.md)
décrit :

- les endpoints ;
- les payloads ;
- les headers ;
- l’authentification ;
- la gestion des erreurs ;
- le traitement des réponses.

### Contrat de mesure

Le
[contrat de mesure](./docs/MEASUREMENT_CONTRACT.md)
définit la signification, la portée et les limites des signaux.

### Table d’interprétation

La
[table d’interprétation des mesures](./docs/MEASUREMENT_INTERPRETATION_TABLE.md)
indique ce qui peut et ne peut pas être conclu d’un signal.

### Contrat d’interopérabilité

La
[documentation d’interopérabilité](./docs/INTEROPERABILITY.md)
décrit la structure, le versionnement, la provenance et l’échange de la mesure.

---

## Limite architecturale

> **NeoMundi mesure.**
>
> **Le système consommateur interprète, gouverne et agit.**

**Mesure ≠ Interprétation ≠ Politique ≠ Exécution**

La NeoMundi Runtime Measurement Layer n’est pas :

- une plateforme de gouvernance de l’IA ;
- un moteur de conformité ;
- un moteur de politiques ;
- un moteur de décision ;
- un tableau de bord de supervision ;
- une application métier ;
- un mécanisme autonome de blocage ou d’autorisation.

NeoMundi ne décide pas :

- `ALLOW` ;
- `BLOCK` ;
- `STOP` ;
- `ROUTE` ;
- ni aucune autre conséquence opérationnelle.

Une mesure NeoMundi ne constitue pas, à elle seule, une preuve de vérité, de
sécurité, de conformité ou d’admissibilité.

Elle fournit un contexte comportemental indépendant, horodaté, traçable et
comparable qui peut renforcer les systèmes responsables de ces fonctions.

Consultez la documentation sur les
[limites du système consommateur](./docs/CONSUMER_BOUNDARIES.md).

---

## Principes d’intégration

### Infrastructure préservée

NeoMundi s’intègre à l’infrastructure existante sans exiger son remplacement.

### Responsabilité préservée

Le système consommateur conserve :

- ses règles ;
- ses seuils ;
- ses politiques ;
- ses décisions ;
- ses actions.

### Privacy by design

L’intégration est conçue pour limiter les échanges aux éléments nécessaires à
la mesure.

### Bring your own keys

Le système consommateur conserve le contrôle de ses clés et de ses accès aux
fournisseurs.

### Consommation indépendante

Le même signal peut être consommé par plusieurs infrastructures sans imposer
un modèle de gouvernance ou une interprétation partagés.

---

## Documentation

### Commencer

[QUICKSTART.md](./QUICKSTART.md)

Activez la couche et obtenez une première mesure.

### Intégrer l’API

[API_INTEGRATION_GUIDE.md](./API_INTEGRATION_GUIDE.md)

Comprenez les endpoints, les payloads, les headers et les mécanismes de gestion
des erreurs.

### Comprendre les mesures

[docs/MEASUREMENT_CONTRACT.md](./docs/MEASUREMENT_CONTRACT.md)

Comprenez la signification, la portée et les limites de chaque mesure.

### Interpréter les signaux

[docs/MEASUREMENT_INTERPRETATION_TABLE.md](./docs/MEASUREMENT_INTERPRETATION_TABLE.md)

Identifiez ce qui peut et ne peut pas être conclu d’un signal.

### Consommer le contrat interopérable

[docs/INTEROPERABILITY.md](./docs/INTEROPERABILITY.md)

Comprenez la structure, le versionnement, la provenance et l’échange des
mesures.

### Respecter les limites d’utilisation

[docs/CONSUMER_BOUNDARIES.md](./docs/CONSUMER_BOUNDARIES.md)

Distinguez la mesure, l’interprétation, les politiques et l’exécution.

### Comprendre le versionnement

[VERSIONING.md](./VERSIONING.md)

Distinguez les versions du schéma, de la métrique et du normaliseur.

### Consulter les évolutions du produit

[CHANGELOG.md](./CHANGELOG.md)

Consultez l’historique des évolutions du produit.

---

## Architecture du produit

Ce dépôt contient uniquement la primitive de mesure NeoMundi.

Les couches qui interprètent la mesure ou agissent à partir du signal sont
intentionnellement séparées.

~~~text
NeoMundi Runtime Measurement Layer
              │
              ▼
Signal de mesure interopérable
              │
              ▼
Systèmes clients et partenaires
              │
              ▼
Interprétation · Politique · Décision · Action
~~~

Ces applications peuvent notamment concerner :

- la conformité ;
- l’assurance ;
- la gouvernance ;
- l’orchestration ;
- le diagnostic ;
- l’aide à la décision ;
- l’assurance des changements.

Cette séparation protège la neutralité de la mesure et permet à plusieurs
infrastructures de consommer le même signal selon leurs propres règles.

---

## Principe fondateur

> **Une primitive de mesure. Plusieurs applications.**
>
> **Votre système. Vos décisions. Notre signal de mesure.**

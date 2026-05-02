---
title: "Veille Souveraineté Numérique"
layout: single
permalink: /watch/souverainete/
classes: wide
author_profile: true
read_time: true
show_date: false
toc: true
toc_label: "Contenu"
---

## <i class="fa-solid fa-flag"></i> Souveraineté numérique
La dépendance technologique vis-à-vis des GAFAM n'est plus seulement un débat politique : elle est devenue un risque opérationnel concret, accéléré par les tensions géopolitiques entre l'Europe et les États-Unis.

Cette section présente une synthèse des principales initiatives et tendances identifiées au cours de ma veille sur la période **septembre 2024 – avril 2026**, centrée sur les réponses françaises et européennes à cette dépendance.

---

### <i class="fa-solid fa-fire"></i> Actualités et tendances récentes

- **Sécurix et Bureautix : l'État développe son propre OS Linux**  
  La DINUM a publié Sécurix, un système d'exploitation basé sur NixOS, conçu pour les postes d'administration, durcis selon les recommandations de l'ANSSI. Authentification FIDO2, TPM2, chiffrement via Secure Boot, système de fichiers racine en lecture seule : le projet vise une configuration reproductible et maîtrisée, dans l'esprit Infrastructure-as-Code. Bureautix en est la déclinaison bureautique. Le projet est actuellement en version alpha.  
  → [it-connect.fr – Sécurix et Bureautix : le Linux de l'État pour remplacer Windows](https://www.it-connect.fr/securix-et-bureautix-le-linux-de-etat-pour-remplacer-windows/) *(avr. 2026)*  
  → [futura-sciences.com – La France prépare un remplaçant à Windows : derrière Sécurix](https://www.futura-sciences.com/tech/actualites/cybersecurite-france-prepare-remplacant-windows-derriere-securix-peur-devenue-tres-concrete-133770/) *(avr. 2026)*

- **LaSuite numérique : l'alternative collaborative de l'État**  
  Développée par la DINUM, LaSuite regroupe des outils souverains destinés à remplacer les solutions GAFAM dans les administrations : Visio (Teams/Zoom), Tchap (messagerie instantanée), Fichiers (Google Drive), FranceTransfert (WeTransfer). Visio est sorti de bêta début 2026 et a été généralisé à l'ensemble des agents publics en janvier 2026 après une expérimentation auprès de 40 000 utilisateurs. LaSuite revendique 500 000 utilisateurs. Le déploiement suscite un débat dans l'écosystème numérique privé, qui y voit une forme de concurrence déloyale.  
  → [lemagit.fr – Polémique autour de LaSuite : la DINUM se défend](https://www.lemagit.fr/actualites/366638848/Polemique-autour-de-LaSuite-la-DINUM-se-defend-et-ne-ferme-pas-la-porte-au-prive/) *(févr. 2026)*  
  → [goodtech.info – LaSuite numérique : le pari réussi de la souveraineté pour 2026](https://goodtech.info/la-suite-numerique-bilan-2025-ambitions-2026-souverainete/) *(janv. 2026)*

- **Mistral AI : le LLM souverain de l'État français**  
  Depuis octobre 2025, 10 000 agents publics répartis dans huit ministères testent un assistant conversationnel basé sur Mistral Medium 3, hébergé en France chez Outscale sur infrastructure SecNumCloud 3.2. En décembre 2025, le ministère des Armées a signé un accord-cadre triennal couvrant l'ensemble des forces armées, le CEA, l'ONERA et le SHOM. L'objectif explicite : éviter la dépendance aux fournisseurs américains soumis au CLOUD Act. Le datacenter propre de Mistral à Bruyères-le-Châtel (Essonne) doit entrer en service au deuxième trimestre 2026.  
  → [teriagen.com – Mistral AI et l'Assistant IA de l'État](https://teriagen.com/mistral-ai-et-lassistant-ia-de-letat-ce-que-les-collectivites-territoriales-doivent-savoir/) *(févr. 2026)*  
  → [clubic.com – Mistral AI, championne française de l'IA : souveraine, mais jusqu'à quel point ?](https://www.clubic.com/dossier-608152-mistral-ai-un-fleuron-souverain-avec-des-limites-bien-reelles.html) *(avr. 2026)*

- **Le CLOUD Act : le risque juridique qui accélère tout**  
  Le CLOUD Act américain (2018) contraint les entreprises technologiques américaines à fournir aux autorités américaines les données hébergées sur leurs serveurs, y compris celles situées en Europe. C'est ce risque juridique — pas seulement une question de principe — qui justifie la migration vers des solutions SecNumCloud, des LLMs hébergés en France et le développement d'un OS souverain. Le séminaire interministériel du 8 avril 2026, réunissant DINUM, ANSSI et DGE, a formalisé cette ambition au niveau gouvernemental.  
  → [vie-publique.fr – Quelle souveraineté numérique face aux États-Unis ?](https://www.vie-publique.fr/questions-reponses/301753-numerique-quelle-dependance-face-aux-etats-unis) *(janv. 2026)*  
  → [aladom.fr – Souveraineté numérique : la France passe de la parole aux actes](https://www.aladom.fr/actualites/secteur-service/11115/souverainete-numerique-la-france-passe-de-la-parole-aux-actes/) *(avr. 2026)*

---

### <i class="fa-solid fa-microchip"></i> Évolutions techniques notables

- **SecNumCloud** : qualification ANSSI pour les offres cloud souveraines — OVHcloud, Outscale (Dassault Systèmes) — garantissant que les données ne sont pas soumises à des législations extra-européennes
- **NixOS comme base d'OS d'État** : approche déclarative et reproductible, chaque poste déployé est identique à la configuration validée, sans dérive possible — une logique IaC appliquée au poste de travail
- **Open source comme levier de souveraineté** : Tchap (Matrix), Visio (LiveKit), Sécurix (NixOS) — mais l'open source ne garantit pas la souveraineté si les briques sous-jacentes dépendent de fondations américaines
- **LLM on-premise** : déploiement de modèles Mistral sur infrastructure locale ou SecNumCloud pour éviter que les données transitent par des serveurs tiers soumis au CLOUD Act
- **EU OS** : initiative communautaire européenne (non officielle UE) basée sur Fedora/KDE, visant à proposer une base commune pour les administrations européennes — projet encore au stade proof-of-concept

---

### <i class="fa-solid fa-user-shield"></i> Impacts pour les entreprises et les administrations

- Chaque ministère est tenu de formaliser un plan de réduction de dépendance couvrant : poste de travail, outils collaboratifs, antivirus, IA, bases de données, virtualisation, équipements réseau
- L'utilisation de solutions GAFAM dans un contexte sensible (données RH, stratégiques, médicales) expose juridiquement à une communication forcée sous CLOUD Act sans recours possible pour l'hébergeur européen
- La migration vers Linux impose une requalification des administrateurs systèmes formés exclusivement sur des environnements Windows/Active Directory
- L'open source réduit la dépendance aux éditeurs, mais transfère le risque sur la capacité interne à maintenir, sécuriser et faire évoluer les solutions
- La souveraineté du logiciel ne résout pas la dépendance matérielle : les GPU nécessaires à l'IA souveraine sont quasi-exclusivement produits par NVIDIA (>90 % du marché), une entreprise américaine

---

### <i class="fa-solid fa-lightbulb"></i> Analyse personnelle

Ce sujet me parle directement. Travailler pendant des années dans un environnement où la sécurité des informations et la maîtrise des outils de communication sont des impératifs opérationnels donne une lecture très concrète du problème : une donnée hébergée chez un prestataire soumis à une législation étrangère n'est pas une donnée maîtrisée. Ce n'est pas un débat théorique.

Ce que je retiens de cette veille, c'est que la France a franchi un cap : elle est passée du discours à l'acte. Sécurix, LaSuite, Mistral déployé en SecNumCloud, plan interministériel de réduction des dépendances — les initiatives sont réelles et récentes. Mais les limites le sont aussi. Open source ne signifie pas indépendance si les composants sous-jacents échappent au contrôle national. Mistral est souverain sur le papier, mais ses modèles ont été entraînés sur les infrastructures de Microsoft Azure, et son premier actionnaire est néerlandais. Ce sont des nuances que je juge importantes à documenter, plutôt que de les effacer derrière un discours de façade.

Sur le plan technique, la migration Linux dans les administrations concerne directement le métier de technicien systèmes et réseaux. Remplacer un écosystème Windows/Active Directory/GPO par un environnement NixOS déclaratif, c'est une transformation profonde des pratiques d'administration. C'est un chantier que je suis avec intérêt, et qui renforce ma conviction que la polyvalence sur plusieurs systèmes d'exploitation est une nécessité, pas une option.

---

### <i class="fa-solid fa-rss"></i> Méthode de veille

Ma veille souveraineté numérique est organisée via **Feedly**, avec des flux couvrant les actualités institutionnelles et techniques :

| Flux | Thématique principale |
|------|-----------------------|
| [LeMagIT](https://www.lemagit.fr) | Stratégie numérique, DINUM, cloud souverain |
| [IT-Connect](https://www.it-connect.fr) | Outils, OS, migrations techniques |
| [ANSSI](https://cyber.gouv.fr) | SecNumCloud, référentiels, doctrine |
| [Le Monde Informatique](https://www.lemondeinformatique.fr) | Actualités IT, souveraineté, GAFAM |
| [ActuIA](https://www.actuia.com) | IA souveraine, Mistral, LLMs européens |
| [Korben](https://korben.info) | Open source, Linux, alternatives |

---

### <i class="fa-solid fa-link"></i> Sources citées dans cette veille

- [it-connect.fr – Sécurix et Bureautix, avr. 2026](https://www.it-connect.fr/securix-et-bureautix-le-linux-de-etat-pour-remplacer-windows/)
- [futura-sciences.com – La France prépare un remplaçant à Windows, avr. 2026](https://www.futura-sciences.com/tech/actualites/cybersecurite-france-prepare-remplacant-windows-derriere-securix-peur-devenue-tres-concrete-133770/)
- [informatiquenews.fr – La DINUM largue Windows en faveur de Linux, avr. 2026](https://www.informatiquenews.fr/la-dinum-largue-windows-en-faveur-de-linux-et-veut-enclencher-un-mouvement-de-fond-110959)
- [lemagit.fr – Polémique autour de LaSuite, févr. 2026](https://www.lemagit.fr/actualites/366638848/Polemique-autour-de-LaSuite-la-DINUM-se-defend-et-ne-ferme-pas-la-porte-au-prive/)
- [goodtech.info – LaSuite numérique bilan 2025, janv. 2026](https://goodtech.info/la-suite-numerique-bilan-2025-ambitions-2026-souverainete/)
- [teriagen.com – Mistral AI et l'Assistant IA de l'État, févr. 2026](https://teriagen.com/mistral-ai-et-lassistant-ia-de-letat-ce-que-les-collectivites-territoriales-doivent-savoir/)
- [clubic.com – Mistral AI souveraine, mais jusqu'à quel point ?, avr. 2026](https://www.clubic.com/dossier-608152-mistral-ai-un-fleuron-souverain-avec-des-limites-bien-reelles.html)
- [vie-publique.fr – Souveraineté numérique face aux États-Unis, janv. 2026](https://www.vie-publique.fr/questions-reponses/301753-numerique-quelle-dependance-face-aux-etats-unis)
- [aladom.fr – La France passe de la parole aux actes, avr. 2026](https://www.aladom.fr/actualites/secteur-service/11115/souverainete-numerique-la-france-passe-de-la-parole-aux-actes/)
- [paul.argoud.net – IA souveraine : pourquoi passer à l'open source local en 2026](https://paul.argoud.net/ia-souveraine-open-source-local-mistral-2026)

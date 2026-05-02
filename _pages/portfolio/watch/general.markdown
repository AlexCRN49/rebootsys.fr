---
title: "Veille Informatique Générale"
layout: single
permalink: /watch/general/
classes: wide
author_profile: true
read_time: true
show_date: true
toc: true
toc_label: "Contenu"
---

## <i class="fa-solid fa-computer"></i> Informatique générale

L'informatique n'a pas cessé d'évoluer depuis sa création, avec des innovations technologiques qui impactent les systèmes, les réseaux et les infrastructures.
Cette évolution et les choix qui en découlent sont aujourd'hui intimement liés au contexte géopolitique. La question de la **souveraineté numérique**, longtemps considérée comme un sujet secondaire, ne l'est plus. Dans un monde où les données sont des richesses convoitées, la dépendance à un acteur unique peut impacter l'activité d'une entreprise comme d'une nation.

Cette veille couvre la période **septembre 2024 – mai 2026**.


## <i class="fa-solid fa-fire"></i> Faits marquants

### L'IA comme accélérateur de tout le reste

L'impact et l'évolution de l'**IA** est probablement ce qui a le plus retenu mon attention sur ces deux ans. Non seulement comme outil d'optimisation, mais aussi comme moteur d'évolution du matériel. L'explosion des besoins en **RAM**, en **GPU** et en **bande passante** liée à l'IA générative a impacté les marchés mondiaux, jusqu'aux simples consommateurs.
La vitesse à laquelle l'IA est passée d'un sujet de laboratoire à un composant structurel de l'infrastructure informatique m'a particulièrement marqué. Bien au-delà d'un usage réservé aux développements, l'IA s'invite partout, y compris dans les systèmes et réseaux.

[blog.madrigan.com - Infrastructure Automation 2025 : GitOps, IDPs, AIOps](https://blog.madrigan.com/en/blog/202603291447/) *(mars 2026)*


### La fiabilité de Windows mise à mal

Sur ces deux ans, j'ai suivi avec attention la récurrence des problèmes liés aux **mises à jour Windows**, qui ne sont pas des faits isolés.

**Mars 2024** : la mise à jour Windows Server fait planter les contrôleurs de domaine à cause d'une fuite mémoire dans le processus **LSASS**, au point que certains redémarrent seuls pendant le week-end.

**Décembre 2024** : la **KB5048667** pour Windows 11 24H2 accumule les échecs d'installation, les ralentissements CPU et les écrans bleus.

**Août 2025** : une mise à jour casse l'outil **"Réinitialiser ce PC"**, Microsoft publie un correctif d'urgence qui ne s'installe pas automatiquement.

Le schéma est récurrent : mise à jour déployée, bug constaté, correctif hors bande publié en urgence, parfois des semaines après. La politique de Microsoft qui tend à l'intégration forcée de **Copilot**, la suppression de services, les paramètres déplacés à chaque version et la pression vers les abonnements **Azure** n'est pas populaire. La fin du support **Windows 10** en octobre 2025 a été vécue comme un ultimatum plutôt qu'une évolution.

[it-connect.fr - Windows Server : la mise à jour de mars 2024 fait planter les contrôleurs de domaine](https://www.it-connect.fr/mise-a-jour-mars-2024-windows-server-planter-et-redemarrer-controleurs-de-domaine/) *(mars 2024)*  
[it-connect.fr - Windows 11 KB5048667 : erreurs d'installation, problèmes de performance](https://www.it-connect.fr/windows-11-kb5048667-mise-a-jour-decembre-2024-erreurs-et-problemes/) *(déc. 2024)*  
[lecrabeinfo.net - La mise à jour d'août 2025 casse la réinitialisation Windows](https://lecrabeinfo.net/actualites/windows-11-et-10-la-mise-a-jour-daout-2025-casse-loutil-reinitialiser-ce-pc-microsoft-publie-un-correctif-durgence/) *(août 2025)*


### La montée de Linux et des alternatives open source

J'ai suivi avec intérêt la progression de **Linux** et des solutions **open source** comme alternatives aux solutions propriétaires. Ce n'est plus un choix militant ou économique uniquement — cela a évolué vers une réponse technique et stratégique à des questions de dépendance et de maîtrise des environnements. La généralisation du **cloud hybride** et du **multi-cloud** suit la même logique : éviter la dépendance, garder la maîtrise de ses données et de son environnement de travail.

Linux a franchi en juin 2025 la barre symbolique des **5% de parts de marché** aux États-Unis, son plus haut niveau jamais atteint. Il avait fallu huit ans pour passer de 1 à 2%, puis deux autres années pour atteindre 3%. Depuis, la dynamique s'est installée : 4% en sept mois, puis 5% quatre mois plus tard. En Europe, Linux atteint **5,23%** du marché. Ce n'est pas une révolution, mais c'est un signal que quelque chose change — et la lassitude croissante vis-à-vis de Windows n'y est pas étrangère.

[actdigital.com - 7 tendances de l'externalisation IT en 2025](https://actdigital.com/fr/insights/7-tendances-de-lexternalisation-it-en-2025/) *(févr. 2026)*  
[solutions-numeriques.com - Trois tendances qui redéfiniront les infrastructures Cloud en 2026](https://www.solutions-numeriques.com/avis-dexpert-trois-tendances-qui-redefiniront-les-infrastructures-cloud-des-entreprises-et-des-administrations-en-2026/) *(janv. 2026)*  
[lesnumeriques.com - Linux dépasse un seuil historique que Microsoft pensait intouchable](https://www.lesnumeriques.com/informatique/c-est-enfin-arrive-linux-depasse-un-seuil-historique-que-microsoft-pensait-intouchable-n239977.html) *(2025)*  
[minimachines.net - Avec 5% de parts de marché aux US, Linux est en grande forme](https://www.minimachines.net/actu/avec-5-de-parts-de-marche-aux-us-linux-est-en-grande-forme-135293) *(juil. 2025)*


### La souveraineté numérique

C'est le sujet qui, selon moi, a le plus évolué sur cette période. La dépendance technologique vis-à-vis des **GAFAM** n'est plus seulement un débat politique — elle est devenue un **risque opérationnel concret**, accéléré par les tensions géopolitiques entre l'Europe et les États-Unis.

Depuis début 2026, les choses se sont accélérées. La **DINUM** a publié **Sécurix**, un OS basé sur **NixOS** pour les postes d'administration, durci selon les recommandations de l'**ANSSI**. **LaSuite numérique** revendique 500 000 utilisateurs dans les administrations. 10 000 agents publics testent un assistant IA basé sur **Mistral**, hébergé en France sur infrastructure **SecNumCloud** pour éviter que les données ne soient soumises au **CLOUD Act** américain.

Je retiens que la France semble avoir franchi un cap sur ce sujet. Cependant, l'open source ne signifie pas indépendance si les composants sous-jacents échappent au contrôle national. Mistral est présenté comme souverain, mais ses modèles ont été entraînés sur l'infrastructure **Azure** de Microsoft, et son premier actionnaire est néerlandais. Ce sont des nuances importantes à appréhender.

Sur le plan technique, cette migration concerne directement le métier d'administrateur systèmes et réseaux. Remplacer un écosystème **Windows/Active Directory/GPO** par un environnement **NixOS** déclaratif constitue une transformation profonde des pratiques d'administration et d'utilisation que je suis avec intérêt.

[it-connect.fr - Sécurix et Bureautix : le Linux de l'État pour remplacer Windows](https://www.it-connect.fr/securix-et-bureautix-le-linux-de-etat-pour-remplacer-windows/) *(avr. 2026)*  
[lemagit.fr - Polémique autour de LaSuite : la DINUM se défend](https://www.lemagit.fr/actualites/366638848/Polemique-autour-de-LaSuite-la-DINUM-se-defend-et-ne-ferme-pas-la-porte-au-prive/) *(févr. 2026)*  
[clubic.com - Mistral AI souveraine, mais jusqu'à quel point ?](https://www.clubic.com/dossier-608152-mistral-ai-un-fleuron-souverain-avec-des-limites-bien-reelles.html) *(avr. 2026)*  
[vie-publique.fr - Quelle souveraineté numérique face aux États-Unis ?](https://www.vie-publique.fr/questions-reponses/301753-numerique-quelle-dependance-face-aux-etats-unis) *(janv. 2026)*

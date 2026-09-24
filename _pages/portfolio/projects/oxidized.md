---
title: "Sauvegarde centralisée et versionnée des équipements réseau avec Oxidized"
layout: single
date: 2026-09-24
permalink: /portfolio/projects/oxidized/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - Oxidized
  - Git
  - Zabbix
  - Sauvegarde
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Oxidized-424242?style=for-the-badge&logoColor=white" alt="Oxidized" style="height:41px;">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" style="height:41px;">
  <img src="https://img.shields.io/badge/Zabbix-D40000?style=for-the-badge&logo=zabbix&logoColor=white" alt="Zabbix" style="height:41px;">
</div>

## Cahier des charges

La perte de configuration d'un équipement cœur de réseau, à la suite d'une panne matérielle ou d'une erreur humaine, aurait pu paralyser l'entreprise. Il fallait une solution de sauvegarde automatique, centralisée et versionnée pour ces équipements.

## Solutions choisies

J'ai déployé Oxidized. Chaque modification de configuration génère un commit Git, ce qui permet de conserver un historique complet et de revenir en arrière à tout moment. Son architecture API-first m'a permis de l'interconnecter directement avec Zabbix, pour automatiser la vérification des sauvegardes.

## Mise en œuvre

**Environnement technique :**  
`Oxidized` - `Git` - `Zabbix`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-user-shield" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Installation d'Oxidized sur une VM dédiée</strong>, avec un utilisateur système sans droit d'administration locale
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-list" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Déclaration des équipements</strong> dans le fichier d'inventaire
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-code-branch" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Configuration du transfert automatique</strong> du dépôt Git local vers un dépôt distant privé, via un token d'accès personnel
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-plug" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Interconnexion avec Zabbix</strong>, via un élément de supervision interrogeant périodiquement le statut JSON d'Oxidized
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fab fa-js" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Développement d'un script de prétraitement</strong> dans Zabbix, avec l'aide d'un assistant IA, pour compter les équipements en échec à partir du JSON brut
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-bell" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Création d'un déclencheur d'alerte</strong> et d'un élément dépendant, pour identifier l'équipement en échec
    </div>
  </div>

</div>

## Tests et imprévus

Le test de récupération d'une configuration antérieure via l'historique Git a confirmé le bon fonctionnement du versioning. L'alerte Zabbix s'est déclenchée correctement lors d'une panne simulée d'un équipement, avec identification du bon équipement en échec sur le tableau de bord.

## Bilan

Oxidized transforme une sauvegarde de configuration en historique consultable, un peu à la manière de Time Machine. Le passage par un jeton d'accès personnel plutôt qu'une clé SSH a permis de contourner un bug documenté de la librairie interne d'Oxidized, sans perdre en fiabilité lors de transfert vers le dépôt distant.

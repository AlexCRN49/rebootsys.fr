---
title: "Externalisation chiffrée des sauvegardes avec Restic"
layout: single
date: 2026-09-24
permalink: /portfolio/projects/resticrepo/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - Restic
  - Sauvegarde
  - SFTP
  - Chiffrement
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Restic-424242?style=for-the-badge&logoColor=white" alt="Restic" style="height:41px;">
  <img src="https://img.shields.io/badge/SFTP-424242?style=for-the-badge&logoColor=white" alt="SFTP" style="height:41px;">
  <img src="https://img.shields.io/badge/AES--256-424242?style=for-the-badge&logoColor=white" alt="AES-256" style="height:41px;">
</div>

## Cahier des charges

Pour garantir la pérennité de l'infrastructure en cas de sinistre majeur sur le site principal, il fallait une solution de sauvegarde externalisée et chiffrée. Cette solution devait rester complémentaire aux outils de sauvegarde locaux déjà en place.

## Solutions choisies

J'ai déployé Restic en mode Push vers un dépôt hébergé sur un serveur Cloud externe. Chaque fichier est chiffré en AES-256 côté client avant de transiter sur le réseau. Le serveur distant ne stocke que des blocs illisibles sans la clé maître. La déduplication à la source limite la consommation de bande passante et les coûts de stockage. Contrairement à un snapshot complet, Restic permet de restaurer un seul fichier en quelques secondes.

## Mise en œuvre

**Environnement technique :**  
`Restic` - `SFTP` - `AES-256` - `Zabbix`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-download" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Déploiement du binaire Restic</strong> localement sur chaque serveur à sauvegarder
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-cloud" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Initialisation du dépôt</strong> sur le serveur Cloud, via le protocole SFTP
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-lock" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Stockage du mot de passe maître</strong> dans un fichier local aux droits stricts, pour permettre l'automatisation
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-tags" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Structuration des sauvegardes par étiquettes</strong>, afin de permettre une restauration ciblée sur un seul service
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-clock" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Planification d'une tâche nocturne quotidienne</strong>, avec une politique de rétention sur 7 jours, 4 semaines et 6 mois
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-bell" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Intégration à la supervision Zabbix</strong>, avec une alerte si le journal de sauvegarde reste inchangé depuis plus de 24 heures
    </div>
  </div>

</div>

## Tests et imprévus

Le test de restauration ciblée sur un seul tag a confirmé qu'il était possible de récupérer un fichier de configuration précis sans toucher aux autres sauvegardes du même dépôt. L'alerte Zabbix s'est également déclenchée correctement lors d'un test d'absence de sauvegarde simulée.

## Bilan

Restic complète les sauvegardes locales par une copie externalisée et chiffrée, pensée pour la restauration fine plutôt que pour la reprise complète d'une machine. Combiné à cette solution complémentaire, le chiffrement systématique et la déduplication à la source permettent d'avoir une vraie politique de sauvegarde 3-2-1-1-0.

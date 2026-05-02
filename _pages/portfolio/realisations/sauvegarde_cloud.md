---
title: "Mise en place d'un dispositif de redondance locale pour les données stockées en environnement Cloud"
layout: single
date: 2025-03-10
permalink: /portfolio/realisations/synchronisation/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Réalisations
tags:
  - TrueNAS
  - Rclone
  - Google Drive
  - Sauvegarde
  - Cron
  - LXC
  - Proxmox
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/TrueNAS-0095D5?style=for-the-badge&logo=truenas&logoColor=white" alt="TrueNAS" style="height:45px;">
  <img src="https://img.shields.io/badge/Proxmox-E57000?style=for-the-badge&logo=proxmox&logoColor=white" alt="Proxmox" style="height:45px;">
  <img src="https://img.shields.io/badge/Rclone-3F79AD?style=for-the-badge&logo=rclone&logoColor=white" alt="Rclone" style="height:45px;">
  <img src="https://img.shields.io/badge/Google_Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white" alt="Google Drive" style="height:45px;">
</div>

## Cahier des charges

Dans le cadre de la politique de sauvegarde de l'entreprise, il a été décidé de mettre en place une copie locale des données hébergées sur Google Drive, afin de garantir leur disponibilité indépendamment du Cloud et de réduire l'exposition aux risques liés à la dépendance à un service tiers.

## Analyse du besoin

- Disposer d'une **copie locale** des données Google Drive, **indépendante** du Cloud ;
- **Automatiser la synchronisation** pour garantir la fraîcheur des sauvegardes sans intervention manuelle ;
- S'appuyer sur l'infrastructure existante (Proxmox, TrueNAS) pour limiter les coûts.

## Solutions choisies

**Rclone**, déployé dans un conteneur **LXC hébergé sur Proxmox VE**, est configuré avec une **clé API Google Drive** pour accéder aux données du **Cloud**. Un point de **montage NFS** relie le conteneur LXC au serveur **TrueNAS Scale**, assurant le **stockage centralisé** des sauvegardes. Une **tâche Cron** automatise l'exécution hebdomadaire du script de synchronisation.

## Gestion de projet

### Diagramme de Gantt

![Gantt sauvegarde cloud](/assets/images/projects/backup/gantt.png)

## Mise en œuvre

**Environnement technique :**  
`Proxmox VE` - `LXC` - `Rclone` - `Google Drive API` - `TrueNAS Scale` - `Cron`

**Période :** 10/03/2025 – 20/06/2025

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <!-- Étape 1 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-server" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Préparation et déploiement du serveur TrueNAS Core</strong>
    </div>
  </div>

  <!-- Étape 2 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-exchange-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Migration TrueNAS Core → TrueNAS Scale</strong>
    </div>
  </div>

  <!-- Étape 3 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-cube" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Déploiement de Rclone</strong> dans un conteneur LXC sur Proxmox
    </div>
  </div>

  <!-- Étape 4 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-network-wired" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Configuration du point de montage NFS</strong> entre le conteneur LXC et TrueNAS
    </div>
  </div>

  <!-- Étape 5 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fab fa-google-drive" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Configuration de l'accès API Google Drive</strong> pour Rclone
    </div>
  </div>

  <!-- Étape 6 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-terminal" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Rédaction du script de sauvegarde</strong> et automatisation via tâche Cron
    </div>
  </div>

  <!-- Étape 7 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-vial" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>7. Tests de synchronisation</strong> et vérification de l'intégrité des données
    </div>
  </div>

  <!-- Étape 8 -->
  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-file-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>8. Documentation</strong>
    </div>
  </div>

</div>

## Productions associées

| Document | Description |
|----------|-------------|
| [Procédure de configuration Rclone](/assets/docs/backup/rclone_config.pdf) | Authentification Google Drive API et paramétrage Rclone |
| [Script de synchronisation](/assets/docs/backup/sync_sh.pdf) | Script d'automatisation shell déclenché par Cron |
| [Déploiement TrueNAS et configuration NFS](/assets/docs/backup/truenas_installation.pdf) | Déploiement TrueNAS Core et configuration du partage NFS vers Proxmox |

## Bilan

Ce projet a permis de mettre en place une politique de sauvegarde automatisée des données Cloud, en s'appuyant sur l'infrastructure existante. La principale complexité a résidé dans la configuration du point de montage NFS entre le conteneur LXC et TrueNAS, ainsi que dans la gestion des droits d'accès associés. Une fois opérationnel, le dispositif fonctionne de manière entièrement autonome.

---
title: "Mise en place d'un cluster de virtualisation Proxmox et d'un gestionnaire de sauvegarde automatisé"
layout: single
date: 2024-11-12
permalink: /portfolio/realisations/proxmox/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Réalisations
tags:
  - Proxmox
  - Cluster HA
  - Virtualisation
  - Haute disponibilité
  - PBS
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Proxmox-E57000?style=for-the-badge&logo=proxmox&logoColor=white" alt="Proxmox VE" style="height:41px;">
  <img src="https://img.shields.io/badge/Cluster_HA-E57000?style=for-the-badge&logoColor=white" alt="Cluster HA" style="height:41px;">
  <img src="https://img.shields.io/badge/Corosync_/_Quorum-555555?style=for-the-badge&logoColor=white" alt="Corosync Quorum" style="height:41px;">
  <img src="https://img.shields.io/badge/Proxmox_Backup_Server-E57000?style=for-the-badge&logo=proxmox&logoColor=white" alt="PBS" style="height:41px;">
</div>

## Cahier des charges

L'infrastructure de virtualisation reposait sur un hyperviseur Proxmox VE unique, sans mécanisme de tolérance aux pannes. Une défaillance du nœud entraînait l'arrêt de l'ensemble des VMs et CTs hébergés. Pour pallier ce risque, un cluster à haute disponibilité (HA) devait être mis en place.

## Analyse du besoin

- Mise en place d'une solution de **haute disponibilité** ;
- Garantir la **tolérance de panne** et la **continuité de service**.

## Solutions choisies

**Cluster Proxmox à deux nœuds**, sans stockage partagé centralisé, avec un **Quorum device** pour assurer l'intégrité des décisions de basculement. **Proxmox Backup Server** pour garantir la sauvegarde et la restauration rapide des services.

## Gestion de projet

### Diagramme de Gantt

![Gantt Proxmox cluster](/assets/images/projects/proxmox/gantt.png)

## Mise en œuvre

**Période :** 12/11/2024 – 15/11/2024 &nbsp;&nbsp;&nbsp; 25/11/2024 – 29/11/2024

**Environnement technique :**  
`Proxmox VE` - `Cluster HA` - `Corosync / Quorum` - `PBS`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <!-- Étape 1 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-server" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Préparation du serveur</strong> hébergeant le second nœud Proxmox VE
    </div>
  </div>

  <!-- Étape 2 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-download" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Déploiement de Proxmox VE</strong> sur le second nœud
    </div>
  </div>

  <!-- Étape 3 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-project-diagram" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Mise en cluster</strong> des deux nœuds Proxmox VE
    </div>
  </div>

  <!-- Étape 4 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-balance-scale" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Configuration du Quorum device</strong> sur un serveur tiers
    </div>
  </div>

  <!-- Étape 5 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-server" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Préparation du serveur</strong> hébergeant Proxmox Backup Server
    </div>
  </div>

  <!-- Étape 6 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-database" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Déploiement de Proxmox Backup Server</strong>
    </div>
  </div>

  <!-- Étape 7 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-link" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>7. Configuration de l'association</strong> Proxmox VE / Proxmox Backup Server
    </div>
  </div>

  <!-- Étape 8 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-clock" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>8. Configuration de la tâche de sauvegarde</strong> et vérification automatisée
    </div>
  </div>

  <!-- Étape 9 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-vial" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>9. Tests</strong> de tolérance de panne, de sauvegarde et de restauration
    </div>
  </div>

  <!-- Étape 10 -->
  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-file-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>10. Documentation</strong>
    </div>
  </div>

</div>

## Productions associées

| Document | Description |
|----------|-------------|
| [Procédure de mise en place du cluster](/assets/docs/proxmox/proxmox_installation.pdf) | Installation d'un nœud PVE et configuration du cluster HA |
| [Procédure de mise en place du Quorum](/assets/docs/proxmox/quorum_installation.pdf) | Configuration du Quorum Corosync |
| [Procédure de mise en place de PBS](/assets/docs/proxmox/pbs_installation.pdf) | Installation et configuration du gestionnaire de sauvegarde |

## Bilan

La mise en place du cluster HA et de Proxmox Backup Server a permis de répondre aux deux exigences de l'infrastructure. La continuité de service en cas de défaillance d'un nœud est assurée par le mécanisme de basculement automatique géré par le Quorum. La protection des données par l'automatisation des sauvegardes via PBS. Ces deux éléments complémentaires contribue à la résilience de l'infrastructure virtualisée.

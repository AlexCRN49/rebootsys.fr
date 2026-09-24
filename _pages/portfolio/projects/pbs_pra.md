---
title: "Stratégie de sauvegarde centralisée et PRA avec Proxmox Backup Server"
layout: single
date: 2026-09-23
permalink: /portfolio/projects/pbs_pra/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - Proxmox Backup Server
  - PRA
  - Sauvegarde
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Proxmox_Backup_Server-E57000?style=for-the-badge&logo=proxmox&logoColor=white" alt="Proxmox Backup Server" style="height:41px;">
  <img src="https://img.shields.io/badge/PRA-424242?style=for-the-badge&logoColor=white" alt="PRA" style="height:41px;">
</div>

## Cahier des charges

L'infrastructure virtuelle hébergeait des services critiques (annuaire, bases de données, applications métier). Il fallait pallier le risque d'atteinte à l'intégrité de ces services et de leurs données. L'architecture nécessitait une solution capable de sauvegarder des machines entières sans impacter la production.

## Solutions choisies

J'ai choisi Proxmox Backup Server plutôt que les dumps natifs de Proxmox, peu adaptés à des fichiers volumineux. PBS fonctionne au niveau bloc. Après une première sauvegarde complète, il ne transfère que les blocs modifiés, ce qui réduit l'espace de stockage utilisé et le temps de sauvegarde. J'ai isolé les flux de sauvegarde sur un réseau dédié, pour ne pas saturer le réseau de production.

## Mise en œuvre

**Environnement technique :**  
`Proxmox Backup Server` - `VLAN` - `Fail2ban`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-download" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Installation du serveur Proxmox Backup Server</strong>
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-network-wired" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Création d'une interface réseau dédiée</strong> aux sauvegardes, pour un lien direct avec le serveur PBS sans passer par le routeur virtuel
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-hdd" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Provisionnement du disque de sauvegarde</strong>, distinct du disque système
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-lock" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Durcissement du serveur</strong>
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-link" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Liaison du cluster Proxmox au serveur PBS</strong>, via un utilisateur aux droits restreints
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-clock" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Planification des tâches</strong> de sauvegarde nocturne, de nettoyage selon la politique de rétention, et de vérification hebdomadaire de l'intégrité des blocs
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-copy" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>7. Déploiement d'un second serveur PBS indépendant</strong>, synchronisé par tirage incrémental pour dupliquer physiquement l'archive
    </div>
  </div>

</div>

## Tests et imprévus

Le test de restauration a confirmé la récupération complète d'une machine virtuelle depuis une sauvegarde. La tâche de vérification hebdomadaire a permis de contrôler l'intégrité des blocs sur la durée, et la synchronisation entre les deux serveurs PBS a été validée après plusieurs cycles.

## Bilan

La sauvegarde incrémentielle au niveau bloc économise un espace de stockage conséquent par rapport à des sauvegardes complètes répétées. Le second serveur PBS, alimenté par synchronisation incrémentale, duplique physiquement l'archive sur un support autonome. L'architecture répond ainsi à la fois au besoin de sauvegarde courante et à un plan de reprise d'activité en cas de perte du premier serveur.

---
title: "Centralisation de l'administration à distance"
layout: single
date: 2026-09-22
permalink: /portfolio/achievements/guacamole_pdm/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Réalisations
tags:
  - Guacamole
  - Proxmox Datacenter Manager
  - Administration
  - Sécurisation
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Guacamole-424242?style=for-the-badge&logoColor=white" alt="Guacamole" style="height:41px;">
  <img src="https://img.shields.io/badge/Proxmox_Datacenter_Manager-E57000?style=for-the-badge&logo=proxmox&logoColor=white" alt="Proxmox Datacenter Manager" style="height:41px;">
  <img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white" alt="MariaDB" style="height:41px;">
</div>

## Cahier des charges

L'administration à distance des serveurs reposait soit via des connexions directes, soit via l'interface webUI. Concernant les nœuds Proxmox et le serveur de sauvegarde, ils étaient gérés indépendamment, sans vue d'ensemble centralisée.

## Analyse du besoin

- Centraliser l'accès distant aux serveurs, sans exposer directement les ports ;
- Disposer d'un **tableau de bord unique** pour piloter les nœuds Proxmox et le serveur de sauvegarde, facilitant l'administration ;
- Appliquer le **principe du moindre privilège**.

## Solutions choisies

**Apache Guacamole**, bastion web sans client lourd, pour l'accès RDP/SSH depuis un navigateur.
**Proxmox Datacenter Manager**, pour l'administration centralisée des nœuds Proxmox VE et du serveur PBS depuis une interface unique.

## Mise en œuvre

**Environnement technique :**  
`Guacamole` - `Docker` - `MariaDB` - `Proxmox Datacenter Manager`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fab fa-docker" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Déploiement de Guacamole</strong> en conteneur Docker
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-database" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Création de la base MariaDB dédiée</strong> sur une VM Proxmox distincte
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-diagram-project" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Publication derrière le reverse proxy Caddy</strong>, avec certificat dédié
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-key" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Configuration de l'authentification native</strong> de Guacamole
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-download" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Mise en place de Proxmox Datacenter Manager</strong>
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-server" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Ajout des nœuds Proxmox VE et du serveur PBS</strong> au tableau de bord
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-file-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>7. Documentation</strong>
    </div>
  </div>

</div>

## Productions associées

| Document | Description |
|----------|-------------|
| [Procédure d'installation de Proxmox Datacenter Manager](/assets/docs/proxmox/pdm_installation.pdf) | Installation et configuration de PDM |

## Bilan

Guacamole supprime l'exposition directe des ports RDP/SSH sur le réseau tout en conservant un accès simple, depuis un navigateur web. Proxmox Datacenter Manager apporte la vue d'ensemble qui manquait sur le cluster de nœuds Proxmox et le serveur de sauvegarde. Les deux outils sont complémentaires et permettent donc de centraliser l'administration en limitant les accès à privilèges élevés.

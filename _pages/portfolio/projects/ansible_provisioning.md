---
title: "Provisionnement automatisé et idempotent avec Ansible"
layout: single
date: 2026-09-24
permalink: /portfolio/projects/ansible_provisioning/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - Ansible
  - Proxmox
  - Infrastructure as Code
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white" alt="Ansible" style="height:41px;">
  <img src="https://img.shields.io/badge/Proxmox-E57000?style=for-the-badge&logo=proxmox&logoColor=white" alt="Proxmox" style="height:41px;">
  <img src="https://img.shields.io/badge/Infrastructure_as_Code-424242?style=for-the-badge&logoColor=white" alt="Infrastructure as Code" style="height:41px;">
</div>

## Cahier des charges

Déployer des VMs et des conteneurs manuellement, de manière identique, est lent et source d'erreurs. L'objectif était d'industrialiser ce provisionnement, de façon reproductible et idempotente.

## Solutions choisies

J'ai choisi Ansible, un outil d'infrastructure as code déclaratif et sans agent. Le control node pilote les cibles Linux en SSH, les cibles Windows en WinRM, et Proxmox directement via son API REST. Les playbooks suivent la structure recommandée par Ansible, avec des dossiers dédiés à l'inventaire, aux playbooks et aux rôles. Les secrets sont chiffrés avec Ansible Vault.

## Mise en œuvre

**Environnement technique :**  
`Ansible` - `Proxmox` - `Cloud-Init` - `Ansible Vault`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-download" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Installation d'Ansible sur le control node</strong>
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-folder-tree" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Structuration du projet</strong> selon les bonnes pratiques Ansible (inventaire, playbooks, rôles)
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-key" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Chiffrement des secrets</strong> avec Ansible Vault
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-server" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Configuration du provisionnement des VMs</strong> via Cloud-Init au premier démarrage
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-cube" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Configuration du provisionnement des conteneurs LXC</strong>, avec une phase de post-installation en SSH pour compléter les limites de l'injection native Proxmox
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-list" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Enregistrement automatique</strong> des nouvelles machines dans l'inventaire opérationnel
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-check-double" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>7. Validation de la connectivité</strong> de l'ensemble des cibles, via les modules ping et win_ping
    </div>
  </div>

</div>

## Tests et imprévus

Le premier déploiement sur un cluster vide a confirmé l'état "changed" attendu. J'ai vérifié l'idempotence en relançant le même playbook sur un cluster partiellement déployé. Résultats : les conteneurs déjà conformes sont restés en état "ok", et seuls les nouveaux sont passés en "changed". La connectivité de l'ensemble des machines gérées a été validée. Cependant, WinRM peut se montrer capricieux, et pour éviter tout problème de connectivité, j'aurais dû l'intégrer à mon template Cloud-Init Windows.

## Bilan

Le playbook garantit un déploiement reproductible, avec une idempotence vérifiée en conditions réelles. Le pilotage reste aujourd'hui exclusivement en ligne de commande, ce qui limite la délégation à des profils moins techniques. Intégrer Semaphore UI apporterait un tableau de bord centralisé pour le lancement de playbooks, la gestion des inventaires et la planification.

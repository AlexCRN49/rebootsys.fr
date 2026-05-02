---
title: "Mise en œuvre d'une infrastructure de signature électronique auto-hébergée sous Docker"
layout: single
date: 2025-08-11
permalink: /portfolio/realisations/opensign/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Réalisations
tags:
  - OpenSign
  - Docker
  - Signature électronique
  - AWS
  - VPS
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" style="height:45px;">
  <img src="https://img.shields.io/badge/AWS_Lightsail-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS Lightsail" style="height:45px;">
  <img src="https://img.shields.io/badge/Debian-A81D33?style=for-the-badge&logo=debian&logoColor=white" alt="Debian" style="height:45px;">
  <img src="https://img.shields.io/badge/OpenSign-000000?style=for-the-badge&logoColor=white" alt="OpenSign" style="height:45px;">
</div>

## Cahier des charges

L'entreprise utilisait DocuSign comme solution de signature électronique, avec un coût proportionnel au nombre de signatures effectuées. Face à la hausse tarifaire et à l'impact financier croissant, il est apparu nécessaire de rechercher une solution plus adaptée.

## Analyse du besoin

- Remplacement d'une solution coûteuse par une solution **open-source** ;
- Gestion souveraine de la **dématérialisation sécurisée** des documents et des procédures de **signature électronique**.

## Solution choisie

**OpenSign** est une alternative open-source **auto-hébergée** à DocuSign, déployée via **Docker** sur un serveur VPS **AWS Lightsail**.

## Gestion de projet

### Diagramme de Gantt

![Gantt OpenSign](/assets/images/projects/opensign/gantt.png)

## Mise en œuvre

**Période :** 11/08/2025 – 14/08/2025

**Environnement technique :**  
`AWS Lightsail` - `Debian` - `Docker` - `OpenSign`

**Période :** 11/08/2025 – 14/08/2025

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <!-- Étape 1 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-search" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Recueil du besoin</strong> et analyse de la solution DocuSign existante
    </div>
  </div>

  <!-- Étape 2 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-balance-scale" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Identification et évaluation d'OpenSign</strong> comme alternative open-source
    </div>
  </div>

  <!-- Étape 3 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-flask" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Déploiement de test</strong> sur VM locale Proxmox
    </div>
  </div>

  <!-- Étape 4 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:1.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-cloud" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Commande et configuration du VPS</strong> AWS Lightsail (Debian, 2 vCPU, 2 Go RAM, 60 Go SSD)
    </div>
  </div>

  <!-- Étape 5 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fab fa-docker" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Installation et configuration d'OpenSign</strong> sur le VPS via Docker
    </div>
  </div>

  <!-- Étape 6 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-users-cog" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Coordination avec l'équipe de développement</strong> pour la configuration métier
    </div>
  </div>

  <!-- Étape 7 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-vial" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>7. Tests et validation</strong>
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
| [Procédure d'installation OpenSign](/assets/docs/opensign/opensign_installation.pdf) | Déploiement Docker et configuration initiale |


## Bilan

Le remplacement de DocuSign par OpenSign, solution open-source auto-hébergée, a permis de réduire significativement les coûts liés à la signature électronique. Le déploiement sur un VPS AWS Lightsail, précédé d'un test en environnement local sur Proxmox, a permis de valider la solution avant sa mise en production. La coordination avec l'équipe de développement pour la configuration métier a été l'occasion de travailler en mode projet avec des interlocuteurs techniques.

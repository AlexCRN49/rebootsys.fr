---
title: "Déploiement d'un environnement de conteneurisation Docker administré via Portainer"
layout: single
date: 2026-09-22
permalink: /portfolio/achievements/docker/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Réalisations
tags:
  - Docker
  - Portainer
  - Conteneurisation
  - Sécurisation
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" style="height:41px;">
  <img src="https://img.shields.io/badge/Portainer-13BEF9?style=for-the-badge&logo=portainer&logoColor=white" alt="Portainer" style="height:41px;">
  <img src="https://img.shields.io/badge/Fail2ban-000000?style=for-the-badge&logoColor=white" alt="Fail2ban" style="height:41px;">
  <img src="https://img.shields.io/badge/UFW-555555?style=for-the-badge&logoColor=white" alt="UFW" style="height:41px;">
</div>

## Cahier des charges

Plusieurs services internes devaient être hébergés (GLPI, Pi-hole, Stirling PDF, etc.) sans nécessité de provisionner une machine virtuelle dédiée à chacun, afin de s'adapter au besoin réel de chaque service et ainsi d'économiser les ressources. Une administration à distance complexe en ligne de commande (CLI) rendait par ailleurs la gestion quotidienne peu efficace.

## Analyse du besoin

- Mutualiser les ressources en hébergeant plusieurs services sur un socle unique **léger et isolé** ;
- Disposer d'une **interface d'administration centralisée**, accessible sans passer systématiquement par le CLI ;
- **Sécuriser** l'accès à cette interface, exposée en réseau interne.

## Solutions choisies

**Docker** comme moteur de conteneurisation, avec **Portainer** déployé en conteneur pour l'administration via une interface web.

## Mise en œuvre

**Environnement technique :**  
`Docker` - `Portainer` - `Fail2ban` - `UFW`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fab fa-docker" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Installation et configuration de Docker</strong>
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-box" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Déploiement de Portainer</strong>
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-key" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Durcissement des accès et de l'authentification</strong>
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-save" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Mise en place des sauvegardes</strong>
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-cubes" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Déploiement des services</strong> à partir de fichiers docker-compose
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-file-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Documentation</strong>
    </div>
  </div>

</div>

## Productions associées

| Document | Description |
|----------|-------------|
| [Procédure d'installation de Docker](/assets/docs/docker/docker_installation.pdf) | Installation de Docker sur un sevreur Linux dédié |
| [Procédure de gestion des logs Docker](/assets/docs/docker/docker_logs.pdf) | Configuration de la rotation des logs Docker |
| [Procédure de déploiement de Portainer](/assets/docs/docker/portainer_deploiement.pdf) | Déploiment de Portainer sur un Docker |
| [Procédure de sauvegarde d'une image Docker](/assets/docs/docker/docker_sauvegarde_image.pdf) | Sauvegarde d'image Docker |
| [Procédure de sauvegarde d'une base de données sur Docker](/assets/docs/docker/docker_sauvegarde_bdd.pdf) | Sauvegarde d'une base de données sur Docker |

## Bilan

La conteneurisation via Docker et Portainer a permis de mutualiser les ressources d'hébergement tout en simplifiant l'administration au quotidien grâce à une interface web centralisée. Le durcissement de l'accès et de l'authentuification répond à l'exigence de sécurisation d'un point d'administration exposé sur le réseau interne, et les procédures de sauvegarde mises en place garantissent la récupération des services en cas d'incident.

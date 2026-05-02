---
title: "Mise en place d'une plateforme de supervision proactive par intégration multiservice"
layout: single
date: 2026-02-01
permalink: /portfolio/realisations/supervision/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Formation
tags:
  - Zabbix
  - GLPI
  - Slack
  - Supervision
  - Webhook
  - Proxmox
  - LXC
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Zabbix-CC0000?style=for-the-badge&logo=zabbix&logoColor=white" alt="Zabbix" style="height:45px;">
  <img src="https://img.shields.io/badge/GLPI-000000?style=for-the-badge&logoColor=white" alt="GLPI" style="height:45px;">
  <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white" alt="Slack" style="height:45px;">
  <img src="https://img.shields.io/badge/Proxmox-E57000?style=for-the-badge&logo=proxmox&logoColor=white" alt="Proxmox" style="height:45px;">
</div>

## Contexte

Dans le cadre de mon apprentissage autonome, j'ai souhaité explorer les mécanismes d'interconnexion entre les services. L'objectif était de constituer une infrastructure de supervision cohérente, capable de détecter une anomalie, de créer automatiquement un ticket d'incident et d'alerter en temps réel et de manière autonome.

Cette réalisation a été menée sur l'infrastructure personnelle que j'ai notamment mise en place pour l'épreuve E6.

## Objectifs

- **Superviser** l'ensemble des serveurs et services de l'infrastructure via un **agent centralisé** ;
- **Automatiser** la création de **tickets d'incident** dans **GLPI** en fonction des seuils d'alerte Zabbix ;
- **Notifier** en temps réel via **Slack** lors du déclenchement d'une **alerte** ;
- Basculer vers une **gestion proactive** des incidents grâce à l'interaction entre les outils mis en place.

## Schéma d'infrastructure

![Schéma flux webhook Zabbix](/assets/images/picture/realisations/flux_webhook_zabbix.png){: style="max-width:100%;"}

## Solutions choisies

**Zabbix** assure la supervision de l'ensemble des serveurs et services via l'agent Zabbix (port 10050). Chaque hôte est monitoré en temps réel grâce au modèle natif.

**GLPI** centralise la gestion des incidents. Les alertes Zabbix déclenchent automatiquement la création d'un ticket par l'intermédiaire du webhook. À la résolution du problème dans Zabbix, le ticket est clôturé automatiquement.

**Slack** reçoit les notifications d'alertes et de résolution en temps réel dans un canal dédié (_#zabbix-alerts_).

L'interconnexion de ces trois outils en fait une solution de supervision proactive.

## Mise en œuvre

**Période :** 01/02/2026 - 24/03/2026

**Environnement technique :**  
`Proxmox VE` - `LXC` - `Zabbix` - `GLPI` - `Slack` - `Webhook`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <!-- Étape 1 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-server" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Déploiement de Zabbix Server</strong> sur une VM Proxmox dédiée (Debian)
    </div>
  </div>

  <!-- Étape 2 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:1.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-cube" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Déploiement des services</strong> dans des conteneurs LXC sur Proxmox (GLPI, Guacamole, Nextcloud)
    </div>
  </div>

  <!-- Étape 3 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:1.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-eye" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Déploiement des agents Zabbix</strong> sur l'ensemble des hôtes monitorés et <strong>configuration manuelle des hôtes sur le serveur Zabbix</strong>
    </div>
  </div>

  <!-- Étape 4 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-project-diagram" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Configuration des dépendances de triggers</strong>
    </div>
  </div>

  <!-- Étape 5 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-ticket-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Configuration du webhook Zabbix - GLPI</strong>
    </div>
  </div>

  <!-- Étape 6 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fab fa-slack" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Configuration du webhook Zabbix - Slack</strong>
    </div>
  </div>

  <!-- Étape 7 -->
  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-vial" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>7. Tests et validation</strong>
    </div>
  </div>

</div>

## Productions associées

| Document | Description |
|----------|-------------|
| [Procédure webhook Zabbix - GLPI](/assets/docs/zabbix/webhook_glpi.pdf) | Configuration du webhook GLPI pour ticketing |
| [Procédure webhook Zabbix - Slack](/assets/docs/zabbix/webhook_slack.pdf) | Configuration du webhook Slack pour alerting |

## Bilan

Cette réalisation m'a permis de comprendre concrètement comment des outils de supervision, de ticketing et de notification peuvent être interconnectés pour former une chaîne d'alerte cohérente et entièrement automatisée. Une anomalie détectée par Zabbix génère automatiquement un ticket GLPI et une notification Slack immédiate. De même, à la résolution, le ticket se clôture de lui-même.
Cette démarche autonome m'a permis d'approfondir ma compréhension des webhooks et des APIs REST, sur des solutions largement adoptées en entreprise.

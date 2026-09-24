---
title: "Déploiement d'une supervision proactive et automatisée avec Zabbix"
layout: single
date: 2026-09-24
permalink: /portfolio/projects/zabbix/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - Zabbix
  - MariaDB
  - GLPI
  - Supervision
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Zabbix-D40000?style=for-the-badge&logo=zabbix&logoColor=white" alt="Zabbix" style="height:41px;">
  <img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white" alt="MariaDB" style="height:41px;">
  <img src="https://img.shields.io/badge/GLPI_/_Slack-424242?style=for-the-badge&logoColor=white" alt="GLPI / Slack" style="height:41px;">
</div>

## Cahier des charges

Pour garantir la disponibilité et la performance de l'infrastructure, la mise en place d'un outil de supervision était indispensable. L'objectif n'était pas seulement d'être alerté en cas de panne, mais d'anticiper les incidents.

## Solutions choisies

J'ai déployé Zabbix, dont l'architecture distribuée m'a permis de déporter sa base de données vers le cluster MariaDB existant, via MaxScale. Zabbix communique par webhook avec d'autres outils (GLPI et Slack), ce qui permet de passer d'une gestion réactive à une remédiation proactive. J'ai ajouté chaque équipement manuellement, pour garantir une classification stricte et empêcher toute machine non autorisée d'intégrer le périmètre de supervision.

## Mise en œuvre

**Environnement technique :**  
`Zabbix` - `MariaDB` - `GLPI` - `Slack`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-download" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Installation du serveur Zabbix</strong> sur une VM dédiée
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-database" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Création de la base de données</strong>, avec une collation adaptée à la sensibilité à la casse de Zabbix, et import du schéma routé via MaxScale
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-heartbeat" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Déploiement de l'agent sur le cluster MariaDB</strong>, avec un utilisateur SQL dédié aux droits de lecture stricts
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-list-check" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Déploiement des agents en mode passif</strong>, avec une déclaration manuelle de chaque hôte côté serveur
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-clipboard-list" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Application des modèles de supervision</strong> adaptés à chaque type d'hôte
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-ticket-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Interconnexion avec l'API REST de GLPI</strong>, pour l'automatisation du suivi des incidents
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fab fa-slack" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>7. Interconnexion avec Slack</strong> via webhook, pour les alertes en temps réel
    </div>
  </div>

</div>

## Tests et imprévus

Le test de supervision de la base de données a confirmé la remontée des métriques sans risque d'altération, grâce aux droits de lecture stricts de l'agent. Les alertes déclenchées ont bien généré des tickets automatiques dans GLPI et des notifications sur Slack.

## Bilan

La supervision, couplée à GLPI et Slack, transforme une alerte technique en ticket assigné et en notification immédiate. La déclaration manuelle de chaque hôte, plus contraignante qu'une découverte automatique, garantit en contrepartie qu'aucune machine non autorisée ne s'invite dans l'infrastructure supervisée.

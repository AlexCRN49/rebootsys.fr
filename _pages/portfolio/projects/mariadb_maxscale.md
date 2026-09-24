---
title: "Haute disponibilité d'un cluster MariaDB avec MaxScale"
layout: single
date: 2026-09-24
permalink: /portfolio/projects/mariadb_maxscale/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - MariaDB
  - MaxScale
  - Haute disponibilité
  - Réplication
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white" alt="MariaDB" style="height:41px;">
  <img src="https://img.shields.io/badge/MaxScale-003545?style=for-the-badge&logoColor=white" alt="MaxScale" style="height:41px;">
  <img src="https://img.shields.io/badge/Haute_Disponibilité-424242?style=for-the-badge&logoColor=white" alt="Haute disponibilité" style="height:41px;">
</div>

## Cahier des charges

Un audit interne a mis en évidence un point faible classique. Un unique serveur MariaDB centralisait les bases de données de Zabbix, Guacamole, GLPI et Nextcloud. Ce serveur représentait un SPOF et sa panne aurait entraîné l'arrêt de l'ensemble des services applicatifs.

## Solutions choisies

J'ai mis en place une réplication asynchrone maître-esclave entre deux nœuds MariaDB, pilotée par MaxScale comme proxy intelligent. MaxScale répartit les écritures vers le maître et les lectures vers l'esclave, et surveille le cluster pour basculer automatiquement en cas de panne. Les flux sont chiffrés en SSL/TLS avec des certificats issus de la CA interne. Les sauvegardes s'exécutent sur le nœud esclave, pour ne jamais dégrader les performances du maître.

## Mise en œuvre

**Environnement technique :**  
`MariaDB` - `MaxScale` - `GTID` - `TLS`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-server" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Installation et durcissement des deux serveurs MariaDB</strong>, sur des VMs distinctes
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-download" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Installation de MaxScale</strong> sur un nœud dédié, distinct des deux serveurs MariaDB
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-code-branch" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Configuration de la réplication asynchrone maître-esclave</strong>, synchronisée par GTID pour tracer les transactions et simplifier les bascules
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-lock" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Configuration des journaux binaires au format ROW</strong>, et restriction du nœud esclave en lecture seule
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-certificate" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Sécurisation des flux de réplication</strong> par certificats SSL/TLS issus de la CA interne
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-random" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Configuration de MaxScale</strong> pour le Read/Write splitting et la surveillance du cluster toutes les 5 secondes
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-save" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>7. Mise en place de MariaDB Backup</strong> sur le nœud esclave, pour ne pas dégrader les performances du maître
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-exchange-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>8. Validation du failover automatique</strong> et de la procédure de switchover manuel
    </div>
  </div>

</div>

## Tests et imprévus

Le test de sauvegarde et de restauration complète a été validé sans accroc. Le failover automatique du maître vers l'esclave a également été confirmé, conformément au comportement attendu de MaxScale. Le test de switchover, une bascule manuelle et réversible, a en revanche révélé un problème. Une fragmentation du privilège SUPER dans les versions récentes de MariaDB a cassé la procédure standard. J'ai dû revoir les droits de l'utilisateur MaxScale, reconfigurer l'utilisateur de réplication en mode miroir sur le nouveau maître, puis rétablir le serveur d'origine comme maître nominal via l'API REST de MaxScale. Ce problème n'était documenté nulle part et ne s'est révélé qu'en pratique.

## Bilan

Le cluster répond à l'objectif de haute disponibilité fixé au départ, à savoir un failover automatique fonctionnel, et une procédure de switchover corrigée après le problème de privilège SUPER. Passer à un cluster Galera à trois nœuds en réplication synchrone multi-maître éliminerait le risque de perte de données inhérent à l'asynchrone. C'est l'évolution que j'envisagerais si ce projet devait passer en production.

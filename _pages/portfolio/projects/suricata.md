---
title: "Mise en place d'une protection périmétrique active avec Suricata"
layout: single
date: 2026-09-24
permalink: /portfolio/projects/suricata/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - Suricata
  - OPNsense
  - IDS
  - IPS
  - Zabbix
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Suricata-424242?style=for-the-badge&logoColor=white" alt="Suricata" style="height:41px;">
  <img src="https://img.shields.io/badge/OPNsense-D94F00?style=for-the-badge&logoColor=white" alt="OPNsense" style="height:41px;">
  <img src="https://img.shields.io/badge/Zabbix-D40000?style=for-the-badge&logo=zabbix&logoColor=white" alt="Zabbix" style="height:41px;">
</div>

## Cahier des charges

Le filtrage réseau de base bloque les accès non autorisés au niveau 3, mais reste aveugle aux attaques applicatives qui transitent par des ports ouverts. Il fallait pouvoir inspecter le trafic en temps réel pour détecter et prévenir les intrusions.

## Solutions choisies

J'ai activé Suricata, nativement intégré à OPNsense, avec les signatures Emerging Threats pour la protection contre les vulnérabilités récentes. Le moteur Intel Hyperscan limite la latence introduite par l'inspection. J'ai couplé cette protection à une supervision Zabbix du processus Suricata lui-même, car un crash silencieux de l'IPS laisserait le réseau sans protection sans que personne ne s'en aperçoive.

## Mise en œuvre

**Environnement technique :**  
`Suricata` - `OPNsense` - `Zabbix`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-toggle-on" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Activation du plugin Suricata</strong>, natif d'OPNsense
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-microchip" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Désactivation de l'accélération matérielle</strong> des cartes réseau, prérequis au bon fonctionnement de Suricata qui doit analyser les paquets bruts
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-download" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Activation des modes IPS inline et Promiscuous</strong>, puis téléchargement des signatures Emerging Threats
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-bell" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Configuration de la politique de sécurité en mode Alert</strong> pendant 48 heures, pour analyser les faux positifs avant tout blocage
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-sync-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Planification d'une tâche nocturne</strong> pour l'actualisation automatique des signatures
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-key" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Déploiement de l'agent Zabbix sur le routeur</strong>, avec une clé pré-partagée pour chiffrer le trafic de supervision
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-exclamation-triangle" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>7. Création d'un indicateur personnalisé</strong> comptant les processus Suricata actifs, avec une alerte critique si ce nombre tombe à zéro
    </div>
  </div>

</div>

## Tests et imprévus

Le passage en mode Alert a permis d'identifier les faux positifs avant tout basculement en blocage. Les ressources matérielles des nœuds Proxmox hébergeant l'infrastructure ne permettaient cependant pas de maintenir les modes IPS inline et Promiscuous activés en continu avec un basculement complet en mode Drop, comme cela aurait été fait en environnement de production réel. J'ai donc conservé une configuration adaptée aux contraintes matérielles disponibles, plutôt qu'une configuration idéale mais inexploitable.

## Bilan

Suricata comble l'angle mort du filtrage de base en inspectant le contenu du trafic autorisé, là où un pare-feu classique ne regarde que l'en-tête des paquets. La supervision du processus lui-même, via Zabbix, garantit qu'une panne silencieuse de l'IPS ne passe pas inaperçue. Le compromis assumé entre mode Alert et mode Drop illustre une contrainte réelle liée aux limites matériels du projet. Cela illustre la distinction entre le choix technique idéal et le choix technique applicable.

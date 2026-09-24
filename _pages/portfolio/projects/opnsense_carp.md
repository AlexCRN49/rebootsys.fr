---
title: "Cluster de routeurs virtuels en haute disponibilité avec OPNsense"
layout: single
date: 2026-09-23
permalink: /portfolio/projects/opnsense_carp/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - OPNsense
  - CARP
  - Haute disponibilité
  - VLAN
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/OPNsense-D94F00?style=for-the-badge&logoColor=white" alt="OPNsense" style="height:41px;">
  <img src="https://img.shields.io/badge/CARP-424242?style=for-the-badge&logoColor=white" alt="CARP" style="height:41px;">
  <img src="https://img.shields.io/badge/VLAN-424242?style=for-the-badge&logoColor=white" alt="VLAN" style="height:41px;">
</div>

## Cahier des charges

Le routeur virtuel représentait un point de passage unique pour l'ensemble du trafic interne de l'infrastructure. Il constituait donc un SPOF, un point de défaillance unique, dont la panne aurait impacté l'ensemble de l'activité. L'infrastructure nécessitait par ailleurs une segmentation réseau stricte, en particulier pour les services exposés.

## Solutions choisies

J'ai mis en place un cluster de deux pare-feux OPNsense en haute disponibilité, via le protocole CARP en mode actif/passif. La synchronisation XMLRPC réplique la configuration entre les deux nœuds, et pfSync réplique la table d'états des connexions. J'ai segmenté le réseau en VLANs dédiés (administration, serveurs, utilisateurs, imprimantes, DMZ), avec une politique de filtrage restrictive par défaut en *deny all*.

## Mise en œuvre

**Environnement technique :**  
`OPNsense` - `CARP` - `VLAN` - `Suricata`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-download" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Déploiement de deux VMs OPNsense identiques</strong>, une par nœud Proxmox
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-network-wired" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Segmentation par VLANs</strong> sur les hyperviseurs (ponts réseau VLAN-aware) et sur OPNsense
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-shield-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Configuration des adresses IP virtuelles (VIP) CARP</strong>, une par VLAN, comme passerelle par défaut
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-heartbeat" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Mise en place d'un lien dédié</strong> pour le transport des heartbeats CARP entre les deux nœuds
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-sync-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Activation de la synchronisation XMLRPC</strong> de la configuration entre les deux nœuds
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-exchange-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Activation de pfSync</strong>, pour répliquer la table d'états des connexions en temps réel
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-ban" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>7. Définition de la politique de filtrage</strong> : deny all par défaut, matrice des flux légitimes
    </div>
  </div>

</div>

## Tests et imprévus

Le test de bascule, réalisé en simulant la coupure d'un nœud, a confirmé une reprise transparente par le nœud secondaire. Aucune coupure perceptible n'a été constatée, et les sessions SSH et VPN en cours n'ont pas été interrompues. Ce comportement correspond à ce qui était attendu du mécanisme CARP couplé à pfSync.

## Bilan

La segmentation en VLANs limite la propagation latérale d'une menace entre les différentes zones du réseau. Le cluster CARP élimine, de son côté, le SPOF que représentait un routeur virtuel unique. La synchronisation XMLRPC et pfSync garantit que la bascule d'un nœud à l'autre reste transparente, sans reconfiguration manuelle ni perte des connexions en cours.

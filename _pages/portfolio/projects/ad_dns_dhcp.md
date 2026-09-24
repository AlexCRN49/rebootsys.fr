---
title: "Services cœur de réseau (AD, DNS, DHCP) en haute disponibilité"
layout: single
date: 2026-09-23
permalink: /portfolio/projects/ad_dns_dhcp/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - Active Directory
  - DNS
  - DHCP
  - Haute disponibilité
  - Windows Server
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Windows_Server-0078D4?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Server" style="height:41px;">
  <img src="https://img.shields.io/badge/Active_Directory-0078D4?style=for-the-badge&logoColor=white" alt="Active Directory" style="height:41px;">
  <img src="https://img.shields.io/badge/DNS_/_DHCP-424242?style=for-the-badge&logoColor=white" alt="DNS / DHCP" style="height:41px;">
</div>

## Cahier des charges

L'infrastructure nécessitait un système centralisé pour la gestion des identités (annuaire LDAP), la résolution des noms (DNS) et la distribution dynamique des adresses IP (DHCP). Ces services étant indispensables au fonctionnement quotidien, leur indisponibilité aurait sensiblement impacté l'activité.

## Solutions choisies

J'ai déployé deux serveurs Windows Server 2022 distincts, centralisant les rôles AD DS, DNS et DHCP en haute disponibilité. Le premier sert de contrôleur de domaine primaire, le second de secondaire, chacun tolérant à la panne de l'autre. J'ai configuré la réplication DHCP en mode équilibrage de charge, et redirigé le DNS vers le routeur virtuel OPNsense pour centraliser l'analyse des requêtes.

## Mise en œuvre

**Environnement technique :**  
`Windows Server 2022` - `AD DS` - `DNS` - `DHCP`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-compact-disc" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Installation de deux serveurs Windows Server 2022</strong> distincts
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-server" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Préparation de l'environnement Proxmox</strong> avec installation des pilotes VirtIO pour optimiser les performances réseau des VMs Windows Server
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-sitemap" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Déploiement du rôle AD DS multi-maîtres</strong> avec promotion du premier contrôleur de domaine, intégration du second, structuration de l'annuaire LDAP calquée sur la topologie réseau (pour appliquer les GPO par VLAN)
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-network-wired" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Configuration du rôle DHCP</strong> avec création de l'étendue avec plage d'adresses dédiée, passerelle par défaut pointant vers la VIP CARP d'OPNsense
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-shield-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Sécurisation du cluster DHCP</strong> avec réplication en mode équilibrage de charge entre les deux serveurs, authentification des messages par secret partagé pour prévenir les attaques Man-in-the-Middle sur l'adressage
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-globe" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Optimisation de la résolution DNS</strong> par configuration des redirecteurs des deux contrôleurs de domaine vers l'IP interne d'OPNsense pour les requêtes sortantes
    </div>
  </div>

</div>

## Tests et imprévus

Le test de tolérance de panne a confirmé la continuité du service d'annuaire et de résolution de noms lors de l'indisponibilité simulée d'un des deux serveurs. La bascule DHCP en mode équilibrage de charge a également été validée, sans interruption d'attribution d'adresses côté clients.

## Bilan

La duplication des rôles AD DS, DNS et DHCP sur deux serveurs distincts élimine le risque de panne unique sur des services indispensables au quotidien. L'authentification des échanges DHCP par secret partagé ferme une surface d'attaque (usurpation d'un serveur DHCP sur le réseau), et la structuration de l'annuaire calquée sur la topologie réseau simplifie l'application des GPO par zone.

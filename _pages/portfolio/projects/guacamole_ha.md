---
title: "Déploiement d'un bastion d'administration Guacamole en haute disponibilité"
layout: single
date: 2026-09-23
permalink: /portfolio/projects/guacamole_ha/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - Guacamole
  - Bastion
  - MariaDB
  - LDAP
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Apache_Guacamole-424242?style=for-the-badge&logoColor=white" alt="Apache Guacamole" style="height:41px;">
  <img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white" alt="MariaDB" style="height:41px;">
  <img src="https://img.shields.io/badge/LDAP-424242?style=for-the-badge&logoColor=white" alt="LDAP" style="height:41px;">
</div>

## Cahier des charges

Dans le cadre de l'administration sécurisée du système d'information, il fallait fournir un accès distant sécurisé aux serveurs internes, sans exposer directement leurs ports sur le réseau.

## Solutions choisies

J'ai déployé Apache Guacamole comme bastion sans client, accessible depuis un simple navigateur. Ce point d'accès unique centralise la gestion des accès, sans exposer directement les ports des serveurs internes. Guacamole ne stocke rien localement, l'ensemble repose sur une base de données, ce qui m'a permis de concevoir une architecture redondante à deux instances.

## Mise en œuvre

**Environnement technique :**  
`Guacamole` - `MariaDB` - `LDAP` - `Apache`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-download" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Installation de deux instances Guacamole identiques</strong>, une par nœud Proxmox
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-database" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Découplage des services</strong> avec configuration et sessions stockées sur le cluster MariaDB existant, via la répartition de charge MaxScale
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-copy" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Réplication du fichier de configuration et des extensions</strong> entre les deux instances
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-random" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Répartition de la charge par DNS Round-Robin</strong>, pour simuler une haute disponibilité transparente
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-code" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Compilation du moteur guacd depuis les sources</strong>, avec les bibliothèques nécessaires à la prise en charge de l'authentification NLA de Windows Server
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-diagram-project" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Mise en place d'un reverse proxy Apache en frontal</strong>, pour masquer le serveur applicatif interne et activer le support des WebSockets
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-user-lock" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>7. Configuration de l'authentification LDAP</strong>, avec un compte de service restreint et un filtre limitant l'accès au groupe d'administration
    </div>
  </div>

</div>

## Tests et imprévus

Le test de bascule entre les deux instances Guacamole a confirmé la continuité du service via le DNS Round-Robin. J'ai rencontré un problème de négociation des certificats RDP lors de la compilation de guacd depuis les sources. J'ai dû créer manuellement l'arborescence `/usr/sbin/.config/freerdp` avec des droits stricts attribués à l'utilisateur de service, pour résoudre l'erreur.

## Bilan

Le bastion Guacamole supprime toute exposition directe des ports RDP et SSH sur le réseau, tout en permettant un accès simple depuis un navigateur. Bien que Guacamole ne prévoie pas nativement la haute disponibilité, l'architecture à deux instances tient la charge grâce au découplage complet des données vers le cluster MariaDB partagé.

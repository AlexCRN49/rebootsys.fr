---
title: "Déploiement d'une solution ITSM et de gestion de parc avec GLPI"
layout: single
date: 2026-09-23
permalink: /portfolio/projects/glpi/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - GLPI
  - ITSM
  - MariaDB
  - LDAP
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/GLPI-16A085?style=for-the-badge&logoColor=white" alt="GLPI" style="height:41px;">
  <img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white" alt="MariaDB" style="height:41px;">
  <img src="https://img.shields.io/badge/LDAP-424242?style=for-the-badge&logoColor=white" alt="LDAP" style="height:41px;">
</div>

## Cahier des charges

L'évolution de l'entreprise nécessitait une solution pour centraliser l'assistance aux utilisateurs et automatiser la gestion du parc informatique.

## Solutions choisies

J'ai déployé GLPI dans sa version 11, un standard ITSM open-source qui intègre les bonnes pratiques ITIL. Son architecture découple le serveur web de la base de données. Je l'ai donc connecté au cluster MariaDB existant via MaxScale, ce qui lui apporte la même tolérance de panne que le reste de l'infrastructure. La synchronisation avec l'annuaire Active Directory centralise la gestion des identités, sans créer de compte dédié à ce service.

## Mise en œuvre

**Environnement technique :**  
`GLPI 11` - `Debian` - `MariaDB` - `LDAP`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-server" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Déploiement du socle web</strong> sur Debian avec Apache et PHP, avec une configuration optimisée pour supporter la charge des rapports
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-lock" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Sortie des répertoires sensibles</strong> (configuration, fichiers, logs) hors de la racine publique web, via un fichier de redirection sécurisé
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-database" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Connexion à la base de données</strong> via un utilisateur SQL aux privilèges restreints, autorisé uniquement depuis l'IP du serveur GLPI
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-users-cog" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Configuration de l'authentification LDAP</strong>, avec un compte de service en lecture seule et une synchronisation automatisée nocturne des comptes
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-laptop" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Déploiement de l'agent GLPI</strong> sur l'ensemble du parc (MSI via GPO pour Windows, script Perl pour Linux), avec communication sécurisée par secret partagé
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-ticket-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Mise en place de formulaires conditionnels</strong>, pour générer automatiquement des tickets pré-catégorisés et assignés selon le niveau d'urgence
    </div>
  </div>

</div>

## Tests et imprévus

Le test d'inventaire automatique a confirmé la remontée correcte des machines Windows et Linux dans GLPI. La synchronisation LDAP nocturne a été validée sur plusieurs cycles, sans duplication de comptes ni compte machine parasite dans l'annuaire.

## Bilan

GLPI centralise désormais l'inventaire et le support, sans duplication d'identifiants grâce à l'authentification LDAP déléguée. Le découplage du frontend et de la base de données permet à ce service de bénéficier de la même tolérance de panne que le reste de l'infrastructure, plutôt que de constituer un point de défaillance isolé.

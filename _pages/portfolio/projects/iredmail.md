---
title: "Mise en place d'un serveur de messagerie avec iRedMail"
layout: single
date: 2026-09-23
permalink: /portfolio/projects/iredmail/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - iRedMail
  - Postfix
  - Dovecot
  - LDAP
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/iRedMail-424242?style=for-the-badge&logoColor=white" alt="iRedMail" style="height:41px;">
  <img src="https://img.shields.io/badge/Postfix-424242?style=for-the-badge&logoColor=white" alt="Postfix" style="height:41px;">
  <img src="https://img.shields.io/badge/Dovecot-424242?style=for-the-badge&logoColor=white" alt="Dovecot" style="height:41px;">
</div>

## Cahier des charges

L'entreprise devait se doter d'un service de messagerie électronique complet, sécurisé et souverain. Ce service devait gérer les flux de courriels tout en centralisant la gestion des identifiants avec l'annuaire existant.

## Solutions choisies

J'ai déployé iRedMail en hébergement *on-premise*, ce qui garantit un contrôle strict sur les données sensibles sans dépendance à un acteur tiers. iRedMail n'est pas un système propriétaire, mais un assemblage de standards open source : Postfix pour le SMTP, Dovecot pour l'IMAP, SpamAssassin et Amavis pour le filtrage, Fail2ban pour la sécurité. L'authentification s'appuie sur l'annuaire Active Directory, ce qui centralise la gestion des comptes lors des arrivées et des départs de collaborateurs.

## Mise en œuvre

**Environnement technique :**  
`iRedMail` - `Postfix` - `Dovecot` - `LDAP`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-server" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Déploiement sur Debian dans le VLAN DMZ</strong>, avec configuration du FQDN et vérification des enregistrements DNS internes (A et MX)
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-id-badge" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Connexion du serveur à l'annuaire LDAP</strong>, plutôt qu'à une base SQL autonome pour la gestion des comptes
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-cogs" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Configuration de Dovecot et Postfix</strong> avec un compte de service dédié pour interroger l'annuaire
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-user-check" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Vérification de l'accès collaborateur</strong> avec l'identifiant Windows habituel, sans compte de messagerie distinct
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-certificate" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Remplacement des certificats auto-signés</strong> par ceux émis par la PKI interne de l'entreprise
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-lock" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Durcissement de la configuration</strong> pour forcer le chiffrement des flux IMAPS et SMTP Submission
    </div>
  </div>

</div>

## Tests et imprévus

Le test de connexion avec les identifiants Windows a confirmé l'authentification correcte via l'annuaire, sans compte de messagerie distinct à gérer. La désactivation d'un compte côté annuaire a également coupé son accès à la messagerie, confirmant la révocation centralisée.

## Bilan

iRedMail repose sur des solutions open source, plutôt que sur une solution propriétaire fermée.L'authentification déléguée à l'annuaire évite la gestion de deux jeux d'identifiants séparés pour chaque collaborateur, et le chiffrement forcé des flux IMAPS et SMTP protège les échanges de bout en bout.

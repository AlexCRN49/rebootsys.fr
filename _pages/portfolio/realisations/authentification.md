---
title: "Mise en place d'une politique de gestion et de sécurisation des mots de passe"
layout: single
date: 2025-01-14
permalink: /portfolio/realisations/authentification/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Réalisations
tags:
  - Bitwarden
  - GCPW
  - Sécurité
  - Gestion des accès
  - Mots de passe
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Bitwarden-175DDC?style=for-the-badge&logo=bitwarden&logoColor=white" alt="Bitwarden" style="height:45px;">
  <img src="https://img.shields.io/badge/Google_Workspace-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Workspace" style="height:45px;">
  <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows" style="height:45px;">
</div>

## Cahier des charges

L'entreprise ne disposait d'aucune politique de gestion des mots de passe. Les pratiques constatées exposaient l'organisation à des risques significatifs. Par ailleurs, l'authentification aux postes de travail n'était pas unifiée avec les identités Google Workspace de l'organisation.

L'absence d'infrastructure Active Directory excluait un déploiement centralisé par GPO. La solution devait donc être adaptée à un environnement workgroup et déployable poste par poste.

## Analyse du besoin

- **Unifier l'authentification** Windows avec les **identités Google Workspace** via **GCPW** ;
- **Centraliser** la gestion des **mots de passe** dans un **coffre-fort sécurisé** via **Bitwarden** ;
- **Intégrer** les mots de passe **existants** des collaborateurs ;
- Assurer la **formation** et l'**accompagnement** des utilisateurs.

## Solutions choisies

**GCPW (Google Credential Provider for Windows)** permet aux collaborateurs de se connecter à leur poste Windows avec leurs identifiants Google Workspace, unifiant ainsi les accès sans nécessiter d'infrastructure Active Directory.

**Bitwarden Cloud** (serveur EU) a été retenu comme gestionnaire de mots de passe centralisé. La solution est accessible depuis le navigateur, sans infrastructure serveur à maintenir. Les collections Bitwarden ont été organisées en miroir des unités organisationnelles Google Workspace afin d'assurer une gestion granulaire des accès aux mots de passe par profil utilisateur.

Les deux solutions ont été déployées simultanément dans le cadre d'une même démarche de sécurisation des accès.

## Mise en œuvre

**Période :** 14/01/2025 – 17/01/2025

**Environnement technique :**  
`Bitwarden Cloud` - `GCPW` - `Google Workspace` - `Windows` - `Environnement workgroup`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <!-- Étape 1 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-user-shield" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Création du compte Bitwarden</strong> dédié à l'organisation (serveur EU)
    </div>
  </div>

  <!-- Étape 2 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:1.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-desktop" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Déploiement de GCPW</strong> sur l'ensemble des postes de travail en environnement workgroup (~50 postes)
    </div>
  </div>

  <!-- Étape 3 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-lock" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Création des coffres Bitwarden</strong> pour chaque collaborateur
    </div>
  </div>

  <!-- Étape 4 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:1.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-sitemap" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Organisation des collections</strong> : structure calquée sur les unités organisationnelles Google Workspace pour une gestion granulaire des accès
    </div>
  </div>

  <!-- Étape 5 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:1.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-database" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Intégration des mots de passe existants</strong> et nettoyage (doublons, mots de passe faibles ou obsolètes)
    </div>
  </div>

  <!-- Étape 6 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-chalkboard-teacher" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Formation collective</strong> des utilisateurs (session de 30 minutes)
    </div>
  </div>

  <!-- Étape 7 -->
  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:1.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-check" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>7. Accompagnement individuel</strong> à la génération et à l'enregistrement de nouveaux mots de passe sécurisés
    </div>
  </div>

</div>

## Productions associées

| Document | Description |
|----------|-------------|
| [Guide utilisateur Bitwarden](/assets/docs/authentification/user_guide_bitwarden.pdf) | Prise en main de Bitwarden pour les collaborateurs |
| [Guide utilisateur GCPW](/assets/docs/authentification/user_guide_gcpw.pdf) | Connexion Windows avec les identifiants Google Workspace |

## Bilan

La mise en place conjointe de GCPW et Bitwarden a permis d'unifier l'authentification des postes de travail et de structurer la gestion des mots de passe au sein de l'organisation. Le déploiement manuel, imposé par l'absence d'infrastructure Active Directory, a été l'occasion d'un accompagnement individualisé de chaque collaborateur, favorisant l'adoption des bonnes pratiques dès la mise en service. Afin de réduire les risques inhérents aux pratiques antérieures, une formation collective et une phase de nettoyage des mots de passe existants ont complété la démarche.

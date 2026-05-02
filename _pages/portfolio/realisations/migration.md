---
title: "Migration d'infrastructure et réorganisation du brassage réseau par segmentation fonctionnelle"
layout: single
date: 2026-01-19
permalink: /portfolio/realisations/migration/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Réalisations
tags:
  - Réseau
  - Brassage
  - Infrastructure
  - Segmentation
  - VLAN
---

## Cahier des charges

Dans le cadre d'une restructuration interne, la direction a souhaité regrouper l'ensemble des équipes situées dans l'aile EST vers l'aile OUEST du bâtiment. Cette réorganisation avait pour objectif de favoriser la communication entre les collaborateurs en les regroupant en open-space, organisés par Business Unit.

L'aile de destination disposait déjà d'un câblage réseau en place, accessible via des poteaux et des points de raccordement muraux. En revanche, cette infrastructure, initialement dédiée à un projet de sous-location, n'était pas raccordée au réseau de production de la société.

L'enjeu principal consistait donc à rendre opérationnelle cette zone en l'intégrant au réseau existant, tout en limitant au maximum l'interruption de service pour les collaborateurs.

## Analyse du besoin

L'infrastructure actuelle reposait sur un réseau déjà configuré, avec une segmentation existante (notamment pour le Wi-Fi), qui ne devait pas être modifiée dans le cadre de ce projet. Le périmètre d'intervention se limitait donc à l'intégration physique et logique des prises réseau dans l'infrastructure existante.

Une contrainte importante est apparue dès la phase d'analyse : le plan d'implantation des postes défini par la direction ne correspondait pas aux emplacements des prises réseau disponibles. Il a donc fallu adapter le brassage en conséquence, sans possibilité de modifier le câblage structurel.

## Solutions choisies

Le choix a été fait de s'appuyer entièrement sur l'infrastructure réseau en place, sans modification de l'architecture ni des configurations globales, afin de garantir la portabilité et d'éviter tout impact sur les services existants.

L'intervention s'est donc concentrée sur du brassage physique, en connectant les ports du panneau de brassage aux switches appropriés. Certains ports ont toutefois nécessité un ajustement logique, notamment pour les équipements connectés au switch PoE, réaffectés sur les VLANs correspondants conformément à la configuration existante.

## Gestion de projet

### Diagramme de Gantt

![Gantt Déménagement infrastructure](/assets/images/projects/demenagement/gantt.png)

## Mise en œuvre

**Période :** 19/01/2026 – 23/01/2026

**Environnement technique :**  
`Baie de brassage` - `Panneau de brassage` - `Switch PoE` - `Câblage RJ45` - `VLAN`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <!-- Étape 1 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-search" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Recueil du besoin et analyse de l'existant</strong>
    </div>
  </div>

  <!-- Étape 2 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-network-wired" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Repérage et cartographie</strong> : correspondances prises murales / ports de brassage
    </div>
  </div>

  <!-- Étape 3 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-server" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Préparation de la baie</strong> : organisation du câblage et des cordons de brassage
    </div>
  </div>

  <!-- Étape 4 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:1.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-plug" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Brassage physique</strong> : raccordement des ports et réaffectation des VLANs sur les ports PoE
    </div>
  </div>

  <!-- Étape 5 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:1.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-vial" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Tests de connectivité</strong> : accès réseau local, obtention d'une adresse IP, accès Internet
    </div>
  </div>

  <!-- Étape 6 -->
  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-people-carry" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Déplacement progressif des postes utilisateurs</strong>
    </div>
  </div>

  <!-- Étape 7 -->
  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-file-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>7. Documentation</strong>
    </div>
  </div>

</div>

## Productions associées

| Document | Description |
|----------|-------------|
| Plan de brassage | Non communicable pour des raisons de sécurité |

## Bilan

Cette réalisation a mis en évidence l'importance de la phase de repérage et de préparation dans un contexte où l'infrastructure physique ne correspond pas aux besoins organisationnels. La principale difficulté rencontrée a été l'écart entre le plan d'implantation des collaborateurs et les contraintes techniques du câblage existant. Cela a nécessité une adaptation dans le brassage afin de répondre au besoin sans modification structurelle. Le choix de ne pas intervenir sur la configuration réseau existante a permis de sécuriser le déploiement et de limiter les risques d'incident, tout en ouvrant la voie à une future segmentation plus fine des équipements critiques.

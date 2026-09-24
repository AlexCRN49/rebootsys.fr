---
title: "Mise en place d'une PKI interne à deux niveaux sous OPNsense"
layout: single
date: 2026-09-22
permalink: /portfolio/achievements/opnsense/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Réalisations
tags:
  - OPNsense
  - PKI
  - Certificats
  - Sécurisation
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/OPNsense-D94F00?style=for-the-badge&logoColor=white" alt="OPNsense" style="height:41px;">
  <img src="https://img.shields.io/badge/PKI-424242?style=for-the-badge&logoColor=white" alt="PKI" style="height:41px;">
  <img src="https://img.shields.io/badge/TLS_/_x509-424242?style=for-the-badge&logoColor=white" alt="TLS / x509" style="height:41px;">
</div>

## Cahier des charges

L'utilisation de certificats auto-signés pour les services web internes générait des alertes de sécurité dans les navigateurs, dégradant la confiance des utilisateurs et rendant difficile la distinction entre une alerte légitime et un simple certificat non reconnu.

## Analyse du besoin

- Éliminer les alertes de sécurité liées aux certificats auto-signés sur l'ensemble des services internes ;
- Garantir une chaîne de confiance **résiliente** où la compromission d'une autorité de signature ne doit pas remettre en cause l'ensemble de la chaîne ;
- Faciliter l'ajout de nouveaux services sans reconfigurer la confiance sur chaque poste client.

## Solutions choisies

Une **PKI à deux niveaux** sous OPNsense constituée d'une **autorité racine** hors-ligne, et d'une **autorité intermédiaire** qui gère les **certificats dédié à chaque service**. En cas de compromission de l'autorité intermédiaire, elle peut être révoquée depuis la racine sans affecter les certificats déjà émis par une éventuelle autre autorité intermédiaire, et sans avoir à redéployer la confiance racine sur les postes clients.

## Mise en œuvre

**Environnement technique :**  
`OPNsense` - `PKI` - `x509`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-landmark" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Création de l'autorité racine</strong> (Root CA)
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-sitemap" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Création de l'autorité intermédiaire</strong>
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-certificate" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Génération d'un certificat dédié par service</strong>, signé par l'autorité intermédiaire
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-check-double" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Diffusion de la confiance</strong> sur les postes clients, par l'installation du seul certificat racine
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-file-alt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Documentation</strong>
    </div>
  </div>

</div>

## Productions associées

| Document | Description |
|----------|-------------|
| [Procédure de mise en place d'un PKI interne](/assets/docs/opnsense/pki.pdf) | Configuration d'une PKI internes à deux niveaux avec certificat dédié par service |

## Bilan

La PKI à deux niveaux élimine les alertes de certificats auto-signés pour l'ensemble des services internes, tout en limitant l'exposition de l'autorité racine et permettant de révoquer un certificat de service compromis sans affecter les autres. Un certificat dédié par service, plutôt qu'un certificat unique partagé, limite également l'impact d'une éventuelle compromission à ce seul service.

---
title: "Mise en place d'un reverse proxy Caddy pour l'accès aux services internes"
layout: single
date: 2026-09-22
permalink: /portfolio/achievements/caddy/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Réalisations
tags:
  - Caddy
  - Reverse Proxy
  - HTTPS
  - PKI
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Caddy-424242?style=for-the-badge&logo=caddy&logoColor=white" alt="Caddy" style="height:41px;">
  <img src="https://img.shields.io/badge/Reverse_Proxy-424242?style=for-the-badge&logoColor=white" alt="Reverse Proxy" style="height:41px;">
  <img src="https://img.shields.io/badge/TLS-424242?style=for-the-badge&logoColor=white" alt="TLS" style="height:41px;">
</div>

## Cahier des charges

Plusieurs services web internes étaient accessibles séparément, chacun nécessitant sa propre gestion de certificat, sans centralisation du point d'entrée ni chiffrement cohérent d'un service à l'autre.

## Analyse du besoin

- Centraliser l'accès à plusieurs services web internes derrière un **point d'entrée unique** ;
- Chiffrer l'ensemble des échanges en HTTPS, sans certificats auto-signés générant des alertes navigateur ;
- Prendre en charge les spécificités des différents services.

## Solutions choisies

Déploiement du reverse proxy **Caddy**, avec leintégration des certificats générés par la **PKI interne OPNsense**.

## Mise en œuvre

**Environnement technique :**  
`Caddy` - `PKI OPNsense` - `TLS`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-download" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Installation de Caddy</strong>
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-certificate" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Récupération de la chaîne de certificats</strong> depuis la PKI OPNsense
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-lock" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Sécurisation des permissions</strong> des fichiers de certificat et de clé privée
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-file-code" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Configuration et validation du Caddyfile</strong>
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-globe" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Ajout des enregistrements DNS locaux</strong> pour chaque service proxifié
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-rotate" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Rechargement du service Caddy</strong> pour application de la configuration
    </div>
  </div>

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
| [Procédure de mise en place de Caddy](/assets/docs/caddy/caddy_installation.pdf) | Installation et configuration de Caddy |

## Bilan

Le reverse proxy Caddy centralise désormais l'accès à l'ensemble des services web internes derrière un point d'entrée unique et chiffré, avec des certificats émis depuis la PKI interne plutôt que des certificats auto-signés. La configuration par blocs réutilisables simplifie l'ajout de nouveaux services : il suffit d'importer le bloc TLS commun, sans devoir reconfigurer le chiffrement à chaque fois.

---
title: "Déploiement d'une PKI à deux niveaux avec Windows Server AD CS"
layout: single
date: 2026-09-22
permalink: /portfolio/projects/pki_adcs/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - Windows Server
  - AD CS
  - PKI
  - Certificats
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Windows_Server-0078D4?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Server" style="height:41px;">
  <img src="https://img.shields.io/badge/AD_CS-0078D4?style=for-the-badge&logoColor=white" alt="AD CS" style="height:41px;">
  <img src="https://img.shields.io/badge/PKI-424242?style=for-the-badge&logoColor=white" alt="PKI" style="height:41px;">
</div>

## Cahier des charges

L'utilisation de certificats auto-signés générait des alertes de sécurité dans les navigateurs. Ces alertes dégradaient la confiance des utilisateurs envers les services internes. Une autorité de certification interne devenait nécessaire.

## Solutions choisies

J'ai mis en place une PKI Windows à deux niveaux avec le rôle AD CS. L'autorité racine reste installée sur un serveur autonome, hors du domaine, et ne sert qu'à signer l'autorité intermédiaire. L'autorité intermédiaire, membre du domaine Active Directory, délivre les certificats des services au quotidien.

## Mise en œuvre

**Environnement technique :**  
`Windows Server 2022` - `AD CS` - `OpenSSL`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-landmark" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Installation de l'autorité racine</strong> sur un serveur Windows autonome, hors du domaine, et génération de son certificat
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-sitemap" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Installation de l'autorité intermédiaire</strong> sur un serveur membre du domaine, signée par la racine via export/import de la demande de signature
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-power-off" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Mise hors-ligne de l'autorité racine</strong>, déconnectée du réseau une fois l'intermédiaire signée
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-list-check" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Publication d'un point de distribution HTTP</strong> pour la vérification en temps réel des listes de révocation
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-certificate" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Génération des certificats de service</strong> pour les services Linux, via une demande de signature OpenSSL incluant les SAN, puis conversion aux formats PEM/CRT
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-check-double" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Diffusion du certificat racine</strong> sur les postes clients du domaine, via GPO
    </div>
  </div>

</div>

## Tests et imprévus

Le test de validation côté client a confirmé l'absence d'alerte de sécurité sur les navigateurs, une fois le certificat racine déployé par GPO. La conversion des certificats du format Windows vers les formats PEM et CRT a également été validée sur les services Linux, sans erreur d'intégration.
J'ai cependant rencontré un problème lié à la date d'expiration de la liste de révocation, que j'ai dû adapter afin de résoudre l'erreur.

## Bilan

L'architecture à deux niveaux limite l'exposition de l'autorité racine, maintenue hors-ligne l'essentiel du temps. Si l'autorité intermédiaire venait à être compromise, sa révocation depuis la racine ne détruirait pas toute la chaîne de confiance.

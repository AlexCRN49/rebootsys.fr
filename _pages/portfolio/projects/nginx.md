---
title: "Mise en place d'un reverse proxy Nginx en architecture Zero Trust"
layout: single
date: 2026-09-24
permalink: /portfolio/projects/nginx/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - Nginx
  - Reverse Proxy
  - Zero Trust
  - TLS
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="Nginx" style="height:41px;">
  <img src="https://img.shields.io/badge/Zero_Trust-424242?style=for-the-badge&logoColor=white" alt="Zero Trust" style="height:41px;">
  <img src="https://img.shields.io/badge/TLS-424242?style=for-the-badge&logoColor=white" alt="TLS" style="height:41px;">
</div>

## Cahier des charges

L'infrastructure hébergeait plusieurs services web répartis sur différents VLANs. Seul le serveur de messagerie, placé en DMZ, était accessible depuis l'extérieur. Il fallait centraliser l'accès à ces services, sécuriser les flux et masquer l'architecture interne.

## Solutions choisies

J'ai mis en place un reverse proxy Nginx comme point d'entrée unique, dans une logique Zero Trust. Couplé à une politique stricte sur le routeur OPNsense, aucun accès direct n'est autorisé depuis l'extérieur, ainsi les utilisateurs nomades doivent passer par un tunnel VPN. Le reverse proxy centralise également la validation des certificats SSL/TLS pour l'ensemble des services, ce qui allège la charge sur les serveurs cibles et facilite le renouvellement des clés.

## Mise en œuvre

**Environnement technique :**  
`Nginx` - `LXC` - `Ansible` - `TLS`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-cube" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Déploiement d'un conteneur LXC Debian</strong> dans le VLAN DMZ et installation du paquet nginx
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-key" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Durcissement de l'accès SSH</strong> par authentification par clé asymétrique, gérée via Ansible
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-route" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Création d'un modèle de configuration standardisé</strong>, pour rediriger le flux vers l'adresse interne du serveur cible
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-fingerprint" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Transmission des en-têtes d'origine</strong>, afin que les services de destination conservent la trace du client
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-plug" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Ajout du support des WebSockets</strong> et augmentation de la taille maximale des requêtes, pour ne pas entraver les applications proxifiées
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-lock" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Rangement sécurisé des certificats</strong>, avec des droits stricts sur les clés privées
    </div>
  </div>

</div>

## Tests et imprévus

Le test d'accès depuis l'extérieur a confirmé que seul le tunnel VPN permettait d'atteindre les services proxifiés, conformément à la politique Zero Trust. L'envoi de pièces jointes volumineuses depuis le Webmail a également été validé après l'augmentation de la taille maximale des requêtes.

## Bilan

Le reverse proxy Nginx masque l'architecture interne derrière un point d'entrée unique, et centralise la gestion des certificats plutôt que de la disperser sur chaque service. Couplé à la politique du routeur OPNsense, il ferme tout accès direct depuis l'extérieur. Conséquence, la seule porte d'entrée passe par le VPN.

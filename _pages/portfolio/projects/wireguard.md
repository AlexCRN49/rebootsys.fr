---
title: "Interconnexion VPN site-à-site avec WireGuard"
layout: single
date: 2026-09-24
permalink: /portfolio/projects/wireguard/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - WireGuard
  - VPN
  - OPNsense
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/WireGuard-88171A?style=for-the-badge&logo=wireguard&logoColor=white" alt="WireGuard" style="height:41px;">
  <img src="https://img.shields.io/badge/VPN-424242?style=for-the-badge&logoColor=white" alt="VPN" style="height:41px;">
  <img src="https://img.shields.io/badge/OPNsense-D94F00?style=for-the-badge&logoColor=white" alt="OPNsense" style="height:41px;">
</div>

## Cahier des charges

Il fallait permettre une communication sécurisée et transparente entre l'infrastructure physique locale et des serveurs Cloud externalisés.

## Solutions choisies

J'ai mis en place un VPN site-à-site avec WireGuard, intégré nativement au noyau d'OPNsense. Le protocole repose sur un simple échange de clés publiques entre pairs, ce qui réduit la surface d'attaque et les risques d'erreur de configuration. J'ai ajouté une clé pré-partagée pour une résistance post-quantique, en plus des algorithmes de chiffrement modernes utilisés par défaut.

## Mise en œuvre

**Environnement technique :**  
`WireGuard` - `OPNsense`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-toggle-on" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Activation du service WireGuard</strong>, natif d'OPNsense, sur les deux routeurs
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-microchip" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Désactivation du déchargement matériel</strong> des cartes réseau virtuelles, qui corrompt les paquets chiffrés en environnement virtualisé
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-key" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Génération d'une paire de clés</strong> publique/privée sur chaque routeur OPNsense
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-arrows-left-right" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Configuration réciproque des deux sites</strong> comme points de terminaison l'un de l'autre, avec croisement des clés publiques
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-route" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Définition d'une route statique</strong> redirigeant le trafic vers le sous-réseau distant, via l'interface du tunnel
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-heartbeat" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Configuration d'un Keepalive</strong>, pour éviter la fermeture silencieuse de la connexion en cas d'inactivité
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-ban" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>7. Isolation du trafic WireGuard</strong> sur une interface dédiée, avec des règles de filtrage restreintes aux ports strictement nécessaires
    </div>
  </div>

</div>

## Tests et imprévus

Le test de connectivité entre les deux sites a confirmé l'établissement d'un tunnel permanent et bidirectionnel. Le Keepalive configuré a empêché la coupure de la connexion en période d'inactivité, comme vérifié lors de tests répétés à différents intervalles de temps.

## Bilan

WireGuard relie les deux sites comme s'ils formaient un unique réseau, avec une configuration relativement simple. L'ajout d'une clé pré-partagée en complément de la cryptographie native permet l'anticipation de la casse post-quantique, bien qu'il s'agisse d'une menace relativement théorique à ce jour.

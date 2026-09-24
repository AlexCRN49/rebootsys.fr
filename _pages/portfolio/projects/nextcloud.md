---
title: "Déploiement d'une plateforme collaborative sur site en haute disponibilité"
layout: single
date: 2026-09-23
permalink: /portfolio/projects/nextcloud/
classes: wide
read_time: true
show_date: false
toc: true
toc_sticky: true
categories:
  - Projets
tags:
  - Nextcloud
  - Redis
  - MariaDB
  - LDAP
---
<br>

<div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:2rem;">
  <img src="https://img.shields.io/badge/Nextcloud-0082C9?style=for-the-badge&logo=nextcloud&logoColor=white" alt="Nextcloud" style="height:41px;">
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis" style="height:41px;">
  <img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white" alt="MariaDB" style="height:41px;">
</div>

## Cahier des charges

L'entreprise avait besoin de fournir à ses collaborateurs une plateforme de partage de fichiers et de collaboration sécurisée. L'objectif était de remplacer l'usage d'outils cloud publics par une solution maîtrisée en interne.

## Solutions choisies

J'ai déployé Nextcloud en hébergement *on-premise*, ce qui garantit un contrôle strict sur les données sensibles sans dépendance à un acteur tiers. J'ai connecté le serveur web directement au cluster MariaDB existant via MaxScale, et délégué la gestion du cache à un serveur Redis. L'authentification s'appuie sur l'annuaire LDAP, sans créer de compte dédié à ce service.

## Mise en œuvre

**Environnement technique :**  
`Nextcloud` - `Redis` - `MariaDB` - `LDAP`

<div style="position:relative; padding-left:2.5rem; margin:2rem 0;">

  <div style="position:absolute; left:1rem; top:0; bottom:0; width:2px; background:#41b0f2;"></div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-server" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>1. Déploiement du socle web</strong> sur Debian avec Apache et PHP, configuration optimisée pour les fichiers lourds
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-database" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>2. Connexion à une base de données dédiée</strong>, via la répartition de charge MaxScale
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-bolt" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>3. Déploiement d'un serveur Redis local</strong> pour le verrouillage transactionnel des fichiers, afin de soulager la base de données
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-wrench" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>4. Durcissement via l'outil en ligne de commande occ</strong> : indices manquants, réparation des types MIME, liens de partage propres
    </div>
  </div>

  <div style="position:relative; margin-bottom:1.5rem;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#41b0f2; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-clock" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>5. Remplacement du déclencheur de tâches de fond</strong> par défaut, par une tâche planifiée toutes les 5 minutes
    </div>
  </div>

  <div style="position:relative; margin-bottom:0;">
    <div style="position:absolute; left:-2.5rem; top:0.6rem; width:2rem; height:2rem; background:#5cb85c; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <i class="fas fa-id-badge" style="color:white; font-size:0.8rem;"></i>
    </div>
    <div style="background:#f8f9fa; border:1px solid #e0e0e0; border-radius:6px; padding:0.8rem 1rem;">
      <strong>6. Intégration de l'annuaire LDAP</strong>, avec mapping des comptes sur l'identifiant Windows des collaborateurs
    </div>
  </div>

</div>

## Tests et imprévus

Le test de verrouillage concurrent de fichiers a confirmé que le passage par Redis absorbait la charge sans ralentissement perceptible de la base de données. La désactivation d'un compte côté annuaire a bien entraîné la révocation immédiate de l'accès à Nextcloud.

## Bilan

Nextcloud offre aux collaborateurs une alternative interne aux outils cloud publics, avec les données maîtrisées de bout en bout. Le passage par Redis pour le verrouillage transactionnel évite que cette plateforme ne devienne un point de contention pour le cluster MariaDB partagé avec les autres services. L'authentification LDAP déléguée garantit que la révocation d'un accès reste centralisée, sans compte orphelin à gérer manuellement.

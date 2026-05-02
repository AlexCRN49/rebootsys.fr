---
title: "Mise en place d'un serveur Docker - Portainer"
layout: single
date: 31/10/2025
permalink: /portfolio/projects/docker/
toc: true
toc_sticky: true
date: 2025-10-31
categories: 
  - Projet
tags: 
  - Docker
  - Portainer
  - Virtualisation
  - Conteneurisation
  - BTS-SIO
---

## Contexte 

### État des lieux initial

L’infrastructure de départ reposait sur un **unique serveur Proxmox VE**.  
Limites constatées :  
- Administration isolée (pas de cluster, ni de quorum).  
- Pas de haute disponibilité (**single point of failure**).  
- Pas de sauvegarde centralisée.  

![Schéma de l'infrastructure Proxmox initiale](/assets/images/projects/proxmox/infra-proxmoxinitiale.png)

### Expression du besoin

Mettre en place un serveur Docker afin de déployer des solutions au sein de conteneurs pour des tests ou de la production.

### Cahier des charges

À partir des équipements physique à disposition, configurer un serveur physique avec les ressources matérielles adéquates.  
Sur ce serveur physique, installer un serveur Docker.  

### Analyse de la demande

Recycler un équipement informatique de type ordinateur tour ;  
Configurer les ressources de l'ordinateur afin de répondre aux pré-requis nécessaires au déploiement de Docker et à de plusieurs conteneurs (CTs) ;  
Déployer Docker sur le serveur mis en place.

### Proposition effectuées

- Sur la base d'un ordinateur de marque DELL modèle OPTIPLEX 7020, équipé d'un processeur Intel I5 compatible avec la virtualisation, installation de 32Go de RAM DDR4 et de deux disques SSD (un pour l'hyperviseur, un pour les VMs) puis configuration du BIOS ;  
- Installation de Docker ;  
- Installation de l'interface Web Portainer.




### Objectifs  
- **Gestion centralisée** : administration simplifiée grâce à Portainer ;  
- **Optimisation** : équilibrage de charge entre les conteneurs ;  


### Amélioration proposée
- Gestion des sauvegardes

---

## Organisation du projet

Le projet a été mené en plusieurs étapes, ponctuées de réunions de suivi.  

### Liste des tâches réalisées

Phases :  
1. Recueil du besoin et état des lieux  
2. Installation du serveur Docker
3. Installation de l'interface Web Portainer
4. Tests et validation 
5. Documentation  

### Diagramme de Gantt simplifié

![Gantt Proxmox](/assets/images/proxmox/gantt_docker.png)

---

## Réalisation

- Installation et configuration du **serveur Docker**.  
- Mise en place de l'interface de gestion **Portainer**.  
- Création de **conteneurs**.  
- Mise en place d'une solution de **sauvegarde pour les conteneurs**.  

### Schéma de l’infrastructure après évolution  
![Schéma final](/assets/images/docker/infra_finale.png)  

---

## Documentation associée

- [Procédure installation Proxmox VE](/docs/proxmox-install.md)  
- [Mise en place d’un cluster](/docs/proxmox-cluster.md)  
- [Configuration quorum](/docs/quorum.md)  
- [Installation Proxmox Backup Server](/docs/pbs-setup.md)  

---

## Liste des compétences mobilisées

- Gérer le patrimoine informatique ;  
- Répondre aux incidents et aux demandes d’assistance et d’évolution ;  
- Travailler en mode projet ;  
- Mettre à disposition des utilisateurs un service informatique.  

---

## Bilan personnel

À travers ce projet, j'ai appris à mettre en place un serveur Proxmox, à l'intégrer au sein d'un cluster, et à optimiser sa sauvegarde.

Grâce à la documentation Proxmox et au forum Proxmox Support, j'ai pu trouver relativement facilement les éléments nécessaires à la mise en place et la sécurisation des serveurs.

La mise en place du quorum, nécessaire à la mise en place de la haute disponibilité, s'est avérée plus délicate. Le choix d'un serveur, désigné quorum et l'absence de stockage centralisé pour les VMs ont représenter des obstacles.  

À travers la mise en place de Proxmox Backup Server, j'ai découvert une solution parfaitement adaptée à la sauvegarde et à la restauration des VMs sur Proxmox, qui m'ont permis de pallier à l'absence de haute disponibilité.

---

## Bilan personnel

### Compétences acquises

- Transcription de l'expression d'un besoin orale en une solution technique ;  
- Installation d'un hyperviseur basé sur un système Linux ;  
- Mise en place d'un cluster ;  
- Compréhension des mécanismes nécessaires à la mise en place de la haute disponibilité ;  
- Compréhension des mécanismes de sauvegarde et de restauration associé à des VMs sur un hyperviseur.

### Amélioration possible

- Mise en place de serveur de stockage pour la centralisation des VMs ;  
- Mise en place d'un troisième serveur Proxmox VE pour intégration au cluster et remplacement du quorum ;  
- Mise en place de la haute disponibilité pour assurer la continuité de service.  
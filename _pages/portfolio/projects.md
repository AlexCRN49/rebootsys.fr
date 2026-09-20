---
title: "Mes projets"
layout: single
date: 16/09/2026
permalink: /portfolio/projects/
classes: wide
author_profile: true
read_time: true
show_date: false
toc: true
toc_label: "Sur cette page"
---

## Projet de BTS : une infrastructure d'entreprise construite en autonomie

Dans le cadre du BTS SIO option SISR, en m'appuyant sur le référentiel de la formation, j'ai souhaité aller au-delà de l'attendu nécessaire au passage de l'examen.  

L'objectif était pour moi de monter en compétence et de me challenger en terme d'**architecture réseau**, d'**administration** et de **sécurisation** d'une infrastructure d'entreprise.  

J'ai donc conçu et déployé en totale **autonomie** une **infrastructure complète** pour une **société fictive** répondant aux exigences de **résilience**, de **sécurité** et de **scalabilité**.  

Ce qui suit est le résultat de ce travail, que j'ai mené essentiellement au cours de la seconde année de formation et que j'ai souhaité partagé ici.  

<!-- Cette infrastructure répondant aux exigences du BTS SIO est aujourd'hui démonté. Cependant, j'ai reconstruit une nouvelle infrastructure reprenant cette colonne vertébrale sur une base matérielle plus étendue pour me permettre de développer toujours plus mes compétences au cours de ma Licence ASRS (voir mon [Homelab](https://rebootsys.fr/portfolio/homelab/)). -->




## Fondations réseau et identité

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-shield-halved" style="font-size: 24px; margin-right: 8px;"></i>
      Cluster de routeurs virtuels OPNsense en haute disponibilité
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/opnsense.png" alt="Logo OPNsense" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Deux pare-feux OPNsense en cluster CARP, avec segmentation stricte en VLAN et filtrage par défaut en <em>deny all</em>.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="#" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-sitemap" style="font-size: 24px; margin-right: 8px;"></i>
      Services cœur de réseau Windows Server en haute disponibilité
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/windows.png" alt="Logo Windows Server" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Deux contrôleurs de domaine Windows Server répliqués et DHCP en équilibrage de charge, pour un annuaire et un adressage qui survivent à la perte d'un site.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="#" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-certificate" style="font-size: 24px; margin-right: 8px;"></i>
      PKI interne à deux niveaux
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/windows.png" alt="Logo Windows Server" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Une CA racine hors-ligne et une CA intermédiaire qui délivre les certificats du quotidien, pour limiter l'impact d'une compromission.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="#" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

## Résilience des données

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-database" style="font-size: 24px; margin-right: 8px;"></i>
      Haute disponibilité d'un cluster MariaDB avec MaxScale
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/mariadb.png" alt="Logo MariaDB" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Réplication asynchrone maître-esclave avec bascule automatique et répartition de charge.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="/portfolio/projets/mariadb-maxscale" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-clock-rotate-left" style="font-size: 24px; margin-right: 8px;"></i>
      Sauvegarde centralisée et PRA avec Proxmox Backup Server
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/pbs.png" alt="Logo Proxmox Backup Server" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Deux serveurs PBS indépendants sur deux nœuds différents, synchronisés par tirage incrémental.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="#" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-code-branch" style="font-size: 24px; margin-right: 8px;"></i>
      Sauvegarde versionnée des équipements réseau avec Oxidized
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/github.png" alt="Logo GitHub" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Chaque modification de configuration réseau génère un commit Git, poussé automatiquement vers un dépôt distant et supervisé par Zabbix.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="#" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-cloud-arrow-up" style="font-size: 24px; margin-right: 8px;"></i>
      Externalisation chiffrée des sauvegardes avec Restic
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/restic.png" alt="Logo Restic" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Sauvegarde chiffrée AES-256 vers un dépôt Cloud externe, avec déduplication à la source et restauration fichier par fichier.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="#" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

## Services applicatifs

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-gears" style="font-size: 24px; margin-right: 8px;"></i>
      Provisionnement automatisé et idempotent avec Ansible
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/ansible.png" alt="Logo Ansible" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Déploiement reproductible de machines virtuelles et conteneurs sur Proxmox.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="/portfolio/projets/ansible-provisioning" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-headset" style="font-size: 24px; margin-right: 8px;"></i>
      Déploiement d'une solution ITSM avec GLPI
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/glpi.png" alt="Logo GLPI" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Gestion de parc et support helpdesk, connectés à l'annuaire et au cluster MariaDB.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="#" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-cloud" style="font-size: 24px; margin-right: 8px;"></i>
      Plateforme collaborative Nextcloud en haute disponibilité
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/nextcloud.png" alt="Logo Nextcloud" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Alternative on-premise aux clouds publics, avec un cache Redis pour absorber la charge liée au verrouillage de fichiers.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="#" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-envelope" style="font-size: 24px; margin-right: 8px;"></i>
      Serveur de messagerie iRedMail
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/iredmail.png" alt="Logo iRedMail" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Messagerie souveraine, isolée en DMZ, avec authentification déléguée à l'annuaire.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="#" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

## Sécurité et supervision

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-desktop" style="font-size: 24px; margin-right: 8px;"></i>
      Bastion d'administration Apache Guacamole en haute disponibilité
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/guacamole.png" alt="Logo Apache Guacamole" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Accès distant aux serveurs internes sans exposer le moindre port, deux instances redondantes réparties par DNS round-robin.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="#" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-chart-line" style="font-size: 24px; margin-right: 8px;"></i>
      Supervision proactive et automatisée avec Zabbix
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/zabbix.png" alt="Logo Zabbix" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Supervision interconnectée à GLPI et Slack via webhooks, pour transformer une alerte en ticket assigné automatiquement.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="#" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-shield-virus" style="font-size: 24px; margin-right: 8px;"></i>
      Protection périmétrique active avec Suricata (IDS/IPS)
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/suricata.png" alt="Logo Suricata" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Suricata, intégré à OPNsense, inspecte le trafic en profondeur et bloque un paquet malveillant avant qu'il n'atteigne sa cible.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="#" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-diagram-project" style="font-size: 24px; margin-right: 8px;"></i>
      Reverse proxy Nginx
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/nginx.png" alt="Logo Nginx" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Point d'entrée unique pour les services web internes, avec chiffrement centralisé et ajout de nouveaux services simplifié.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="#" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details>
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold; cursor:pointer;">
      <i class="fa-solid fa-lock" style="font-size: 24px; margin-right: 8px;"></i>
      Interconnexion VPN site-à-site avec WireGuard
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/wireguard.png" alt="Logo WireGuard" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Tunnel chiffré entre l'infrastructure locale et les serveurs Cloud externes, cryptographie moderne et configuration minimale.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="#" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>
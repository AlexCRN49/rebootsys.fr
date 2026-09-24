---
title: "Mes réalisations"
layout: single
date: 20/09/2026
permalink: /portfolio/achievements/
classes: wide
author_profile: true
read_time: true
show_date: false
toc: true
toc_label: "Sur cette page"
---

# Mon alternance en BTS

Les réalisations suivantes retracent mon apport à la structuration, à la sécurisation et à la résilience de l'infrastructure informatique de Delivagri durant mon alternance.

<style>
.realisation-item summary {
  list-style: none;
  display: flex;
  align-items: center;
  cursor: pointer;
}
.realisation-item summary::-webkit-details-marker {
  display: none;
}
.realisation-arrow {
  display: inline-block;
  margin-right: 8px;
  transition: transform 0.2s ease;
  flex-shrink: 0;
}
.realisation-item[open] .realisation-arrow {
  transform: rotate(90deg);
}
</style>

## <i class="fa-solid fa-server"></i> Infrastructure et virtualisation

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details class="realisation-item">
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold;">
      <span class="realisation-arrow">▶</span><i class="fa-solid fa-server" style="font-size: 24px; margin-right: 8px;"></i>Proxmox (VE, PBS, clustering)
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/realisations/proxmox.png" alt="Logo Proxmox" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Cluster Proxmox VE à haute disponibilité, couplé à un serveur de sauvegarde automatisé Proxmox Backup Server.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="/portfolio/achievements/proxmox" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details class="realisation-item">
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold;">
      <span class="realisation-arrow">▶</span><i class="fa-brands fa-docker" style="font-size: 24px; margin-right: 8px;"></i>
      Conteneurisation avec Docker / Portainer
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/realisations/docker.png" alt="Logo Docker" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Environnement de conteneurisation Docker administré via Portainer, avec durcissement de l'accès et de l'authentification, et sauvegardes régulières des images et bases de données.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="/portfolio/achievements/docker" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details class="realisation-item">
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold;">
      <span class="realisation-arrow">▶</span><i class="fa-solid fa-diagram-project" style="font-size: 24px; margin-right: 8px;"></i>Portail d'accès aux services internes
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/realisations/caddy.png" alt="Logo Caddy" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Reverse proxy Caddy comme point d'entrée unique vers les services internes, avec certificats générés automatiquement depuis la PKI interne.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="/portfolio/achievements/caddy" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

## <i class="fa-solid fa-shield-halved"></i> Sécurisation

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details class="realisation-item">
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold;">
      <span class="realisation-arrow">▶</span><i class="fa-solid fa-certificate" style="font-size: 24px; margin-right: 8px;"></i>
      Autorité de certification interne
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/realisations/opnsense.png" alt="Logo certificats" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      PKI interne à deux niveaux sous OPNsense.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="/portfolio/achievements/opnsense" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details class="realisation-item">
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold;">
      <span class="realisation-arrow">▶</span><i class="fa-solid fa-lock" style="font-size: 24px; margin-right: 8px;"></i>
      Gestion sécurisée de l'authentification
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/projects/authentification/password.png" alt="Logo mot de passe" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Déploiement de Bitwarden Cloud et GCPW sur une cinquantaine de postes, avec organisation des accès et formation des utilisateurs.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="/portfolio/achievements/authentification" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

## <i class="fa-solid fa-cloud-arrow-up"></i> Sauvegarde et administration

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details class="realisation-item">
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold;">
      <span class="realisation-arrow">▶</span><i class="fa-solid fa-cloud-arrow-down" style="font-size: 24px; margin-right: 8px;"></i>Redondance des données Cloud
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/realisations/rclone.png" alt="Logo Rclone" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Synchronisation hebdomadaire automatisée de Google Drive vers un NAS TrueNAS Scale, via un conteneur Rclone sur Proxmox.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="/portfolio/achievements/synchronisation" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details class="realisation-item">
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold;">
      <span class="realisation-arrow">▶</span><i class="fa-solid fa-desktop" style="font-size: 24px; margin-right: 8px;"></i>Centralisation de l'administration
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/projets/guacamole.png" alt="Logo Guacamole" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Accès RDP/SSH aux serveurs depuis un navigateur avec Guacamole, et administration centralisée des nœuds Proxmox via Proxmox Datacenter Manager.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="/portfolio/achievements/guacamole_pdm" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

<div style="border:1px solid #ccc; border-radius:8px; margin-bottom:1rem; overflow:hidden;">
  <details class="realisation-item">
    <summary style="background-color:#41b0f2; color:white; padding:0.5rem 1rem; font-weight:bold;">
      <span class="realisation-arrow">▶</span><i class="fa-solid fa-file-signature" style="font-size: 24px; margin-right: 8px;"></i>
      Solution de signature électronique
    </summary>
    <br>
    <div style="padding:1rem; text-align:center;">
      <img src="/assets/images/picture/realisations/opensign.png" alt="Logo OpenSign" style="max-width:200px; margin-bottom:1rem;">
    </div>
    <div style="padding:1rem; text-align:justify;">
      Serveur de gestion de documents et de signatures électroniques, accessible en ligne.
      <p style="margin-top: 1rem; text-align: right;">
        <a href="/portfolio/achievements/opensign" style="color: #41b0f2; text-decoration: none; font-weight: bold;">
          Voir la fiche complète →
        </a>
      </p>
    </div>
  </details>
</div>

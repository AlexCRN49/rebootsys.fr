---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: single
#title: "Accueil"
#subtitle: "Bienvenue sur mon Portfolio"
classes: full-width-content
sidebar:
  nav: false
  bio: true
---

<div class="hero-image">
  <img src="/assets/images/baie.jpg" alt="Switch" />
</div>

# Bonjour et Bienvenue !!!

<div class="typewriter-line">
  <span class="static-text">Je suis&nbsp;&nbsp;</span>
  <a href="/portfolio/about" class="typewriter-text">
    Alexis<span class="tight-space"> </span>COURTIN
  </a> 
</div>

<span id="typing-effect"></span>

<br>

<!-- Règles CSS pour corriger le retour à la ligne et le comportement du curseur -->
<style>
  #typing-effect {
    white-space: normal !important; /* Autorise le retour à la ligne sur les phrases longues */
    word-break: break-word;         /* Garantit la césure si la largeur d'écran est très réduite */
    display: inline;                /* Maintient l'élément en flux 'inline' */
  }

  .typed-cursor {
    display: inline-block;          /* Maintient le curseur aligné avec le dernier mot */
  }
</style>

<!-- Script d'initialisation de Typed.js -->
<script>
  document.addEventListener('DOMContentLoaded', function() {
    var typedStrings = [
      'Je suis en reconversion professionnelle',
      'Je suis en alternance',
      'Je suis en Licence Informatique spécialité Administration des systèmes et réseaux sécurisés'
    ];

    setTimeout(function() {
      var typed = new Typed('#typing-effect', {
        strings: typedStrings,
        typeSpeed: 50,
        backSpeed: 50,
        loop: true,
        showCursor: true,
        cursorChar: '|',
        autoInsertCss: false
      });
    }, 4000); // Délai de 4000 millisecondes (4 secondes)
  });
</script>

# Découvrez mon parcours

<style>
.wide-container {
  max-width: 1200px;
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1rem;
  padding-right: 1rem;
}

.card-container {
  display: flex;
  flex-wrap: nowrap;
  gap: 2rem;
  justify-content: space-between;
}

.card {
  flex: 0 0 30%;
  max-width: 30%;
  text-align: center;
  position: relative;
}

.tooltip-text {
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  background: #1C2028;
  color: #fff;
  padding: 0.5rem 0.9rem;
  border-radius: 6px;
  font-size: 0.85rem;
  width: 300px;
  text-align: center;
  line-height: 1.3;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.2s ease, transform 0.2s ease;
  pointer-events: none;
  z-index: 10;
}

.card:hover .tooltip-text {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(-6px);
}

.card img {
  max-width: 100%;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  transition: transform 0.2s ease;
}

.card img:hover {
  transform: scale(1.03);
}

/* Responsive : les cartes passent en colonne sur mobile */
@media (max-width: 900px) {
  .card-container {
    flex-wrap: wrap;
  }
  .card {
    flex: 0 0 100%;
    max-width: 100%;
  }
}
</style>

<div class="wide-container">

  <div class="card-container">

    <div class="card">
      <a href="/portfolio/training/">
        <img src="/assets/images/picture/home/training.jpg" alt="Formation">
      </a>
      <h3>Formation</h3>
      <span class="tooltip-text">BTS SIO SISR<br>Licence Informatique ASRS</span>
    </div>

    <div class="card">
      <a href="/portfolio/company/">
        <img src="/assets/images/picture/home/company.jpg" alt="Entreprise">
      </a>
      <h3>Alternance</h3>
      <span class="tooltip-text">Technicien Systèmes et Réseaux chez Delivagri (BTS SIO)</span>
    </div>

    <div class="card">
      <a href="/portfolio/realisations/">
        <img src="/assets/images/picture/home/skills.jpg" alt="Réalisations">
      </a>
      <h3>Réalisations</h3>
      <span class="tooltip-text">Provisionnement Proxmox via Ansible<br><br>Cluster de base de données en réplication asynchrone maître-esclave via MaxScale</span>
    </div>

    <!-- <div class="card">
      <a href="/portfolio/skills/">
        <img src="/assets/images/picture/home/skills.jpg" alt="Compétences">
      </a>
      <h3>Compétences</h3>
      <p>Mes compétences acquises.</p>
    </div> -->

  </div>

</div>

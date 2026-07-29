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
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
}

.card {
  text-align: center;
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

/* Responsive : 2 colonnes en tablette, 1 colonne en mobile */
@media (max-width: 900px) {
  .card-container {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 500px) {
  .card-container {
    grid-template-columns: 1fr;
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
    </div>

    <div class="card">
      <a href="/portfolio/company/">
        <img src="/assets/images/picture/home/company.jpg" alt="Alternance">
      </a>
      <h3>Alternance</h3>
    </div>

    <div class="card">
      <a href="/portfolio/realisations/">
        <img src="/assets/images/picture/home/skills.jpg" alt="Réalisations">
      </a>
      <h3>Réalisations</h3>
    </div>

    <!-- <div class="card">
      <a href="/portfolio/homelab/">
        <img src="/assets/images/picture/home/homelab.jpg" alt="Homelab">
      </a>
      <h3>Homelab</h3>
    </div>

    <div class="card">
      <a href="/portfolio/skills/">
        <img src="/assets/images/picture/home/skills.jpg" alt="Compétences">
      </a>
      <h3>Compétences</h3>
      <p>Mes compétences acquises.</p>
    </div> -->

  </div>

</div>
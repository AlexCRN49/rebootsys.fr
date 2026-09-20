---
title: "Veille technologique"
#date:
layout: single
permalink: /portfolio/watch
classes: wide
author_profile: true
read_time: true
show_date: false
toc: true
toc_label: "Sur cette page"
---

## <i class="fa-solid fa-rss"></i> Publications récentes

Cette liste est mise à jour automatiquement chaque semaine par une GitHub Action qui récupère les derniers avis et alertes du CERT-FR.

<ul>
{% for item in site.data.veille %}
  <li>
    <strong>{{ item.source }}</strong> —
    <a href="{{ item.link }}" target="_blank" rel="noopener">{{ item.title }}</a>
    {% if item.date %}<br><small>{{ item.date }}</small>{% endif %}
  </li>
{% endfor %}
</ul>

<!-- ## <i class="fa-solid fa-lightbulb"></i> Ce qui m'a marqué

> ⚠️ Section rédigée à la main, volontairement — voir la note ci-dessous.

- [À compléter : une CVE, un avis, une technique qui t'a marqué, avec ton avis en 2-3 lignes] -->

## <i class="fa-solid fa-list"></i> Mes sources

ANSSI, CERT-FR, MITRE ATT&CK, IT Connect, Le crabe Info, Le Mag IT - suivis via l'agrégateur Feedly.


<!-- Scroll horizontal -->
<section class="x mandatory-scroll-snapping scroll-snap-second" dir="ltr">
  <div class="slide">
    <a href="#" title="ANSSI">
      <img src="/assets/images/logo/watch/anssi.png" alt="Logo ANSSI">
    </a>
    <a href="#" title="CERT-FR">
      <img src="/assets/images/logo/watch/cert.png" alt="Logo CERT-FR">
    </a>
    <a href="#" title="MITRE ATT&CK">
      <img src="/assets/images/logo/watch/mitreattack.png" alt="Logo MITREATTACK">
    </a>
  </div>
  <div class="slide">
    <a href="#" title="IT CONNECT">
      <img src="/assets/images/logo/watch/itc.png" alt="Logo IT CONNECT">
    </a>
    <a href="#" title="Le Crabe Info">
      <img src="/assets/images/logo/watch/lci.jpg" alt="Logo Le Crabe Info">
    </a>
    <a href="#" title="Le Mag IT">
      <img src="/assets/images/logo/watch/lmi.jpg" alt="Logo Le Mag IT">
    </a>
  </div>
</section>
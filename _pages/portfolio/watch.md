---
title: "Veille technologique"
#date:
layout: single
permalink: /portfolio/watch/
classes: wide
author_profile: true
read_time: true
show_date: false
toc: true
toc_label: "Sur cette page"
---

## <i class="fa-solid fa-gear"></i> Principe de ma veille technologique

Ma veille technologique repose sur sept flux RSS répartis en trois catégories :
- les sources institutionnelles françaises avec l’**ANSSI** et le **CERT-FR**,  
- les ressources pratiques d’administration avec **IT-Connect**, **Korben** et **ZDNET France**,
- les médias spécialisés en cybersécurité avec **The Hacker News** et **BleepingComputer**.

Cette organisation me permet de suivre les recommandations officielles, les techniques d’administration des systèmes et réseaux, ainsi que les menaces actuelles.


## <i class="fa-solid fa-rss"></i> Publications récentes

Cette liste est mise à jour automatiquement chaque semaine par une GitHub Action qui récupère les flux RSS.

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

- [À compléter : une CVE, un avis, une technique qui t'a marqué, avec ton avis en 2-3 lignes] -->

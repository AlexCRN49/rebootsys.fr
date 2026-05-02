---
title: "Veille Cybersécurité"
layout: single
permalink: /watch/cyber-1/
classes: wide
author_profile: true
read_time: true
show_date: true
toc: true
toc_label: "Contenu"
---

## 🛡️ Cybersécurité

La cybersécurité est un enjeu majeur pour les entreprises, les gouvernements et les utilisateurs.  
Voici un suivi des actualités, outils et vulnérabilités que je surveille régulièrement.

---

### 🔥 Actualités récentes

<div class="rss-cards">
{% assign rss_posts = site.posts | sort: 'date' | reverse %}
{% for post in rss_posts limit:5 %}
  <div class="rss-card">
    <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
    <p class="rss-date">{{ post.date | date: "%d %B %Y" }}</p>
    {% if post.excerpt %}
      <p>{{ post.excerpt | strip_html | truncate: 120 }}</p>
    {% endif %}
  </div>
{% endfor %}
</div>


---

### 🧰 Outils et pratiques surveillés

- 🔐 **Surveillance de logs avec Fail2Ban, Wazuh**
- 📦 **Sécurisation des conteneurs Docker / LXC**
- 🔎 **Analyse de trafic avec Wireshark et Zeek**
- 🔍 **Pentest éthique avec Kali Linux, nmap, Nikto**

---

### 🔗 Ressources utiles

- [CVE Details](https://www.cvedetails.com)
- [Zataz](https://www.zataz.com) — site francophone de veille
- [The Hacker News](https://thehackernews.com)

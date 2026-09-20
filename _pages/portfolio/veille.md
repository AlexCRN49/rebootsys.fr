# Ma veille technologique

> ⚠️ Front matter Jekyll à adapter. Ci-dessous : uniquement le contenu de la page.

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

## <i class="fa-solid fa-lightbulb"></i> Ce qui m'a marqué

> ⚠️ Section rédigée à la main, volontairement — voir la note ci-dessous.

- [À compléter : une CVE, un avis, une technique qui t'a marqué, avec ton avis en 2-3 lignes]

## <i class="fa-solid fa-list"></i> Mes sources

CERT-FR, ANSSI, MITRE ATT&CK, Journal du Hack, IT Connect — suivies via Feedly.

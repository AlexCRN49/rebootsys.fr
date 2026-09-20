"""
Script de collecte automatique de veille technologique.
Récupère les derniers items de flux RSS et les écrit dans _data/veille.yml,
consommé ensuite par la page Jekyll portfolio/veille.

Exécuté automatiquement par la GitHub Action .github/workflows/veille.yml
"""

import feedparser
import yaml

# Liste des flux RSS à surveiller.
# Pour en ajouter un : trouve l'URL du flux RSS du site (souvent /feed/ ou /rss),
# vérifie qu'elle fonctionne dans un navigateur ou un lecteur RSS, puis ajoute-la ici.
FEEDS = [
    {"name": "CERT-FR - Avis", "url": "https://www.cert.ssi.gouv.fr/avis/feed/"},
    {"name": "CERT-FR - Alertes", "url": "https://www.cert.ssi.gouv.fr/alerte/feed/"},
    {"name": "ANSSI - Actualités", "url": "https://cyber.gouv.fr/actualites/rss/"},
    {"name": "IT-Connect", "url": "https://www.it-connect.fr/feed/"},
    {"name": "Le Crabe Info", "url": "https://lecrabeinfo.net/feed/"},
    {"name": "LeMagIT", "url": "https://www.lemagit.fr/rss/ContentSyndication.xml"},
]

MAX_ITEMS_PER_FEED = 5


def fetch_feed(feed):
    parsed = feedparser.parse(feed["url"])
    items = []
    for entry in parsed.entries[:MAX_ITEMS_PER_FEED]:
        items.append({
            "source": feed["name"],
            "title": entry.get("title", "").strip(),
            "link": entry.get("link", ""),
            "date": entry.get("published", entry.get("updated", "")),
        })
    return items


def main():
    all_items = []
    for feed in FEEDS:
        try:
            items = fetch_feed(feed)
            all_items.extend(items)
            print(f"OK - {feed['name']} : {len(items)} items récupérés")
        except Exception as e:
            print(f"ERREUR - {feed['name']} : {e}")

    with open("_data/veille.yml", "w", encoding="utf-8") as f:
        yaml.dump(all_items, f, allow_unicode=True, sort_keys=False)

    print(f"Total : {len(all_items)} items écrits dans _data/veille.yml")


if __name__ == "__main__":
    main()

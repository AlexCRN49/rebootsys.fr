# Utilisation de l'include timeline

## 1. Placer le fichier

Copier `timeline.html` dans le dossier `_includes/` de ton projet Jekyll.

## 2. Définir les étapes dans le front matter

Dans chaque fiche, ajouter le bloc `timeline` dans le front matter :

```yaml
timeline:
  - icon: "fas fa-flask"        # Classe Font Awesome
    title: "Titre de l'étape"   # Obligatoire
    detail: "Détail optionnel"  # Optionnel — s'affiche après le titre avec " : "
  - icon: "fas fa-check"
    title: "Dernière étape"     # Automatiquement en vert
```

## 3. Appeler l'include dans la page

Dans le corps de ta fiche Markdown, à l'endroit où tu veux afficher la timeline :

```liquid
{% include timeline.html steps=page.timeline %}
```

## 4. Icônes suggérées par type de tâche

| Tâche | Icône |
|-------|-------|
| Analyse / recueil du besoin | `fas fa-search` |
| Installation / déploiement | `fas fa-download` |
| Configuration | `fas fa-cog` |
| Réseau / câblage | `fas fa-network-wired` |
| Sécurité | `fas fa-shield-alt` |
| Tests | `fas fa-vial` |
| Documentation | `fas fa-file-alt` |
| Formation utilisateurs | `fas fa-chalkboard-teacher` |
| Sauvegarde | `fas fa-database` |
| Serveur / VM | `fas fa-server` |
| Validation / fin | `fas fa-check` |
| Migration | `fas fa-exchange-alt` |
| Script / automatisation | `fas fa-terminal` |

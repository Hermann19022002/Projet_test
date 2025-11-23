# Guide pour le dépôt GitHub - Version 1

## Fichiers à inclure dans GitHub

### Fichiers essentiels du code source :
```
v1_project[1]/
├── .gitignore              ✓ À inclure
├── Document.py             ✓ À inclure
├── RedditDocument.py       ✓ À inclure
├── ArxivDocument.py        ✓ À inclure
├── Author.py               ✓ À inclure
├── Corpus.py               ✓ À inclure
├── fetch_data.py           ✓ À inclure
├── main.py                 ✓ À inclure
├── test_simple.py          ✓ À inclure
├── requirements.txt        ✓ À inclure
├── requirements_minimal.txt ✓ À inclure
├── README.md               ✓ À inclure
├── QUICKSTART.md           ✓ À inclure
└── GITHUB.md               ✓ À inclure (ce fichier)
```

### Fichiers à NE PAS inclure (déjà dans .gitignore) :
- `corpus_v1.pkl` - Fichier généré par le programme
- `corpus_v1.csv` - Fichier généré par le programme
- `__pycache__/` - Cache Python
- `.vscode/` - Configuration IDE

## Commandes Git pour initialiser le dépôt

```bash
# 1. Se placer dans le dossier du projet
cd "v1_project[1]"

# 2. Initialiser le dépôt Git
git init

# 3. Ajouter tous les fichiers (le .gitignore filtrera automatiquement)
git add .

# 4. Premier commit
git commit -m "Version 1: Implémentation complète TDs 3-5"

# 5. Créer un tag pour la version 1
git tag -a v1 -m "Version 1 - Socle de base (TDs 3-5)"

# 6. Lier au dépôt GitHub (remplacer par votre URL)
git remote add origin https://github.com/VOTRE_USERNAME/VOTRE_REPO.git

# 7. Pousser le code
git push -u origin main
git push --tags
```

## Structure recommandée du README sur GitHub

Votre README.md actuel est déjà bien structuré. Assurez-vous qu'il contient :
- Description du projet
- Fonctionnalités implémentées
- Instructions d'installation
- Instructions d'utilisation
- Informations sur les versions

## Tags Git recommandés

Pour respecter les consignes du projet :
- `v1` : TDs 3-5 (socle de base)
- `v2` : TDs 6-7 (moteur de recherche) - à créer plus tard
- `v3` : TDs 8-10 (interface et extensions) - à créer plus tard

## Checklist avant le push

- [ ] .gitignore créé
- [ ] Tous les fichiers .py sont présents
- [ ] README.md à jour
- [ ] requirements.txt et requirements_minimal.txt présents
- [ ] Pas de fichiers générés (.pkl, .csv)
- [ ] Pas de données sensibles (clés API)
- [ ] Code testé et fonctionnel

## Note importante

Le fichier fetch_data.py contient des placeholders pour les identifiants API Reddit :
```python
client_id="VOTRE_CLIENT_ID",
client_secret="VOTRE_CLIENT_SECRET",
```


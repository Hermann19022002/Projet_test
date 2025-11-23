# Projet Python - Version 1 (TDs 3-5)
## Gestion de Corpus de documents Reddit et Arxiv

### 📋 Description

Ce projet implémente un système de gestion de corpus de documents provenant de Reddit et Arxiv. Il permet de récupérer, stocker, organiser et analyser des documents textuels avec leurs métadonnées.

**Version actuelle :** v1 (TDs 3 à 5)

### 🎯 Fonctionnalités implémentées

#### TD3 - Récupération de données
- ✅ Récupération de posts Reddit via l'API PRAW
- ✅ Récupération d'articles Arxiv via leur API XML
- ✅ Nettoyage et formatage des données

#### TD4 - Structuration objet
- ✅ Classe `Document` (titre, auteur, date, url, texte)
- ✅ Classe `Author` (name, ndoc, production)
- ✅ Classe `Corpus` (nom, authors, id2doc, ndoc, naut)
- ✅ Tri des documents par titre et par date
- ✅ Sauvegarde/chargement du corpus (pickle et CSV)

#### TD5 - Héritage et patrons de conception
- ✅ Classe `RedditDocument` héritant de `Document`
  - Attribut spécifique : `subreddit`, `nb_commentaires`
- ✅ Classe `ArxivDocument` héritant de `Document`
  - Attribut spécifique : `coauthors` (liste des co-auteurs)
- ✅ Méthode `getType()` dans les classes filles
- ✅ **Pattern Singleton** pour la classe Corpus
- ✅ **Pattern Factory** pour créer des documents (`DocumentFactory`)

### 📁 Structure du projet

```
v1_project[1]/
├── Document.py           # Classe Document et DocumentFactory
├── RedditDocument.py     # Classe fille pour documents Reddit
├── ArxivDocument.py      # Classe fille pour articles Arxiv
├── Author.py             # Classe pour gérer les auteurs
├── Corpus.py             # Classe Corpus avec Singleton
├── fetch_data.py         # Récupération de données APIs
├── main.py               # Programme principal avec démonstrations
├── requirements.txt      # Dépendances Python
└── README.md             # Ce fichier
```

### 🚀 Installation

```bash
pip install -r requirements.txt
```

#### Configuration API Reddit (optionnel)
   
   Pour utiliser la récupération de données Reddit, vous devez :
   
   a. Créer une application Reddit : https://www.reddit.com/prefs/apps
   
   b. Obtenir vos identifiants (client_id, client_secret)
   
   c. Modifier `fetch_data.py` ligne 26-28 :
   ```python
   reddit = praw.Reddit(
       client_id="VOTRE_CLIENT_ID",
       client_secret="VOTRE_CLIENT_SECRET",
       user_agent="python:corpus_app:v1.0 (by /u/VOTRE_USERNAME)"
   )
   ```

### 💻 Utilisation

#### Exécution du programme principal

```bash
python main.py
```

Le programme exécute 6 démonstrations :
1. **Factory Pattern** - Création de documents
2. **Opérations Corpus** - Ajout et gestion de documents
3. **Tri** - Tri par titre et par date
4. **Statistiques auteurs** - Analyse de la production des auteurs
5. **Sauvegarde/Chargement** - Persistance des données
6. **Récupération données** - Information sur l'API (optionnel)

#### Exemple d'utilisation du code

```python
from Corpus import Corpus
from Document import DocumentFactory

# Création d'un corpus (Singleton)
corpus = Corpus("MonCorpus")

# Création de documents via Factory
doc1 = DocumentFactory.create_document(
    "reddit",
    title="Titre du post",
    author="Auteur",
    date="2024-11-23",
    url="https://reddit.com/...",
    text="Contenu du post...",
    subreddit="python",
    nb_commentaires=42
)

# Ajout au corpus
corpus.add(doc1)

# Tri et affichage
for doc in corpus.list_by_title(5):
    print(doc)

# Sauvegarde
corpus.save("mon_corpus.pkl")
corpus.save_csv("mon_corpus.csv")

# Chargement
loaded_corpus = Corpus.load("mon_corpus.pkl")
```

### 📊 Exemples de sortie

```
============================================================
🐍 PROJET PYTHON - VERSION 1 (TDs 3-5)
    Gestion de Corpus de documents Reddit et Arxiv
============================================================

DÉMONSTRATION 1 : Factory Pattern
============================================================

✓ Document créé via Factory : Python 3.12 est sorti !
  Type: Reddit
  Détails: python, 145 commentaires

✓ Document créé via Factory : Deep Learning for Natural Language Processing
  Type: Arxiv
  Co-auteurs: Dr. Johnson, Prof. Lee, Dr. Martinez

[...]

✓ Corpus sauvegardé dans corpus_v1.pkl
✓ Corpus sauvegardé en CSV dans corpus_v1.csv
✓ Corpus chargé depuis corpus_v1.pkl
```

### 🧪 Tests

Le programme principal (`main.py`) inclut des tests complets de toutes les fonctionnalités :
- Création de documents via Factory
- Ajout de documents au corpus
- Tri par différents critères
- Statistiques sur les auteurs
- Sauvegarde et chargement de données

### 📦 Dépendances

- `praw==7.7.1` - API Reddit
- `xmltodict==0.13.0` - Parsing XML pour Arxiv
- `pandas==2.1.4` - Manipulation de données
- `numpy==1.26.2` - Calculs numériques

### 🏗️ Architecture

#### Patterns de conception utilisés

1. **Singleton Pattern** (Corpus)
   - Garantit une seule instance du corpus
   - Implémenté via `__new__`

2. **Factory Pattern** (DocumentFactory)
   - Création centralisée de documents
   - Support de différents types (Reddit, Arxiv)

3. **Héritage**
   - `Document` (classe mère)
   - `RedditDocument` et `ArxivDocument` (classes filles)

### 🔄 Évolution du projet

- **v1** (actuel) : TDs 3-5 - Socle de base
- **v2** (à venir) : TDs 6-7 - Moteur de recherche
- **v3** (à venir) : TDs 8-10 - Interface et extensions

### 👥 Auteurs

Projet réalisé dans le cadre du cours "Programmation de Spécialité : Python"
- Enseignant : Julien Velcin
- Enseignante : Tetiana Yemelianenko

### 📝 Notes importantes

- Le programme fonctionne sans connexion aux APIs (utilise des données de test)
- La récupération Reddit nécessite une configuration API (optionnel)
- La récupération Arxiv fonctionne sans authentification
- Python 3.10+ requis

### 🐛 Résolution de problèmes

**Problème** : Erreur de compilation numpy/pandas sur Python 3.13

- Cette version utilise le module `csv` standard à la place de pandas et fonctionne parfaitement

**Problème** : ImportError lors de l'exécution
- **Solution** : Vérifier que toutes les dépendances sont installées

**Problème** : Erreur avec l'API Reddit
- **Solution** : Vérifier la configuration des identifiants dans `fetch_data.py`

**Problème** : Erreur d'encodage sur Windows
- **Solution** : Le code utilise déjà `encoding='utf-8'` partout où nécessaire

**Problème** : Chemins UNC non pris en charge (sur serveur réseau Windows)

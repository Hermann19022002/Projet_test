# 🚀 Guide de Démarrage Rapide - Version 1

## Installation en 2 minutes

### Étape 1 : Installer les dépendances

```bash
pip install -r requirements_minimal.txt
```

✅ Compatible Python 3.10+ (y compris Python 3.13)

### Étape 2 : Tester l'installation

```bash
python test_simple.py
```

Vous devriez voir :
```
✅ TOUS LES TESTS RÉUSSIS !
```

### Étape 3 : Exécuter le programme complet

```bash
python main.py
```

C'est tout ! Le programme va exécuter 6 démonstrations complètes.

## 📝 Ce que fait le programme

Le programme crée un **corpus de documents** provenant de Reddit et Arxiv, avec :

1. ✅ Création automatique de documents via **Factory Pattern**
2. ✅ Gestion intelligente avec **Singleton Pattern**
3. ✅ Tri par titre et par date
4. ✅ Statistiques sur les auteurs
5. ✅ Sauvegarde en pickle et CSV
6. ✅ Chargement depuis fichiers

## 💡 Exemple simple d'utilisation

```python
from Corpus import Corpus
from Document import DocumentFactory

# Créer un corpus
corpus = Corpus("MonCorpus")

# Ajouter un document Reddit
doc = DocumentFactory.create_document(
    "reddit",
    title="Hello World !",
    author="Alice",
    date="2024-11-23",
    url="https://reddit.com/test",
    text="Mon premier document",
    subreddit="python",
    nb_commentaires=42
)
corpus.add(doc)

# Sauvegarder
corpus.save("mon_corpus.pkl")

print(corpus)  # Affiche : Corpus MonCorpus: 1 documents, 1 authors
```

## 🎯 Fichiers générés

Après exécution, vous trouverez :
- `corpus_v1.pkl` - Corpus sauvegardé (format binaire)
- `corpus_v1.csv` - Corpus au format CSV (lisible)

## ⚠️ Python 3.13 ?

Si vous avez une erreur avec pandas/numpy, c'est normal !
👉 Le projet utilise déjà `requirements_minimal.txt` qui fonctionne parfaitement.

## 📚 Pour aller plus loin

- Lisez `README.md` pour la documentation complète
- Consultez `main.py` pour voir tous les exemples
- Modifiez `fetch_data.py` pour ajouter vos identifiants API Reddit

## 🆘 Problème ?

Le test simple ne passe pas ? Vérifiez que vous êtes dans le bon répertoire :
```bash
cd v1_project[1]
python test_simple.py
```

Toujours bloqué ? Consultez la section "Résolution de problèmes" dans `README.md`

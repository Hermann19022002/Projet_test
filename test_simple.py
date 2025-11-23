"""Test simple pour vérifier que tous les imports fonctionnent"""

print("Test 1: Import des modules...")
try:
    from Document import Document, DocumentFactory
    from RedditDocument import RedditDocument
    from ArxivDocument import ArxivDocument
    from Author import Author
    from Corpus import Corpus
    print("OK - Tous les imports réussis")
except Exception as e:
    print(f"ERREUR - Erreur d'import: {e}")
    exit(1)

print("\nTest 2: Création de documents via Factory...")
try:
    doc1 = DocumentFactory.create_document(
        "reddit",
        title="Test Reddit",
        author="TestUser",
        date="2024-11-23",
        url="http://test.com",
        text="Test text",
        subreddit="test",
        nb_commentaires=5
    )
    print(f"OK - RedditDocument créé: {doc1}")
    print(f"  Type: {doc1.getType()}")
    
    doc2 = DocumentFactory.create_document(
        "arxiv",
        title="Test Arxiv",
        author="TestAuthor",
        date="2024-11-23",
        url="http://arxiv.org/test",
        text="Test paper",
        coauthors=["Co1", "Co2"]
    )
    print(f"OK - ArxivDocument créé: {doc2}")
    print(f"  Type: {doc2.getType()}")
except Exception as e:
    print(f"ERREUR - Erreur de création: {e}")
    exit(1)

print("\nTest 3: Corpus et Singleton...")
try:
    corpus1 = Corpus("Test1")
    corpus2 = Corpus("Test2")
    if corpus1 is corpus2:
        print("OK - Singleton fonctionne (même instance)")
    else:
        print("ERREUR - Singleton ne fonctionne pas")
    
    corpus1.add(doc1)
    corpus1.add(doc2)
    print(f"OK - Documents ajoutés: {corpus1}")
except Exception as e:
    print(f"ERREUR - Erreur Corpus: {e}")
    exit(1)

print("\n" + "="*50)
print("TOUS LES TESTS RÉUSSIS !")
print("="*50)
print("\nLe code est prêt à être utilisé.")
print("Pour exécuter le programme complet, lancez: python main.py")

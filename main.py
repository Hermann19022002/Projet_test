"""
Programme principal - Version 1 du projet Python
TDs 3 à 5 : Corpus de documents Reddit et Arxiv
"""

from Corpus import Corpus
from Document import DocumentFactory
from fetch_data import fetch_all
from datetime import datetime


def demo_factory_pattern():
    """Démonstration du Factory Pattern"""
    print("\n" + "="*60)
    print("DÉMONSTRATION 1 : Factory Pattern")
    print("="*60)
    
    # Création de documents via la Factory
    doc1 = DocumentFactory.create_document(
        "reddit",
        title="Python 3.12 est sorti !",
        author="Alice",
        date="2024-11-20",
        url="https://reddit.com/r/python/comments/123",
        text="La nouvelle version de Python apporte de nombreuses améliorations...",
        subreddit="python",
        nb_commentaires=145
    )
    
    doc2 = DocumentFactory.create_document(
        "arxiv",
        title="Deep Learning for Natural Language Processing",
        author="Dr. Smith",
        date="2024-10-15",
        url="https://arxiv.org/abs/2410.12345",
        text="This paper presents a novel approach to NLP using transformers...",
        coauthors=["Dr. Johnson", "Prof. Lee", "Dr. Martinez"]
    )
    
    print(f"\n✓ Document créé via Factory : {doc1}")
    print(f"  Type: {doc1.getType()}")
    print(f"  Détails: {doc1.subreddit}, {doc1.nb_commentaires} commentaires")
    
    print(f"\n✓ Document créé via Factory : {doc2}")
    print(f"  Type: {doc2.getType()}")
    print(f"  Co-auteurs: {', '.join(doc2.coauthors)}")
    
    return [doc1, doc2]


def demo_corpus_operations(documents):
    """Démonstration des opérations sur le Corpus"""
    print("\n" + "="*60)
    print("DÉMONSTRATION 2 : Opérations sur le Corpus (Singleton)")
    print("="*60)
    
    # Création du corpus (Singleton)
    corpus = Corpus("MonCorpusV1")
    print(f"\n✓ Corpus créé : {corpus}")
    
    # Ajout de documents
    print("\nAjout des documents au corpus...")
    for doc in documents:
        corpus.add(doc)
        print(f"  + {doc.title[:50]}... [{doc.getType()}]")
    
    print(f"\n✓ {corpus}")
    
    # Ajout de quelques documents supplémentaires pour les tests
    corpus.add(DocumentFactory.create_document(
        "reddit",
        title="AI Ethics Discussion",
        author="Bob",
        date="2024-11-15",
        url="https://reddit.com/r/artificial/comments/456",
        text="We need to discuss the ethical implications of AI...",
        subreddit="artificial",
        nb_commentaires=89
    ))
    
    corpus.add(DocumentFactory.create_document(
        "arxiv",
        title="Quantum Computing Applications",
        author="Dr. Zhang",
        date="2024-09-30",
        url="https://arxiv.org/abs/2409.98765",
        text="Exploring practical applications of quantum computing...",
        coauthors=["Dr. Kumar", "Prof. Chen"]
    ))
    
    corpus.add(DocumentFactory.create_document(
        "reddit",
        title="Best Python Libraries 2024",
        author="Charlie",
        date="2024-12-01",
        url="https://reddit.com/r/learnpython/comments/789",
        text="Here are my top picks for Python libraries this year...",
        subreddit="learnpython",
        nb_commentaires=234
    ))
    
    print(f"\n✓ Corpus final : {corpus}")
    
    return corpus


def demo_sorting(corpus):
    """Démonstration du tri des documents"""
    print("\n" + "="*60)
    print("DÉMONSTRATION 3 : Tri des documents")
    print("="*60)
    
    print("\nDocuments triés par titre (top 5):")
    for i, doc in enumerate(corpus.list_by_title(5), 1):
        print(f"  {i}. {doc.title} [{doc.getType()}]")
    
    print("\nDocuments triés par date (top 5):")
    for i, doc in enumerate(corpus.list_by_date(5), 1):
        print(f"  {i}. ({doc.date}) {doc.title[:40]}... [{doc.getType()}]")


def demo_authors(corpus):
    """Démonstration des statistiques auteurs"""
    print("\n" + "="*60)
    print("DÉMONSTRATION 4 : Statistiques des auteurs")
    print("="*60)
    
    print(f"\nNombre d'auteurs uniques : {corpus.naut}")
    print("\nDétails des auteurs :")
    
    for author_name, author in corpus.authors.items():
        print(f"\n  • {author}")
        docs_by_author = list(author.production.values())
        for doc in docs_by_author:
            print(f"    - {doc.title[:50]}... [{doc.getType()}]")


def demo_save_load(corpus):
    """Démonstration de la sauvegarde et du chargement"""
    print("\n" + "="*60)
    print("DÉMONSTRATION 5 : Sauvegarde et chargement")
    print("="*60)
    
    # Sauvegarde pickle
    print("\nSauvegarde du corpus (format pickle)...")
    corpus.save("corpus_v1.pkl")
    
    # Sauvegarde CSV
    print("\nSauvegarde du corpus (format CSV)...")
    corpus.save_csv("corpus_v1.csv")
    
    # Chargement
    print("\nChargement du corpus depuis fichier pickle...")
    loaded_corpus = Corpus.load("corpus_v1.pkl")
    print(f"✓ {loaded_corpus}")
    print(f"  Nombre de documents : {loaded_corpus.ndoc}")
    print(f"  Nombre d'auteurs : {loaded_corpus.naut}")


def demo_fetch_data():
    """Démonstration de la récupération de données (optionnel)"""
    print("\n" + "="*60)
    print("DÉMONSTRATION 6 : Récupération de données (OPTIONNEL)")
    print("="*60)
    
    print("\nNote : Cette fonctionnalité nécessite des identifiants API Reddit")
    print("  Configuration requise dans fetch_data.py :")
    print("  - client_id")
    print("  - client_secret")
    print("  - user_agent")
    
    print("\nPour activer cette fonctionnalité :")
    print("  1. Créer une application sur https://www.reddit.com/prefs/apps")
    print("  2. Configurer les identifiants dans fetch_data.py")
    print("  3. Décommenter l'appel à fetch_all() ci-dessous")
    
    # Décommenter pour tester la récupération réelle (nécessite configuration API)
    # try:
    #     documents = fetch_all("artificial intelligence", reddit_limit=5, arxiv_limit=5)
    #     corpus = Corpus("CorpusLive")
    #     for doc in documents:
    #         corpus.add(doc)
    #     print(f"\nCorpus avec données réelles : {corpus}")
    # except Exception as e:
    #     print(f"\nErreur : {e}")


def main():
    """Programme principal"""
    print("\n" + "="*60)
    print("PROJET PYTHON - VERSION 1 (TDs 3-5)")
    print("Gestion de Corpus de documents Reddit et Arxiv")
    print("="*60)
    
    # 1. Factory Pattern
    documents = demo_factory_pattern()
    
    # 2. Opérations sur le Corpus
    corpus = demo_corpus_operations(documents)
    
    # 3. Tri des documents
    demo_sorting(corpus)
    
    # 4. Statistiques auteurs
    demo_authors(corpus)
    
    # 5. Sauvegarde et chargement
    demo_save_load(corpus)
    
    # 6. Récupération de données (optionnel)
    demo_fetch_data()
    
    print("\n" + "="*60)
    print("TOUTES LES DÉMONSTRATIONS TERMINÉES")
    print("="*60)
    print("\nFonctionnalités implémentées (v1) :")
    print("  - Classe Document avec héritage (RedditDocument, ArxivDocument)")
    print("  - Classe Author avec gestion de production")
    print("  - Classe Corpus avec pattern Singleton")
    print("  - Factory Pattern pour création de documents")
    print("  - Méthode getType() dans les classes filles")
    print("  - Tri par titre et par date")
    print("  - Sauvegarde/chargement (pickle et CSV)")
    print("  - Récupération de données Reddit et Arxiv (fetch_data.py)")
    print("\nFichiers du projet :")
    print("  - Document.py (+ DocumentFactory)")
    print("  - RedditDocument.py")
    print("  - ArxivDocument.py")
    print("  - Author.py")
    print("  - Corpus.py")
    print("  - fetch_data.py")
    print("  - main.py")
    print("  - requirements.txt")
    print("\nPrêt pour la version 2 !")
    print()


if __name__ == "__main__":
    main()

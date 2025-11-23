"""
Module pour récupérer des données depuis Reddit et Arxiv
TD3 - Récupération de données
"""

import praw
import urllib.request
import xmltodict
from Document import DocumentFactory
from datetime import datetime


def fetch_reddit(query, limit=10):
    """
    Récupère des posts Reddit selon une requête
    
    Args:
        query: terme de recherche
        limit: nombre maximum de posts à récupérer
    
    Returns:
        Liste de RedditDocument
    """
    print(f"Recherche Reddit pour '{query}'...")
    
    # Configuration Reddit API
    # IMPORTANT: Remplacer par vos propres identifiants
    reddit = praw.Reddit(
        client_id="VOTRE_CLIENT_ID",
        client_secret="VOTRE_CLIENT_SECRET",
        user_agent="python:corpus_app:v1.0 (by /u/VOTRE_USERNAME)"
    )
    
    documents = []
    try:
        for post in reddit.subreddit("all").search(query, limit=limit):
            # Nettoyage du texte
            text = (post.selftext or post.title).replace("\n", " ")
            
            # Création du document via Factory
            doc = DocumentFactory.create_document(
                "reddit",
                title=post.title,
                author=post.author.name if post.author else "Anonyme",
                date=datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d'),
                url=f"https://reddit.com{post.permalink}",
                text=text,
                subreddit=post.subreddit.display_name,
                nb_commentaires=post.num_comments
            )
            documents.append(doc)
        
        print(f"OK - {len(documents)} documents Reddit récupérés")
    except Exception as e:
        print(f"ATTENTION - Erreur lors de la récupération Reddit: {e}")
    
    return documents


def fetch_arxiv(query, limit=10):
    """
    Récupère des articles Arxiv selon une requête
    
    Args:
        query: terme de recherche
        limit: nombre maximum d'articles à récupérer
    
    Returns:
        Liste de ArxivDocument
    """
    print(f"Recherche Arxiv pour '{query}'...")
    
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={limit}"
    
    documents = []
    try:
        data = urllib.request.urlopen(url).read()
        parsed = xmltodict.parse(data)
        
        entries = parsed["feed"].get("entry", [])
        if isinstance(entries, dict):
            entries = [entries]
        
        for entry in entries:
            # Extraction des auteurs
            authors_data = entry.get("author", [])
            if isinstance(authors_data, dict):
                authors_data = [authors_data]
            
            author_names = [a.get("name", "Anonyme") for a in authors_data]
            main_author = author_names[0] if author_names else "Anonyme"
            coauthors = author_names[1:] if len(author_names) > 1 else []
            
            # Nettoyage du texte
            text = entry.get("summary", "").replace("\n", " ")
            
            # Date de publication
            published = entry.get("published", "")[:10]  # Format YYYY-MM-DD
            
            # Création du document via Factory
            doc = DocumentFactory.create_document(
                "arxiv",
                title=entry.get("title", "Sans titre").replace("\n", " "),
                author=main_author,
                date=published,
                url=entry.get("id", ""),
                text=text,
                coauthors=coauthors
            )
            documents.append(doc)
        
        print(f"OK - {len(documents)} documents Arxiv récupérés")
    except Exception as e:
        print(f"ATTENTION - Erreur lors de la récupération Arxiv: {e}")
    
    return documents


def fetch_all(query, reddit_limit=10, arxiv_limit=10):
    """
    Récupère des documents depuis Reddit et Arxiv
    
    Args:
        query: terme de recherche
        reddit_limit: nombre de posts Reddit
        arxiv_limit: nombre d'articles Arxiv
    
    Returns:
        Liste de tous les documents
    """
    print(f"\n{'='*50}")
    print(f"Récupération de documents sur le thème : {query}")
    print(f"{'='*50}\n")
    
    documents = []
    documents.extend(fetch_reddit(query, reddit_limit))
    documents.extend(fetch_arxiv(query, arxiv_limit))
    
    print(f"\nTotal: {len(documents)} documents récupérés\n")
    
    return documents

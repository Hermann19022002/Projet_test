class Document:
    def __init__(self, title, author, date, url, text):
        self.title = title
        self.author = author
        self.date = date
        self.url = url
        self.text = text
        self.type = "Document"  # Type générique

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Date: {self.date}")
        print(f"URL: {self.url}")
        print(f"Text: {self.text[:200]}...")

    def getType(self):
        return self.type

    def __str__(self):
        return f"{self.title}"


class DocumentFactory:
    """Factory Pattern pour créer des documents selon leur type"""
    
    @staticmethod
    def create_document(doc_type, **kwargs):
        """
        Crée un document selon son type
        
        Args:
            doc_type: "reddit" ou "arxiv"
            **kwargs: paramètres spécifiques au type de document
        
        Returns:
            Instance de RedditDocument ou ArxivDocument
        """
        from RedditDocument import RedditDocument
        from ArxivDocument import ArxivDocument
        
        if doc_type.lower() == "reddit":
            return RedditDocument(
                title=kwargs.get('title', 'Sans titre'),
                author=kwargs.get('author', 'Anonyme'),
                date=kwargs.get('date', ''),
                url=kwargs.get('url', ''),
                text=kwargs.get('text', ''),
                subreddit=kwargs.get('subreddit', 'unknown'),
                nb_commentaires=kwargs.get('nb_commentaires', 0)
            )
        elif doc_type.lower() == "arxiv":
            return ArxivDocument(
                title=kwargs.get('title', 'Sans titre'),
                author=kwargs.get('author', 'Anonyme'),
                date=kwargs.get('date', ''),
                url=kwargs.get('url', ''),
                text=kwargs.get('text', ''),
                coauthors=kwargs.get('coauthors', [])
            )
        else:
            raise ValueError(f"Type de document inconnu: {doc_type}")

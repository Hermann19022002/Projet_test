from Document import Document

class ArxivDocument(Document):
    def __init__(self, title, author, date, url, text, coauthors):
        super().__init__(title, author, date, url, text)
        self.coauthors = coauthors  # Liste des co-auteurs
        self.type = "Arxiv"  # Ajout du champ type
    
    def getType(self):
        return "Arxiv"
    
    def __str__(self):
        coauth_str = ", ".join(self.coauthors) if self.coauthors else "Aucun"
        return f"[Arxiv] {self.title} - Co-auteurs: {coauth_str}"

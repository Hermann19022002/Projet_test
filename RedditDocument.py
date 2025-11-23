from Document import Document

class RedditDocument(Document):
    def __init__(self, title, author, date, url, text, subreddit, nb_commentaires=0):
        super().__init__(title, author, date, url, text)
        self.subreddit = subreddit
        self.nb_commentaires = nb_commentaires  # Attribut spécifique Reddit
        self.type = "Reddit"  # Ajout du champ type
    
    def getType(self):
        return "Reddit"
    
    def __str__(self):
        return f"[Reddit] {self.title} (r/{self.subreddit}) - {self.nb_commentaires} commentaires"

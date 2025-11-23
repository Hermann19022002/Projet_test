from Author import Author
import pickle
import os
import csv

class Corpus:
    _instance = None

    def __new__(cls, name=None):
        if cls._instance is None:
            cls._instance = super(Corpus, cls).__new__(cls)
        return cls._instance

    def __init__(self, name=None):
        if hasattr(self, "_initialized"): 
            return
        self._initialized = True
        self.name = name if name else "Corpus"
        self.id2doc = {}
        self.authors = {}
        self.ndoc = 0
        self.naut = 0
    
    def __reduce__(self):
        """Support pour pickle avec Singleton"""
        return (self.__class__, (self.name,), self.__dict__)
    
    def __setstate__(self, state):
        """Restauration de l'état depuis pickle"""
        self.__dict__.update(state)

    def add(self, doc):
        doc_id = self.ndoc
        self.id2doc[doc_id] = doc
        self.ndoc += 1

        if doc.author not in self.authors:
            self.authors[doc.author] = Author(doc.author)
            self.naut += 1

        self.authors[doc.author].add(doc_id, doc)

    def list_by_title(self, n=5):
        docs = sorted(self.id2doc.values(), key=lambda d: d.title)
        return docs[:n]

    def list_by_date(self, n=5):
        docs = sorted(self.id2doc.values(), key=lambda d: d.date)
        return docs[:n]

    def save(self, filename=None):
        """Sauvegarde le corpus sur disque (format pickle)"""
        if filename is None:
            filename = f"{self.name}.pkl"
        
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        print(f"✓ Corpus sauvegardé dans {filename}")
    
    def save_csv(self, filename=None):
        """Sauvegarde le corpus au format CSV (utilise le module csv standard)"""
        if filename is None:
            filename = f"{self.name}.csv"
        
        # Collecter les données
        data = []
        fieldnames = ['id', 'title', 'author', 'date', 'url', 'text', 'type']
        
        for doc_id, doc in self.id2doc.items():
            row = {
                'id': doc_id,
                'title': doc.title,
                'author': doc.author,
                'date': doc.date,
                'url': doc.url,
                'text': doc.text,
                'type': doc.getType()
            }
            
            # Ajouter les champs spécifiques
            if hasattr(doc, 'subreddit'):
                row['subreddit'] = doc.subreddit
                row['nb_commentaires'] = doc.nb_commentaires
                if 'subreddit' not in fieldnames:
                    fieldnames.extend(['subreddit', 'nb_commentaires'])
            elif hasattr(doc, 'coauthors'):
                row['coauthors'] = ', '.join(doc.coauthors) if doc.coauthors else ''
                if 'coauthors' not in fieldnames:
                    fieldnames.append('coauthors')
            
            data.append(row)
        
        # Écrire le CSV
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"✓ Corpus sauvegardé en CSV dans {filename}")
    
    @staticmethod
    def load(filename):
        """Charge un corpus depuis un fichier pickle"""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Fichier {filename} introuvable")
        
        with open(filename, 'rb') as f:
            corpus = pickle.load(f)
        print(f"✓ Corpus chargé depuis {filename}")
        return corpus

    def __repr__(self):
        return f"Corpus {self.name}: {self.ndoc} documents, {self.naut} authors"

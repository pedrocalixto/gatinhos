from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random

db = SQLAlchemy()

class CatFact(db.Model):
    """Modelo para armazenar curiosidades sobre gatos."""
    id = db.Column(db.Integer, primary_key=True)
    fact = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), nullable=True)
    icon = db.Column(db.String(50), default="fa-paw")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    @classmethod
    def get_random(cls, limit=1):
        """Retorna uma ou mais curiosidades aleatórias."""
        # Conta o número total de curiosidades
        count = cls.query.count()
        
        if count == 0:
            return []
            
        # Se pedimos mais curiosidades do que existem, retornamos todas em ordem aleatória
        if limit >= count:
            return cls.query.all()
        
        # Seleciona curiosidades aleatórias sem repetição
        facts = []
        used_ids = set()
        
        while len(facts) < limit:
            # Gera um ID aleatório entre 1 e o número total de curiosidades
            random_id = random.randint(1, count)
            
            # Evita repetições
            if random_id in used_ids:
                continue
                
            fact = cls.query.get(random_id)
            if fact:
                facts.append(fact)
                used_ids.add(random_id)
        
        return facts

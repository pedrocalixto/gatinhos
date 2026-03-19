from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import datetime

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
        """Retorna curiosidades aleatórias sem repetição."""
        return cls.query.order_by(func.random()).limit(limit).all()

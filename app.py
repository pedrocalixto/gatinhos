import os
import logging
from datetime import datetime
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, CatFact

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'cat_facts.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

_INITIAL_FACTS = [
    {"fact": "Gatos passam 70% de suas vidas dormindo", "icon": "fa-moon"},
    {"fact": "Um grupo de gatos é chamado de 'gataria'", "icon": "fa-users"},
    {"fact": "Gatos têm 32 músculos em cada orelha", "icon": "fa-ear-listen"},
    {"fact": "O ronronar de um gato pode ajudar na cura de ossos e músculos", "icon": "fa-heart-pulse"},
    {"fact": "Gatos podem pular até 6 vezes sua altura", "icon": "fa-person-running"},
    {"fact": "O nariz de cada gato tem uma impressão única, como nossas digitais", "icon": "fa-fingerprint"},
    {"fact": "Gatos domésticos correm a uma velocidade de até 48 km/h", "icon": "fa-gauge-high"},
    {"fact": "Gatos não conseguem sentir o sabor doce", "icon": "fa-cookie"},
    {"fact": "Gatos têm uma memória de 16 horas (humanos têm 5 minutos)", "icon": "fa-brain"},
    {"fact": "Gatos podem fazer mais de 100 sons vocais, enquanto cachorros fazem apenas 10", "icon": "fa-volume-high"},
    {"fact": "Gatos usam seus bigodes para medir se cabem em espaços apertados", "icon": "fa-ruler"},
    {"fact": "Gatos podem beber água do mar (os rins filtram o sal)", "icon": "fa-droplet"},
    {"fact": "O cérebro de um gato é 90% similar ao cérebro humano", "icon": "fa-brain"},
    {"fact": "Gatos têm 5 dedos nas patas dianteiras, mas apenas 4 nas traseiras", "icon": "fa-paw"},
    {"fact": "Gatos não enxergam diretamente abaixo do nariz", "icon": "fa-eye"},
    {"fact": "A visão noturna dos gatos é 6 vezes melhor que a dos humanos", "icon": "fa-moon"},
    {"fact": "Gatos podem girar suas orelhas 180 graus", "icon": "fa-ear-listen"},
    {"fact": "A maioria dos gatos não tem cílios", "icon": "fa-eye"},
    {"fact": "Gatos têm o terceiro conjunto de pálpebras chamado 'membrana nictitante'", "icon": "fa-eye"},
    {"fact": "Gatos podem fazer cerca de 100 vocalizações diferentes", "icon": "fa-comment"},
]


def seed_db():
    for item in _INITIAL_FACTS:
        db.session.add(CatFact(fact=item["fact"], icon=item["icon"]))
    db.session.commit()
    logger.info("Banco de dados populado com %d curiosidades.", len(_INITIAL_FACTS))


with app.app_context():
    db.create_all()
    if CatFact.query.count() == 0:
        seed_db()


@app.context_processor
def inject_globals():
    return {"current_year": datetime.utcnow().year}


@app.route('/')
def home():
    facts = CatFact.get_random(3)
    return render_template('index.html', facts=facts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/api/facts/random')
def random_facts():
    facts = CatFact.get_random(3)
    return jsonify([{"id": f.id, "fact": f.fact, "icon": f.icon} for f in facts])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

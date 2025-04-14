from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, CatFact
import os
import random

app = Flask(__name__)

# Configuração do banco de dados
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'cat_facts.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados
db.init_app(app)

# Função para inicializar o banco de dados com algumas curiosidades
def init_db():
    with app.app_context():
        db.create_all()
        
        # Só adiciona curiosidades se a tabela estiver vazia
        if CatFact.query.count() == 0:
            curiosidades = [
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
                {"fact": "Gatos podem fazer cerca de 100 vocalizações diferentes", "icon": "fa-comment"}
            ]
            
            for item in curiosidades:
                fact = CatFact(fact=item["fact"], icon=item["icon"])
                db.session.add(fact)
            
            db.session.commit()
            print("Banco de dados inicializado com 20 curiosidades sobre gatos!")

# Inicializa o banco de dados antes de qualquer requisição
with app.app_context():
    try:
        db.create_all()
        # Verifica se já existem dados
        if CatFact.query.count() == 0:
            init_db()
            print("Banco de dados inicializado com sucesso!")
        else:
            print("Banco de dados já existe e contém dados.")
    except Exception as e:
        print(f"Erro ao inicializar o banco de dados: {e}")

@app.route('/')
def home():
    # Tenta obter curiosidades, se falhar, retorna uma lista vazia
    try:
        facts = CatFact.get_random(3)
    except Exception as e:
        print(f"Erro ao obter curiosidades: {e}")
        facts = []
    return render_template('index.html', facts=facts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/facts/random', methods=['GET'])
def random_facts():
    """API endpoint para obter curiosidades aleatórias."""
    try:
        facts = CatFact.get_random(3)
        return jsonify([{
            'id': fact.id,
            'fact': fact.fact,
            'icon': fact.icon
        } for fact in facts])
    except Exception as e:
        print(f"Erro na API de curiosidades: {e}")
        return jsonify([]), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

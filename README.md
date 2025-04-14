# Galeria de Gatinhos Fofos

Uma aplicação web Flask que exibe uma galeria de fotos de gatos fofos com curiosidades que mudam dinamicamente a cada 10 segundos.

## Tecnologias Utilizadas

- Python 3.9
- Flask 3.1.0
- SQLAlchemy (banco de dados)
- HTML5
- CSS3
- JavaScript
- Docker

## Funcionalidades

- Galeria de fotos de gatos
- Curiosidades sobre gatos que mudam automaticamente a cada 10 segundos
- API REST para fornecer curiosidades aleatórias
- Banco de dados SQLite para armazenamento escalável de curiosidades

## Como Executar Localmente

### Usando Python e venv

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a aplicação:
   ```bash
   python app.py
   ```
5. Acesse http://localhost:8080 no navegador

### Usando Docker

1. Clone o repositório
2. Construa a imagem Docker:
   ```bash
   docker build -t galeria-gatinhos .
   ```
3. Execute o contêiner:
   ```bash
   docker run -p 8080:8080 galeria-gatinhos
   ```
4. Acesse http://localhost:8080 no navegador

### Usando Docker Compose

1. Clone o repositório
2. Execute com Docker Compose:
   ```bash
   docker-compose up
   ```
3. Acesse http://localhost:8080 no navegador

## Estrutura do Projeto

```
flask_app/
├── app.py                  # Aplicação Flask principal
├── models.py               # Modelos de banco de dados
├── cat_facts.db            # Banco de dados SQLite
├── requirements.txt        # Dependências Python
├── Dockerfile              # Configuração para construir a imagem Docker
├── docker-compose.yml      # Configuração para Docker Compose
├── static/                 # Arquivos estáticos
│   ├── css/
│   │   └── style.css       # Estilos CSS
│   └── js/
│       └── script.js       # JavaScript
└── templates/              # Templates HTML
    ├── index.html          # Página inicial
    └── about.html          # Página sobre
```

## API Endpoints

- `GET /api/facts/random`: Retorna 3 curiosidades aleatórias sobre gatos

## Escalabilidade

Este projeto foi projetado pensando em escalabilidade:

1. **Banco de dados**: Usa SQLAlchemy que permite migrar facilmente para PostgreSQL ou MySQL
2. **Arquitetura API**: Separação clara entre frontend e backend
3. **Containerização**: Pronto para implantação em qualquer plataforma que suporte Docker

## Implantação

Esta aplicação pode ser implantada em várias plataformas que suportam contêineres Docker, como:

- AWS App Runner
- Google Cloud Run
- Azure Container Instances
- Render
- Fly.io

## Licença

Este projeto é distribuído sob a licença MIT.

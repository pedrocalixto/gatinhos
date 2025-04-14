# Galeria de Gatinhos Fofos

Uma aplicação web Flask que exibe uma galeria de fotos de gatos fofos.

## Tecnologias Utilizadas

- Python 3.9
- Flask 3.1.0
- HTML5
- CSS3
- JavaScript
- Docker

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

## Implantação

Esta aplicação pode ser implantada em várias plataformas que suportam contêineres Docker, como:

- AWS App Runner
- Google Cloud Run
- Azure Container Instances
- Render
- Fly.io

## Licença

Este projeto é distribuído sob a licença MIT.

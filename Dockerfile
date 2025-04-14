FROM python:3.9-slim

WORKDIR /app

# Copiar requirements e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copiar o resto do código
COPY . .

# Expor a porta que a aplicação usará
EXPOSE 8080

# Comando para iniciar a aplicação com gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo do diretório local para o contêiner
COPY . .

EXPOSE 8084

CMD ["streamlit", "run", "app.py", "--server.port=8084"]
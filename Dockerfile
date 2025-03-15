FROM python:3.11

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar arquivo de requisitos para container
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo código do projeto para dentro do container
COPY . .

# Expor a porta 5000 para acesso externo
EXPOSE 5000

# Definir o comando para rodar a aplicação
CMD ["python", "app.py"]

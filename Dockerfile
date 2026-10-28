# Utilisation d'une image Python légère
FROM python:3.9-slim

# Répertoire de travail
WORKDIR /app

# Installation de Flask et de l'outil ping pour l'exercice d'injection
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir flask

# Copie de l'application
COPY vulnerable_app.py .

# Exposition du port
EXPOSE 5000

# Lancement de l'application
CMD ["python", "vulnerable_app.py"]

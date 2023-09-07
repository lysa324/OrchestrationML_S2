# Utilisez l'image de base Python
FROM python:3.8-slim

# Installez libGL avec apt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Définissez le répertoire de travail dans l'image
WORKDIR /OrchestrationProject
# Copiez le code de l'application Flask dans le conteneur
COPY . /OrchestrationProject
# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt /OrchestrationProject
# Installez les dépendances nécessaires
RUN pip install -r requirements.txt
# Exposez le port sur lequel l'application Flask écoute
EXPOSE 5000
# Commande pour exécuter l'application Flask lorsque le conteneur est démarré
CMD ["python", "app.py"]





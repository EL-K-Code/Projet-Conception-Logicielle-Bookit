# On part d'un environnement Ubuntu 22.04
FROM ubuntu:22.04

# Définir le répertoire de travail
WORKDIR /src/backend

# Installer Python et pip, et ajouter un alias pour python
RUN apt-get update && apt-get install -y python3-pip && ln -s /usr/bin/python3 /usr/bin/python

# Copier les fichiers de notre projet dans l'environnement
COPY . .

# Installer les dépendances
RUN python3 -m pip install -r requirements.txt

# Exposer le port de l'application
EXPOSE 8000

# Lancer l'application Django
ENTRYPOINT ["sh", "-c", "python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver"]
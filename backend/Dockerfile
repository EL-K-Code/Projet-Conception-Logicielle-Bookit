# Utilisation d'une image légère basée sur Python 3.11 et Debian
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /backend

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Créer un environnement virtuel pour isoler les dépendances
ENV VIRTUAL_ENV=/env
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copier uniquement les fichiers nécessaires pour installer les dépendances
COPY requirements.txt .

# Installer les dépendances avec pip
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copier le reste du projet dans le conteneur
COPY . .

# Exposer le port de l'application
EXPOSE 8000

# Exécuter les migrations et lancer Gunicorn
CMD ["sh", "-c", "python manage.py makemigrations --noinput && \
                   python manage.py migrate --noinput && \
                   python manage.py collectstatic --noinput && \
                   gunicorn --bind 0.0.0.0:8000 --workers 3 backend.wsgi:application"]

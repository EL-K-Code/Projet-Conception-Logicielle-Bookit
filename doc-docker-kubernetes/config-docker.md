# Documentation : Configuration Docker pour un Projet Django

## 1. Prérequis
Avant de commencer, assurez-vous d'avoir installé :
- [Docker](https://docs.docker.com/get-docker/) sur votre machine
- Un compte sur [Docker Hub](https://hub.docker.com/)
- Un projet Django fonctionnel avec un fichier `requirements.txt`

## 2. Création du `Dockerfile`
Créez un fichier nommé `Dockerfile` à la racine de votre projet et ajoutez-y le contenu suivant :

```dockerfile
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
ENTRYPOINT ["sh", "-c", "python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]
```

## 3. Construction de l'image Docker
Exécutez la commande suivante dans le terminal, à la racine du projet :

```sh
docker build -t django-docker .
```

Cela va créer une image Docker nommée `django-docker`.

## 4. Exécution du conteneur
Pour exécuter le conteneur, utilisez la commande suivante :

```sh
docker run django-docker
```

Votre application Django sera accessible à l'adresse : [http://localhost:8000](http://localhost:8000)

## 5. Connexion à Docker Hub
Connectez-vous à votre compte Docker Hub avec la commande :

```sh
docker login
```

Entrez votre nom d'utilisateur et votre mot de passe Docker Hub lorsque cela est demandé.

## 6. Taguer l'image pour Docker Hub
Avant de publier l'image, il faut lui attribuer un tag avec votre nom d'utilisateur Docker Hub. Si votre identifiant Docker Hub est `yatoute`, exécutez :

```sh
docker tag django-docker yatoute/django-docker:latest
```

## 7. Pousser l'image sur Docker Hub
Envoyez l'image sur Docker Hub avec la commande :

```sh
docker push yatoute/django-docker:latest
```

## 8. Télécharger et exécuter l'image depuis Docker Hub
Une fois l'image publiée, vous pouvez la récupérer et l'exécuter sur n'importe quelle machine en exécutant :

```sh
docker pull yatoute/django-docker:latest
```

Puis exécutez :

```sh
docker run yatoute/django-docker:latest
```

L'application sera de nouveau accessible à [http://localhost:8000](http://localhost:8000).

## 9. Nettoyage des images et conteneurs inutilisés
Pour éviter d'accumuler des images et des conteneurs inutiles, vous pouvez exécuter :

```sh
docker system prune -a
```

Cela supprimera toutes les images, conteneurs et volumes non utilisés.

## 10. Conclusion
Cette documentation vous guide à travers toutes les étapes nécessaires pour créer, exécuter et publier une image Docker pour un projet Django sur Docker Hub. Vous pouvez maintenant facilement déployer votre application sur n'importe quel environnement prenant en charge Docker ! 🚀


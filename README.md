# Bookit - Application de réservation de services

## 🎓 Contexte

Ce projet a été réalisé dans le cadre du cours de **Conception de logiciel** en **2ᵉ année** à l'**ENSAI**. Il vise à appliquer les principes d'ingénierie de développement afin de concevoir une application complète et fonctionnelle répondant à un besoin concret.

## 📖 Description

**Bookit** est une application de réservation des services tels que des **bus**, **salles** et **matériaux**. Elle permet de centraliser la gestion des ressources, de visualiser les disponibilités des ressources, et de permettre aux utilisateurs de faire des réservations facilement.

### ✨ Fonctionnalités
...


### 💻 Technologies utilisées
- [ ] Backend: Django
- [ ] Frontend: React
- [ ] Base de données: SQLite
- [ ] Conteneurisation et déploiement : Docker, Kubernetes
- [ ] CI/CD : GitHub Actions


## 🚀 Quickstart (Démarrage rapide)

L'application est déployée et accessible à l'adresse suivante: [https://bookit-ensai.kub.sspcloud.fr/](https://bookit-ensai.kub.sspcloud.fr/)



## 📌 Instructions

L'application peut être lancée de plusieurs manières :

- [ ] **Lancer via Docker Hub (images préconstruites)**
- [ ] **Lancer localement**
   - **Avec image Docker**
   - **sans image Docker**

## :arrow_forward: Lancer l'application via Docker Hub
Assurez-vous d'avoir installé Docker (ou Docker Desktop sous windows) sur votre machine.
Vous pouvez lancer l'application en utilisant les images docker que nous avons publié sur Docker Hub

- [ ] Pull des images depuis Docker Hub

```bash
docker pull richard0209/bookit-backend:latest
docker pull richard0209/bookit-frontend:latest
```

- [ ] Exécuter l'application
  - backend
  ```bash
  docker run -p 8000:8000 richard0209/bookit-backend:latest
  ```
  - frontend
  ```bash
  docker run -p 8000:8000 richard0209/bookit-frontend:latest
  ```
  Une fois les deux services lancés, le backend sera accessible à l'adresse: [http://127.0.0.1:8000](http://127.0.0.1:8000) et le frontend à l'adresse: [http://localhost:3000](http://localhost:3000)


## :arrow_forward: Lancer l'application localement

- Clonez ce dépôt:
```bash
git clone https://github.com/EL-K-Code/Projet-Conception-Logicielle-Bookit.git
```
- Positionnez-vous dans le projet cloné
```bash
cd Projet-Conception-Logicielle-Bookit
```

L'application peut être lancée avec ou sans image Docker

- [ ] Lancer l'application via Docker
 - backend:
Accédez au répertoireee backend, construisez puis lancez l'image Docker:
```bash
cd backend
docker build -t backend .
docker run -p 8000:8000 backend
```
L'application backend sera accessible à [http://127.0.0.1:8000](http://127.0.0.1:8000)

- Frontend
Accédez au répertoireee frontend, construisez puis lancez l'image Docker:
```bash
cd frontend
docker build -t frontend .
docker run -p 3000:3000 frontend
```
L'application frontend sera accessible à [http://localhost:3000](http://localhost:3000)

### :arrow_forward: Lancer l'application sans image Docker

- [ ] Créez un environnement virtuel :
  ```bash
  python -m venv venv
  ```
  - Sur Mac/Linux
  ```bash
  source venv/bin/activate
  ```
  - Sur windows
     ```bash
     source venv/bin/activate
     ```

 - Installer les dépendances
   - Backend
  ```bash
  pip install -r backend/requirements.txt
  ```
   - Frontend
  ```bash
  cd frontend
  npm install
  ```

 - [ ] Définir les variables d'environnements
  Pour configurer l'application, vous devez définir certaines variables d'environnement nécessaires au bon fonctionnement de l'application.

   1. Copiez le fichier `.env.template` et renommez-le en `.env` :

      Exécutez les commandes suivantes pour dupliquer le fichier modèle .env.template et créer le fichier .env qui sera utilisé par votre application :
```bash
cp ../backend/.env.template ./backend/.env.template.env
cp ../frontend/.env.template ./frontend/.env.template.env
```

   2. Complétez les variables d'environnement dans le fichier .env du backend :

      Ouvrez le fichier .env du backend et remplissez les variables avec les valeurs appropriées. Certaines variables sont déjà renseignées par défaut(vous pouvez ajuster ces valeurs selon vos besoins)
      
Voici les variables à compléter :
- **DJANGO_SUPERUSER_USERNAME** : Entrez un nom d'utilisateur pour l'administrateur Django.
- **DJANGO_SUPERUSER_EMAIL** : Entrez l'email de l'administrateur Django.
- **DJANGO_SUPERUSER_PASSWORD** : Entrez un mot de passe pour l'administrateur Django.
- **DJANGO_SECRET_KEY** : Générez une nouvelle clé secrète Django. Vous pouvez utiliser la commande suivante pour générer une clé secrète:
  ```bash
  python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
  ```
- **DJANGO_DEBUG** : Valeur par défaut True. Changez-la en False pour un environnement de production.
- **DJANGO_ALLOWED_HOSTS** : Liste des hôtes autorisés. La valeur par défaut inclut localhost et 127.0.0.1, mais Vous devrez l'ajuster si votre application doit être accessible depuis d'autres hôtes.
- **FRONTEND_APP_API_URL** : Liste des URL de l'API frontend. La valeur par défaut inclut http://localhost:3000 pour un développement local et https://bookit-ensai.kub.sspcloud.fr pour la production.
- **EMAIL_HOST_USER** et **EMAIL_HOST_PASSWORD** : Entrez les informations de connexion de votre serveur SMTP pour l'envoi d'emails. Ces champs sont vides par défaut. Si vous utilisez Gmail, remplissez-les avec les informations nécessaires pour l'authentification via le service Gmail. Assurez-vous de bien sécuriser ces informations. 


- [ ] Appliquer les migrations :
```bash
cd ../backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
L'application backend sera accessible à [http://127.0.0.1:8000](http://127.0.0.1:8000)

- [ ] Lancer le frontend :
```bash
cd frontend
npm run dev
```
L'application frontend sera accessible à [http://localhost:3000](http://localhost:3000)

## 📈 Tests unitaires
Les tests unitaires sont automatisés à chaque push via GitHub Actions.
Pour lancer les tests manuellement, exécutez:
```bash
cd backend
coverage run manage.py test
coverage html
```
Ensuite vous pouvez ouvrir le fichier `coverage_report/index.html` dans votre navigateur pour consulter le rapport de couverture des tests.


## 🛠️ Automatisation

Le projet utilise GitHub Actions pour automatiser les tests, la vérification du code à chaque push et le déploiement des images Docker vers Docker Hub


## 👥 Équipe du projet
Le projet est réalisé par les élèves:
- [ ] Richard GOZAN
- [ ] Alex LABOU
- [ ] Yatoute MINTOMA

Sous la supervision de :
- [ ] Antoine Brunetti: Analyste Développeur à l'INSEE
- [ ] Oriane Foussard: Analyste Développeur à l'INSEE

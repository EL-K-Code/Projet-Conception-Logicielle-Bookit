# Bookit - Application de réservation de services

## 🎓 Contexte

Ce projet a été réalisé dans le cadre du cours de **Conception de logiciel** en **2ᵉ année** à l'**ENSAI**. Il vise à appliquer les principes d'ingénierie de développement afin de concevoir une application complète et fonctionnelle répondant à un besoin concret.

## 📖 Description

**Bookit** est une application de réservation des services tels que des **bus**, **salles** et **matériaux**. Elle permet de centraliser la gestion des ressources, de visualiser les disponibilités des ressources, et de permettre aux utilisateurs de faire des réservations facilement.

### ✨ Fonctionaités
...


### 💻 Technologies utilités
- [ ] Backend: Django
- [ ] Frontend: React
- [ ] Base de données: SQLite
- [ ] Conteneurisation et déploiement : Docker, Kubernetes
- [ ] CI/CD : GitHub Actions


## 🚀 Quickstart (Démarrage rapide)



## 📌 Instructions

L'application peut être lancée de plusieurs manières :

- [ ] **Lancer via Docker Hub (images préconstruites)**
- [ ] **Lancer localement**
   - **Avec image Docker**
   - **sans image Docker**

## :arrow_forward: Lancer l'application via Docker Hub
Assurez-vous d'avoir installé Docker (ou Docker Desktop sous windows) sur votre machine.
Vous pouvez lancer l'application en utilisant les images docker que nous avons publié sur Dockerhub

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
  Une fois les deux services lancés, le backend sera accessible à [http://127.0.0.1:8000/](http://127.0.0.1:8000/) et le frontend à [http://127.0.0.1:3000/](http://127.0.0.1:3000/)


## :arrow_forward: Lancer l'application localement

- Clonez ce dépôt:
```bash
git clone https://github.com/EL-K-Code/Projet-Conception-Logicielle-Bookit.git
```
- Positionnez-vous dans le projet cloné
```bash
cd Projet-Conception-Logicielle-Bookit.git
```

L'aplication peut être lancée avec ou sans image Docker

- [ ] Lancer l'application via Docker
 - backend:
Accédez au répertoire backend, construisez puis lancez l'image Docker:
```bash
cd backend
docker build -t backend .
docker run -p 8000:8000 backend
```
L'application backend sera accessible à [http://127.0.0.1:8000](http://127.0.0.1:8000)

- Frontend
Accédez au répertoire frontend, construisez puis lancez l'image Docker:
```bash
cd frontend
docker build -t frontend .
docker run -p 3000:3000 frontend
```
L'application frontend sera accessible à http://127.0.0.1:3000

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

   - Allez dans le dossier backend et créez un fichier `.env` en utilisant le modèle `.env.template` fourni.
   - Allez dans le dossier frontend et créez un fichier `.env` en utilisant également le modèle `.env.template` fourni.
Les fichiers .env.template contiennent la liste des variables d'environnement nécessaires, avec des commentaires pour vous aider à les configurer correctement.

- [ ] Appliquer les migrations :
```bash
cd ../backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


L'application backend sera accessible à http://127.0.0.1:8000

- [ ] Lancer le frontend :
```bash
cd frontend
npm run dev
```
L'application frontend sera accessible à http://127.0.0.1:3000

## 📈 Tests unitaires
Les tests unitaires sont automatisés à chaque push via GitHub Actions.
Pour lancer les tests manuellement, exécutez:
```bash
cd backend
coverage run manage.py test
coverage html
```
Ensuite vous pouvez ouvrir le fichier `coverage_report/index.html` dans votre navigateur pour consulter le rapport de couverture des test.


## 🛠️ Automatisation

Le projet utilise GitHub Actions pour automatiser les tests, la vérification du code à chaque push et le dépoiement des images Docker vers DockerHub


## 👥 Équipe du projet
Le projet est réalisé par les élèves:
- [ ] Richard GOZAN
- [ ] Alex LABOU
- [ ] Yatoute MINTOMA

Sous la supervision de :
- [ ] Antoine Brunetti: Analyste Développeur à l'INSEE
- [ ] Oriane Foussard: Analyste Développeur à l'INSEE























# Bookit - Application de réservation de services

## 🎓 Contexte du projet

Ce projet a été réalisé dans le cadre du cours de **Conception de logiciel** en **2ᵉ année** à l'**ENSAI**. Il vise à appliquer les principes d'ingénierie de développement afin de concevoir une application complète et fonctionnelle répondant à un besoin concret.

## 📖 Description de l'application

**Bookit** est une application de réservation des services tels que des **bus**, **salles** et **matériaux**. Elle permet de centraliser la gestion des ressources, de visualiser les disponibilités des ressources, et de permettre aux utilisateurs de faire des réservations facilement.

### ✨ Fonctionaités principales
...


### 💻 Technologies utilités
...


## 🚀 Quickstart (Démarrage rapide)

L'application est déployée et accessible à l'adresse suivante : [https://bookit-ensai.kub.sspcloud.fr/](https://bookit-ensai.kub.sspcloud.fr/)


## 📌 Instructions

L'application peut être lancée de plusieurs manières :

1. **Lancer via Docker Hub (images préconstruites)**
2. **Lancer localement**
   - **Avec image Docker**
   - **sans image Docker**

### 1. Lancer l'application via Docker Hub
Assurez-vous d'avoir installé Docker (ou Docker Desktop sous windows) sur votre machine.
Vous pouvez lancer l'application en utilisant les images docker que nous avons publié sur Dockerhub

- [ ] Pull des images depuis Docker Hub 

```bash
docker pull <votre-username>/frontend:<version>
docker pull <votre-username>/backend:<version>
```

- [ ] Exécuter l'application
  - backend
  ```bash
  docker run -p 8000:8000 richard0209/bookit-backend:<version>
  ```
  - frontend
  ```bash
  docker run -p 8000:8000 richard0209/bookit-frontend:<version>
  ```
  Une fois les deux services lancés, le backend sera accessible à [http://localhost:8000](http://localhost:8000) et le frontend à [http://localhost:3000](http://localhost:3000)
    

### 2. Lancer l'application localement

- Clonez ce dépôt:
```bash
`git clone https://github.com/EL-K-Code/Projet-Conception-Logicielle-Bookit.git`
```
- Positionnez-vous dans le projet cloné
`cd Projet-Conception-Logicielle-Bookit.git`

L'aplication peut être lancée avec ou sans image Docker

- [ ] Lancer l'application via Docker
 - backend:
Accédez au répertoire backend, construisez puis lancez l'image Docker:
```bash
cd backend
docker build -t backend .
docker run -p 8000:8000 backend
```
L'application backend sera accessible à [http://localhost:8000](http://localhost:8000)

- Frontend
Accédez au répertoire frontend, construisez puis lancez l'image Docker:
```bash
cd frontend
docker build -t frontend .
docker run -p 3000:3000 frontend
```
L'application frontend sera accessible à http://localhost:3000

- [ ] Lancer l'application sans image Docker

 - Créez un environnement virtuel :
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

 - Définir les variables d'environnements
  Pour configurer l'application, vous devez définir certaines variables d'environnement nécessaires au bon fonctionnement de l'application.

  - Allez dans le dossier backend et créez un fichier `.env` en utilisant le modèle `.env.template` fourni.
  - Allez dans le dossier frontend et créez un fichier `.env` en utilisant également le modèle `.env.template` fourni.
Les fichiers .env.template contiennent la liste des variables d'environnement nécessaires, avec des commentaires pour vous aider à les configurer correctement.

Lancer le backend :
```bash
cd ../backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
L'application backend sera accessible à http://localhost:8000

Lancer le frontend :
```bash
cd frontend
npm run dev
```
L'application frontend sera accessible à http://localhost:3000










  








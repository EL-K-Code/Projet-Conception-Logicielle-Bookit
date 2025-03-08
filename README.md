# Bookit - Application de réservation de services

## 🎓 Contexte

Ce projet a été réalisé dans le cadre du cours de **Conception de logiciel** en **2ᵉ année** à l'**ENSAI**. Il vise à appliquer les principes d'ingénierie de développement afin de concevoir une application complète et fonctionnelle répondant à un besoin concret.

## 📖 Description

**Bookit** est une application de réservation des services tels que des **bus**, **salles** et **matériaux**. Elle permet de centraliser la gestion des ressources, de visualiser les disponibilités des ressources, et de permettre aux utilisateurs de faire des réservations facilement.

### ✨ Fonctionaités

Notre application présente trois types d'utilisateurs : les consommateurs (Consumer), les administrateurs d'évènements (Event Admin) et les administrateurs (Admin)

- [ ] Event Admin : Créer, supprimer et modifier les évènements
- [ ] Consumer : Consulter les évènements, Réserver les évènements, Annuler une réservation

A noter qu'une notification via mail est envoyé à tous les consommateurs lorsqu'un évènement est créé ou mis à jour par l'administrateur évènement.


### 💻 Technologies utilisées
- [ ] Backend: Django
- [ ] Frontend: React
- [ ] Base de données: SQLite
- [ ] Conteneurisation et déploiement : Docker, Kubernetes
- [ ] CI/CD : GitHub Actions


## 🚀 Quickstart (Démarrage rapide)

### :arrow_forward: Application délpoyée

L'application est déployée avec sur Kubernetes et accessible à l'adresse suivante: [https://bookit-ensai.kub.sspcloud.fr/](https://bookit-ensai.kub.sspcloud.fr/)

### :arrow_forward: Lancer l'application via Docker Hub

Assurez-vous d'avoir installé Docker (ou Docker Desktop sous windows) sur votre machine.
Vous allez lancer l'application en utilisant les images docker que nous avons publié sur Docker Hub


- [ ] Cloner le projet:
      
   Récupérez le code source en clonant ce dépôt sur votre machine locale :
```bash
git clone https://github.com/EL-K-Code/Projet-Conception-Logicielle-Bookit.git
cd Projet-Conception-Logicielle-Bookit
```

- [ ] Configurer les variables d'environnements:
      
   Avant de lancer l'application, vous devez définir certaines variables d'environnement nécessaires au bon fonctionnement de l'application:
      
1. Copiez le fichier `.env.template` et renommez-le en `.env` :

   Exécutez les commandes suivantes pour dupliquer le fichier modèle .env.template et créer le fichier .env qui sera utilisé par votre application :
```bash
cp backend/.env.template backend/.env
cp frontend/.env.template frontend/.env
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
- **FRONTEND_APP_API_URL** : Liste des URL de l'API frontend. La valeur par défaut inclut http://localhost:3000, https://bookit-ensai.kub.sspcloud.fr
- **EMAIL_HOST_USER** et **EMAIL_HOST_PASSWORD** : Entrez les informations de connexion de votre serveur SMTP pour l'envoi d'emails. Ces champs sont vides par défaut. Si vous utilisez Gmail, remplissez-les avec les informations nécessaires pour l'authentification via le service Gmail. Assurez-vous de bien sécuriser ces informations.

- [ ] Pull des images depuis Docker Hub

```bash
docker pull richard0209/bookit-backend:latest
docker pull richard0209/bookit-frontend:latest
```

- [ ] Exécuter l'application
  - backend
  ```bash
  docker run --env-file .env -p 8000:8000 richard0209/bookit-backend:latest
  ```
  📌 **Remarque** : Assurez-vous que le fichier .env est présent dans le dossier depuis lequel vous exécutez la commande(veuillez consulter la section Variables d'environnement plus bas pour obtenir des instructions sur la création et la configuration de ce fichier)
   Si ce n'est pas le cas, spécifiez son chemin complet :
   ```bash
   docker run --env-file /chemin/vers/.env -p 8000:8000 richard0209/bookit-backend:latest
   ```

  - frontend
  ```bash
  docker run -d -e NEXT_PUBLIC_API_URL=http://127.0.0.1:8000 -p 3000:3000 --name bookit-frontend richard0209/bookit-frontend:latest
  ```
  
- [ ] Accéder à l'application :

Une fois les services démarrés, accédez au :

Backend :  [http://127.0.0.1:8000](http://127.0.0.1:8000)
Frontend : [http://localhost:3000](http://localhost:3000)


  
## 📌 Instructions pour lancer l'application en local

Assurez-vous d'avoir **Node.js** installé sur votre machine(pour le frontend).
Vous pouvez installer Node.js via nvm, le gestionnaire de version de Node.js:

- [ ] Installation de nvm (Node Version Manager)
      
   Si nvm n'est pas déjà installé sur votre système, suivez les étapes ci-dessous pour l'installer

   1. Installer nvm
   
   Exécutez la commande suivante dans votre terminal pour installer nvm :
   ```bash
   curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash
   ```
   2. Appliquer les modifications au shell
   
   Après l'installation de nvm, rechargez votre shell pour appliquer les changements :
   ```bash
   source ~/.bashrc
   ```
   3. Vérifier l'installation de nvm
   
   Vérifiez que nvm est correctement installé en exécutant :
   ```bash
   nvm --version
   ```
   Si la version de nvm est affichée, l'installation a réussi.

- [ ] Installer Node.js 20

Une fois nvm installé, vous pouvez utiliser nvm pour installer la version de Node.js 20, qui est requise pour le projet. Exécutez les commandes suivantes :

   1. Installer Node.js 20 :
   ```bash
   nvm install 20
   ```

   2. Définir Node.js 20 comme version par défaut :
   ```bash
   nvm use 20
   nvm alias default 20
   ```

   3. Vérifier l'installation de Node.js et npm
   
   Pour confirmer que Node.js et npm sont installés correctement, exécutez les commandes suivantes :
   ```bash
   node -v
   npm -v
   ```
   Cela affichera les versions respectives de Node.js et npm.
   

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

 - [ ] Installer les dépendances
   - Backend
  ```bash
  pip install -r backend/requirements.txt
  ```
   - Frontend
  ```bash
  cd frontend
  npm install
  ```

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

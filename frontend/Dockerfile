# Utilisation d'une image Node Alpine légère
FROM node:18-alpine AS dev

# Définition du répertoire de travail
WORKDIR /frontend

# Copie des fichiers de dépendances pour optimiser le cache Docker
COPY package.json package-lock.json ./

# Installation des dépendances en mode développement
RUN npm install --frozen-lockfile

# Copie du reste du projet
COPY . .

# Exposition du port utilisé par Next.js en mode développement
EXPOSE 3000

# Lancement de l'application en mode développement
CMD ["npm", "run", "dev", "--", "-H", "0.0.0.0"]


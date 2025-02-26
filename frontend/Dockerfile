# Utilisation d'une image Node Alpine légère
FROM node:18-alpine AS build

# Définition du répertoire de travail
WORKDIR /frontend

# Copie des fichiers de dépendances pour optimiser le cache Docker
COPY package.json package-lock.json ./

# Installation des dépendances en mode production
RUN npm install --frozen-lockfile

# Copie du reste du projet
COPY . .

# Construction de l’application frontend (Next.js)
RUN npm run build

# Utilisation d'un serveur léger pour servir l'application Next.js
FROM node:18-alpine AS production

WORKDIR /frontend

# Copie des fichiers générés après le build
COPY --from=build /frontend ./

# Exposition du port sur lequel Next.js va tourner
EXPOSE 3000

# Commande de démarrage pour Next.js (démarrage en mode production)
CMD ["npm", "run", "start"]

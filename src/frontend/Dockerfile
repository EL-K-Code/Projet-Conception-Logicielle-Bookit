# Utilisation d'une image Node Alpine légère
FROM node:18-alpine AS build

# Définition du répertoire de travail
WORKDIR /src/frontend

# Copie des fichiers de dépendances pour optimiser le cache Docker
COPY package.json package-lock.json ./

# Installation des dépendances en mode production
RUN npm install --frozen-lockfile

# Copie du reste du projet
COPY . .

# Définition des variables d’environnement
ENV VITE_API_URL=""

# ARG VITE_ENVIRONNEMENT=local
# ENV VITE_ENVIRONNEMENT=${VITE_ENVIRONNEMENT}

# Construction de l’application frontend
RUN npm run build

# Utilisation d'un serveur léger pour servir les fichiers statiques
FROM node:18-alpine AS production

WORKDIR /src/frontend

# Installation d'un serveur HTTP léger pour les fichiers statiques
RUN npm install -g serve

# Copie des fichiers générés après le build
COPY --from=build /src/frontend/dist /src/frontend/dist

# Exposition du port 3000
EXPOSE 3000

# Commande de démarrage
CMD ["serve", "-s", "dist", "-l", "3000"]

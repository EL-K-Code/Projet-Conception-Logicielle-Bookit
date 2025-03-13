# Étape 1 : Build de l'application Next.js
FROM node:18-alpine AS builder

# Définition du répertoire de travail
WORKDIR /frontend

# Copie uniquement les fichiers nécessaires pour l'installation des dépendances
COPY package.json package-lock.json ./

# Installation des dépendances en mode production
RUN npm ci --frozen-lockfile

# Copie du reste du projet
COPY . .

# Build de l'application Next.js
RUN npm run build

# Étape 2 : Image finale pour l'exécution en production
FROM node:18-alpine AS runner

# Définition du répertoire de travail
WORKDIR /frontend

# Copier uniquement le nécessaire depuis l'étape de build
COPY --from=builder /frontend/package.json /frontend/package-lock.json ./
COPY --from=builder /frontend/.next ./.next
COPY --from=builder /frontend/public ./public
COPY --from=builder /frontend/node_modules ./node_modules

# Exposition du port Next.js en production
EXPOSE 3000

# Lancer l'application Next.js en mode production
CMD ["npm", "run", "start"]

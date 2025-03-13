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



# # Étape 1 : Build de l'application
# FROM node:18-alpine AS builder

# # Définition du répertoire de travail
# WORKDIR /frontend

# # Copie des fichiers de dépendances pour optimiser le cache Docker
# COPY package.json package-lock.json ./

# # Installation des dépendances en mode production
# RUN npm ci --frozen-lockfile

# # Copie du reste du projet
# COPY . .

# # Variables d'environnement pour désactiver la télémétrie et ESLint pendant le build
# ENV NEXT_TELEMETRY_DISABLED=1
# ENV NEXT_PUBLIC_ESLINT_IGNORE=true

# # Build de l'application Next.js
# RUN npm run build

# # Étape 2 : Exécution de l'application en mode production
# FROM node:18-alpine AS runner

# WORKDIR /frontend

# # Copie des fichiers nécessaires depuis l'étape builder
# COPY --from=builder /frontend/package.json /frontend/package.json
# COPY --from=builder /frontend/node_modules /frontend/node_modules
# COPY --from=builder /frontend/.next /frontend/.next
# COPY --from=builder /frontend/public /frontend/public

# # Exposition du port utilisé par Next.js
# EXPOSE 3000

# # Lancement de l'application en mode production
# CMD ["npm", "run", "start"]

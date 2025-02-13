## Installation `nvm` (Node Version Manager)

### 1. Installer `nvm`
Ouvre un terminal et exécute la commande suivante pour installer `nvm` :

```sh
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash
```

Ensuite, recharge ton shell pour appliquer les modifications :

```sh
source ~/.bashrc 
```

### 2. Vérifier l'installation
Assure-toi que `nvm` est bien installé en exécutant :

```sh
nvm --version
```

### 3. Installer Node.js 20
Maintenant, installe Node.js 20 avec :

```sh
nvm install 20
```

Et définis-le comme version par défaut :

```sh
nvm use 20
nvm alias default 20
```

Tu peux vérifier si l’installation a réussi en affichant la version de Node.js :

```sh
node -v
```


## Initialisation d'un projet react avec un template react de Vite 

```sh
cd src
npm create vite@latest frontend -- --template react
```

## Iinstallation de `axios` (pour les requêtes HTTP en JavaScript), `react-router-dom` (routing pour React) et `jwt-decode`

```sh
cd frontend
npm install axios react-router-dom jwt-decode
```

---

## 🌱 **Qu'est-ce qu'un `root` en React ?**  
En React, **"root"** fait référence au **point d'ancrage** où toute l'application React est montée dans la page HTML.  

### 🔹 **Comment fonctionne le "root" ?**
- Quand on crée une application React, on doit dire à React **où afficher l'interface utilisateur** dans le DOM.
- Cet endroit est **une div dans le fichier `index.html`**, souvent avec `id="root"`.
- React prend le contrôle de cette div et y affiche tous les composants.

📌 **Exemple de fichier `index.html` :**  
```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <title>Mon App React</title>
</head>
<body>
    <div id="root"></div>  <!-- L'application React sera affichée ici -->
</body>
</html>
```

---

## 🚀 **Qu'est-ce qu'un "root concurrent" ?**  
Avec **React 18**, la création du root a changé pour introduire **le mode concurrent** (**Concurrent Mode**), qui améliore la fluidité et les performances.

### 🔹 **Avant React 18 (root classique)**
Avant React 18, on utilisait :
```js
ReactDOM.render(<App />, document.getElementById('root'));
```
❌ **Problème** :  
- Cette méthode bloquait tout le rendu jusqu'à ce que **tout soit chargé**, ce qui pouvait ralentir l'affichage.  

---

### 🔹 **Depuis React 18 (root concurrent)**
React 18 introduit :
```js
ReactDOM.createRoot(document.getElementById('root')).render(<App />);
```
✅ **Avantages du mode concurrent :**  
- 📌 **Mises à jour non bloquantes** → React peut afficher une partie de l'interface pendant qu'il charge le reste.  
- 📌 **Meilleure gestion des priorités** → Il peut traiter d'abord les interactions utilisateur (ex : clics, formulaires) avant les mises à jour lourdes.  
- 📌 **Transitions fluides** → Améliore les animations et transitions.  
- 📌 **Meilleur rendu asynchrone** → Compatible avec des outils comme `Suspense` pour charger du contenu progressivement.  

---

## 🛠 **Exemple concret de Root Concurrent**
Imaginons une application qui charge une liste d’articles et affiche un bouton pour ajouter un commentaire.  

### **🔴 Sans mode concurrent**  
L'ajout d'un commentaire **bloquerait** l'affichage des articles en cours de chargement. 😬  

### **🟢 Avec mode concurrent**  
L'ajout du commentaire est prioritaire, tandis que React continue de charger les articles **sans bloquer** l'interface. 🎉  

```js
import React, { useState, useTransition } from "react";
import ReactDOM from "react-dom/client";

function App() {
    const [comments, setComments] = useState([]);
    const [isPending, startTransition] = useTransition();  // Permet d'exécuter des tâches en priorité

    function addComment() {
        startTransition(() => {
            setComments([...comments, "Nouveau commentaire"]);
        });
    }

    return (
        <div>
            <button onClick={addComment}>Ajouter un commentaire</button>
            {isPending && <p>Chargement...</p>}
            <ul>
                {comments.map((c, i) => (
                    <li key={i}>{c}</li>
                ))}
            </ul>
        </div>
    );
}

// 🚀 Création du root en mode concurrent
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
```
🔹 **`useTransition` permet de rendre l'ajout du commentaire prioritaire**, sans ralentir l'affichage des autres éléments.

---

## 📝 **Résumé**
| 🏷️ Terme | 📌 Explication |
|----------|--------------|
| **Root (classique)** | Le point où React monte l'application dans le DOM. |
| **Root Concurrent** | Nouvelle façon de créer un root (avec `createRoot`), qui améliore la gestion des mises à jour et des priorités. |
| **Avantages** | Rendu plus fluide, non bloquant, meilleur support des animations et chargements progressifs. |

👉 **En bref** : React 18 permet un rendu **plus réactif** et **optimisé** avec le root concurrent. 🚀

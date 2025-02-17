## 🌿 **Le DOM (Document Object Model) expliqué simplement**  

Le **DOM (Document Object Model)** est une **représentation en mémoire** d'une page web sous forme d'un arbre d'objets manipulables par JavaScript.  

### 🏗 **1. Qu'est-ce que le DOM ?**  
Quand un navigateur charge une page web (`index.html` par exemple), il ne comprend pas directement le fichier HTML. Il **convertit** le code HTML en une structure hiérarchique en mémoire : **le DOM**.  

🔹 **HTML initial**  
```html
<!DOCTYPE html>
  <head>
    <title>Ma page</title>
  </head>
  <body>
    <h1>Bonjour, monde !</h1>
    <p>Bienvenue sur ma page.</p>
  </body>
</html>
```

🔹 **Représentation en DOM**  
```
document
 ├── html
 │    ├── head
 │    │    ├── title
 │    │    │    └── "Ma page"
 │    ├── body
 │         ├── h1
 │         │    └── "Bonjour, monde !"
 │         ├── p
 │              └── "Bienvenue sur ma page."
```
👉 Le DOM transforme le HTML en **un arbre d'éléments (nœuds)** que JavaScript peut modifier dynamiquement.  

---

## 🔥 **2. Manipuler le DOM avec JavaScript**  

Comme le DOM est un objet JavaScript, on peut le modifier avec des scripts.  

### ✏️ **Exemple : Modifier un élément du DOM**  
Si on veut changer le texte du `<h1>`, on peut écrire :  
```js
document.querySelector("h1").textContent = "Salut, React !";
```
✅ Le navigateur mettra instantanément à jour le texte du `<h1>` dans la page.  

---

## ⚡ **3. Le Virtual DOM en React**  

Avec React, on utilise **un DOM virtuel (Virtual DOM)** pour optimiser les mises à jour.  

🔹 **DOM classique (lent) :**  
Chaque changement met à jour **directement** le DOM réel, ce qui peut être **lent**.  
```js
document.getElementById("message").textContent = "Nouveau message";
```
👉 Si plusieurs éléments changent, chaque mise à jour prend du temps.  

🔹 **Virtual DOM (React - rapide) :**  
1. React crée un **Virtual DOM** (une copie du DOM réel).  
2. Il compare les différences (diffing).  
3. Il met à jour uniquement les éléments qui ont changé (reconciliation).  

Exemple avec React :  
```jsx
function App() {
  const [message, setMessage] = React.useState("Bonjour !");
  
  return (
    <div>
      <h1>{message}</h1>
      <button onClick={() => setMessage("Salut, React !")}>Changer</button>
    </div>
  );
}
```
👉 **Seul le texte du `<h1>` est mis à jour**, sans toucher au reste du DOM.  

---

## 🏆 **Résumé**  
| Notion | Explication |
|--------|------------|
| **DOM** | Représentation en mémoire de la page HTML sous forme d'arbre. |
| **Manipulation du DOM** | JavaScript peut modifier les éléments (`document.querySelector().textContent`). |
| **Virtual DOM** | React crée une copie du DOM, détecte les changements et met à jour uniquement ce qui a changé. |
| **Avantage du Virtual DOM** | Optimise les performances en évitant les mises à jour inutiles du DOM réel. |

En gros, **React ne modifie que ce qui est nécessaire**, ce qui rend l’application plus fluide et rapide ! 🚀
import { ACCESS_TOKEN } from "@/store/constants";
import axios from "axios";

// Créer une instance de Axios
// pour rediriger les requêtes vers notre serveur django REST framework.
const api = axios.create({

    baseURL: process.env.NEXT_PUBLIC_API_URL || "https://backend-ensai.kub.sspcloud.fr",
})


// Un interceptor pour ajouter l'authorization token à chaque requête
api.interceptors.request.use(
  async (config) => {
    // Définit auth_required 
    const requiresAuth = config.auth_required ?? true;

    if (requiresAuth) {
      const accessToken = localStorage.getItem(ACCESS_TOKEN);
      if (accessToken) {
        config.headers.Authorization = `Bearer ${accessToken}`;
      } else {
        console.warn("⚠️ Authentification requise mais aucun token trouvé !");
      }
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);



// Intercepteur pour gérer les erreurs généré par le serveur
api.interceptors.response.use(
    (response) => {
      return response;
    },
    (error) => {
      return Promise.reject(error);
    }
  );
//
export default api;
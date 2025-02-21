import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

// Créer une instance de Axios
// pour rediriger les requêtes vers notre serveur django REST framework.
const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
})


// Un interceptor pour ajouter l'authorization token à chaque requête
api.interceptors.request.use(
    async (config) => {
        const accessToken = localStorage.getItem(ACCESS_TOKEN);
        if (accessToken) {
            config.headers.Authorization = `Bearer ${accessToken}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

//
export default api;
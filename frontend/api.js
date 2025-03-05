import { ACCESS_TOKEN } from "@/store/constants";
import axios from "axios";

// Créer une instance de Axios
// pour rediriger les requêtes vers notre serveur django REST framework.
// process.env.NEXT_PUBLIC_API_URL
const api = axios.create({

    baseURL: process.env.NEXT_PUBLIC_API_URL,
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
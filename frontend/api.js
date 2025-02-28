import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

// Créer une instance de Axios
// pour rediriger les requêtes vers notre serveur django REST framework.
// process.env.NEXT_PUBLIC_API_URL
const api = axios.create({

    baseURL: "https://backend-ensai.kub.sspcloud.fr",
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
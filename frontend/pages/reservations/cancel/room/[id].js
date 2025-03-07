"use client";

import api from '@/api';
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';

export default function DeleteEvent() {
  const router = useRouter();
  const { id } = router.query; // Récupération du paramètre id
  const [loading, set_loading] = useState(true);

  useEffect(() => {
    if (!id) {
      return; // Si l'id n'est pas présent, on arrête l'exécution
    }

    // Définition de l'URL de l'API pour l'événement
    const api_url = `/api/reservations/cancel-reservation-room/${id}`;

    const deleteEvent = async () => {
      try {
        await api.delete(api_url);
        alert("Événement supprimé avec succès !");
        router.push('/'); // Redirection après suppression
      } catch (error) {
        console.error("Erreur:", error);
        alert("Erreur lors de la suppression !");
      } finally {
        set_loading(false);
      }
    };

    deleteEvent();
  }, [id]);

  return loading ? <p>Suppression en cours...</p> : null;
}

"use client";

import { Button, Typography } from '@mui/material';
import { useRouter } from 'next/router';
import { useState } from 'react';

import api from '@/api';

export default function CancelReservation({ event_type, api_url, id }) {
  const [loading, set_loading] = useState(false);
  const router = useRouter();

  const handle_cancel = async () => {
    set_loading(true);

    try {
      await api.delete(`${api_url}/${id}`);

      // Rediriger l'utilisateur après l'annulation
      router.push('/home');
    } catch (error) {
      console.error('Erreur:', error);
      alert('Erreur lors de l\'annulation de la réservation');
    } finally {
      set_loading(false);
    }
  };

  return (
    <div className="form-container">
      <Typography variant="h4" gutterBottom>
        Annuler la réservation de {event_type === 'eventbus' ? 'Bus' : event_type === 'eventroom' ? 'Salle' : 'Matériel'}
      </Typography>

      <Button variant="contained" color="secondary" onClick={handle_cancel} fullWidth disabled={loading}>
        {loading ? 'Annulation en cours...' : 'Annuler la réservation'}
      </Button>
    </div>
  );
}

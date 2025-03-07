"use client";

import { Button, Typography } from '@mui/material';
import { useRouter } from 'next/router';
import { useState } from 'react';
import ErrorBox from "../erro";


import api from '@/api';

export default function CancelReservation({ event_type, api_url, id }) {
  const [loading, set_loading] = useState(false);
  const router = useRouter();
  const [error, set_error] = useState(null);

  const handle_cancel = async () => {
    set_loading(true);

    try {
      await api.delete(`${api_url}/${id}`);
      // Rediriger l'utilisateur après l'annulation
      router.push('/');
      set_error(null);
    } catch (error) {
      set_error({
        statusCode: error.response?.status || 500,
      });
    } finally {
      set_loading(false);
    }
  };

  return (
    <>
    {error && (
        <ErrorBox
          statusCode={error.statusCode}
          defaultMessage={error.defaultMessage}
        />
      )}
    <div className="form-container">
      <Typography variant="h4" gutterBottom>
        Annuler la réservation de {event_type === 'eventbus' ? 'Bus' : event_type === 'eventroom' ? 'Salle' : 'Matériel'}
      </Typography>

      <Button variant="contained" color="secondary" onClick={handle_cancel} fullWidth disabled={loading}>
        {loading ? 'Annulation en cours...' : 'Annuler la réservation'}
      </Button>
    </div>
  </>
  );
}

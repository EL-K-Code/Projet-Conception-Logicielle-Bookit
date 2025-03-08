"use client";

import ErrorBox from "@/utils/erro";
import { Button } from '@mui/material';
import { useRouter } from 'next/router';
import { useState } from 'react';


import api from '@/utils/api';

export default function CancelReservation({api_url}) {
  const [loading, set_loading] = useState(false);
  const router = useRouter();
  const [error, set_error] = useState(null);

  const handle_cancel = async () => {
    set_loading(true);

    try {
      await api.delete(api_url);
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
          defaultMessage={error?.defaultMessage}
        />
      )}
    <div className="form-container">
      <Button variant="contained" color="secondary" onClick={handle_cancel} fullWidth disabled={loading}>
        {loading ? 'Annulation en cours...' : 'Annuler la réservation'}
      </Button>
    </div>
  </>
  );
}

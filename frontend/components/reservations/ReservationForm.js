"use client";

import ErrorBox from '@/utils/erro';
import { Button, TextField, Typography } from '@mui/material';
import { useRouter } from 'next/router';
import { useState } from 'react';

import api from '@/utils/api';

export default function ReservationForm({ event_type, api_url, id}) {
  const event_key = event_type === 'eventroom' ? 'event_room' : event_type === 'eventmaterial' ? 'event_material' : 'event_bus';
  const [quantity, set_quantity] = useState(1);
  const [date, set_date] = useState("");
  const [start_time, set_start_time] = useState("");
  const [end_time, set_end_time] = useState("");
  const [loading, set_loading] = useState(false);
  const router = useRouter();
  const [error, set_error] = useState(null);

  const handle_submit = async (e) => {
    e.preventDefault();
    set_loading(true);

    try {
    const reservationData = {
        [event_key]: id, // Utilisation de la clé dynamique
        ...(event_type === 'eventroom' && { date, start_time, end_time }),
        ...(event_type === 'eventmaterial' && { date, start_time, end_time, quantity })

      };

      await api.post(api_url, reservationData );
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
    <form onSubmit={handle_submit} className="form-container">
      <Typography variant="h4" gutterBottom>
        Réserver {event_type === 'eventbus' ? 'Bus' : event_type === 'eventroom' ? 'Salle' : 'Matériel'}
      </Typography>

      {event_type === 'eventroom' || event_type === 'eventmaterial' ? (
        <>
          <TextField label="Date" type="date" required fullWidth value={date} onChange={(e) => set_date(e.target.value)} InputLabelProps={{ shrink: true }} />
          <TextField label="Heure de début" type="time" required fullWidth value={start_time} onChange={(e) => set_start_time(e.target.value)} InputLabelProps={{ shrink: true }} />
          <TextField label="Heure de fin" type="time" required fullWidth value={end_time} onChange={(e) => set_end_time(e.target.value)} InputLabelProps={{ shrink: true }} />
        </>
      ) : null}

      {event_type === 'eventmaterial' && (
        <TextField label="Quantité" type="number" required fullWidth value={quantity} onChange={(e) => set_quantity(e.target.value)} min="1" />
      )}

      <Button variant="contained" color="primary" type="submit" fullWidth disabled={loading}>
        {loading ? 'Réservation en cours...' : 'Réserver'}
      </Button>
    </form>
  </>
  );
}

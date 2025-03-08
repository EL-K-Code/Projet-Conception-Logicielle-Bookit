"use client";

import ErrorBox from '@/utils/erro';
import { Button, TextField, Typography, Box, useMediaQuery } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import { useRouter } from 'next/router';
import { useState } from 'react';
import api from '@/utils/api';

export default function ReservationForm({ event_type, api_url, id }) {
  const theme = useTheme();
  const match_down_sm = useMediaQuery(theme.breakpoints.down('md'));
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
        [event_key]: id,
        ...(event_type === 'eventroom' && { date, start_time, end_time }),
        ...(event_type === 'eventmaterial' && { date, start_time, end_time, quantity })
      };

      await api.post(api_url, reservationData);
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

      <Box
        component="form"
        onSubmit={handle_submit}
        sx={{
          display: 'flex',
          flexDirection: 'column',
          gap: 2, // Espace uniforme entre les champs (8px * 2 = 16px)
          maxWidth: 400,
          margin: '0 auto',
        }}
      >
      <Typography
          color={theme.palette.secondary.main}
          gutterBottom
          variant={match_down_sm ? 'h3' : 'h2'}
          align="center" // Propriété MUI pour centrer le texte
        >
          Réserver 
          {event_type === "eventbus" && " un bus"} 
          {event_type === "eventroom" && " une salle"} 
          {event_type === "eventmaterial" && " un matériel"}
        </Typography>

        {(event_type === 'eventroom' || event_type === 'eventmaterial') && (
          <>
            <TextField
              label="Date"
              type="date"
              required
              fullWidth
              value={date}
              onChange={(e) => set_date(e.target.value)}
              InputLabelProps={{ shrink: true }}
            />
            <TextField
              label="Heure de début"
              type="time"
              required
              fullWidth
              value={start_time}
              onChange={(e) => set_start_time(e.target.value)}
              InputLabelProps={{ shrink: true }}
            />
            <TextField
              label="Heure de fin"
              type="time"
              required
              fullWidth
              value={end_time}
              onChange={(e) => set_end_time(e.target.value)}
              InputLabelProps={{ shrink: true }}
            />
          </>
        )}

        {event_type === 'eventmaterial' && (
          <TextField
            label="Quantité"
            type="number"
            required
            fullWidth
            value={quantity}
            onChange={(e) => set_quantity(e.target.value)}
            inputProps={{ min: "1" }}
          />
        )}

        <Button
          variant="contained"
          color="primary"
          type="submit"
          fullWidth
          disabled={loading}
        >
          {loading ? 'Réservation en cours...' : 'Réserver'}
        </Button>
      </Box>
    </>
  );
}


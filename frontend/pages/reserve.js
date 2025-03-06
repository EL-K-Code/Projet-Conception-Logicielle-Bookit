import { Button, TextField, Typography } from '@mui/material';
import { useRouter } from 'next/router';
import { useState } from 'react';

export default function ReservationForm({ event_type, event_data }) {
  const [quantity, set_quantity] = useState(1); // Quantité pour le matériel
  const [date, set_date] = useState(""); // Date pour la salle ou le matériel
  const [start_time, set_start_time] = useState(""); // Heure de début pour la salle ou matériel
  const [end_time, set_end_time] = useState(""); // Heure de fin pour la salle ou matériel
  const [loading, set_loading] = useState(false);
  const router = useRouter();

  // Soumission du formulaire
  const handle_submit = async (e) => {
    e.preventDefault();
    set_loading(true);

    try {
      const reservationData = {
        event_type,
        ...(event_type === 'eventbus' && { event_bus: event_data.id }),
        ...(event_type === 'eventroom' && {
          event_room: event_data.id,
          date,
          start_time,
          end_time
        }),
        ...(event_type === 'eventmaterial' && {
          event_material: event_data.id,
          date,
          start_time,
          end_time,
          quantity
        })
      };

      // Envoi de la réservation
      const res = await fetch('/api/reservation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(reservationData)
      });

      if (res.ok) {
        router.push('/dashboard'); // Redirection après la réservation
      } else {
        alert('Erreur lors de la réservation');
      }
    } catch (error) {
      console.error('Erreur:', error);
      alert('Erreur lors de la réservation');
    } finally {
      set_loading(false);
    }
  };

  return (
    <form onSubmit={handle_submit} className="form-container">
      <Typography variant="h4" gutterBottom>
        Réserver {event_type === 'eventbus' && 'Bus'} {event_type === 'eventroom' && 'Salle'} {event_type === 'eventmaterial' && 'Matériel'}
      </Typography>

      {/* Pour le type 'eventbus' */}
      {event_type === 'eventbus' && (
        <div>
          <Typography variant="h6">Bus: {event_data.name}</Typography>
          <TextField
            label="Nombre de places"
            type="number"
            required
            fullWidth
            value={event_data.available_seats}
            disabled
          />
        </div>
      )}

      {/* Pour le type 'eventroom' */}
      {event_type === 'eventroom' && (
        <div>
          <Typography variant="h6">Salle: {event_data.name}</Typography>
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
        </div>
      )}

      {/* Pour le type 'eventmaterial' */}
      {event_type === 'eventmaterial' && (
        <div>
          <Typography variant="h6">Matériel: {event_data.name}</Typography>
          <TextField
            label="Quantité"
            type="number"
            required
            fullWidth
            value={quantity}
            onChange={(e) => set_quantity(e.target.value)}
            min="1"
          />
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
        </div>
      )}

      {/* Bouton de soumission */}
      <Button
        variant="contained"
        color="primary"
        type="submit"
        fullWidth
        disabled={loading}
      >
        {loading ? 'Réservation en cours...' : 'Réserver'}
      </Button>
    </form>
  );
}

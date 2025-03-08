import { FormControl, InputLabel, MenuItem, Select, TextField, Typography, useMediaQuery } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import { useRouter } from "next/navigation";
import PropTypes from 'prop-types';
import { useEffect, useState } from "react";

//Projet import
import api from "@/utils/api";
import ErrorBox from '@/utils/erro';

// Mise à jour d'un événement
const UpdateEventForm = ({ event_type, route, api_url, id }) => {
  const theme = useTheme();
  const match_down_sm = useMediaQuery(theme.breakpoints.down('md'));
  const [description, set_description] = useState("");
  const [resource, set_resource] = useState("");
  const [available_seats, set_available_seats] = useState("");
  const [start_time, set_start_time] = useState("");
  const [end_time, set_end_time] = useState("");
  const [departure, set_departure] = useState("");
  const [destination, set_destination] = useState("");
  const [available_stock, set_available_stock] = useState("");
  const [loading, set_loading] = useState(false);
  const [resources, set_resources] = useState([]);
  const router = useRouter();
  const [error, set_error] = useState(null);

  // Charger les ressources disponibles
  useEffect(() => {
    const fetchResources = async () => {
      try {
        const response = await api.get(route);
        set_resources(response.data);
      } catch (error) {
        console.error("Erreur lors du chargement des ressources:", error);
      }
    };
    fetchResources();
  }, [route]);

  // Soumission du formulaire
  const handle_submit = async (e) => {
    e.preventDefault();
    set_loading(true);

    console.log("Données envoyées :", {
      description,
      resource,
      ...(event_type === "eventbus" && {
        available_seats,
        start_time,
        end_time,
        departure,
        destination
      }),
      ...(event_type === "eventmaterial" && {
        available_stock
      })
    });

    try {
      await api.put(`${api_url}/${id}`, {
        description,
        resource,
        ...(event_type === "eventbus" && {
          available_seats,
          start_time,
          end_time,
          departure,
          destination
        }),
        ...(event_type === "eventmaterial" && {
          available_stock
        })
      });

      router.push("/");
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
      <Typography color={theme.palette.secondary.main} gutterBottom variant={match_down_sm ? 'h3' : 'h2'}>
        Modifier l'Événement {event_type === "eventbus" && "Bus"} {event_type === "eventroom" && "Salle"} {event_type === "eventmaterial" && "Matériel"}
      </Typography>

      <TextField
        className="form-input"
        type="text"
        value={description}
        onChange={(e) => set_description(e.target.value)}
        placeholder="Description"
        label="Description"
        required
        fullWidth
      />

      <FormControl fullWidth required>
        <InputLabel>Ressource</InputLabel>
        <Select
          className="form-input"
          value={resource}
          onChange={(e) => set_resource(e.target.value)}
          label="Ressource"
        >
          {resources.length > 0 ? (
            resources.map((res) => (
              <MenuItem key={res.id} value={res.id}>{res.name}</MenuItem>
            ))
          ) : (
            <MenuItem disabled>Aucune ressource disponible</MenuItem>
          )}
        </Select>
      </FormControl>

      {event_type === "eventbus" && (
        <>
          <TextField type="number" value={available_seats} onChange={(e) => set_available_seats(e.target.value)} label="Nombre de Places Disponibles" required fullWidth />
          <TextField type="datetime-local" value={start_time} onChange={(e) => set_start_time(e.target.value)} label="Heure de Départ" required fullWidth InputLabelProps={{ shrink: true }} />
          <TextField type="datetime-local" value={end_time} onChange={(e) => set_end_time(e.target.value)} label="Heure d'Arrivée" required fullWidth InputLabelProps={{ shrink: true }} />
          <TextField type="text" value={departure} onChange={(e) => set_departure(e.target.value)} label="Lieu de Départ" required fullWidth />
          <TextField type="text" value={destination} onChange={(e) => set_destination(e.target.value)} label="Lieu d'Arrivée" required fullWidth />
        </>
      )}

      {event_type === "eventmaterial" && (
        <TextField type="number" value={available_stock} onChange={(e) => set_available_stock(e.target.value)} label="Stock Disponible" required fullWidth />
      )}

      <button className="form-button" type="submit" disabled={loading}>
        {loading ? "Modification en cours..." : "Modifier l'Événement"}
      </button>
    </form>
  </>
  );
}

UpdateEventForm.propTypes = {
  event_type: PropTypes.string.isRequired,
  route: PropTypes.string.isRequired,
  api_url: PropTypes.string.isRequired,
  id: PropTypes.string.isRequired
};

export default UpdateEventForm;

import api from "@/utils/api";
import { Box, FormControl, InputLabel, MenuItem, Select, TextField, Typography, useMediaQuery } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import { useRouter } from "next/navigation";
import PropTypes from 'prop-types';
import { useEffect, useState } from "react";
import ErrorBox from "../../utils/erro";

const EventForm = ({ event_type, route, api_url }) => {
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
  const [error, set_error] = useState(null);
  const router = useRouter();

  useEffect(() => {
    const fetchResources = async () => {
      try {
        const response = await api.get(api_url);
        set_resources(response.data);
        set_error(null);
      } catch (error) {
        set_error({
          statusCode: error.response?.status || 500,
        });
      }
    };
    fetchResources();
  }, [api_url]);

  const handle_submit = async (e) => {
    e.preventDefault();
    set_loading(true);

    try {
      await api.post(route, {
        description,
        resource,
        ...(event_type === "eventbus" && {
          available_seats,
          start_time,
          end_time,
          departure,
          destination,
        }),
        ...(event_type === "eventmaterial" && { available_stock }),
      });
      set_error(null);
      router.push("/");
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
      {error && <ErrorBox statusCode={error.statusCode} defaultMessage={error.defaultMessage} />}

      <Box width="100%" mx="auto" p={3}>
  <form onSubmit={handle_submit} className="form-container">
    <Typography
      color={theme.palette.secondary.main}
      gutterBottom
      align="center"
      variant={match_down_sm ? 'h3' : 'h2'}
    >
      Créer un Événement
      {event_type === "eventbus" && " Bus"}
      {event_type === "eventroom" && " Salle"}
      {event_type === "eventmaterial" && " Matériel"}
    </Typography>

    <Box display="flex" flexDirection="column" gap={2} maxWidth="100%">
      <TextField
        type="text"
        value={description}
        onChange={(e) => set_description(e.target.value)}
        label="Description"
        required
        fullWidth
      />

      <FormControl fullWidth required>
        <InputLabel>Ressource</InputLabel>
        <Select
          value={resource}
          onChange={(e) => set_resource(e.target.value)}
          label="Ressource"
          fullWidth
        >
          {resources.length > 0 ? (
            resources.map((res) => (
              <MenuItem key={res.id} value={res.id}>
                {res.name}
              </MenuItem>
            ))
          ) : (
            <MenuItem disabled>Aucune ressource disponible</MenuItem>
          )}
        </Select>
      </FormControl>

      {event_type === "eventbus" && (
        <>
          <TextField
            type="number"
            value={available_seats}
            onChange={(e) => set_available_seats(e.target.value)}
            label="Nombre de Places Disponibles"
            required
            fullWidth
          />
          <TextField
            type="datetime-local"
            value={start_time}
            onChange={(e) => set_start_time(e.target.value)}
            label="Heure de Départ"
            required
            fullWidth
            InputLabelProps={{ shrink: true }}
          />
          <TextField
            type="datetime-local"
            value={end_time}
            onChange={(e) => set_end_time(e.target.value)}
            label="Heure d'Arrivée"
            required
            fullWidth
            InputLabelProps={{ shrink: true }}
          />
          <TextField
            type="text"
            value={departure}
            onChange={(e) => set_departure(e.target.value)}
            label="Lieu de Départ"
            required
            fullWidth
          />
          <TextField
            type="text"
            value={destination}
            onChange={(e) => set_destination(e.target.value)}
            label="Lieu d'Arrivée"
            required
            fullWidth
          />
        </>
      )}

      {event_type === "eventmaterial" && (
        <TextField
          type="number"
          value={available_stock}
          onChange={(e) => set_available_stock(e.target.value)}
          label="Stock Disponible"
          required
          fullWidth
        />
      )}

      <button className="form-button" type="submit" disabled={loading}>
        {loading ? "Chargement..." : "Créer l'Événement"}
      </button>
    </Box>
  </form>
</Box>

    </>
  );
};

EventForm.propTypes = {
  eventType: PropTypes.string.isRequired,
  route: PropTypes.string.isRequired,
  api_url: PropTypes.string.isRequired,
};

export default EventForm;

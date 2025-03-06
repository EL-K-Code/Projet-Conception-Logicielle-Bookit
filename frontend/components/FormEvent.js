<<<<<<< HEAD
"use client";

import api from "@/api";
import { Typography, useMediaQuery } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import { useRouter } from "next/navigation";
import PropTypes from 'prop-types';
import { useState } from "react";

const EventForm = ({ eventType }) => {
=======
import api from "@/api";
import { FormControl, InputLabel, MenuItem, Select, TextField, Typography, useMediaQuery } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

export default function EventForm({ event_type, route, api_url }) {
>>>>>>> 0d391fa89c86d74a41541c9d42edc737313bcec2
  const theme = useTheme();
  const match_down_sm = useMediaQuery(theme.breakpoints.down('md'));
  const [description, set_description] = useState("");
  const [resource, set_resource] = useState(""); // Champs ressource
  const [available_seats, set_available_seats] = useState("");
  const [departure_time, set_departure_time] = useState("");
  const [arrival_time, set_arrival_time] = useState("");
  const [departure, set_departure] = useState("");
  const [destination, set_destination] = useState("");
  const [available_stock, set_available_stock] = useState("");
  const [loading, set_loading] = useState(false);
  const [resources, set_resources] = useState([]);  // Pour stocker les ressources récupérées
  const router = useRouter();

  // Fonction pour charger les ressources depuis l'API
  const fetchResources = async () => {
    try {
      const response = await api.get(api_url);  // Utilise l'URL de l'API passé en argument
      set_resources(response.data);  // Supposons que l'API renvoie un tableau de ressources
    } catch (error) {
      console.error("Erreur lors du chargement des ressources:", error);
    }
  };

  // Charger les ressources lorsque le composant est monté
  useEffect(() => {
    fetchResources();
  }, [api_url]);

  // Soumission du formulaire
  const handle_submit = async (e) => {
    e.preventDefault();
    set_loading(true);

    console.log("Données envoyées :", {
      description,
      resource, // Envoie uniquement l'ID de la ressource
      ...(event_type === "eventbus" && {
        available_seats,
        departure_time,
        arrival_time,
        departure,
        destination
      }),
      ...(event_type === "eventmaterial" && {
        available_stock
      })
    });

    try {
<<<<<<< HEAD
      // Remplacer cette partie par l'appel API adapté
        await api.post("/create-event", {
=======
      // Envoi des données selon le type d'événement
      const res = await api.post(route, {
>>>>>>> 0d391fa89c86d74a41541c9d42edc737313bcec2
        description,
        resource, // L'ID est envoyé ici
        ...(event_type === "eventbus" && {
          available_seats,
          departure_time,
          arrival_time,
          departure,
          destination
        }),
        ...(event_type === "eventmaterial" && {
          available_stock
        })
      });

      router.push("/home"); // Redirection après la soumission
    } catch (error) {
      alert("Erreur: " + (error.response?.data?.detail || error.message)); // Affichage d'une erreur
    } finally {
      set_loading(false); // Fin de chargement
    }
  };

  return (
    <form onSubmit={handle_submit} className="form-container">
      <Typography color={theme.palette.secondary.main} gutterBottom variant={match_down_sm ? 'h3' : 'h2'}>
        Créer un Événement {event_type === "eventbus" && "Bus"} {event_type === "eventroom" && "Salle"} {event_type === "eventmaterial" && "Matériel"}
      </Typography>

      {/* Champ description commun */}
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

      {/* Sélection des ressources */}
      <FormControl fullWidth required>
        <InputLabel>Ressource</InputLabel>
        <Select
          className="form-input"
          value={resource}
          onChange={(e) => set_resource(e.target.value)} // L'ID est sélectionné ici
          label="Ressource"
        >
          {resources.length > 0 ? (
            resources.map((res) => (
              <MenuItem key={res.id} value={res.id}>
                {res.name} {/* Affichage du nom, mais envoie l'ID */}
              </MenuItem>
            ))
          ) : (
            <MenuItem disabled>Aucune ressource disponible</MenuItem>
          )}
        </Select>
      </FormControl>

      {/* Champs spécifiques pour le type 'eventbus' */}
      {event_type === "eventbus" && (
        <>
          <TextField
            className="form-input"
            type="number"
            value={available_seats}
            onChange={(e) => set_available_seats(e.target.value)}
            placeholder="Nombre de Places Disponibles"
            label="Nombre de Places Disponibles"
            required
            fullWidth
          />
          <TextField
            className="form-input"
            type="datetime-local"
            value={departure_time}
            onChange={(e) => set_departure_time(e.target.value)}
            placeholder="Heure de Départ"
            label="Heure de Départ"
            required
            fullWidth
            InputLabelProps={{ shrink: true }}
          />
          <TextField
            className="form-input"
            type="datetime-local"
            value={arrival_time}
            onChange={(e) => set_arrival_time(e.target.value)}
            placeholder="Heure d'Arrivée"
            label="Heure d'Arrivée"
            required
            fullWidth
            InputLabelProps={{ shrink: true }}
          />
          <TextField
            className="form-input"
            type="text"
            value={departure}
            onChange={(e) => set_departure(e.target.value)}
            placeholder="Lieu de Départ"
            label="Lieu de Départ"
            required
            fullWidth
          />
          <TextField
            className="form-input"
            type="text"
            value={destination}
            onChange={(e) => set_destination(e.target.value)}
            placeholder="Lieu d'Arrivée"
            label="Lieu d'Arrivée"
            required
            fullWidth
          />
        </>
      )}

      {/* Champs spécifiques pour le type 'eventmaterial' */}
      {event_type === "eventmaterial" && (
        <TextField
          className="form-input"
          type="number"
          value={available_stock}
          onChange={(e) => set_available_stock(e.target.value)}
          placeholder="Stock Disponible"
          label="Stock Disponible"
          required
          fullWidth
        />
      )}

      {/* Bouton de soumission avec état de chargement */}
      <button className="form-button" type="submit" disabled={loading}>
        {loading ? "Chargement..." : "Créer l'Événement"}
      </button>
    </form>
  );
};

EventForm.propTypes = {
  eventType: PropTypes.string.isRequired,
};

export default EventForm ;
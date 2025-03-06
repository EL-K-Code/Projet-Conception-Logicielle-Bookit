"use client";

import api from "@/api";
import { Typography, useMediaQuery } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import { useRouter } from "next/navigation";
import PropTypes from 'prop-types';
import { useState } from "react";

const EventForm = ({ eventType }) => {
  const theme = useTheme();
  const matchDownSM = useMediaQuery(theme.breakpoints.down('md'));
  const [description, setDescription] = useState("");
  const [organizer, setOrganizer] = useState("");
  const [loading, setLoading] = useState(false);
  const [additionalFields, setAdditionalFields] = useState({
    busType: "",
    availableSeats: "",
    departureTime: "",
    arrivalTime: "",
    departureLocation: "",
    arrivalLocation: "",
    roomName: "",
    materialName: "",
    stockAvailable: ""
  });

  const router = useRouter();

  const handleAdditionalFieldsChange = (event) => {
    const { name, value } = event.target;
    setAdditionalFields((prev) => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      // Remplacer cette partie par l'appel API adapté
        await api.post("/create-event", {
        description,
        organizer,
        eventType,
        additionalFields
      });

      // Redirect or success handling
      router.push("/events");
    } catch (error) {
      alert("Erreur: " + (error.response?.data?.detail || error.message));
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <Typography color={theme.palette.secondary.main} gutterBottom variant={matchDownSM ? 'h3' : 'h2'}>
        Créer un Événement {eventType === "eventbus" && "Bus"} {eventType === "eventroom" && "Room"} {eventType === "eventmaterial" && "Material"}
      </Typography>

      <input
        className="form-input"
        type="text"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder="Description"
        required
      />

      <input
        className="form-input"
        type="text"
        value={organizer}
        onChange={(e) => setOrganizer(e.target.value)}
        placeholder="Organisateur"
        required
      />

      {eventType === "eventbus" && (
        <>
          <input
            className="form-input"
            type="text"
            name="busType"
            value={additionalFields.busType}
            onChange={handleAdditionalFieldsChange}
            placeholder="Type de Bus"
            required
          />
          <input
            className="form-input"
            type="number"
            name="availableSeats"
            value={additionalFields.availableSeats}
            onChange={handleAdditionalFieldsChange}
            placeholder="Nombre de Places Disponibles"
            required
          />
          <input
            className="form-input"
            type="time"
            name="departureTime"
            value={additionalFields.departureTime}
            onChange={handleAdditionalFieldsChange}
            placeholder="Heure de Départ"
            required
          />
          <input
            className="form-input"
            type="time"
            name="arrivalTime"
            value={additionalFields.arrivalTime}
            onChange={handleAdditionalFieldsChange}
            placeholder="Heure d'Arrivée"
            required
          />
          <input
            className="form-input"
            type="text"
            name="departureLocation"
            value={additionalFields.departureLocation}
            onChange={handleAdditionalFieldsChange}
            placeholder="Lieu de Départ"
            required
          />
          <input
            className="form-input"
            type="text"
            name="arrivalLocation"
            value={additionalFields.arrivalLocation}
            onChange={handleAdditionalFieldsChange}
            placeholder="Lieu d'Arrivée"
            required
          />
        </>
      )}

      {eventType === "eventroom" && (
        <input
          className="form-input"
          type="text"
          name="roomName"
          value={additionalFields.roomName}
          onChange={handleAdditionalFieldsChange}
          placeholder="Nom de la Salle"
          required
        />
      )}

      {eventType === "eventmaterial" && (
        <>
          <input
            className="form-input"
            type="text"
            name="materialName"
            value={additionalFields.materialName}
            onChange={handleAdditionalFieldsChange}
            placeholder="Nom du Matériel"
            required
          />
          <input
            className="form-input"
            type="number"
            name="stockAvailable"
            value={additionalFields.stockAvailable}
            onChange={handleAdditionalFieldsChange}
            placeholder="Stock Disponible"
            required
          />
        </>
      )}

      <button className="form-button" type="submit" disabled={loading}>
        {loading ? "Loading..." : "Créer l'Événement"}
      </button>
    </form>
  );
};

EventForm.propTypes = {
  eventType: PropTypes.string.isRequired,
};

export default EventForm ;
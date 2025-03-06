"use client";

import api from "@/api";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "@/store/constants";
import { Typography, useMediaQuery } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import { useRouter } from "next/navigation";
import PropTypes from 'prop-types';
import { useState } from "react";

const Form = ({ route, method }) => {
  const theme = useTheme();
  const matchDownSM = useMediaQuery(theme.breakpoints.down('md'));
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    console.log("Données envoyées :", {
      username,
      password});

    if (method === "signup"){
      localStorage.clear();
    }

    try {
      const res = await api.post(route, { username, password, ...(method === "signup" && { email }) });

      if (method === "login") {
        localStorage.setItem(ACCESS_TOKEN, res.data.access);
        localStorage.setItem(REFRESH_TOKEN, res.data.refresh);

        // Récupère l'URL demandée avant connexion
        const redirectTo = localStorage.getItem("redirectAfterLogin") || "/";
        localStorage.removeItem("redirectAfterLogin"); // Nettoyage après redirection
        console.log(redirectTo);
        router.push(redirectTo);
      } else {
        router.push("/login");
      }
    } catch (error) {
      alert("Erreur: " + (error.response?.data?.detail || error.message));
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form-container">

    <Typography
        color={theme.palette.secondary.main}
        gutterBottom
        variant={matchDownSM ? 'h3' : 'h2'}
    >
        {method === "login" ? "Login" : "Sign Up"}
    </Typography>

      <input
        className="form-input"
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
        required
      />

      <input
        className="form-input"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
        required
      />

      {method === "signup" && (
        <input
          className="form-input"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          required
        />
      )}

      <button className="form-button" type="submit" disabled={loading}>
        {loading ? "Loading..." : method === "login" ? "Login" : "Sign Up"}
      </button>
    </form>
  );
};

Form.propTypes = {
  route: PropTypes.oneOf(['/login', '/signup']),
  method: PropTypes.oneOf(['login', 'signup'])
};

export default Form ;
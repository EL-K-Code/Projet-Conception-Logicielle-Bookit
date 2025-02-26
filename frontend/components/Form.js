"use client";
import api from "@/api";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "@/constants";
import { useRouter } from "next/navigation";
import { useState } from "react";

export default function Form({ route, method }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const res = await api.post(route, { username, password, ...(method === "signup" && { email }) });

      if (method === "login") {
        localStorage.setItem(ACCESS_TOKEN, res.data.access);
        localStorage.setItem(REFRESH_TOKEN, res.data.refresh);

        // Récupère l'URL demandée avant connexion
        const redirectTo = localStorage.getItem("redirectAfterLogin") || "/";
        localStorage.removeItem("redirectAfterLogin"); // Nettoyage après redirection
        router.replace(redirectTo);
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
      <h1>{method === "login" ? "Login" : "Sign Up"}</h1>

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
}

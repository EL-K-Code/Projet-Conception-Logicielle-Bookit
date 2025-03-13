"use client";

import api from "@/utils/api";
import Link from 'next/link';
import { useEffect, useState } from "react";

export default function SignOut() {
    const [error, setError] = useState(null);
    const [signedOut, setSignedOut] = useState(false);

    useEffect(() => {
        let isMounted = true;
    
        const signOut = async () => {
            try {
                if (isMounted) {
                    await api.delete("/api/auth/signout/");
                    localStorage.clear();
                    setSignedOut(true);
                }
            } catch (error) {
                setError(error.response?.data?.detail || error.message);
            }
        };
    
        signOut();
    
        return () => {
            isMounted = false; // Empêche la seconde exécution
        };
    }, []);
    

    if (signedOut) {
        localStorage.clear();
        return (
            <div className="container">
                <div className="box">
                    <svg className="icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <h1 className="title">Votre compte a été supprimé avec succès.</h1>
                    <p className="message">Nous espérons vous revoir bientôt !</p>

                    <Link href="/" className="button">Back to home</Link>
                </div>
            </div>
        );
    }

    if (error) {
        return <div className="error">Erreur: {error}</div>;
    }

    return <div>Chargement...</div>;
}

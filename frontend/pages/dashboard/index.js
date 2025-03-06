import api from "@/api";
import { useEffect, useState } from 'react';

const Dashboard = () => {
    const [events, setEvents] = useState({
        event_rooms: [],
        event_buses: [],
        event_materials: []
    });
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);

    const apiUrl = '/api/evenements/list-event/';

    const fetchEvents = async () => {
        try {
            const response = await api.get(apiUrl);  // Utilise l'URL de l'API
            setEvents(response.data);  // Met à jour les événements avec les données reçues
            setLoading(false);
        } catch (error) {
            setError(error.message);  // Affiche l'erreur dans l'état
            setLoading(false);
            console.error("Erreur lors de la récupération des événements:", error);
        }
    };

    useEffect(() => {
        fetchEvents();  // Appelle la fonction pour charger les événements lorsque le composant est monté
    }, [apiUrl]);  // Si l'URL change, on refait l'appel à l'API

    const handleClick = (eventId, option, group) => {
        let link = '';

        // Définir le lien selon l'option choisie et le groupe d'événement
        if (group === 'rooms') {
            if (option === 'reserve') {
                link = `/reserve-room/${eventId}`;  // Lien spécifique pour réserver une salle
            } else if (option === 'modify') {
                link = `/update-room/${eventId}`;  // Lien spécifique pour modifier une salle
            }
        } else if (group === 'buses') {
            if (option === 'reserve') {
                link = `/reserve-bus/${eventId}`;  // Lien spécifique pour réserver un bus
            } else if (option === 'modify') {
                link = `/update-bus/${eventId}`;  // Lien spécifique pour modifier un bus
            }
        } else if (group === 'materials') {
            if (option === 'reserve') {
                link = `/reserve-material/${eventId}`;  // Lien spécifique pour réserver un matériel
            } else if (option === 'modify') {
                link = `/update-material/${eventId}`;  // Lien spécifique pour modifier un matériel
            }
        }

        // Rediriger l'utilisateur vers le lien
        window.location.href = link;
    };

    // Filtrer les événements réservés
    const filterReservedEvents = (events) => {
        return events.filter(event => !event.is_reserved); // Filtrer les événements non réservés
    };

    // Fonction pour afficher les événements en ligne avec un maximum de 5 par ligne
    const renderEventGrid = (events, group) => {
        if (events.length === 0) {
            return <div>Aucun événement disponible pour ce groupe</div>;
        }

        const eventRows = [];
        for (let i = 0; i < events.length; i += 5) {
            const row = events.slice(i, i + 5);
            eventRows.push(
                <div key={i} style={styles.gridRow}>
                    {row.map((event) => (
                        <div key={event.id} style={styles.card}>
                            <div style={styles.menu}>
                                <div
                                    style={styles.menuItem}
                                    onClick={() => handleClick(event.id, 'reserve', group)}  // Redirige vers le lien de réservation
                                >
                                    Réserver
                                </div>

                                <div
                                    style={styles.menuItem}
                                    onClick={() => handleClick(event.id, 'modify', group)}  // Redirige vers le lien de modification
                                >
                                    Modifier Événement
                                </div>
                            </div>
                            <div style={styles.amount}>ID : {event.id}</div>
                            <div style={styles.text}>Description : {event.description}</div>
                        </div>
                    ))}
                </div>
            );
        }
        return eventRows;
    };

    return (
        <div>
            {error && <div style={{ color: 'red' }}>Erreur: {error}</div>}

            {loading ? (
                <div>Loading events...</div>
            ) : (
                <>
                    {/* Section pour Room */}
                    <div>
                        <h2>Room Events</h2>
                        {renderEventGrid(filterReservedEvents(events.event_rooms), 'rooms')}
                    </div>

                    {/* Section pour Bus */}
                    <div>
                        <h2>Bus Events</h2>
                        {renderEventGrid(filterReservedEvents(events.event_buses), 'buses')}
                    </div>

                    {/* Section pour Material */}
                    <div>
                        <h2>Material Events</h2>
                        {renderEventGrid(filterReservedEvents(events.event_materials), 'materials')}
                    </div>
                </>
            )}
        </div>
    );
};

const styles = {
    card: {
        backgroundColor: '#333',
        padding: '20px',
        borderRadius: '10px',
        width: '18%',
        color: 'white',
        textAlign: 'center',
        boxShadow: '0 4px 8px rgba(0, 0, 0, 0.2)',
        border: '2px solid #444',
        margin: '10px',
    },
    menu: {
        display: 'flex',
        justifyContent: 'space-around',
        marginBottom: '15px',
    },
    menuItem: {
        fontSize: '14px',
        cursor: 'pointer',
        padding: '5px 10px',
        borderRadius: '5px',
        color: '#ccc',
        transition: 'background-color 0.3s',
    },
    amount: {
        fontSize: '20px',
        fontWeight: 'bold',
        marginBottom: '10px',
    },
    text: {
        fontSize: '14px',
        color: '#ccc',
    },
    gridRow: {
        display: 'flex',
        flexWrap: 'wrap',
        justifyContent: 'space-between',
    },
};

export default Dashboard;

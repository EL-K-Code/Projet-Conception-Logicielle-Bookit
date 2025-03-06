import { useEffect, useState } from 'react';

const EarningCard = () => {
    const [events, setEvents] = useState([]);
    const [activeOption, setActiveOption] = useState(null);

    // URL de l'API pour récupérer les événements
    const apiUrl = 'api/evenements/get-all-room-event/';  // Remplacer par l'URL de ton API

    // Récupérer les événements de l'API
    useEffect(() => {
        const fetchEvents = async () => {
            try {
                const response = await fetch(apiUrl);
                const data = await response.json();
                setEvents(data);  // Mettre à jour l'état avec les événements récupérés
            } catch (error) {
                console.error('Erreur lors de la récupération des événements:', error);
            }
        };

        fetchEvents();
    }, []);

    const handleClick = (option) => {
        setActiveOption(option);
        alert(`Option ${option} clicked!`);
    };

    return (
        <div>
            {events.length === 0 ? (
                <div>Loading events...</div>
            ) : (
                events.map((event) => (
                    <div style={styles.card} key={event.id}>
                        {/* Menu en haut avec les options */}
                        <div style={styles.menu}>
                            <div
                                style={activeOption === 'reserve' ? styles.activeMenuItem : styles.menuItem}
                                onClick={() => handleClick('reserve')}
                            >
                                Réserver
                            </div>
                            <div
                                style={activeOption === 'event' ? styles.activeMenuItem : styles.menuItem}
                                onClick={() => handleClick('event')}
                            >
                                Événement
                            </div>
                            <div
                                style={activeOption === 'modify' ? styles.activeMenuItem : styles.menuItem}
                                onClick={() => handleClick('modify')}
                            >
                                Modifier Événement
                            </div>
                        </div>

                        {/* Contenu de l'événement */}
                        <div style={styles.amount}>{event.id}</div>
                        <div style={styles.text}>{event.description}</div>
                    </div>
                ))
            )}
        </div>
    );
};

const styles = {
    card: {
        backgroundColor: '#333',
        padding: '20px',
        borderRadius: '10px',
        width: '300px',
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
    activeMenuItem: {
        fontSize: '14px',
        cursor: 'pointer',
        padding: '5px 10px',
        borderRadius: '5px',
        color: 'white',
        backgroundColor: '#555',
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
};

export default EarningCard;

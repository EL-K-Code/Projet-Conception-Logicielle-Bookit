//hooks import
import { useEffect, useState } from 'react';

// material-ui
import { Grid } from '@mui/material';

// project imports
import api from '@/api';
import EventBusCard from '@/components/dashboard/EventBusCard';
import EventMaterialCard from '@/components/dashboard/EventMaterialCard';
import EventRoomCard from '@/components/dashboard/EventRoomCard';
import ReservedEventsCard from '@/components/dashboard/ReservedEventsCard';
import { gridSpacing } from '@/store/constants';
import TitleCard from '@/ui-component/cards/TitleCard';

// ==============================|| DEFAULT DASHBOARD ||============================== //

const Dashboard = () => {

    const [isLoading, setLoading] = useState(true);
    const [events, setEvents] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchEvents = async () => {
            try {
                const response = await api.get('api/evenements/list-event/');  // Utilise l'URL de l'API
                setEvents(response.data);  // Met à jour les événements avec les données reçues
                setLoading(false);
                console.log(response);
            } catch (error) {
                setError(error.message);  // Affiche l'erreur dans l'état
                setLoading(false);
                console.error("Erreur lors de la récupération des événements:", error);
            }
        };

        fetchEvents();
    }, []);

    const renderEventCard = (event) => {
        switch (event.type_event) {
            case 'event_bus':
                return <EventBusCard key={event.id} event={event} CardHeight={200} />;
            case 'event_room':
                return <EventRoomCard key={event.id} event={event} CardHeight={200} />;
            case 'event_material':
                return <EventMaterialCard key={event.id} event={event} CardHeight={200} />;
            default:
                return null;
        }
    };

    return (
        <Grid container spacing={gridSpacing}>

{/* Première colonne */}
            <Grid item xs={8}>
                <Grid container spacing={gridSpacing}>
                    {events.map(event => (
                        <Grid item lg={6} md={6} sm={6} xs={12} key={event.id}>
                            {renderEventCard(event)}
                        </Grid>
                    ))}
                </Grid>
            </Grid>

{/* Deuxième colonne */}

            <Grid item xs={4}>
                <Grid container spacing={gridSpacing}>
                    {/* Ligne 1 */}
                    <Grid item lg={12}>
                        <TitleCard/>
                    </Grid>
                    {/* Ligne 2 */}
                    <Grid item lg={12}>
                        <ReservedEventsCard/>
                    </Grid>
                </Grid>
            </Grid>

        </Grid>
    );
};

export default Dashboard;

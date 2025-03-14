import { useEffect, useState } from 'react';
import { Grid, Button, Box, useMediaQuery } from '@mui/material';
import { useTheme } from '@mui/material/styles';

// project imports
import EventBusCard from '@/components/dashboard/EventBusCard';
import EventMaterialCard from '@/components/dashboard/EventMaterialCard';
import EventRoomCard from '@/components/dashboard/EventRoomCard';
import UserReservedEventsCard from '@/components/dashboard/UserReservedEventsCard';
import { gridSpacing } from '@/store/constants';
import TitleCard from '@/ui-component/cards/TitleCard';
import api from '@/utils/api';
import ErrorBox from '@/utils/erro';

const Dashboard = () => {
    const [events, setEvents] = useState([]);
    const [error, set_error] = useState(null);
    const [showSidebar, setShowSidebar] = useState(false); // Toggle sur petit écran

    const theme = useTheme();
    const isSmallScreen = useMediaQuery(theme.breakpoints.down('sm')); // Détecte les écrans < 600px

    useEffect(() => {
        const fetchEvents = async () => {
            try {
                const response = await api.get('api/evenements/list-event/', { auth_required: false });
                setEvents(response.data);
                set_error(null);
            } catch (error) {
                set_error({
                    statusCode: error.response?.status || 500,
                });
            }
        };
        fetchEvents();
    }, []);

    const renderEventCard = (event) => {
        switch (event.type_event) {
            case 'event_bus':
                return <EventBusCard event={event} CardHeight={200} />;
            case 'event_room':
                return <EventRoomCard event={event} CardHeight={200} />;
            case 'event_material':
                return <EventMaterialCard event={event} CardHeight={200} />;
            default:
                return null;
        }
    };

    return (
        <>
            {error && <ErrorBox statusCode={error.statusCode} defaultMessage={error.defaultMessage} />}

            {/* Bouton aligné à droite sur mobile */}
            {isSmallScreen && (
                <Box sx={{ display: 'flex', justifyContent: 'flex-end', mb: 2 }}>
                    <Button
                        variant="contained"
                        color="primary"
                        onClick={() => setShowSidebar(!showSidebar)}
                    >
                        {showSidebar ? 'Back to events' : 'View my bookings'}
                    </Button>
                </Box>
            )}

            <Grid container spacing={gridSpacing}>

                {/* Première colonne */}
                <Grid item xs={12} md={8} sx={{ display: isSmallScreen && showSidebar ? 'none' : 'block' }}>
                    <Grid container spacing={gridSpacing}>
                        {events.map(event => (
                            <Grid item lg={6} md={6} sm={6} xs={12} key={event.id}>
                                {renderEventCard(event)}
                            </Grid>
                        ))}
                    </Grid>
                </Grid>

                {/* Deuxième colonne */}
                <Grid item xs={12} md={4} sx={{ display: isSmallScreen && !showSidebar ? 'none' : 'block' }}>
                    <Grid container spacing={gridSpacing}>
                        <Grid item lg={12} sx={{ width: '100%', maxWidth: '100%' }}>
                            <TitleCard />
                        </Grid>
                        <Grid item lg={12} sx={{ width: '100%', maxWidth: '100%' }}>
                            <UserReservedEventsCard api_url={'api/reservations/user-reservations/'}/>
                        </Grid>
                    </Grid>
                </Grid>

            </Grid>
        </>
    );
};

export default Dashboard;



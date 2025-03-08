//hooks import
import { useEffect, useState } from 'react';

// material-ui
import { Grid } from '@mui/material';

// project imports
import EventBusCard from '@/components/dashboard/EventBusCard';
import EventMaterialCard from '@/components/dashboard/EventMaterialCard';
import EventRoomCard from '@/components/dashboard/EventRoomCard';
import UserReservedEventsCard from '@/components/dashboard/UserReservedEventsCard';
import { gridSpacing } from '@/store/constants';
import TitleCard from '@/ui-component/cards/TitleCard';
import api from '@/utils/api';
import ErrorBox from '@/utils/erro';

// ==============================|| DEFAULT DASHBOARD ||============================== //

const Dashboard = () => {

    const [isLoading, setLoading] = useState(true);
    const [events, setEvents] = useState([]);
    const [error, set_error] = useState(null);

    useEffect(() => {
        const fetchEvents = async () => {
            try {
                const response = await api.get('api/evenements/list-event/', { auth_required: false });
                setEvents(response.data);
                setLoading(false);
                set_error(null);

            } catch (error) {
                setLoading(false);
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
        {error && (
            <ErrorBox
            statusCode={error.statusCode}
            defaultMessage={error.defaultMessage}
            />
        )}
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
                        <UserReservedEventsCard api_url={'api/reservations/user-reservations/'}/>
                    </Grid>
                </Grid>
            </Grid>

        </Grid>
    </>
    );
};

export default Dashboard;

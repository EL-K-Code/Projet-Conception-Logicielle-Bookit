import api from '@/api';
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';

// material-ui
import { Button, CardActions, CardContent, Divider, Grid, Typography } from '@mui/material';
import { useTheme } from '@mui/material/styles';

// project imports
import ErrorBox from '@/components/erro';
import MainCard from '@/ui-component/cards/MainCard';

// types
// import PropTypes from 'prop-types';

// assets

// ==============================|| DASHBOARD DEFAULT -  ReservedEventCard   ||============================== //

const UserReservedEventsCard = ({api_url}) => {
    const theme = useTheme();
    const [reservations, set_reservations] = useState([]);
    const router = useRouter();
    const [error, set_error] = useState(null);

    useEffect(() => {
        const fetchReservations = async () => {
            try {
                const response = await api.get(api_url);
                set_reservations(response.data);
                set_error(null);
            } catch (error) {
                set_error({
                    statusCode: error.response?.status || 500,
                  });
            }
        };

        fetchReservations();
    }, [api_url]);

    const [anchorEl, setAnchorEl] = useState(null);

    const handleClick = (event) => {
        setAnchorEl(event.currentTarget);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    return (
              <>
                {error && (
                <ErrorBox
                statusCode={error.statusCode}
                defaultMessage={error.defaultMessage}
                />
                )}
                <MainCard content={false}>
                <CardContent>
                    <Grid container spacing={2}>
                        {reservations.map((reservation) => (
                            <Grid item xs={12} key={reservation.id}>
                                <Grid container direction="column">
                                    <Grid item>
                                        <Grid container alignItems="center" justifyContent="space-between">
                                            <Grid item>
                                                <Typography variant="subtitle1" color="inherit">
                                                    {reservation?.event_room_details?.description ||
                                                    reservation?.event_bus_details?.description ||
                                                    reservation?.event_material_details?.description || "Réservation"}
                                                </Typography>
                                            </Grid>
                                            <Grid item>
                                                <Typography variant="subtitle1" color="inherit">
                                                    {reservation.created_at || "Date non disponible"}
                                                </Typography>
                                            </Grid>
                                        </Grid>
                                    </Grid>
                                    <Grid item>
                                        <Typography variant="subtitle2" sx={{ color: 'text.secondary' }}>
                                            {reservation.status || "Statut non disponible"}
                                        </Typography>
                                    </Grid>
                                    <Divider sx={{ my: 1.5 }} />
                                </Grid>
                            </Grid>
                        ))}
                    </Grid>
                </CardContent>
                    <CardActions sx={{ p: 1.25, pt: 0, justifyContent: 'center' }}>
                        <Button size="small" disableElevation>
                            View All
                            {/* <ChevronRightOutlinedIcon /> */}
                        </Button>
                    </CardActions>
                </MainCard>

        </>
    );
};

// ReservedEvent.propTypes = {
//     isLoading: PropTypes.bool
// };

export default UserReservedEventsCard;
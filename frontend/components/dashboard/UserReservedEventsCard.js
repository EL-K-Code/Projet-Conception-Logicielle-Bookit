import api from '@/utils/api';
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';

// material-ui
import { Button, CardActions, CardContent, Divider, Grid, Typography } from '@mui/material';
import { useTheme } from '@mui/material/styles';

// project imports
import MainCard from '@/ui-component/cards/MainCard';
import ErrorBox from '@/utils/erro';
import getIconeByType from '../icone';

//date import
import { format, parseISO } from 'date-fns';




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
                    defaultMessage: error.response?.status==401 ? "Certaines ressources de cette page nécessitent une authentification pour y accéder." : '',
                  });
            }
        };

        fetchReservations();
    }, [api_url]);

    const [anchorEl, setAnchorEl] = useState(null);

    const cancelReservation= (reservation) => {
        router.push(`/reservations/cancel/${reservation.type_reservation}/${reservation.id}`);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    const formattedDate = (date) => {
         return format(parseISO(date), 'dd MMM yyyy HH:mm');
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
                    <Grid container spacing={2} sx={{ maxWidth: '100%' }}>
                    {reservations.map((reservation) => (
                        <Grid item xs={12} key={reservation.id}>
                        <Grid
                            container
                            direction="column"
                            sx={{
                            width: '100%',
                            maxWidth: '800px',
                            margin: '0 auto',
                            }}
                        >
                            <Grid item>
                            <Grid container alignItems="center" justifyContent="space-between">
                                <Grid
                                item
                                sx={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    gap: 1,
                                    padding: '4px 8px',
                                    borderRadius: '8px',
                                    backgroundColor: theme.palette.background.default,
                                    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
                                    flexBasis: '100%',
                                    maxWidth: '100%',
                                }}
                                >
                                {getIconeByType(reservation.type_reservation, theme)}
                                <Typography
                                    variant="subtitle1"
                                    sx={{
                                    fontWeight: 600,
                                    color: theme.palette.text.primary,
                                    whiteSpace: 'nowrap',
                                    overflow: 'hidden',
                                    textOverflow: 'ellipsis',
                                    maxWidth: '200px',
                                    fontSize : "120%"
                                    }}
                                >
                                    {reservation?.event_room_details?.resource_name ||
                                    reservation?.event_bus_details?.description ||
                                    reservation?.event_material_details?.resource_name ||
                                    'Réservation'}
                                </Typography>
                                <Typography
                                    variant="subtitle2"
                                    sx={{
                                    color: theme.palette.text.secondary,
                                    marginLeft: 'auto',
                                    padding: '2px 6px',
                                    backgroundColor: theme.palette.action.hover,
                                    borderRadius: '4px',
                                    fontSize: "120%"
                                    }}
                                >
                                    {getIconeByType("date", theme)}
                                    {formattedDate(reservation?.created_at) || 'Date non disponible'}
                                </Typography>

                                {getIconeByType("cancel", theme, () => cancelReservation(reservation))}
                                </Grid>
                            </Grid>
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
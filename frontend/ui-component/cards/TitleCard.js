// material-ui
import { Avatar, Box, List, ListItem, ListItemAvatar, ListItemText, Typography } from '@mui/material';
import { styled, useTheme } from '@mui/material/styles';

// project imports
import MainCard from './MainCard';


// types

// styles
const CardWrapper = styled(MainCard)(({ theme }) => ({
    width: '100%',
    maxWidth: '100%',
    boxSizing: 'border-box',
    overflow: 'hidden',
    position: 'relative',
    '&:after': {
        content: '""',
        position: 'relative',
        width: 210,
        height: 210,
        background: `linear-gradient(210.04deg, ${theme.palette.warning.dark} -50.94%, rgba(144, 202, 249, 0) 83.49%)`,
        borderRadius: '50%',
        top: -30,
        right: '-50%'
    },
    '&:before': {
        content: '""',
        position: 'relative',
        width: '50%',
        height: '50%',
        maxWidth: 210,
        background: `linear-gradient(140.9deg, ${theme.palette.warning.dark} -14.02%, rgba(144, 202, 249, 0) 70.50%)`,
        borderRadius: '50%',
        top: -160,
        right: '-50%'
    }
}));

// ==============================|| Titre CARD ||============================== //

const TitleCard = () => {
    const theme = useTheme();

    return (
        <>
                <CardWrapper border={false} content={false}>
                    <Box sx={{ p: 2 }}>
                        <List sx={{ py: 0 }}>
                            <ListItem alignItems="center" disableGutters sx={{ py: 0 }}>
                                <ListItemAvatar>
                                    <Avatar
                                        variant="rounded"
                                        sx={{
                                            ...theme.typography.commonAvatar,
                                            ...theme.typography.largeAvatar,
                                            backgroundColor: theme.palette.warning.light,
                                            color: theme.palette.warning.dark
                                        }}
                                    >
                                        {/* <StorefrontTwoToneIcon fontSize="inherit" /> */}
                                    </Avatar>
                                </ListItemAvatar>
                                <ListItemText
                                    sx={{
                                        py: 0,
                                        mt: 0.45,
                                        mb: 0.45
                                    }}
                                    primary={<Typography variant="h4">My bookings</Typography>}
                                />
                            </ListItem>
                        </List>
                    </Box>
                </CardWrapper>

        </>
    );
};


export default TitleCard;

import { Avatar, Box, ButtonBase } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import PropTypes from 'prop-types';

import LogoSection from '../LogoSection';
import NotificationSection from './NotificationSection';
import ProfileSection from './ProfileSection';

import { IconMenu2 } from '@tabler/icons-react';


// ==============================|| MAIN NAVBAR / HEADER ||============================== //

const Header = ({ handleLeftDrawerToggle }) => {
    const theme = useTheme();

    return (
        <Box
            sx={{
                display: 'flex',
                alignItems: 'center',
                width: '100%',
                padding: theme.spacing(1, 2)
            }}
        >
            {/* Logo & Menu Button */}
            <Box
                sx={{
                    width: 228,
                    display: 'flex',
                    alignItems: 'center',
                    [theme.breakpoints.down('md')]: {
                        width: 'auto'
                    }
                }}
            >
                <Box component="span" sx={{ display: { xs: 'none', md: 'block' }, flexGrow: 1 }}>
                    <LogoSection />
                </Box>
                <ButtonBase sx={{ borderRadius: '12px', overflow: 'hidden' }}>
                    <Avatar
                        variant="rounded"
                        sx={{
                            ...theme.typography.commonAvatar,
                            ...theme.typography.mediumAvatar,
                            transition: 'all .2s ease-in-out',
                            background: theme.palette.secondary.light,
                            color: theme.palette.secondary.dark,
                            '&:hover': {
                                background: theme.palette.secondary.dark,
                                color: theme.palette.secondary.light
                            }
                        }}
                        onClick={handleLeftDrawerToggle}
                        color="inherit"
                    >
                        <IconMenu2 stroke={1.5} size="1.3rem" />
                    </Avatar>
                </ButtonBase>
            </Box>

            {/* Espace automatique pour pousser les sections à droite */}
            <Box sx={{ flexGrow: 1 }} />

            {/* Notification & Profile Aligned Right */}
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                <NotificationSection />
                <ProfileSection />
            </Box>
        </Box>
    );
};

Header.propTypes = {
    handleLeftDrawerToggle: PropTypes.func
};

export default Header;


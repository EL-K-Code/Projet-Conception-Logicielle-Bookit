import { useRouter } from 'next/router';
import { useState } from "react";
// Material-UI
import { Avatar, Box, Grid, Menu, MenuItem, Typography } from "@mui/material";
import { styled, useTheme } from "@mui/material/styles";
import PropTypes from 'prop-types';

// Project imports
import AccessComponent from '@/components/AccessComponent';
import getIconeByType from '@/components/icone';
import MainCard from "@/ui-component/cards/MainCard";

// Assets

// Styles
const CardWrapper = styled(MainCard)(({ theme, CardHeight }) => ({
  backgroundColor: theme.palette.secondary.dark,
  color: "#fff",
  position: "relative",
  height: CardHeight, // Hauteur fixe
  display: "flex",
  flexDirection: "column",
  justifyContent: "space-between", // Répartit l'espace entre les éléments
  "&:after": {
    content: '""',
    position: "absolute",
    width: 210,
    height: 210,
    background: theme.palette.secondary[800],
    borderRadius: "50%",
    top: -85,
    right: -95,
    [theme.breakpoints.down("sm")]: {
      top: -105,
      right: -140,
    },
  },
  "&:before": {
    content: '""',
    position: "absolute",
    width: 210,
    height: 210,
    background: theme.palette.secondary[800],
    borderRadius: "50%",
    top: -125,
    right: -15,
    opacity: 0.5,
    [theme.breakpoints.down("sm")]: {
      top: -155,
      right: -70,
    },
  },
}));


const EventRoomCard = ({event, CardHeight }) => {
  const theme = useTheme();
  const [anchorEl, setAnchorEl] = useState(null);
  const router = useRouter();

  const handleClick = (eventclicked) => {
    setAnchorEl(eventclicked.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleAction = (url) => {
    handleClose(); // Fermer le menu
    router.push(url); // Rediriger vers la page voulue
};

  return (
    <>
  <CardWrapper border={false} content={false} CardHeight={CardHeight}>
        <Box
  sx={{
    p: 2.25,
    display: "flex",
    flexDirection: "column",
    height: "100%", // Prend toute la hauteur de la CardWrapper
  }}
>
  <Grid
    container
    direction="column"
    sx={{ flexGrow: 1, overflow: "hidden" }}
  >
    {/* En-tête avec les avatars */}
    <Grid item>
      <Grid container justifyContent="space-between">
        <Grid item>
          <Avatar
            variant="rounded"
            sx={{
              ...theme.typography.commonAvatar,
              ...theme.typography.largeAvatar,
              backgroundColor: theme.palette.secondary[800],
              mt: 1,
            }}
          >
            {getIconeByType("room", theme)}
         </Avatar>

        </Grid>
        <Grid item>
        <Avatar
            variant="rounded"
            sx={{
              ...theme.typography.commonAvatar,
              ...theme.typography.mediumAvatar,
              backgroundColor: theme.palette.secondary.dark,
              color: theme.palette.secondary[200],
              zIndex: 1,
            }}
            aria-controls="menu-earning-card"
            aria-haspopup="true"
            onClick={handleClick}
          >
            {getIconeByType("more", theme)}
          </Avatar>
          <Menu
            id="menu-earning-card"
            anchorEl={anchorEl}
            keepMounted
            open={Boolean(anchorEl)}
            onClose={handleClose}
            anchorOrigin={{ vertical: "bottom", horizontal: "right" }}
            transformOrigin={{ vertical: "top", horizontal: "right" }}
          >
             <MenuItem onClick={() => handleAction(`/reservations/make/room/${event.id}`)}>
             {getIconeByType("calender", theme)} Make a reservation
            </MenuItem>


            <AccessComponent requiredGroups={["event_admin"]}>
              <MenuItem onClick={() => handleAction(`/events/update/room/${event.id}`)}>
                {getIconeByType("edit", theme)} Update event
              </MenuItem>
            </AccessComponent>

            <AccessComponent requiredGroups={["event_admin"]}>
              <MenuItem onClick={() => handleAction(`/events/delete/room/${event.id}`)}>
              {getIconeByType("cancel", theme)} Delete event
              </MenuItem>
            </AccessComponent>
          </Menu>
        </Grid>
      </Grid>
    </Grid>

    {/* Section centrale (valeur) avec flexGrow pour s'adapter */}
    <Grid item sx={{ flexGrow: 1, minHeight: 0 }}>
      <Grid container alignItems="center" sx={{ height: "100%" }}>
        <Grid item sx={{ flexGrow: 1 }}>
          <Typography
            sx={{
              fontSize: "clamp(1.25rem, 5vw, 2.125rem)",
              fontWeight: 500,
              mr: 1,
              mt: 1.75,
              mb: 0.75,
              whiteSpace: "nowrap",
              overflow: "hidden",
              textOverflow: "ellipsis",
            }}
          >
            {event.resource_name}
          </Typography>
        </Grid>
        <Grid item>
          <Avatar
            sx={{
              cursor: "pointer",
              ...theme.typography.smallAvatar,
              backgroundColor: theme.palette.secondary[200],
              color: theme.palette.secondary.dark,
            }}
          />
        </Grid>
      </Grid>
    </Grid>

    {/* Pied de page avec le texte */}
    <Grid item sx={{ mb: 1.25 }}>
      <Typography
        sx={{
          fontSize: "clamp(0.75rem, 3vw, 1rem)",
          fontWeight: 500,
          color: theme.palette.secondary[200],
          whiteSpace: "nowrap",
          overflow: "hidden",
          textOverflow: "ellipsis",
        }}
      >
        {event.description}
      </Typography>
    </Grid>
  </Grid>
</Box>

        </CardWrapper>
      {/* )} */}
    </>
  );
};

EventRoomCard.propTypes = {
  CardHeight : PropTypes.number.isRequired,
};

export default EventRoomCard;

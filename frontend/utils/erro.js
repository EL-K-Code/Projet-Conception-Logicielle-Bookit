import { Box, Button, Modal, Typography } from '@mui/material';
import { useState } from 'react';


const ErrorBox = ({ statusCode, defaultMessage }) => {
  const [open, setOpen] = useState(true);

  const handleClose = () => {
    setOpen(false);
  };

  const getMessageFromStatus = (status) => {
    switch (status) {
      case 400:
        return "Requête invalide.";
      case 401:
        return "Vous devez être connecté pour accéder à cette ressource.";
      case 403:
        return "Accès refusé.";
      case 404:
        return "Ressource non trouvée.";
      case 500:
        return "Erreur interne du serveur.";
      default:
        return "Une erreur inattendue est survenue.";
    }
  };

  return (
    <Modal open={open} onClose={handleClose}>
      <Box
        sx={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          bgcolor: 'background.paper',
          boxShadow: 24,
          p: 4,
          borderRadius: 2,
          maxWidth: '400px',
          textAlign: 'center',
        }}
      >
        <Typography variant="body1" sx={{ mb: 3 }}>
          {defaultMessage || getMessageFromStatus(statusCode)}
        </Typography>
        <Button variant="contained" color="error" onClick={handleClose}>
          Fermer
        </Button>
      </Box>
    </Modal>
  );
};



export default ErrorBox;


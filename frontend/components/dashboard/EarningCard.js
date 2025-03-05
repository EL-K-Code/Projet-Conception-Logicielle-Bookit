import { Avatar, Box, Grid, Menu, MenuItem, Typography } from '@mui/material';
import { styled, useTheme } from '@mui/material/styles';
import Image from 'next/image';
import PropTypes from 'prop-types';
import { useState } from 'react';

// Icônes Material-UI
import ArchiveTwoToneIcon from '@mui/icons-material/ArchiveOutlined';
import ArrowUpwardIcon from '@mui/icons-material/ArrowUpward';
import FileCopyTwoToneIcon from '@mui/icons-material/FileCopyOutlined';
import GetAppTwoToneIcon from '@mui/icons-material/GetAppOutlined';
import MoreHorizIcon from '@mui/icons-material/MoreHoriz';
import PictureAsPdfTwoToneIcon from '@mui/icons-material/PictureAsPdfOutlined';

// Importation de l'image
import EarningIcon from '@/assets/images/icons/earning.svg'; // Assure-toi que le chemin est correct

const CardWrapper = styled(Box)(({ theme }) => ({
    backgroundColor: theme.palette.secondary.dark,
    color: '#fff',
    overflow: 'hidden',
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    padding: theme.spacing(3),
    boxShadow: theme.shadows[3],
}));

const EarningCard = ({ isLoading }) => {
    const theme = useTheme();
    const [anchorEl, setAnchorEl] = useState(null);

    const handleClick = (event) => setAnchorEl(event.currentTarget);
    const handleClose = () => setAnchorEl(null);

    return (
        <CardWrapper>
            <Grid container direction="column">
                {/* En-tête */}
                <Grid item>
                    <Grid container justifyContent="space-between">
                        <Grid item>
                            <Avatar
                                variant="rounded"
                                sx={{
                                    backgroundColor: theme.palette.secondary[800],
                                    mt: 1,
                                    width: 56,
                                    height: 56,
                                }}
                            >
                                <Image src={EarningIcon} alt="Earnings" width={40} height={40} />
                            </Avatar>
                        </Grid>
                        <Grid item>
                            <Avatar
                                variant="rounded"
                                sx={{
                                    backgroundColor: theme.palette.secondary.dark,
                                    color: theme.palette.secondary[200],
                                }}
                                onClick={handleClick}
                            >
                                <MoreHorizIcon />
                            </Avatar>
                            <Menu
                                anchorEl={anchorEl}
                                open={Boolean(anchorEl)}
                                onClose={handleClose}
                                anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
                                transformOrigin={{ vertical: 'top', horizontal: 'right' }}
                            >
                                <MenuItem onClick={handleClose}>
                                    <GetAppTwoToneIcon sx={{ mr: 1.75 }} /> Importer
                                </MenuItem>
                                <MenuItem onClick={handleClose}>
                                    <FileCopyTwoToneIcon sx={{ mr: 1.75 }} /> Copier
                                </MenuItem>
                                <MenuItem onClick={handleClose}>
                                    <PictureAsPdfTwoToneIcon sx={{ mr: 1.75 }} /> Exporter PDF
                                </MenuItem>
                                <MenuItem onClick={handleClose}>
                                    <ArchiveTwoToneIcon sx={{ mr: 1.75 }} /> Archiver
                                </MenuItem>
                            </Menu>
                        </Grid>
                    </Grid>
                </Grid>

                {/* Valeur des revenus */}
                <Grid item>
                    <Grid container alignItems="center">
                        <Typography sx={{ fontSize: '2.125rem', fontWeight: 500, mr: 1, mt: 1.75, mb: 0.75 }}>
                            $500.00
                        </Typography>
                        <Avatar
                            sx={{
                                backgroundColor: theme.palette.secondary[200],
                                color: theme.palette.secondary.dark,
                                width: 32,
                                height: 32,
                            }}
                        >
                            <ArrowUpwardIcon fontSize="small" />
                        </Avatar>
                    </Grid>
                </Grid>

                {/* Texte explicatif */}
                <Grid item sx={{ mb: 1.25 }}>
                    <Typography sx={{ fontSize: '1rem', fontWeight: 500, color: theme.palette.secondary[200] }}>
                        Total des gains
                    </Typography>
                </Grid>
            </Grid>
        </CardWrapper>
    );
};

EarningCard.propTypes = {
    isLoading: PropTypes.bool,
};

export default EarningCard;

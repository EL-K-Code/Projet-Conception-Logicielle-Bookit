"use client";

//next import
import Link from "next/link";

import Form from "./Form";

// material-ui
import { Divider, Grid, Stack, Typography, useMediaQuery } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import PropTypes from 'prop-types';

// project imports
import AuthCardWrapper from './AuthCardWrapper';
import AuthWrapper1 from './AuthWrapper1';
// import Logo from '@/ui-component/Logo';
// import AuthFooter from '@/ui-component/cards/AuthFooter';

// assets

// ================================|| AUTH3 - LOGIN ||================================ //

const Auth = ({ route, method }) => {
    const theme = useTheme();
    const matchDownSM = useMediaQuery(theme.breakpoints.down('md'));

    return (
         <AuthWrapper1>
            <Grid container direction="column" justifyContent="flex-end" sx={{ minHeight: '100vh' }}>
                <Grid item xs={12}>
                    <Grid container justifyContent="center" alignItems="center" sx={{ minHeight: 'calc(100vh - 68px)' }}>
                        <Grid item sx={{ m: { xs: 1, sm: 3 }, mb: 0 }}>
                            <AuthCardWrapper>
                                <Grid container spacing={2} alignItems="center" justifyContent="center">
                                    <Grid item sx={{ mb: 3 }}>
                                        {/* <Link href="#">
                                            <Logo />
                                        </Link> */}
                                    </Grid>
                                    <Grid item xs={12}>
                                        <Grid
                                            container
                                            direction={matchDownSM ? 'column-reverse' : 'row'}
                                            alignItems="center"
                                            justifyContent="center"
                                        >
                                            <Grid item>
                                                <Stack alignItems="center" justifyContent="center" spacing={1}>
                                                    <Typography
                                                        color={theme.palette.secondary.main}
                                                        gutterBottom
                                                        variant={matchDownSM ? 'h3' : 'h2'}
                                                    >
                                                        Hi, Welcome Back
                                                    </Typography>
                                                    <Typography
                                                        variant="caption"
                                                        fontSize="16px"
                                                        textAlign={matchDownSM ? 'center' : 'inherit'}
                                                    >
                                                        Enter your credentials to continue
                                                    </Typography>
                                                </Stack>
                                            </Grid>
                                        </Grid>
                                    </Grid>
                                    <Grid item xs={12}>

                                        <Form route={route} method= {method} />

                                    </Grid>
                                    <Grid item xs={12}>
                                        <Divider />
                                    </Grid>
                                    <Grid item xs={12}>
                                    <Grid item container direction="column" alignItems="center" xs={12}>
                                    {method === "login" ?
                                        <Link href="/auth/signup" className="button">Don&apos;t have an account?</Link>:
                                        <Link href="/auth/login" className="button">Already registered?</Link>
                                    }
                                    </Grid>
                                    </Grid>
                                </Grid>
                            </AuthCardWrapper>
                        </Grid>
                    </Grid>
                </Grid>

            </Grid>
        </AuthWrapper1>
    );
};

Auth.propTypes = {
    route: PropTypes.oneOf(['/api/auth/login', '/api/auth/signup']),
    method: PropTypes.oneOf(['login', 'signup'])
  };

export default Auth;
"use client";

import "@/styles/Form.css";
import "@/styles/Global.css";
import "react-perfect-scrollbar/dist/css/styles.css";

import PropTypes from 'prop-types';

// Next.js & React
import { useEffect, useState } from "react";
import { useRouter } from "next/router";


// Redux
import store from "@/store";
import { Provider } from "react-redux";

// Material-UI
import theme from "@/themes";
import { CssBaseline, StyledEngineProvider } from "@mui/material";
import { ThemeProvider } from "@mui/material/styles";

// Layouts & Components
import ProtectedRoute from "@/components/ProtectedRoute";
import MainLayout from "@/layout";
import NavigationScroll from "@/layout/NavigationScroll";


const Bookit =({ Component, pageProps }) => {
  const router = useRouter();

  const [isClient, setIsClient] = useState(false);

  useEffect(() => {
    setIsClient(true);
  }, []);

  if (!isClient) {
    return null; // ou un loader
  }


  // const dispatch = useDispatch();

  // useEffect(() => {
  //   const savedGroups = JSON.parse(localStorage.getItem('userGroups'));
  //   if (savedGroups && savedGroups.length > 0) {
  //     dispatch(setUserGroup(savedGroups));

  //   }
  // }, [dispatch]);

  // Définir les routes nécessitant MainLayout ou MinimalLayout
  const notMainLayoutRoutes = ["/auth/login", "/auth/logout", "/auth/signup", "/auth/signout"];

  // Définir les routes protégées
  const notProtectedRoutes = ["/auth/login", "/auth/signup", "/"];

  // Déterminer le type de layout et si la page est protégée
  const notUseMainLayout = notMainLayoutRoutes.includes(router.pathname);
  const isNotProtected = notProtectedRoutes.includes(router.pathname);

  // Contenu de la page (protégé ou non)
  const pageContent = isNotProtected ? (
      <Component {...pageProps} />
  ) : (
    <ProtectedRoute>
      <Component {...pageProps} />
    </ProtectedRoute>
  );

  return (
    <Provider store={store}>
      <StyledEngineProvider injectFirst>
        <ThemeProvider theme={theme}>
          <CssBaseline />
          <NavigationScroll>
            {notUseMainLayout ? (
              pageContent
            ): (
              <MainLayout>{pageContent}</MainLayout>
            )}
          </NavigationScroll>
        </ThemeProvider>
      </StyledEngineProvider>
    </Provider>
  );
};

Bookit.propTypes = {
  Component: PropTypes.elementType.isRequired,
  pageProps: PropTypes.object,
};

export default Bookit;
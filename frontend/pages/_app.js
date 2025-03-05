"use client";

import "@/styles/Form.css";
import "@/styles/Global.css";
import "react-perfect-scrollbar/dist/css/styles.css";

// Next.js & React
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

export default function MyApp({ Component, pageProps }) {
  const router = useRouter();

  // Définir les routes nécessitant MainLayout ou MinimalLayout
  const mainLayoutRoutes = ["/", "/home", "/dashboard"];

  // Définir les routes protégées
  const protectedRoutes = ["/home", "/logout", "/signout"];

  // Déterminer le type de layout et si la page est protégée
  const useMainLayout = mainLayoutRoutes.includes(router.pathname);
  const isProtected = protectedRoutes.includes(router.pathname);

  // Contenu de la page (protégé ou non)
  const pageContent = isProtected ? (
    <ProtectedRoute>
      <Component {...pageProps} />
    </ProtectedRoute>
  ) : (
    <Component {...pageProps} />
  );

  return (
    <Provider store={store}>
      <StyledEngineProvider injectFirst>
        <ThemeProvider theme={theme}>
          <CssBaseline />
          <NavigationScroll>
            {useMainLayout ? (
              <MainLayout>{pageContent}</MainLayout>
            ): (
              pageContent
            )}
          </NavigationScroll>
        </ThemeProvider>
      </StyledEngineProvider>
    </Provider>
  );
}

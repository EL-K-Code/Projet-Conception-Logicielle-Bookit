"use client";

import ProtectedRoute from "@/components/ProtectedRoute";
import '@/styles/Form.css';
import '@/styles/Global.css';
import { useRouter } from 'next/router';

export default function MyApp({ Component, pageProps }) {
  const router = useRouter();  // Utilise le hook useRouter pour obtenir le router
  const protectedRoutes = ["/home", "/logout", "/signout"];
  const isProtected = protectedRoutes.includes(router.pathname); // Utilise router.pathname

  return isProtected ? (
    <ProtectedRoute>
      <Component {...pageProps} />
    </ProtectedRoute>
  ) : (
    <Component {...pageProps} />
  );
}

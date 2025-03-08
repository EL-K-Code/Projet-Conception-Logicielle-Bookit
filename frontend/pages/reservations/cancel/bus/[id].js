"use client" ;

import { useRouter } from 'next/router';

import CancelReservation from '@/components/reservations/CancelReservation';
export default function ReservEvent() {
  const router = useRouter();
  const { id } = router.query; // Récupère l'ID depuis l'URL

  return (
    <CancelReservation event_type="eventbus" api_url={`/api/reservations/cancel-reservation-bus/${id}`} />
  );
}
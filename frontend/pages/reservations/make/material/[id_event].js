"use client" ;

import { useRouter } from 'next/router';

import ReservationForm from '@/components/reservations/ReservationForm';
export default function ReservEvent() {
  const router = useRouter();
  const { id_event } = router.query; // Récupère l'ID depuis l'URL

  return (
    <ReservationForm event_type="eventmaterial" api_url="/api/reservations/make-reservation/material/" id={id_event}/>
  );
}

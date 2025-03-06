"use client" ;

import { useRouter } from 'next/router';

import ReservationForm from '@/components/events/ReservEvent';
export default function ReservEvent() {
  const router = useRouter();
  const { id_event } = router.query; // Récupère l'ID depuis l'URL

  return (
    <ReservationForm event_type="eventbus" api_url="/api/reservations/make-reservation/bus/" id={id_event}/>
  );
}

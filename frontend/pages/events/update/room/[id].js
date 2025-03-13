"use client" ;

import { useRouter } from 'next/router';

import UpdateEventForm from '@/components/events/UpdateEvent';
export default function ReservEvent() {
  const router = useRouter();
  const { id} = router.query; // Récupère l'ID depuis l'URL

  return (
    <UpdateEventForm event_type="eventroom" route ="api/evenements/list-all-room-resource/" api_url="/api/evenements/update-event-room" id={id}/>
  );
}

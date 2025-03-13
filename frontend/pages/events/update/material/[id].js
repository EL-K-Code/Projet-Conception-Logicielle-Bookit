"use client" ;

import { useRouter } from 'next/router';

import UpdateEventForm from '@/components/events/UpdateEvent';
export default function ReservEvent() {
  const router = useRouter();
  const { id} = router.query; // Récupère l'ID depuis l'URL

  return (
    <UpdateEventForm event_type="eventmaterial" route ="api/evenements/list-all-material-resource/" api_url="/api/evenements/update-event-material" id={id}/>
  );
}

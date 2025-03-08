import EventForm from "@/components/events/EventForm";

export default function CreateEventRoom() {
  return (
    <div>
      <EventForm event_type="eventroom" route="/api/evenements/create-event/room/" api_url= "api/evenements/list-all-room-resource/"/>
    </div>
  );
}

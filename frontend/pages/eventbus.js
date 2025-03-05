import EventForm from "@/components/FormEvent";

export default function CreateEventBus() {
  return (
    <div>
      <EventForm event_type="eventbus" route="/api/evenements/create-event/material/" api_url= "api/evenements/list-all-bus-resource/"/>
    </div>
  );
}

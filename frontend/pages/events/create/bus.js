import EventForm from "@/components/events/EventForm";

export default function CreateEventBus() {
  return (
    <div>
      <EventForm event_type="eventbus" route="/api/evenements/create-event/bus/" api_url= "api/evenements/list-all-bus-resource/"/>
    </div>
  );
}

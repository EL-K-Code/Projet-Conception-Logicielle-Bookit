import EventForm from "@/components/FormEvent";

export default function CreateEventMaterial() {
  return (
    <div>
      <EventForm event_type="eventmaterial" route="/api/evenements/create-event/material/" api_url= "api/evenements/list-all-material-resource/" />
    </div>
  );
}

from rest_framework import generics
from rest_framework.response import Response

from .models import EventBus, EventMaterial, EventRoom
from .permissions import IsEventAdmin, IsEventAdminAndOwner
from .serializers import (
    EventBusSerializer,
    EventMaterialSerializer,
    EventRoomSerializer,
)


class EventListView(generics.ListAPIView):
    """
    Cette vue liste à la fois les EventRoom, EventBus et EventMaterial
    """

    def get(self, request, *args, **kwargs):
        # Récupérer tous les événements des trois modèles
        event_rooms = EventRoom.objects.all()
        event_buses = EventBus.objects.all()
        event_materials = EventMaterial.objects.all()

        # Sérialiser les données
        room_serializer = EventRoomSerializer(event_rooms, many=True)
        bus_serializer = EventBusSerializer(event_buses, many=True)
        material_serializer = EventMaterialSerializer(event_materials, many=True)

        # Combiner les résultats dans une réponse
        return Response(
            {
                "event_rooms": room_serializer.data,
                "event_buses": bus_serializer.data,
                "event_materials": material_serializer.data,
            }
        )


class GetAllRoomEventView(generics.ListAPIView):
    """
    Vue permettant de lister les évenements room
    """

    queryset = EventRoom.objects.all()
    serializer_class = EventRoomSerializer


class GetAllBusEventView(generics.ListAPIView):
    """
    Vue permettant de lister les évenements bus
    """

    queryset = EventBus.objects.all()
    serializer_class = EventBusSerializer


class GetAllMaterialEventView(generics.ListAPIView):
    """
    Vue permettant de lister les évenements material
    """

    queryset = EventMaterial.objects.all()
    serializer_class = EventMaterialSerializer


class CreateEventRoomView(generics.CreateAPIView):
    """
    Vue permettant de créer un évènement room
    """

    queryset = EventRoom.objects.all()
    serializer_class = EventRoomSerializer
    permission_classes = [IsEventAdmin]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class CreateEventBusView(generics.CreateAPIView):
    """
    Vue permettant de créer un évènement bus
    """

    queryset = EventBus.objects.all()
    serializer_class = EventBusSerializer
    permission_classes = [IsEventAdmin]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class CreateEventMaterialView(generics.CreateAPIView):
    """
    Vue permettant de créer un évènement material
    """

    queryset = EventMaterial.objects.all()
    serializer_class = EventMaterialSerializer
    permission_classes = [IsEventAdmin]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class DeleteEventRoomView(generics.DestroyAPIView):
    """
    Vue permettant de supprimer un event room
    """

    queryset = EventRoom.objects.all()
    serializer_class = EventRoomSerializer
    permission_classes = [IsEventAdminAndOwner]


class DeleteEventBusView(generics.DestroyAPIView):
    """
    Vue permettant de supprimer un event bus
    """

    queryset = EventBus.objects.all()
    serializer_class = EventBusSerializer
    permission_classes = [IsEventAdminAndOwner]


class DeleteEventMaterialView(generics.DestroyAPIView):
    """
    Vue permettant de supprimer un event material
    """

    queryset = EventMaterial.objects.all()
    serializer_class = EventMaterialSerializer
    permission_classes = [IsEventAdminAndOwner]


class UpdateEventRoomView(generics.UpdateAPIView):
    """
    Vue permettant de modifier un event room
    """

    queryset = EventRoom.objects.all()
    serializer_class = EventRoomSerializer
    permission_classes = [IsEventAdminAndOwner]


class UpdateEventBusView(generics.UpdateAPIView):
    """
    Vue permettant de modifier un event bus
    """

    queryset = EventBus.objects.all()
    serializer_class = EventBusSerializer
    permission_classes = [IsEventAdminAndOwner]


class UpdateEventMaterialView(generics.UpdateAPIView):
    """
    Vue permettant de modifier un event material
    """

    queryset = EventMaterial.objects.all()
    serializer_class = EventMaterialSerializer
    permission_classes = [IsEventAdminAndOwner]

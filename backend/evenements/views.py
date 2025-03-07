"""
Définition des vues pour la gestion des événements.

Ce module contient les vues permettant de :
- Lister tous les événements ou des catégories spécifiques (bus, salles, matériel).
- Créer, modifier et supprimer des événements.
- Restreindre l'accès à certaines actions via des permissions.
"""

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bus, EventBus, EventMaterial, EventRoom, Material, Room
from .permissions import IsEventAdmin, IsEventAdminAndOwner
from .serializers import (
    BusSerializer,
    EventBusSerializer,
    EventMaterialSerializer,
    EventRoomSerializer,
    MaterialSerializer,
    RoomSerializer,
)


class CreateEventRoomView(generics.CreateAPIView):
    """Vue permettant de créer un événement lié aux salles."""

    permission_classes = [IsAuthenticated, IsEventAdmin]
    queryset = EventRoom.objects.all()
    serializer_class = EventRoomSerializer

    def perform_create(self, serializer):
        """Associe automatiquement l'organisateur à l'utilisateur actuel."""
        serializer.save(organizer=self.request.user)


class CreateEventBusView(generics.CreateAPIView):
    """Vue permettant de créer un événement lié aux bus."""

    permission_classes = [IsAuthenticated, IsEventAdmin]
    queryset = EventBus.objects.all()
    serializer_class = EventBusSerializer

    def perform_create(self, serializer):
        """Associe automatiquement l'organisateur à l'utilisateur actuel."""
        serializer.save(organizer=self.request.user)


class CreateEventMaterialView(generics.CreateAPIView):
    """Vue permettant de créer un événement lié aux matériels."""

    permission_classes = [IsAuthenticated, IsEventAdmin]
    queryset = EventMaterial.objects.all()
    serializer_class = EventMaterialSerializer

    def perform_create(self, serializer):
        """Associe automatiquement l'organisateur à l'utilisateur actuel."""
        serializer.save(organizer=self.request.user)


class EventListView(APIView):
    """
    Vue permettant de récupérer la liste complète des événements non réservés
    """

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """Méthode get pour récuper la liste des différents événements

        Args:
            request (_HttpRequest_): Objet représentant la requête HTTP en cours.

        Returns:
            _HttpResponse_: Objet représentant la réponse HTTP en cours.
        """

        # Récupération des éevenemets non réservés
        event_rooms = EventRoom.objects.filter(is_reserved=False)
        event_buses = EventBus.objects.filter(is_reserved=False)
        event_materials = EventMaterial.objects.filter(is_reserved=False)

        room_serializer = EventRoomSerializer(event_rooms, many=True)
        bus_serializer = EventBusSerializer(event_buses, many=True)
        material_serializer = EventMaterialSerializer(event_materials, many=True)

        # Ajouter un champ 'type_event' à chaque événement
        event_rooms = [
            {"type_event": "event_room", **event} for event in room_serializer.data
        ]
        event_buses = [
            {"type_event": "event_bus", **event} for event in bus_serializer.data
        ]
        event_materials = [
            {"type_event": "event_material", **event}
            for event in material_serializer.data
        ]

        # Combiner tous les événements dans une seule liste
        all_events = event_rooms + event_buses + event_materials

        # Trier les événements par la date de création
        sorted_events = sorted(all_events, key=lambda x: x["created_at"], reverse=True)

        return Response(sorted_events)


class GetAllRoomEventView(generics.ListAPIView):
    """Vue permettant de lister tous les événements liés aux salles."""

    permission_classes = [AllowAny]
    queryset = EventRoom.objects.all()
    serializer_class = EventRoomSerializer


class GetAllBusEventView(generics.ListAPIView):
    """Vue permeettant de lister tous les événements liés aux bus."""

    permission_classes = [AllowAny]
    queryset = EventBus.objects.all()
    serializer_class = EventBusSerializer


class GetAllMaterialEventView(generics.ListAPIView):
    """Vue permettant de lister tous les événements liés aux matériels."""

    permission_classes = [AllowAny]
    queryset = EventMaterial.objects.all()
    serializer_class = EventMaterialSerializer


class DeleteEventRoomView(generics.DestroyAPIView):
    """Vue permettant de supprimer un événement lié aux salles."""

    queryset = EventRoom.objects.all()
    serializer_class = EventRoomSerializer
    permission_classes = [IsAuthenticated, IsEventAdminAndOwner]
    lookup_field = "id"


class DeleteEventBusView(generics.DestroyAPIView):
    """Vue permettant de supprimer un événement lié aux bus."""

    queryset = EventBus.objects.all()
    serializer_class = EventBusSerializer
    permission_classes = [IsAuthenticated, IsEventAdminAndOwner]
    lookup_field = "id"


class DeleteEventMaterialView(generics.DestroyAPIView):
    """Vue permettant de supprimer un événement lié aux matériels."""

    queryset = EventMaterial.objects.all()
    serializer_class = EventMaterialSerializer
    permission_classes = [IsAuthenticated, IsEventAdminAndOwner]
    lookup_field = "id"


class UpdateEventRoomView(generics.UpdateAPIView):
    """Vue permettant de modifier un événement lié aux salles."""

    queryset = EventRoom.objects.all()
    serializer_class = EventRoomSerializer
    permission_classes = [IsAuthenticated, IsEventAdminAndOwner]
    lookup_field = "id"


class UpdateEventBusView(generics.UpdateAPIView):
    """Vue permettant de modifier un événement lié aux bus."""

    queryset = EventBus.objects.all()
    serializer_class = EventBusSerializer
    permission_classes = [IsAuthenticated, IsEventAdminAndOwner]
    lookup_field = "id"


class UpdateEventMaterialView(generics.UpdateAPIView):
    """Vue permettant de modifier un événement lié aux matériels."""

    queryset = EventMaterial.objects.all()
    serializer_class = EventMaterialSerializer
    permission_classes = [IsAuthenticated, IsEventAdminAndOwner]
    lookup_field = "id"


class ListAllBusView(generics.ListAPIView):
    """
    Vue permettant de lister tous les Bus
    """

    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = [IsEventAdmin]


class ListAllRoomView(generics.ListAPIView):
    """
    Vue permettant de lister toutes les salles
    """

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsEventAdmin]


class ListAllMaterialView(generics.ListAPIView):
    """
    Vue permettant de lister tous les matériaux
    """

    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsEventAdmin]

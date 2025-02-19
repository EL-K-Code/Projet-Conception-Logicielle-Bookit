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

from .models import EventBus, EventMaterial, EventRoom
from .permissions import IsEventAdmin, IsEventAdminAndOwner
from .serializers import (
    EventBusSerializer,
    EventMaterialSerializer,
    EventRoomSerializer,
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
    Vue permettant de récupérer la liste complète des événements.
    """

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """Méthode get pour récuper la liste des différents événements

        Args:
            request (_HttpRequest_): Objet représentant la requête HTTP en cours.

        Returns:
            _HttpResponse_: Objet représentant la réponse HTTP en cours.
        """
        event_rooms = EventRoom.objects.all()
        event_buses = EventBus.objects.all()
        event_materials = EventMaterial.objects.all()

        room_serializer = EventRoomSerializer(event_rooms, many=True)
        bus_serializer = EventBusSerializer(event_buses, many=True)
        material_serializer = EventMaterialSerializer(event_materials, many=True)

        return Response(
            {
                "event_rooms": room_serializer.data,
                "event_buses": bus_serializer.data,
                "event_materials": material_serializer.data,
            }
        )


class GetAllRoomEventView(generics.ListAPIView):
    """Vue permettant de lister tous les événements liés aux salles."""

    permission_classes = [AllowAny]
    queryset = EventRoom.objects.all()
    serializer_class = EventRoomSerializer


class GetAllBusEventView(generics.ListAPIView):
    """Vue permettant de lister tous les événements liés aux bus."""

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

"""
Module contenant les vues pour la gestion des réservations dans Bookit.
"""

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ReservationBus, ReservationMaterial, ReservationRoom
from .permissions import IsConsumerAndOwner
from .serializers import (
    ReservationBusSerializer,
    ReservationMaterialSerializer,
    ReservationRoomSerializer,
)


class MakeBusReservationView(generics.CreateAPIView):
    """
    Vue permettant de faire une réservation de salle
    """

    serializer_class = ReservationBusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        event_bus = serializer.validated_data["event_bus"]
        consumer = self.request.user
        reservation_bus = ReservationBus.objects.reserve_bus(consumer, event_bus)
        serializer.instance = (
            reservation_bus  # On associe la réservation créée au serializer
        )


class MakeRoomReservationView(generics.CreateAPIView):
    """
    Vue permettant de faire une réservation de salle
    """

    serializer_class = ReservationRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        consumer = self.request.user
        reservation_room = ReservationRoom.objects.reserve_room(
            consumer, **validated_data
        )
        serializer.instance = reservation_room


class MakeMaterialReservationView(generics.CreateAPIView):
    """
    Vue permettant de faire une réservation de matériel
    """

    serializer_class = ReservationMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        consumer = self.request.user
        reservation_material = ReservationMaterial.objects.reserve_material(
            consumer, **validated_data
        )
        serializer.instance = reservation_material


class CancelBusReservation(generics.DestroyAPIView):
    """
    Vue permettant d'annuler une réservation de bus
    """

    queryset = ReservationBus.objects.all()
    serializer_class = ReservationBusSerializer
    permission_classes = [IsConsumerAndOwner]
    lookup_field = "id"

    def perform_destroy(self, instance):
        ReservationBus.objects.cancel_bus_reservation(instance)


class CancelRoomReservation(generics.DestroyAPIView):
    """
    Vue permettant d'annuler une réservation de salle
    """

    queryset = ReservationRoom.objects.all()
    serializer_class = ReservationRoomSerializer
    permission_classes = [IsConsumerAndOwner]
    lookup_field = "id"


class CancelMaterialReservation(generics.DestroyAPIView):
    """
    Vue permettant d'annuler une réservation de matériel
    """

    queryset = ReservationMaterial.objects.all()
    serializer_class = ReservationMaterialSerializer
    permission_classes = [IsConsumerAndOwner]
    lookup_field = "id"

    def perform_destroy(self, instance):
        ReservationMaterial.objects.cancel_material_reservation(instance)


class UserReservationsView(APIView):
    """
    Vue permettant de récupérer la liste des réservations de l'utilisateur connecté.
    """

    permission_classes = [IsConsumerAndOwner]

    def get(self, request, *args, **kwargs):
        """Méthode GET pour récupérer les différentes réservations de l'utilisateur.

        Args:
            request (HttpRequest): Objet représentant la requête HTTP en cours.

        Returns:
            Response: Objet représentant la réponse HTTP contenant les réservations.
        """
        user = request.user

        # Récupération des réservations de l'utilisateur
        reservation_buses = user.reservationbus_set.all()
        reservation_rooms = user.reservationroom_set.all()
        reservation_materials = user.reservationmaterial_set.all()

        # Sérialisation des données
        bus_serializer = ReservationBusSerializer(reservation_buses, many=True)
        room_serializer = ReservationRoomSerializer(reservation_rooms, many=True)
        material_serializer = ReservationMaterialSerializer(
            reservation_materials, many=True
        )

        # Ajouter un champ 'type_reservation' à chaque réservation
        reservation_buses = [
            {"type_reservation": "bus", **reservation}
            for reservation in bus_serializer.data
        ]
        reservation_rooms = [
            {"type_reservation": "room", **reservation}
            for reservation in room_serializer.data
        ]
        reservation_materials = [
            {"type_reservation": "material", **reservation}
            for reservation in material_serializer.data
        ]

        # Combiner toutes les réservations dans une seule liste
        all_reservations = reservation_buses + reservation_rooms + reservation_materials

        # Trier les réservations par la date de réservation
        sorted_reservations = sorted(
            all_reservations, key=lambda x: x["created_at"], reverse=True
        )

        return Response(sorted_reservations)

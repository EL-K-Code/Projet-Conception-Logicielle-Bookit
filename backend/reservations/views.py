"""
Module contenant les vues pour la gestion des réservations dans Bookit.
"""

from rest_framework import generics, permissions

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

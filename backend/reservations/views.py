"""
Module contenant les vues pour la gestion des réservations dans Bookit.
"""

from django.db.models import Q
from django.utils import timezone
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
    permission_classes = [IsConsumerAndOwner]

    def get(self, request, *args, **kwargs):
        user = request.user
        now = timezone.now()
        today = now.date()
        current_time = now.time()

        # Filtrer uniquement les réservations "en cours" et "à venir" de l'utilisateur
        in_progress = {
            "buses": user.reservationbus_set.filter(
                event_bus__start_time__lte=now, event_bus__end_time__gt=now
            ),
            "rooms": user.reservationroom_set.filter(
                date=today, start_time__gte=current_time, end_time__lt=current_time
            ),
            "materials": user.reservationmaterial_set.filter(
                date=today, start_time__gte=current_time, end_time__lt=current_time
            ),
        }

        upcoming = {
            "buses": user.reservationbus_set.filter(event_bus__start_time__gt=now),
            "rooms": user.reservationroom_set.filter(
                (Q(date=today) & Q(start_time__gt=current_time)) | Q(date__gt=today)
            ),
            "materials": user.reservationmaterial_set.filter(
                (Q(date=today) & Q(start_time__gt=current_time)) | Q(date__gt=today)
            ),
        }

        # Sérialisation des réservations "en cours"
        reservation_buses = [
            {"type_reservation": "bus", "status": "in progress", **data}
            for data in ReservationBusSerializer(in_progress["buses"], many=True).data
        ]
        reservation_rooms = [
            {"type_reservation": "room", "status": "in progress", **data}
            for data in ReservationRoomSerializer(in_progress["rooms"], many=True).data
        ]
        reservation_materials = [
            {"type_reservation": "material", "status": "in progress", **data}
            for data in ReservationMaterialSerializer(
                in_progress["materials"], many=True
            ).data
        ]

        # Sérialisation des réservations "à venir"
        reservation_buses += [
            {"type_reservation": "bus", "status": "upcoming", **data}
            for data in ReservationBusSerializer(upcoming["buses"], many=True).data
        ]
        reservation_rooms += [
            {"type_reservation": "room", "status": "upcoming", **data}
            for data in ReservationRoomSerializer(upcoming["rooms"], many=True).data
        ]
        reservation_materials += [
            {"type_reservation": "material", "status": "upcoming", **data}
            for data in ReservationMaterialSerializer(
                upcoming["materials"], many=True
            ).data
        ]

        # Combiner et trier les réservations
        all_reservations = reservation_buses + reservation_rooms + reservation_materials
        sorted_reservations = sorted(
            all_reservations, key=lambda x: x["created_at"], reverse=True
        )

        return Response(sorted_reservations)

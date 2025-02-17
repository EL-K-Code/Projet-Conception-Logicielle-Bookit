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
    Vue permettant de faire une réservation de bus
    """

    queryset = ReservationBus.objects.all()
    serializer_class = ReservationBusSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Assigner l'utilisateur connecté comme étant le consommateur de cet event
    def perform_create(self, serializer):
        serializer.save(consumer=self.request.user)


class MakeRoomReservationView(generics.CreateAPIView):
    """
    Vue permettant de faire une réservation de salle
    """

    queryset = ReservationRoom.objects.all()
    serializer_class = ReservationRoomSerializer
    permission_classes = [permissions.IsAuthenticated]


class MakeMaterialReservationView(generics.CreateAPIView):
    """
    Vue permettant de faire une réservation de matériel
    """

    queryset = ReservationMaterial.objects.all()
    serializer_class = ReservationMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]


class CancelBusReservation(generics.DestroyAPIView):
    """
    Vue permettant d'annuler une réservation de bus
    """

    queryset = ReservationBus.objects.all()
    serializer_class = ReservationBusSerializer
    permission_classes = [IsConsumerAndOwner]


class CancelRoomReservation(generics.DestroyAPIView):
    """
    Vue permettant d'annuler une réservation de salle
    """

    queryset = ReservationRoom.objects.all()
    serializer_class = ReservationRoomSerializer
    permission_classes = [IsConsumerAndOwner]


class CancelMaterialReservation(generics.DestroyAPIView):
    """
    Vue permettant d'annuler une réservation de matériel
    """

    queryset = ReservationMaterial.objects.all()
    serializer_class = ReservationMaterialSerializer
    permission_classes = [IsConsumerAndOwner]

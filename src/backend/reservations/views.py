from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions

from .models import ReservationBus, ReservationMaterial, ReservationRoom
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
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        On récupère la réservation de bus correspondant à l'ID fourni dans l'URL et
        à l'utilisateur authentifié. Si l'objet n'est pas trouvé ou si l'utilisateur
        ne correspond pas, on lève une exception http404
        """
        return get_object_or_404(
            ReservationBus, id=self.kwargs["id"], consumer=self.request.user
        )


class CancelRoomReservation(generics.DestroyAPIView):
    """
    Vue permettant d'annuler une réservation de salle
    """

    queryset = ReservationRoom.objects.all()
    serializer_class = ReservationRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        On récupère la réservation de salle correspondant à l'ID fourni dans l'URL et
        à l'utilisateur authentifié. Si l'objet n'est pas trouvé ou si l'utilisateur
        ne correspond pas, on lève une exception http404
        """
        return get_object_or_404(
            ReservationRoom, id=self.kwargs["id"], consumer=self.request.user
        )


class CancelMaterialReservation(generics.DestroyAPIView):
    """
    Vue permettant d'annuler une réservation de matériel
    """

    queryset = ReservationMaterial.objects.all()
    serializer_class = ReservationMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        On récupère la réservation de matériel correspondant à l'ID fourni dans l'URL et
        à l'utilisateur authentifié. Si l'objet n'est pas trouvé ou si l'utilisateur
        ne correspond pas, on lève une exception http404
        """
        return get_object_or_404(
            ReservationMaterial, id=self.kwargs["id"], consumer=self.request.user
        )

"""
Module contenant les serializers pour les modèles de réservation dans Bookit.
"""

from evenements.serializers import (
    EventBusSerializer,
    EventMaterialSerializer,
    EventRoomSerializer,
)
from rest_framework import serializers

from .models import ReservationBus, ReservationMaterial, ReservationRoom


class ReservationBusSerializer(serializers.ModelSerializer):
    """
    Classe Serializer pour le modèle ReservationBus
    """

    # Un Serializer imbriqué pour la lecture détaillée
    event_bus_details = EventBusSerializer(source="event_bus", read_only=True)

    class Meta:
        """
        Définit le modèle, ses champs à inclure et ses champs en lecture seule
        """

        model = ReservationBus
        fields = "__all__"
        read_only_fields = ["consumer"]
        write_only_fields = ["event_bus"]


class ReservationRoomSerializer(serializers.ModelSerializer):
    """
    Classe Serializer pour le model ReservationRoom
    """

    # Un Serializer imbriqué pour la lecture détaillée
    event_room_details = EventRoomSerializer(source="event_room", read_only=True)

    class Meta:
        """
        Définit le modèle, ses champs à inclure et ses champs en lecture seule
        """

        model = ReservationRoom
        fields = "__all__"
        read_only_fields = ["consumer"]
        write_only_fields = ["event_room"]


class ReservationMaterialSerializer(serializers.ModelSerializer):
    """
    Classe Serializer pour le model ReservationMaterial
    """

    # Un Serializer imbriqué pour la lecture détaillée
    event_material_details = EventMaterialSerializer(
        source="event_material", read_only=True
    )

    class Meta:
        """
        Définit le modèle, ses champs à inclure et ses champs en lecture seule
        """

        model = ReservationMaterial
        fields = "__all__"
        read_only_fields = ["consumer"]
        write_only_fields = ["event_material"]

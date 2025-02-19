"""
Module contenant les serializers pour les modèles de réservation dans Bookit.
"""

from rest_framework import serializers

from .models import ReservationBus, ReservationMaterial, ReservationRoom


class ReservationBusSerializer(serializers.ModelSerializer):
    """
    Classe Serializer pour le modèle ReservationBus
    """

    class Meta:
        """
        Définit le modèle, ses champs à inclure et ses champs en lecture seule
        """

        model = ReservationBus
        fields = "__all__"
        read_only_fields = ["consumer"]


class ReservationRoomSerializer(serializers.ModelSerializer):
    """
    Classe Serializer pour le model ReservationRoom
    """

    class Meta:
        """
        Définit le modèle, ses champs à inclure et ses champs en lecture seule
        """

        model = ReservationRoom
        fields = "__all__"
        read_only_fields = ["consumer"]


class ReservationMaterialSerializer(serializers.ModelSerializer):
    """
    Classe Serializer pour le model ReservationMaterial
    """

    class Meta:
        """
        Définit le modèle, ses champs à inclure et ses champs en lecture seule
        """

        model = ReservationMaterial
        fields = "__all__"
        read_only_fields = ["consumer"]

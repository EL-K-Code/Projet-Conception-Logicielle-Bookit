from rest_framework import serializers

from .models import ReservationBus, ReservationMaterial, ReservationRoom


class ReservationBusSerializer(serializers.ModelSerializer):
    """
    Classe Serializer pour le model ReservationBus
    """

    class Meta:
        model = ReservationBus
        fields = "__all__"
        read_only_fields = ["consumer"]


class ReservationRoomSerializer(serializers.ModelSerializer):
    """
    Classe Serializer pour le model ReservationRoom
    """

    class Meta:
        model = ReservationRoom
        fields = "__all__"
        read_only_fields = ["consumer"]


class ReservationMaterialSerializer(serializers.ModelSerializer):
    """
    Classe Serializer pour le model ReservationMaterial
    """

    class Meta:
        model = ReservationMaterial
        fields = "__all__"
        read_only_fields = ["consumer"]

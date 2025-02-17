from rest_framework import serializers

from .models import ReservationBus, ReservationMaterial, ReservationRoom


class ReservationBusSerializer(serializers.ModelSerializer):
    """
    Classe Serializer pour le model ReservationBus
    """

    class Meta:
        model = ReservationBus
        fields = "__all__"


class ReservationRoomSerializer(serializers.ModelSerializer):
    """
    Classe Serializer pour le model ReservationRoom
    """

    class Meta:
        model = ReservationRoom
        fields = "__all__"


class ReservationMaterialSerializer(serializers.ModelSerializer):
    """
    Classe Serializer pour le model ReservationMaterial
    """

    class Meta:
        model = ReservationMaterial
        fields = "__all__"

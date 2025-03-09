"""
Module contenant les serializers pour les modèles de réservation dans Bookit.
"""

from datetime import datetime

from django.utils import timezone
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

    start_datetime = serializers.SerializerMethodField()
    end_datetime = serializers.SerializerMethodField()

    class Meta:
        """
        Définit le modèle, ses champs à inclure et ses champs en lecture seule
        """

        model = ReservationRoom
        fields = "__all__"
        read_only_fields = ["consumer", "end_datetime", "start_datetime"]
        write_only_fields = ["event_room", "data", "start_time", "end_time"]

    def get_start_datetime(self, obj):
        """
        Méthode pour combiner 'date' et 'start_time' en un 'datetime'
        """
        # On récupère la date et l'heure
        reservation_date = obj.date
        reservation_start_time = obj.start_time

        # On combine les deux pour obtenir un datetime
        combined_datetime = datetime.combine(reservation_date, reservation_start_time)

        # Rendre le datetime conscient du fuseau horaire
        aware_datetime = timezone.make_aware(
            combined_datetime, timezone.get_current_timezone()
        )

        # Retourner le datetime en heure locale
        return timezone.localtime(aware_datetime)

    def get_end_datetime(self, obj):
        """
        Méthode pour combiner 'date' et 'end_time' en un 'datetime'
        """
        # On récupère la date et l'heure
        reservation_date = obj.date
        reservation_end_time = obj.end_time

        # On combine les deux pour obtenir un datetime
        combined_datetime = datetime.combine(reservation_date, reservation_end_time)

        # Rendre le datetime conscient du fuseau horaire
        aware_datetime = timezone.make_aware(
            combined_datetime, timezone.get_current_timezone()
        )

        # Retourner le datetime en heure locale
        return timezone.localtime(aware_datetime)


class ReservationMaterialSerializer(serializers.ModelSerializer):
    """
    Classe Serializer pour le model ReservationMaterial
    """

    # Un Serializer imbriqué pour la lecture détaillée
    event_material_details = EventMaterialSerializer(
        source="event_material", read_only=True
    )

    start_datetime = serializers.SerializerMethodField()
    end_datetime = serializers.SerializerMethodField()

    class Meta:
        """
        Définit le modèle, ses champs à inclure et ses champs en lecture seule
        """

        model = ReservationMaterial
        fields = "__all__"
        read_only_fields = ["consumer", "end_datetime", "start_datetime"]
        write_only_fields = ["event_material", "data", "start_time", "end_time"]

    def get_start_datetime(self, obj):
        """
        Méthode pour combiner 'date' et 'start_time' en un 'datetime'
        """
        # On récupère la date et l'heure
        reservation_date = obj.date
        reservation_start_time = obj.start_time

        # On combine les deux pour obtenir un datetime
        combined_datetime = datetime.combine(reservation_date, reservation_start_time)

        # Rendre le datetime conscient du fuseau horaire
        aware_datetime = timezone.make_aware(
            combined_datetime, timezone.get_current_timezone()
        )

        # Retourner le datetime en heure locale
        return timezone.localtime(aware_datetime)

    def get_end_datetime(self, obj):
        """
        Méthode pour combiner 'date' et 'end_time' en un 'datetime'
        """
        # On récupère la date et l'heure
        reservation_date = obj.date
        reservation_end_time = obj.end_time

        # On combine les deux pour obtenir un datetime
        combined_datetime = datetime.combine(reservation_date, reservation_end_time)

        # Rendre le datetime conscient du fuseau horaire
        aware_datetime = timezone.make_aware(
            combined_datetime, timezone.get_current_timezone()
        )

        # Retourner le datetime en heure locale
        return timezone.localtime(aware_datetime)

"""
Module serializers pour la gestion des événements.

Ce module contient les serializers pour les différents types d'événements
(l'événement de bus, de matériel et de salle) définis dans le modèle.
"""

from rest_framework import serializers

from .models import Bus, EventBus, EventMaterial, EventRoom, Material, Room


class BusSerializer(serializers.ModelSerializer):
    """
    Serializer pour lister les ressources de bus
    """

    class Meta:
        """
        Définit le modèle, ses champs à inclure
        """

        model = Bus
        fields = ["id", "name"]


class RoomSerializer(serializers.ModelSerializer):
    """
    Serializer pour lister les événements de salles
    """

    class Meta:
        """
        Définit le modèle, ses champs à inclure
        """

        model = Room
        fields = ["id", "name"]


class MaterialSerializer(serializers.ModelSerializer):
    """
    Serializer pour lister les ressources de materiels
    """

    class Meta:
        """
        Définit le modèle, ses champs à inclure
        """

        model = Material
        fields = ["id", "name"]


class EventBusSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle EventBus.
    """

    resource_name = serializers.SlugRelatedField(
        source="resource", read_only=True, slug_field="name"
    )

    class Meta:
        """
        Classe Meta pour le serializer EventBus.

        Cette classe définit les métadonnées pour le serializer, en précisant le
        modèle auquel il est lié et les champs à inclure dans la sérialisation.
        Elle spécifie également que le champ 'organizer' doit être en lecture seule.
        """

        model = EventBus
        fields = "__all__"
        read_only_fields = ["organizer", "is_reserved"]


class EventRoomSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle EventRoom.

    Ce serializer est utilisé pour valider et transformer les données liées
    à un événement de type salle.
    """

    resource_name = serializers.SlugRelatedField(
        source="resource", read_only=True, slug_field="name"
    )

    class Meta:
        """
        Classe Meta pour le serializer EventRoom.
        """

        model = EventRoom
        fields = "__all__"
        read_only_fields = ["organizer", "is_reserved"]


class EventMaterialSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle EventMaterial.

    Ce serializer est utilisé pour valider et transformer les données liées
    à un événement de type matériel.
    """

    # Utilisé pour la lecture (affichage du nom du bus)
    resource_name = serializers.SlugRelatedField(
        source="resource", read_only=True, slug_field="name"
    )

    class Meta:
        """
        Classe Meta pour le serializer EventMaterial.
        """

        model = EventMaterial
        fields = "__all__"
        read_only_fields = ["organizer", "is_reserved"]

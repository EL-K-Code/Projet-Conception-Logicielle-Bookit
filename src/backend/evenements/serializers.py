"""
Module serializers pour la gestion des événements.

Ce module contient les serializers pour les différents types d'événements
(l'événement de bus, de matériel et de salle) définis dans le modèle.
Les serializers sont utilisés pour la validation et la transformation des données
lors de la communication avec l'API.
"""

from rest_framework import serializers

from .models import EventBus, EventMaterial, EventRoom


class EventBusSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle EventBus.

    Ce serializer est utilisé pour valider et transformer les données liées
    à un événement de type bus. Il permet de récupérer ou de mettre à jour
    les informations relatives aux événements de bus, y compris l'organisateur
    de l'événement. L'attribut 'organizer' est en lecture seule.
    """

    class Meta:
        """
        Classe Meta pour le serializer EventBus.

        Cette classe définit les métadonnées pour le serializer, en précisant le
        modèle auquel il est lié et les champs à inclure dans la sérialisation.
        Elle spécifie également que le champ 'organizer' doit être en lecture seule.
        """

        model = EventBus
        fields = "__all__"
        read_only_fields = ["organizer"]


class EventRoomSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle EventRoom.

    Ce serializer est utilisé pour valider et transformer les données liées
    à un événement de type salle. Il permet de récupérer ou de mettre à jour
    les informations relatives aux événements de salle, y compris l'organisateur
    de l'événement. L'attribut 'organizer' est en lecture seule.
    """

    class Meta:
        """
        Classe Meta pour le serializer EventRoom.

        Cette classe définit les métadonnées pour le serializer, en précisant le
        modèle auquel il est lié et les champs à inclure dans la sérialisation.
        Elle spécifie également que le champ 'organizer' doit être en lecture seule.
        """

        model = EventRoom
        fields = "__all__"
        read_only_fields = ["organizer"]


class EventMaterialSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle EventMaterial.

    Ce serializer est utilisé pour valider et transformer les données liées
    à un événement de type matériel. Il permet de récupérer ou de mettre à jour
    les informations relatives aux événements de matériel, y compris l'organisateur
    de l'événement. L'attribut 'organizer' est en lecture seule.
    """

    class Meta:
        """
        Classe Meta pour le serializer EventMaterial.

        Cette classe définit les métadonnées pour le serializer, en précisant le
        modèle auquel il est lié et les champs à inclure dans la sérialisation.
        Elle spécifie également que le champ 'organizer' doit être en lecture seule.
        """

        model = EventMaterial
        fields = "__all__"
        read_only_fields = ["organizer"]

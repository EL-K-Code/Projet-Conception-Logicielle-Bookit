"""
Module pour la gestion des notifications par email dans l'application Evenements.

Ce module définit des classes pour l'envoie des notifications par email concernant
la création d'événements.
"""

from abc import ABC, abstractmethod

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from userspace.models import Group

from .models import Event, EventBus, EventMaterial, EventRoom


class SendEventNotification(EmailMessage, ABC):
    """
    Classe de base pour l'envoi de notifications par email lors de la création d'un événement.
    """

    def __init__(self, instance: Event):
        """
        Initialise l'objet avec l'instance de l'événement et configure le sujet,
        l'expéditeur et les destinataires de l'email.

        L'email sera envoyé à tous les utilisateurs du groupe 'consumer'.

        Args:
            instance (Event): L'instance de l'événement contenant les informations nécessaires.
        """
        self.instance = instance
        super().__init__(
            subject=self.instance.description,
            bcc=[
                consumer.email
                for consumer in Group.objects.get(name="consumer").user_set.all()
            ],
        )
        self.extra_headers = {"Reply-To": self.instance.organizer.email}

    @property
    @abstractmethod
    def email_body(self):
        """
        Propriété abstraite devant être définie dans les sous-classes pour
        spécifier le contenu de l'email.
        """
        pass

    def send_email(self):
        """
        Méthode pour envoyer l'email.
        """
        self.content_subtype = "html"
        self.body = self.email_body
        return super().send()


class SendEventBusNotification(SendEventNotification):
    """Gestion d'envoi d'email lors  de la création d'un événement Bus"""

    def __init__(self, instance: EventBus):
        """Initialise l'object"""
        super().__init__(instance)

    @property
    def email_body(self):
        """Méthode pour renvoyer le contenu du mail"""
        context = {
            "event_description": self.instance.description,
            "bus_name": self.instance.resource.name,
            "available_seats": self.instance.available_seats,
            "departure": self.instance.departure,
            "destination": self.instance.destination,
            "start_time": self.instance.start_time,
            "end_time": self.instance.end_time,
            "organizer_first_name": self.instance.organizer.first_name,
            "organizer_last_name": self.instance.organizer.last_name,
        }
        return render_to_string("event_bus_email.html", context)


class SendEventRoomNotification(SendEventNotification):
    """Gestion d'envoi d'email lors  de la création d'un événement Room"""

    def __init__(self, instance: EventRoom):
        """Initialise l'object"""
        super().__init__(instance)

    @property
    def email_body(self):
        """Méthode pour renvoyer le contenu du mail"""

        context = {
            "event_description": self.instance.description,
            "room_name": self.instance.resource.name,
            "organizer_first_name": self.instance.organizer.first_name,
            "organizer_last_name": self.instance.organizer.last_name,
        }
        return render_to_string("event_room_email.html", context)


class SendEventMaterialNotification(SendEventNotification):
    """Gestion d'envoi d'email lors  de la création d'un événement Material"""

    def __init__(self, instance: EventMaterial):
        """Initialise l'object"""
        super().__init__(instance)

    @property
    def email_body(self):
        """Méthode pour renvoyer le contenu du mail"""

        context = {
            "event_description": self.instance.description,
            "material_name": self.instance.resource.name,
            "available_stock": self.instance.available_stock,
            "organizer_first_name": self.instance.organizer.first_name,
            "organizer_last_name": self.instance.organizer.last_name,
        }
        return render_to_string("event_material_email.html", context)

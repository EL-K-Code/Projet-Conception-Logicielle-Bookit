"""
Module de gestion des signaux pour l'application evenementd.

"""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .email_services import (
    SendEventBusNotification,
    SendEventMaterialNotification,
    SendEventRoomNotification,
)
from .models import EventBus, EventMaterial, EventRoom


@receiver(post_save, sender=EventBus)
def send_email_for_event_bus(sender, instance, created, **_):  # pylint: disable=W0613
    """
    Envoyer le mail à tous les consommateurs pour notifier la création d'un événement bus
    """
    if created:
        email = SendEventBusNotification(instance)
        email.send_email()


@receiver(post_save, sender=EventRoom)
def send_email_for_event_room(sender, instance, created, **_):  # pylint: disable=W0613
    """
    Envoyer le mail à tous les consommateurs pour notifier la création d'un événement Room
    """
    if created:
        email = SendEventRoomNotification(instance)
        email.send_email()


@receiver(post_save, sender=EventMaterial)
def send_email_for_event_material(
    sender, instance, created, **_
):  # pylint: disable=W0613
    """
    Envoyer le mail à tous les consommateurs pour notifier la création d'un événement Matériel
    """
    if created:
        email = SendEventMaterialNotification(instance)
        email.send_email()

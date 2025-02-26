"""
Manager personnalisé pour gérer les réservations de bus, salles et matériels.
Contient des méthodes pour vérifier la disponibilité et créer des réservations.
"""

from django.core.exceptions import ValidationError
from django.db import models


class ReservationManager(models.Manager):
    """
    Manager personalisé pour gérer les résrervations
    """

    def reserve_bus(self, consumer, event_bus):
        """
        vérifie la disponibilité du bus et crée une réservation
        """
        if event_bus.available_seats > 0:
            event_bus.available_seats -= 1
            event_bus.save()
            return self.create(consumer=consumer, event_bus=event_bus)

        raise ValidationError("Plus de places disponibles")

    def reserve_room(self, consumer, event_room, **kwargs):
        """
        vérifie la disponibilité d'une salle et crée une réservation
        """
        date = kwargs.get("date")
        start_time = kwargs.get("start_time")
        end_time = kwargs.get("end_time")
        exists = (
            self.filter(event_bus=event_room, date=date)
            .filter(
                models.Q(start_time__lt=end_time) & models.Q(end_time__gt=start_time)
            )
            .exists()
        )
        if exists:
            raise ValidationError("Cette salle existe déjà pour ce créneau")

        return self.create(
            consumer=consumer,
            date=date,
            event_room=event_room,
            start_time=start_time,
            end_time=end_time,
        )

    def reserve_material(self, consumer, event_material, **kwargs):
        """
        Vérifie le stock disponible et crée une réservation de matériel.
        """
        date = kwargs.get("date")
        start_time = kwargs.get("start_time")
        end_time = kwargs.get("end_time")
        quantity = kwargs.get("quantity")

        if event_material.available_stock >= quantity:
            event_material.available_stock -= quantity
            event_material.save()
            return self.create(
                consumer=consumer,
                event_material=event_material,
                date=date,
                start_time=start_time,
                end_time=end_time,
                quantity=quantity,
            )

        raise ValidationError("Stock insuffisant pour cette réservation")

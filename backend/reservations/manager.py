"""
Manager personnalisé pour gérer les réservations de bus, salles et matériels.
Contient des méthodes pour vérifier la disponibilité et créer des réservations.
"""

from django.db import models
from rest_framework.exceptions import ValidationError


class ReservationManager(models.Manager):
    """
    Manager personalisé pour gérer les résrervations
    """

    def reserve_bus(self, consumer, event_bus):
        """
        vérifie la disponibilité du bus et crée une réservation

        Args:
            consumer (User): L'utilisateur qui effectue la réservation.
            event_bus (EventBus): L'objet représentant un evenement de bus

        Returns:
            ReservationBus: L'objet de réservation créé si des places sont diponibles
        """
        if event_bus.available_seats > 0:
            event_bus.available_seats -= 1
            if event_bus.available_seats == 0:
                event_bus.is_reserved = True
            event_bus.save()
            return self.create(consumer=consumer, event_bus=event_bus)

        raise ValidationError(
            {"error": "Plus de places disponibles", "code": "NO_SEATS_AVAILABLE"}
        )

    def reserve_room(self, consumer, event_room, **kwargs):
        """
        vérifie la disponibilité d'une salle et crée une réservation

        Args:
        consumer (User): L'utilisateur effectuant la réservation.
        event_room (EventRoom): L'objet représentant un evenement de salle
        **kwargs:
            date (datetime.date): La date de la réservation.
            start_time (datetime.time): L'heure de début de la réservation.
            end_time (datetime.time): L'heure de fin de la réservation.

        Returns:
        ReservationMaterial: L'objet de réservation créé si le stock est suffisant.

        """
        date = kwargs.get("date")
        start_time = kwargs.get("start_time")
        end_time = kwargs.get("end_time")
        exists = self.filter(
            event_room=event_room,
            date=date,
            start_time__lt=end_time,
            end_time__gt=start_time,
        ).exists()
        if exists:
            raise ValidationError(
                {
                    "error": "Cette salle est déjà réservée pour ce créneau",
                    "code": "ROOM_ALREADY_BOOKED",
                }
            )

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

        Args:
        consumer (User): L'utilisateur effectuant la réservation.
        event_material (EventMaterial): L'objet matériel concerné par la réservation.
        **kwargs:
            date (datetime.date): La date de la réservation.
            start_time (datetime.time): L'heure de début de la réservation.
            end_time (datetime.time): L'heure de fin de la réservation.
            quantity (int): La quantité de matériel à réserver.

        Returns:
        ReservationMaterial: L'objet de réservation créé si le stock est suffisant.
        """
        date = kwargs.get("date")
        start_time = kwargs.get("start_time")
        end_time = kwargs.get("end_time")
        quantity = kwargs.get("quantity")

        if event_material.available_stock >= quantity:
            event_material.available_stock -= quantity
            if event_material.available_stock == 0:
                event_material.is_reserved = True
            event_material.save()
            return self.create(
                consumer=consumer,
                event_material=event_material,
                date=date,
                start_time=start_time,
                end_time=end_time,
                quantity=quantity,
            )

        raise ValidationError(
            {
                "error": "Stock insuffisant pour cette réservation",
                "code": "INSUFFICIENT_STOCK",
            }
        )

    def cancel_bus_reservation(self, reservation_bus):
        """
        Annule une réservation de bus et libère une place

        Args:
            reservation_bus(ReservationBus): L'objet de réservation de bus à annuler.
        """

        event_bus = reservation_bus.event_bus
        event_bus.available_seats += 1
        event_bus.is_reserved = False
        event_bus.save()
        reservation_bus.delete()

    def cancel_room_reservation(self, reservation_room):
        """
        Annule une réservation de salle

        Args:
            reservation_room(ReservationRoom): L'objet de réservation de salle à annuler.
        """
        event_room = reservation_room.event_room
        event_room.save()
        reservation_room.delete()

    def cancel_material_reservation(self, reservation_material):
        """
        Annule une réservation de matériel et remet le stock à jour

        Args:
            reservation_material(ReservationMaterial): L'objet de réservation de matériel à annuler.
        """

        event_material = reservation_material.event_material
        event_material.available_stock += reservation_material.quantity
        event_material.is_reserved = False
        event_material.save()
        reservation_material.delete()

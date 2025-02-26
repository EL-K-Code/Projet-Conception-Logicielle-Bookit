"""
Module contenant les modèles pour la gestion des réservations dans Bookit.
"""

from django.core.validators import MinValueValidator
from django.db import models
from evenements.models import EventBus, EventMaterial, EventRoom
from reservations.manager import ReservationManager
from userspace.models import User


class Reservation(models.Model):
    """
    Classe abstraite pour la gestion des réservations.
    """

    consumer = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False
    )

    class Meta:
        """
        Définit que ce modèle est abstrait et ne sera pas utilisé pour créer une table
        """

        abstract = True

    def save(self, *args, **kwargs):
        """
        Valide le modèle avant sauvegarde.
        """
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Réservation de {self.consumer}"


class ReservationBus(Reservation):
    """
    Modèle de réservation d'un bus (plusieurs utilisateurs peuvent réserver le même bus)
    """

    event_bus = models.ForeignKey(
        EventBus, on_delete=models.CASCADE, blank=False, null=False
    )

    objects = ReservationManager()

    def __str__(self):
        return f"Réservation de {self.consumer} pour {self.event_bus}"


class ReservationRoom(Reservation):
    """
    Modèle de réservation d'une salle (une seule réservation possible par créneau)
    """

    event_room = models.ForeignKey(
        EventRoom, on_delete=models.CASCADE, blank=False, null=False
    )
    date = models.DateField(blank=False, null=False)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)

    objects = ReservationManager()

    class Meta:
        """
        Contrainte d'unicité.
        """

        constraints = [
            models.UniqueConstraint(
                fields=["event_room", "date", "start_time", "end_time"],
                name="unique_reservation_room",
            ),
            models.CheckConstraint(
                condition=models.Q(start_time__lt=models.F("end_time")),
                name="check_start_time_before_end_time",
            ),
        ]

    def __str__(self):
        return f"Réservation de {self.consumer} pour {self.event_room}"


class ReservationMaterial(Reservation):
    """
    Modèle de réservation de matériel
    """

    event_material = models.ForeignKey(
        EventMaterial, on_delete=models.CASCADE, blank=False, null=False
    )
    date = models.DateField(blank=False, null=False)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)
    quantity = models.IntegerField(
        blank=False, null=False, validators=[MinValueValidator(1)]
    )

    objects = ReservationManager()

    def __str__(self):
        return f"Réservation de {self.consumer} pour {self.event_material} ({self.quantity} unités)"

from django.core.validators import MinValueValidator
from django.db import models
from evenements.models import EventBus, EventMaterial, EventRoom
from userspace.models import User


class Reservation(models.Model):
    """
    Modèle abstait pour une réservation générique
    """

    consumer = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        validele modèle avant sauvegarde
        """
        self.full_clean()
        super().save(*args, **kwargs)


class ReservationBus(Reservation):
    """
    Modèle de réservation d'un bus (plusieurs utilisateurs peuvent réserver le même bus)
    """

    event = models.ForeignKey(
        EventBus, on_delete=models.CASCADE, blank=False, null=False
    )

    def save(self, *args, **kwargs):
        """
        vérifie si des places sont disponibles avant d'enregistrer la réservation
        Si des places sont disponibles, elle réduit le nombre de places et sauvegarde
        """
        if self.event.available_seats > 0:
            self.event.available_seats -= 1
            self.event.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError("Plus de places disponibles")


class ReservationRoom(Reservation):
    """
    Modèle de réservation d'une salle(une seule réservation possible par créneau)
    """

    event = models.ForeignKey(
        EventRoom, on_delete=models.CASCADE, blank=False, null=False
    )
    date = models.DateField(blank=False, null=False)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)

    class Meta:
        """
        Contrainte d'unicité
        """

        constraints = [
            models.UniqueConstraint(
                fields=["event", "date", "start_time", "end_time"],
                name="unique_reservation_room",
            ),
        ]


class ReservationMaterial(Reservation):
    """
    Modèle de réservation de matériel
    """

    event = models.ForeignKey(
        EventMaterial, on_delete=models.CASCADE, blank=False, null=False
    )
    date = models.DateField(blank=False, null=False)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)
    quantity = models.IntegerField(
        blank=False, null=False, validators=[MinValueValidator(1)]
    )

    def save(self, *args, **kwargs):
        """
        vérifie si le stock disponible est suffisant avant d'enregistrer la réservation
        Si la quantité demandée est disponible, elle réduit le stock et sauvegarde
        """
        if self.event.available_stock >= self.quantity:
            self.event.available_stock -= self.quantity
            self.event.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError("Stock insuffisant pour cette réservation")

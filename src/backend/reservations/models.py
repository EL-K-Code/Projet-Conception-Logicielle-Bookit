from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from evenements.models import EventBus, EventMaterial, EventRoom


class Reservation(models.Model):
    """
    Classe mère pour toutes les réservations
    """

    id = models.AutoField(primary_key=True)
    consumer = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class ReservationBus(Reservation):
    """
    Réservation d'un bus (plusieurs utilisateurs peuvent réserver le même bus)
    """

    event = models.ForeignKey(EventBus, on_delete=models.CASCADE)

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
    Réservation d'une salle(une seule réservation possible par créneau)
    """

    event = models.ForeignKey(EventRoom, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

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
    Réservation de matériel
    """

    event = models.ForeignKey(EventMaterial, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

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

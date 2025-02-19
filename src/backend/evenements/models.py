"""
Module des modèles pour les évènements.

Ce module contient les modèles qui définissent les ressources et les évènements
associés à des salles, des bus et des matériels. Chaque modèle est associé à un
évènement spécifique, comme une réservation de salle, de bus ou de matériel.
"""

from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from userspace.models import User


class Room(models.Model):
    """
    Modèle représentant une salle.

    Ce modèle est utilisé pour définir des salles où peuvent avoir lieu des évènements.
    """

    name = models.CharField(max_length=64, unique=True, blank=False, null=False)
    description = models.TextField(max_length=512)

    def __str__(self):
        """Retourne le nom de la salle."""
        return str(self.name)

    def save(self, *args, **kwargs):
        """Force la validation avant de sauvegarder l'objet."""
        self.full_clean()
        super().save(*args, **kwargs)


class Bus(models.Model):
    """
    Modèle représentant un bus.

    Ce modèle définit les caractéristiques d'un bus, y compris son nom,
    ainsi que le nombre de places disponibles.
    """

    name = models.CharField(
        max_length=64,
        unique=True,
        blank=False,
        null=False,
        validators=[MinLengthValidator(2)],
    )
    number_seats = models.IntegerField(
        blank=False, null=False, validators=[MinValueValidator(1)]
    )

    def __str__(self):
        """Retourne le nom du bus."""
        return str(self.name)

    def save(self, *args, **kwargs):
        """Force la validation avant de sauvegarder l'objet."""
        self.full_clean()
        super().save(*args, **kwargs)


class Material(models.Model):
    """
    Modèle représentant un matériel.

    Ce modèle définit les ressources matérielles disponibles pour les évènements.
    Chaque matériel possède un nom et un stock.
    """

    name = models.CharField(
        max_length=64, unique=True, null=False, validators=[MinLengthValidator(2)]
    )
    stock = models.IntegerField(
        blank=False, null=False, validators=[MinValueValidator(0)]
    )

    def __str__(self):
        """Retourne le nom du matériel."""
        return str(self.name)

    def save(self, *args, **kwargs):
        """Force la validation avant de sauvegarder l'objet."""
        self.full_clean()
        super().save(*args, **kwargs)


class Event(models.Model):
    """
    Modèle abstrait pour un évènement générique.

    Ce modèle sert de base pour les évènements spécifiques (salle, bus, matériel).
    Il définit les champs communs à tous les types d'évènements : description, organisateur,
    et statut de réservation.
    """

    description = models.CharField(
        max_length=512,
        help_text=_("Give some description to this event."),
        blank=False,
        null=False,
        validators=[MinLengthValidator(2)],
    )
    organizer = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False
    )
    is_reserved = models.BooleanField(
        _("reserved"),
        default=True,
    )

    class Meta:
        """Définir ce modèle comme abstrait."""

        abstract = True

    def __str__(self):
        """Retourne la description de l'évènement."""
        return str(self.description)

    def save(self, *args, **kwargs):
        """Force la validation avant de sauvegarder l'objet."""
        self.full_clean()
        super().save(*args, **kwargs)


class EventRoom(Event):
    """
    Modèle pour un évènement de salle.

    Ce modèle représente un évènement où une salle est réservée. Il hérite du modèle
    `Event` et ajoute une référence à la ressource `Room`.
    """

    resource = models.ForeignKey(
        Room, on_delete=models.CASCADE, blank=False, null=False
    )


class EventBus(Event):
    """
    Modèle pour un évènement de bus.

    Ce modèle représente un évènement où un bus est réservé. Il hérite du modèle
    `Event` et ajoute des informations spécifiques sur le bus, telles que les places
    disponibles, la destination, et les horaires de départ et d'arrivée.
    """

    resource = models.ForeignKey(Bus, on_delete=models.CASCADE, blank=False, null=False)
    available_seats = models.IntegerField(
        blank=False, null=False, validators=[MinValueValidator(0)]
    )
    departure = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        validators=[MinLengthValidator(2)],
    )
    destination = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        validators=[MinLengthValidator(2)],
    )
    departure_time = models.DateTimeField(blank=False, null=False)
    arrival_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        """
        Initialize the available seats at the creation of the event, if not provided.
        """
        if self.pk is None and self.available_seats is None:
            self.available_seats = self.resource.number_seats
        super().save(*args, **kwargs)


class EventMaterial(Event):
    """
    Modèle pour un évènement de matériel.

    Ce modèle représente un évènement où du matériel est réservé. Il hérite du modèle
    `Event` et ajoute une référence à la ressource `Material`, ainsi qu'une gestion
    du stock disponible.
    """

    resource = models.ForeignKey(
        Material, on_delete=models.CASCADE, null=False, blank=False
    )
    available_stock = models.IntegerField(
        null=False, blank=False, validators=[MinValueValidator(0)]
    )

    def save(self, *args, **kwargs):
        """
        Initialize the available stock at the creation of the event, if not provided.
        """
        if self.pk is None and self.available_stock is None:
            self.available_stock = self.resource.stock
        super().save(*args, **kwargs)

from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from userspace.models import User


class Room(models.Model):
    """
    Modèle représentant une salle
    """

    name = models.CharField(max_length=64, unique=True, blank=False, null=False)
    description = models.TextField(max_length=512)

    def __str__(self):

        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Bus(models.Model):
    """
    Modèle représentant une salle
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

        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Material(models.Model):
    """
    Modèle représentant un matériel
    """

    name = models.CharField(
        max_length=64, unique=True, null=False, validators=[MinLengthValidator(2)]
    )
    stock = models.IntegerField(
        blank=False, null=False, validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Event(models.Model):
    """
    Modèle abstait pour un évènement générique
    """

    description = models.CharField(
        max_length=512,
        help_text=_("Give some description to this even."),
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
        abstract = True

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class EventRoom(Event):
    """
    Modèle pour un évènement de salle
    """

    resource = models.ForeignKey(
        Room, on_delete=models.CASCADE, blank=False, null=False
    )


class EventBus(Event):
    """
    Modèle pour un évènement de bus
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
        Initialization of the number of available seats at the creation
        and first save of the event.
        """
        if self.pk is None and self.available_seats is None:
            self.available_seats = self.resource.number_seats
        super().save(*args, **kwargs)


class EventMaterial(Event):
    """
    Modèle pour un évènement de matériel
    """

    resource = models.ForeignKey(
        Material, on_delete=models.CASCADE, null=False, blank=False
    )
    available_stock = models.IntegerField(
        null=False, blank=False, validators=[MinValueValidator(0)]
    )

    def save(self, *args, **kwargs):
        """
        Initialization of the available stock at the creation
        and first save of the event.
        """
        if self.pk is None and self.available_stock is None:
            self.available_stock = self.resource.stock
        super().save(*args, **kwargs)

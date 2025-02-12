from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Room(models.Model):
    """
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(max_length=512)

    def __str__(self):

        return (str(self.id))


class Bus(models.Model):
    """
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    number_seats = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):

        return (str(self.id))


class Material(models.Model):
    """
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    stock = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):

        return (str(self.id))


class Event(models.Model):
    """
    """

    id = models.AutoField(primary_key=True)
    description = models.CharField(
        max_length=512,
        help_text=_(
            "Give some description to this even."
        ))
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    is_reserved  = models.BooleanField(
        _("reserved"),
        default=True, 
        )
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return(str(self.id))
    

class EvenRoom(Event):
    """
    """
    resource = models.ForeignKey(Room, on_delete=models.CASCADE)


class EvenBus(Event):
    """
    """
    resource = models.ForeignKey(Bus, on_delete=models.CASCADE)
    available_seats = models.IntegerField(validators=[MinValueValidator(0)])
    departure  = models.CharField(max_length=64)
    destination  = models.CharField(max_length=64)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()


    def save(self, *args, **kwargs):
        """
        Initialization of the number of available seats at the creation 
        and first save of the event.
        """
        if self.pk is None and self.available_seats is None: 
            self.available_seats = self.resource.number_seats  
        super().save(*args, **kwargs)

class EvenMaterial(Event):
    """
    """
    resource = models.ForeignKey(Material, on_delete=models.CASCADE)
    available_stock = models.IntegerField(validators=[MinValueValidator(0)])

    def save(self, *args, **kwargs):
        """
        Initialization of the available stock at the creation 
        and first save of the event.
        """
        if self.pk is None and self.available_stock  is None: 
            self.available_stock = self.resource.stock 
        super().save(*args, **kwargs)



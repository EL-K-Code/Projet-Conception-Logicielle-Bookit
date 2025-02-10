from django.db import models
from ..auth.models import User


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=512)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
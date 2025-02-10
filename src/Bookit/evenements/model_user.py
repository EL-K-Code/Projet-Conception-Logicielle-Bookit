from django.db import models
from django.contrib.auth.models import Group, AbstractUser

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    group = models.ManyToManyField(Group)

    def __str__(self):
        
        return (self.id)


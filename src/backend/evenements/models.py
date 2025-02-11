from django.db import models
from django.utils.translation import gettext_lazy as _
from ..auth.models import User


class Event(models.Model):

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
    
    def __str__(self):
        
        return(self.id)

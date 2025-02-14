from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Modèle utilisateur"""

    email = models.EmailField(
        _("email address"),
        unique=True,
        blank=False,
        null=False,
        validators=[EmailValidator(message="The email address provided is invalid.")],
    )

    def save(self, *args, **kwargs):
        self.full_clean()  # Force la validation
        super().save(*args, **kwargs)

from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import EmailValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Modèle utilisateur"""

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=False,
        null=False,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
    )

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

"""
Module de définition du modèle utilisateur pour l'application userspace.

Ce module définit une classe `User` qui hérite de `AbstractUser` pour étendre
le modèle utilisateur par défaut de Django. Il ajoute des contraintes sur l'email
et redéfinit l'association aux groupes.
"""

from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import EmailValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Modèle utilisateur personnalisé.

    Ce modèle étend `AbstractUser` et ajoute des contraintes spécifiques, notamment :
    - Un champ `email` unique et obligatoire avec validation.
    - Une gestion spécifique des groupes avec une relation `ManyToManyField`.

    Attributs :
        groups (ManyToManyField) : Liste des groupes auxquels l'utilisateur appartient.
        email (EmailField) : Adresse email unique et validée de l'utilisateur.
    """

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=False,
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
        """
        Enregistre l'utilisateur après validation des champs.

        Cette méthode surcharge `save()` pour appeler `full_clean()`, ce qui garantit
        que les contraintes de validation sont respectées avant l'enregistrement.
        """
        self.full_clean()  # Force la validation
        super().save(*args, **kwargs)

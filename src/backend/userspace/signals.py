"""
Module de gestion des signaux pour l'application userspace.

Ce module définit des signaux Django permettant d'automatiser certaines
actions après les migrations et la création d'un utilisateur.
"""

import logging
import os

from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from userspace.models import User

logger = logging.getLogger("django")


@receiver(post_migrate)
def create_default_groups_and_superuser(sender, **_):
    """
    Crée les groupes d’utilisateurs par défaut après la migration.

    Cette fonction est exécutée automatiquement après chaque migration et
    garantit que les groupes "admin", "event_admin" et "consumer" existent.

    Args:
        sender (module): Le module émetteur du signal.
        **kwargs: Arguments supplémentaires du signal.
    """
    if sender.name == "userspace":
        groups = ["admin", "event_admin", "consumer"]
        for group_name in groups:
            Group.objects.get_or_create(name=group_name)


@receiver(post_migrate)
def create_default_superuser(sender, **_):
    """
    Crée un superutilisateur par défaut après la migration.

    Utilise les variables d’environnement `DJANGO_SUPERUSER_USERNAME`,
    `DJANGO_SUPERUSER_EMAIL` et `DJANGO_SUPERUSER_PASSWORD` pour configurer
    le compte administrateur. Le superutilisateur est automatiquement ajouté
    au groupe "admin".

    Args:
        sender (module): Le module émetteur du signal.
        **kwargs: Arguments supplémentaires du signal.
    """

    if sender.name == "userspace":
        try:
            # Création du superutilisateur
            superuser = User.objects.create_superuser(
                username=os.getenv("DJANGO_SUPERUSER_USERNAME", default="admin"),
                email=os.getenv("DJANGO_SUPERUSER_EMAIL", default="admin@gmail.com"),
                password=os.getenv("DJANGO_SUPERUSER_PASSWORD", default="admin"),
            )

            # Ajout du superutilisateur au groupe "admin"
            admin_group, _ = Group.objects.get_or_create(name="admin")
            superuser.groups.add(admin_group)

        except Exception as e:
            logger.error("Une erreur est survenue : %s", e)


@receiver(post_save, sender=User)
def add_default_group(sender, instance, created, **_):  # pylint: disable=W0613
    """
    Assigne un groupe par défaut à un nouvel utilisateur.

    Tout utilisateur nouvellement créé est automatiquement ajouté au groupe "consumer"
    s'il n'appartient à aucun groupe.

    Args:
        sender (Model): Le modèle `User` qui déclenche le signal.
        instance (User): L'instance de l'utilisateur créé.
        created (bool): Indique si l'utilisateur vient d'être créé.
        **kwargs: Arguments supplémentaires du signal.
    """
    if created and not instance.groups.exists():
        instance.groups.set([Group.objects.get(name="consumer")])

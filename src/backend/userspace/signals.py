import logging
import os

from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from userspace.models import User

logger = logging.getLogger("django")


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    """Créer les groupes d’utilisateurs après la migration."""
    if sender.name == "userspacue":
        groups = ["admin", "event_admin", "consumer"]
        for group_name in groups:
            Group.objects.get_or_create(name=group_name)


@receiver(post_migrate)
def create_default_superuser(sender, **kwargs):
    """Créer un super utilisateur après la migration."""
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
            logger.error(f"Une erreur est survenue : {e}", exc_info=True)


@receiver(post_save, sender=User)
def add_default_group(sender, instance, created, **kwargs):
    """Assigner un groupe par défaut à chaque inscription d'une utilisateur"""
    if created and not instance.groups.exists():
        instance.groups.set([Group.objects.get(name="consumer")])

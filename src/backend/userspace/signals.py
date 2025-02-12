from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, User
import os

@receiver(post_migrate)
def create_default_superuser(sender, **kwargs):
    """Créer un super utilisateur après la migration."""
    if sender.name == "userspace": 
        try :
            User.objects.create_superuser(
                username = os.getenv("DJANGO_SUPERUSER_USERNAME", default="admin"),
                email = os.getenv("DJANGO_SUPERUSER_EMAIL", default="admin@gmail.com"),
                password = os.getenv("DJANGO_SUPERUSER_PASSWORD", default="admin"),
            )
        except:
            pass


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    """Créer les groupes d’utilisateurs après la migration."""
    if sender.name == "userspace": 
        groups = ["event_admin", "consommateur"]
        for group_name in groups:
            Group.objects.get_or_create(name=group_name)


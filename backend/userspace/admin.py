"""
Enregistrement du modèle User à l'interface d'administration Django.
"""

from django.contrib import admin
from django.contrib.auth.models import Group as authGroup

from .models import Group, User

admin.site.unregister(authGroup)

admin.site.register(User)

admin.site.register(Group)

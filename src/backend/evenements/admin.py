"""
Module d'enregistrement des modèles pour l'interface d'administration Django.

Ce module permet d'ajouter les modèles `Room`, `Bus` et `Material`
dans l'interface d'administration Django afin de pouvoir les gérer facilement.
"""

from django.contrib import admin
from evenements.models import Bus, Material, Room

for model in (Room, Bus, Material):
    admin.site.register(model)

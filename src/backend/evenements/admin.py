"""
Module d'enregistrement des modèles pour l'interface d'administration Django.

Ce module permet d'ajouter les modèles `Room`, `Bus` et `Material`
dans l'interface d'administration Django afin de pouvoir les gérer facilement.

Classes et Fonctions :
----------------------
- admin.site.register(model) : Enregistre un modèle dans l'admin Django.

Modèles enregistrés :
---------------------
- Room : Représente une salle d'événement.
- Bus : Représente un bus utilisé pour l'événement.
- Material : Représente le matériel utilisé lors de l'événement.
"""

from django.contrib import admin
from evenements.models import Bus, Material, Room

for model in (Room, Bus, Material):
    admin.site.register(model)

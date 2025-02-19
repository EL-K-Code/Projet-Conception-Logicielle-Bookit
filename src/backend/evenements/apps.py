"""
Configuration de l'application 'evenements'.

Ce module définit la configuration de l'application Django `evenements`.
Il permet de spécifier le nom de l'application et le type de clé primaire
par défaut utilisée pour les modèles.

Classes :
---------
- ReservationsConfig : Configure l'application `evenements`.

Attributs :
-----------
- default_auto_field : Définit le type de clé primaire par défaut pour les modèles.
- name : Nom de l'application Django.
"""

from django.apps import AppConfig


class ReservationsConfig(AppConfig):
    """
    Configuration de l'application 'evenements'.

    Cette classe définit les paramètres de l'application `evenements`,
    y compris le type de champ par défaut pour les clés primaires.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "evenements"

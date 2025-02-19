"""
Module pour la configuration de l'application 'reservations' dans Django
"""

from django.apps import AppConfig


class ReservationsConfig(AppConfig):
    """
    Classe de configuration pour l'application 'reservations'
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "reservations"

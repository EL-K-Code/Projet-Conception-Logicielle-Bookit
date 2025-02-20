"""
Configuration de l'application 'evenements'.

Ce module définit la configuration de l'application Django `evenements`.
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
    verbose_name = "📦 Ressources"

    def ready(self):
        """Importe les signaux lors du démarrage de l'application."""
        import evenements.signals  # noqa: F401 # pylint: disable=C0415,W0611

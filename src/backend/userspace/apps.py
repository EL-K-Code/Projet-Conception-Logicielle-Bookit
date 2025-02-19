"""
Module de configuration de l'application userspace.
Ce module définit la configuration de l'application Django,
notamment l'import des signaux lors du démarrage.
"""

from django.apps import AppConfig


class UserspaceConfig(AppConfig):
    """Configuration de l'application userspace."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "userspace"
    verbose_name = "👤userspace"

    def ready(self):
        """Importe les signaux lors du démarrage de l'application."""
        import userspace.signals  # noqa: F401 # pylint: disable=C0415,W0611

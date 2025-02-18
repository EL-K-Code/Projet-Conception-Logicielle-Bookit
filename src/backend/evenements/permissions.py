"""
Module contenant des permissions personnalisées pour l'accès à certaines vues,
en fonction du rôle d'utilisateur et de la relation avec l'événement.
Ce module définit deux classes de permissions :

- IsEventAdmin : Autorise uniquement les utilisateurs appartenant au groupe 'event_admin'.
- IsEventAdminAndOwner : Autorise les utilisateurs appartenant au groupe 'event_admin'
  et étant propriétaires de l'événement.
"""

from rest_framework.permissions import BasePermission


class IsEventAdmin(BasePermission):
    """
    Permission personnalisée qui autorise uniquement les utilisateurs
    appartenant au groupe 'event_admin' à accéder à la vue .
    """

    def has_permission(self, request, view):
        """
        Vérifie si l'utilisateur est connecté et appartient au groupe 'event_admin'.

        Args:
            request : L'objet request contenant l'utilisateur connecté.
            view : La vue demandée.

        Returns:
            bool : Retourne True si l'utilisateur appartient au groupe 'event_admin',
                   sinon False.
        """
        return request.user and request.user.groups.filter(name="event_admin").exists()


class IsEventAdminAndOwner(IsEventAdmin):
    """
    Permission personnalisée qui autorise uniquement les utilisateurs
    appartenant au groupe 'event_admin' et qui sont propriétaires de l'événement
    à accéder à la vue.
    """

    def has_object_permission(self, request, view, event):
        """
        Vérifie que l'utilisateur appartient au groupe 'event_admin' et qu'il est
        le propriétaire de l'événement.

        Args:
            request : L'objet request contenant l'utilisateur connecté.
            view : La vue demandée.
            event : L'événement pour lequel la permission est vérifiée.

        Returns:
            bool : Retourne True si l'utilisateur est à la fois dans le groupe 'event_admin'
                   et est le propriétaire de l'événement, sinon False.
        """
        return super().has_permission(request, view) and event.organizer == request.user

"""
Permissions personnalisées pour gérer l'accès aux événements.

Ce module définit des classes de permissions qui permettent de restreindre
l'accès aux vues en fonction des rôles des utilisateurs, principalement
en fonction de leur appartenance au groupe 'event_admin' et de leur
relation avec un événement spécifique (administrateur et/ou organisateur).
"""

from rest_framework.permissions import BasePermission


class IsEventAdmin(BasePermission):
    """
    Permission personnalisée permettant uniquement aux utilisateurs appartenant
    au groupe 'event_admin' d'accéder à la vue.
    """

    def has_permission(self, request, view):
        """
        Vérifie si l'utilisateur est authentifié et appartient au groupe 'event_admin'.

        Paramètres :
        ------------
        request : HttpRequest
            Objet représentant la requête HTTP en cours.
        view : APIView
            Vue à laquelle l'utilisateur tente d'accéder.

        Retourne :
        ---------
        bool :
            True si l'utilisateur est authentifié et appartient au groupe 'event_admin',
            False sinon.
        """
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name="event_admin").exists()
        )


class IsEventAdminAndOwner(IsEventAdmin):
    """
    Permission personnalisée permettant uniquement aux utilisateurs appartenant
    au groupe 'event_admin' et étant propriétaires de l'événement d'accéder à la vue.
    """

    def has_object_permission(self, request, view, obj):
        """
        Vérifie si l'utilisateur est administrateur et est l'organisateur de l'événement.

        Paramètres :
        ------------
        request : HttpRequest
            Objet représentant la requête HTTP en cours.
        view : APIView
            Vue à laquelle l'utilisateur tente d'accéder.
        obj : Event
            Objet représentant l'événement sur lequel l'autorisation est vérifiée.

        Retourne :
        ---------
        bool :
            True si l'utilisateur est administrateur et est l'organisateur de l'événement,
            False sinon.
        """
        return super().has_permission(request, view) and obj.organizer == request.user

"""
Permissions personnalisées pour gérer l'accès aux événements.

Ce module définit des classes de permissions qui permettent de restreindre
l'accès aux vues en fonction des rôles des utilisateurs, principalement
en fonction de leur appartenance au groupe 'event_admin' et de leur
relation avec un événement spécifique (administrateur et/ou organisateur).

Classes :
---------
- IsEventAdmin : Vérifie si l'utilisateur appartient au groupe 'event_admin'.
- IsEventAdminAndOwner : Vérifie si l'utilisateur est administrateur et
l'organisateur de l'événement.

Chaque classe hérite de la classe `BasePermission` de Django Rest Framework
et implémente une ou plusieurs méthodes permettant de contrôler l'accès
à une vue ou un objet spécifique.

Les permissions sont principalement utilisées pour sécuriser l'accès aux
vues ou ressources liées aux événements.

Exemple d'utilisation :
------------------------
- Lors de l'accès à une vue d'événement, la permission `IsEventAdmin`
  vérifiera si l'utilisateur appartient au groupe 'event_admin'.
- Lors de l'accès à un événement spécifique, la permission
  `IsEventAdminAndOwner` vérifiera à la fois si l'utilisateur est
  administrateur et s'il est l'organisateur de l'événement.

Chaque méthode `has_permission` ou `has_object_permission` retourne un
booléen indiquant si l'accès est autorisé ou non.
"""

from rest_framework.permissions import BasePermission


class IsEventAdmin(BasePermission):
    """
    Permission personnalisée permettant uniquement aux utilisateurs appartenant
    au groupe 'event_admin' d'accéder à la vue.

    Méthodes :
    ----------
    has_permission(request, view) :
        Vérifie si l'utilisateur authentifié appartient au groupe 'event_admin'.
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

    Hérite de :
    -----------
    IsEventAdmin : Vérifie si l'utilisateur est un administrateur d'événement.

    Méthodes :
    ----------
    has_object_permission(request, view, obj) :
        Vérifie si l'utilisateur est à la fois administrateur et organisateur de l'événement.
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

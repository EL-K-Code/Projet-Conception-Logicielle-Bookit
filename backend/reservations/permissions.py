"""
Module contenant des permissions personnalisées pour les réservations.
"""

from rest_framework.permissions import BasePermission


class IsConsumer(BasePermission):
    """
    Permission personnalisée qui autorise uniquement les utilisateurs
    appartenant au groupe 'consumer' à accéder à la vue .
    """

    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="consumer").exists()


class IsConsumerAndOwner(IsConsumer):
    """
    Permission personnalisée qui autorise uniquement les utilisateurs
    appartenant au groupe 'consumer' et qui sont propriétaires de la
    réservation à accéder à la vue.
    """

    def has_object_permission(self, request, view, obj):
        return super().has_permission(request, view) and obj.consumer == request.user

from rest_framework.permissions import BasePermission

class IsEventAdmin(BasePermission):
    """
    Permission personnalisée qui autorise uniquement les utilisateurs
    appartenant au groupe 'event_admin' à accéder à la vue.
    """
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='event_admin').exists()

class IsEventAdminAndOwner(IsEventAdmin):
    """
    Permission personnalisée qui autorise uniquement les utilisateurs
    appartenant au groupe 'event_admin' et qui sont propriétaires de l'événement
    à accéder à la vue.
    """
    def has_object_permission(self, request, view, event):
        return super().has_permission(request, view) and event.organizer == request.user
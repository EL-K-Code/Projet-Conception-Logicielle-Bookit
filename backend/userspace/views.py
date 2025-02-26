"""
Module des vues pour la gestion des utilisateurs dans l'application userspace.

Ce module définit les vues permettant l'inscription, la déconnexion et
la révocation des tokens JWT des utilisateurs.
"""

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User
from .serializers import UserSerializer


class SignUpView(generics.CreateAPIView):
    """
    Vue permettant l'inscription d'un nouvel utilisateur.

    Cette vue utilise le serializer `UserSerializer` pour créer un compte utilisateur.
    L'accès est ouvert à tous (`AllowAny`).
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class SignOutView(generics.DestroyAPIView):
    """
    Vue permettant la suppression du compte utilisateur.

    Un utilisateur authentifié peut supprimer son propre compte.
    L'accès est restreint aux utilisateurs connectés (`IsAuthenticated`).
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Récupère l'utilisateur actuellement authentifié.

        Returns:
            User: L'instance de l'utilisateur connecté.
        """
        return self.request.user

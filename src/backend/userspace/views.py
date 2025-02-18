"""
Module des vues pour la gestion des utilisateurs dans l'application userspace.

Ce module définit les vues permettant l'inscription, la déconnexion et
la révocation des tokens JWT des utilisateurs.
"""

from django.contrib.auth import logout
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

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


class LogOutView(APIView):
    """
    Vue permettant la déconnexion d'un utilisateur.

    Cette vue supprime le refresh token de l'utilisateur en le mettant sur liste noire
    et appelle la fonction `logout()` pour déconnecter l'utilisateur de la session.

    L'accès est restreint aux utilisateurs connectés (`IsAuthenticated`).
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Déconnecte l'utilisateur et invalide son token JWT.

        Args:
            request (Request): La requête HTTP contenant éventuellement le refresh token.

        Returns:
            Response: Un message de confirmation ou une erreur en cas de problème.
        """
        try:
            refresh_token = request.data.get("refresh_token")
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
        except Exception as e:
            return Response({"error": f"Token invalide : {e}"}, status=400)

        # Supprimer l'utilisateur de la session
        logout(request)
        return Response({"message": "Déconnexion réussie"})

"""
Module des vues pour la gestion des utilisateurs dans l'application userspace.

Ce module définit les vues permettant l'inscription, la déconnexion et
la révocation des tokens JWT des utilisateurs.
"""

from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserSerializer


class LoginView(TokenObtainPairView):
    """Login"""

    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        """Requête post"""
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.user

            # Créer la réponse personnalisée
            response_data = {
                "refresh": serializer.validated_data["refresh"],
                "access": serializer.validated_data["access"],
                "username": user.username,
                "groups": user.groups.values_list("name", flat=True),
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_401_UNAUTHORIZED)


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

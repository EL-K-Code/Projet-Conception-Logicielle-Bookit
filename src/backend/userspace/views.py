from django.contrib.auth import logout
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class SignOutView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Récupérer l'utilisateur connecté.
        """
        return self.request.user


class LogOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Ajouter le refresh token à la liste noire
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

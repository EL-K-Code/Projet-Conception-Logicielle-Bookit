"""
Module de gestion des URLs pour l'application userspace.

Ce module définit les routes permettant l'inscription, la connexion,
la déconnexion et le rafraîchissement des tokens JWT.
"""

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signout/", views.SignOutView.as_view(), name="signout"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("login/refresh/", TokenRefreshView.as_view(), name="loginrefresh"),
]

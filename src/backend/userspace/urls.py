from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signout/", views.SignOutView.as_view(), name="signout"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("login/refresh/", TokenRefreshView.as_view(), name="loginrefresh"),
    path("logout/<int:id>", views.LogOutView.as_view(), name="logout"),
]

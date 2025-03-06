"""
Ce module contient des tests unitaires pour ll'application userspace
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from userspace.models import User


class UserspaceTestSetup(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.user = User.objects.create_user(
            username="testuser", password="12345678", email="testuser@gmail.com"
        )


class UserspaceViewsTests(UserspaceTestSetup, APITestCase):

    def test_sign_up_view(self):
        """
        teste la vue SignUpView pour l'inscription d'un utilisateur avec des donées valides
        """
        url = reverse("signup")
        data = {
            "username": "newuser",
            "password": "new12345678",
            "email": "newuser@gmail.com",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)

    def test_sign_out_view_authentificated_user(self):
        """
        teste la suppresion de compte pour un utilisateur authentifié
        """
        self.client.force_authenticate(self.user)

        url = reverse("signout")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(
                username="testuser"
            )  # on verifie qu'il a bien été supprimé

    def test_sign_out_view_unauthenticated_user(self):
        """
        Teste la tentative de compte pour un utilisateur non authentifié.
        """
        url = reverse("signout")
        response = self.client.delete(url)

        # on vérifie que l'accès est refusé pour un utilisateur non authentifié
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

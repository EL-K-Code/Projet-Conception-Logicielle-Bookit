"""
Module de tests pour l'pplication evenements
"""

from datetime import datetime

from django.test import TestCase
from django.utils import timezone
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase
from userspace.models import Group, User

from .models import Bus, EventBus, EventMaterial, EventRoom, Material, Room


class UserGroupAssignmentTests(TestCase):
    """
    Classe de tests pour vérifier l'assignation des utilisateurs aux groupes

    Args:
        TestCase (class): Classe de base pour les tests unitaires de Django
    """

    def test_user_created_without_group_is_added_to_consumer(self):
        """Test qu'un utilisateur créé sans groupe est ajouté au groupe 'consumer'."""
        user = User.objects.create_user(
            username="test_user", email="test_user@example.com", password="password123"
        )
        # Vérifie que l'utilisateur est bien ajouté au groupe 'consumer'
        consumer_group = Group.objects.get(name="consumer")
        self.assertIn(consumer_group, user.groups.all())


class EventViewsTests(APITestCase, TestCase):
    """
    Classe contenant les méthodes pour tester les vues liées aux événements.

    Args:
        APITestCase (class): Classe de base pour tester les vues API de Django
        TestCase (class): Classe de base pour les tests unitaires de Django
    """

    @classmethod
    def setUpTestData(cls):

        cls.event_admin_group = Group.objects.get(name="event_admin")

        # Création de l'utilisateur ayant le groupe 'event_admin'
        cls.user_event_admin = User.objects.create_user(
            username="event_admin_user",
            email="event_admin@example.com",
            password="password123",
        )
        cls.user_event_admin.groups.add(cls.event_admin_group)
        cls.user_event_admin.save()

        # Création de l'utilisateur ayant le groupe 'consumer'
        cls.user_consumer = User.objects.create_user(
            username="consumer_user",
            email="consumer@example.com",
            password="password123",
        )
        cls.bus1 = Bus.objects.create(name="Bus 1", number_seats=50)
        cls.bus2 = Bus.objects.create(name="Bus 2", number_seats=50)
        cls.room1 = Room.objects.create(name="101", description="Salle 112 niveau 1")
        cls.room2 = Room.objects.create(name="201", description="Salle 201 niveau 2")
        cls.material1 = Material.objects.create(
            name="Adaptateur USB C vers HDMI", stock=10
        )
        cls.material2 = Material.objects.create(name="Video Projecteurs", stock=10)

        # Création des ressources
        cls.event_bus = EventBus.objects.create(
            description="Sortie gala de fin d'année",
            organizer=cls.user_event_admin,
            resource=cls.bus1,
            departure="Paris",
            destination="Lyon",
            start_time=timezone.make_aware(datetime(2025, 3, 1, 18, 0, 0)),
            end_time=timezone.make_aware(datetime(2025, 3, 1, 19, 0, 0)),
        )
        cls.event_room = EventRoom.objects.create(
            description="salle disponible sur réservation",
            organizer=cls.user_event_admin,
            resource=cls.room1,
        )
        cls.event_material = EventMaterial.objects.create(
            description="Adaptateurs disponibles sur réservation",
            organizer=cls.user_event_admin,
            resource=cls.material1,
        )

        # Initialisation de l'APIClient
        cls.client = APIClient()

    def setUp(self):
        """
        force l'authentification de l'utilisateur 'self.user_event_admin' avec le client API
        avant chaque test, afin de simuler des requêtes authentifés
        """
        self.client.force_authenticate(user=self.user_event_admin)

    def test_create_event_room_view(self):
        """
        Teste la vue 'CreateEventRoomView' pour l'utilisateur ayant le groupe 'event_admin'.
        """
        url = reverse("create-room-event")
        data = {
            "description": "Salle disponible sur réservation",
            "resource": self.room2.id,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EventRoom.objects.count(), 2)
        self.assertEqual(EventRoom.objects.last().resource, self.room2)

    def test_create_event_room_view_non_event_admin(self):
        """
        Teste la création d'un événement de salle pour un utilisateur non 'event_admin'.
        L'utilisateur ne devrait pas avoir la permission de créer un événement.
        """
        self.client.force_authenticate(user=self.user_consumer)

        url = reverse("create-room-event")
        data = {
            "description": "Salle disponible sur réservation",
            "resource": self.room1.id,
        }
        response = self.client.post(url, data)

        # On vérifie que la réponse renvoie un statut 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_event_bus_view(self):
        """
        Teste la vue 'CreateEventBusView' pour l'utilisateur ayant le groupe 'event_admin'.
        """
        url = reverse("create-bus-event")
        data = {
            "description": "Visite",
            "resource": self.bus2.id,
            "departure": "Paris",
            "destination": "Lyon",
            "start_time": timezone.make_aware(datetime(2025, 3, 1, 18, 0, 0)),
            "end_time": timezone.make_aware(datetime(2025, 3, 1, 19, 0, 0)),
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EventBus.objects.count(), 2)
        self.assertEqual(EventBus.objects.last().resource, self.bus2)

    def test_create_event_material_view(self):
        """
        Teste la vue 'CreateEventMaterialView' pour l'utilisateur ayant le groupe 'event_admin'.
        """
        url = reverse("create-material-event")
        data = {
            "description": "VidéoProjecteurs disponibles",
            "resource": self.material2.id,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EventMaterial.objects.count(), 2)
        self.assertEqual(EventMaterial.objects.last().resource, self.material2)

    def test_get_all_bus_event_view(self):
        """
        Teste la vue 'GetAllBusEventView' pour lister tous les événements liés aux bus.
        """
        url = reverse("get-all-bus-event")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_all_room_event_view(self):
        """
        Teste la vue 'GetAllRoomEventView' pour lister tous les événements liés aux salles.
        """
        url = reverse("get-all-room-event")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_et_all_material_event_view(self):
        """
        Teste la vue 'GetAllMaterialEventView' pour lister tous les événements liés aux matériels.
        """
        url = reverse("get-all-material-event")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_event_room_view(self):
        """
        Teste la vue 'UpdateEventRoomView' pour modifier un événement lié aux salles.
        """
        url = reverse("update-room-event", args=[self.event_room.id])
        data = {"description": "Salle modifiée", "resource": self.room2.id}
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            EventRoom.objects.get(id=self.event_room.id).description, "Salle modifiée"
        )

    def test_update_event_bus_view(self):
        """
        Teste la vue 'UpdateEventBusView' pour modifier un événement lié aux bus.
        """
        url = reverse("update-bus-event", args=[self.event_bus.id])
        data = {
            "description": "Gala modifié",
            "resource": self.bus1.id,
            "departure": "Paris",
            "destination": "Marseille",
            "start_time": timezone.make_aware(datetime(2025, 3, 1, 18, 0, 0)),
            "end_time": timezone.make_aware(datetime(2025, 3, 1, 19, 0, 0)),
        }
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            EventBus.objects.get(id=self.event_bus.id).destination, "Marseille"
        )

    def test_update_event_material_view(self):
        """
        Teste la vue 'UpdateEventMaterialView' pour modifier un événement lié aux matériels.
        """
        url = reverse("update-material-event", args=[self.event_material.id])
        data = {"description": "Adaptateurs mis à jour", "resource": self.material1.id}
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            EventMaterial.objects.get(id=self.event_material.id).description,
            "Adaptateurs mis à jour",
        )

    def test_delete_event_room_view(self):
        """
        Teste la vue 'DeleteEventRoomView' pour supprimer un événement lié aux salles.
        """
        url = reverse("delete-room-event", args=[self.event_room.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EventRoom.objects.count(), 0)

    def test_delete_event_bus_view(self):
        """
        Teste la vue 'DeleteEventBusView' pour supprimer un événement lié aux bus.
        """
        url = reverse("delete-bus-event", args=[self.event_bus.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EventBus.objects.count(), 0)

    def test_delete_event_material_view(self):
        """
        Teste la vue 'DeleteEventMaterialView' pour supprimer un événement lié aux matériels.
        """
        url = reverse("delete-material-event", args=[self.event_material.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EventMaterial.objects.count(), 0)

"""
Ce module contient des tests unitaires pour les reservations de bus, salle et matérial
"""

from datetime import date, datetime, time

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from evenements.models import Bus, EventBus, EventMaterial, EventRoom, Material, Room
from reservations.models import ReservationBus, ReservationMaterial, ReservationRoom
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from userspace.models import User


class ReservationTestSetup(TestCase):
    """
    Classe de configutation avec les données de test
    Elle hérite de TestCase

    Args:
        TestCase (class): Classe de base pour les tests unitaires de Django
    """

    @classmethod
    def setUpTestData(cls):
        """
        définie les données à utiliser dans les tests de ReservationTestCase
        (utilisateur, bus, salle, matériel, événements)
        """
        cls.client = APIClient()
        cls.user = User.objects.create_user(
            username="testuser", password="12345678", email="testuser@gmail.com"
        )
        cls.other_user = User.objects.create_user(
            username="other_user", password="123456789", email="otheruser@gmail.com"
        )

        cls.bus = Bus.objects.create(name="Bus 1", number_seats=50)
        cls.room = Room.objects.create(name="101", description="Salle 112 niveau 1")
        cls.material = Material.objects.create(
            name="Adaptateur USB C vers HDMI", stock=10
        )
        cls.event_bus = EventBus.objects.create(
            description="Sortie gala de fin d'année",
            organizer=cls.user,
            resource=cls.bus,
            departure="Paris",
            destination="Lyon",
            departure_time=timezone.make_aware(datetime(2025, 3, 1, 18, 0, 0)),
            arrival_time=timezone.make_aware(datetime(2025, 3, 1, 19, 0, 0)),
        )
        cls.event_room = EventRoom.objects.create(
            description="salle disponible sur réservation",
            organizer=cls.user,
            resource=cls.room,
        )
        cls.event_material = EventMaterial.objects.create(
            description="Adaptateurs disponibles sur réservation",
            organizer=cls.user,
            resource=cls.material,
        )


class ReservationManagerTests(ReservationTestSetup):
    """
    Classe pour tester les méthodes de réservation et d'annulation définis dans ReservationMananger

    Args:
        ReservationTestSetup (class): Classe de configuration des des données de test
    """

    def test_reserve_bus_success(self):
        """
        Test pour vérifier la réservtaion réussie d'un bus
        """
        reservation_bus = ReservationBus.objects.reserve_bus(
            consumer=self.user, event_bus=self.event_bus
        )
        self.assertEqual(self.event_bus.available_seats, 49)
        self.assertEqual(self.event_bus.is_reserved, False)
        self.assertEqual(ReservationBus.objects.count(), 1)
        self.assertEqual(reservation_bus.consumer, self.user)
        self.assertEqual(reservation_bus.event_bus, self.event_bus)
        self.assertEqual(
            str(reservation_bus),
            "Réservation de testuser pour Sortie gala de fin d'année",
        )

    def test_reserve_bus_no_seats(self):
        """
        Test pour vérifier la réservation d'un bus sans places disponibles
        """
        self.event_bus.available_seats = 1
        self.event_bus.save()
        ReservationBus.objects.reserve_bus(consumer=self.user, event_bus=self.event_bus)

        # On vérifie si is_reserved==True après réservation de la dernière place du bus
        self.assertEqual(self.event_bus.is_reserved, True)

        with self.assertRaises(ValidationError, msg="Plus de places disponibles"):
            ReservationBus.objects.reserve_bus(
                consumer=self.user, event_bus=self.event_bus
            )

    def test_reserve_room_success(self):
        """
        Test pour vérifier la réservation réussie d'une salle
        """
        reservation_room = ReservationRoom.objects.reserve_room(
            consumer=self.user,
            event_room=self.event_room,
            date=date(2025, 3, 3),
            start_time=time(16, 0),
            end_time=time(18, 0),
        )
        self.assertEqual(self.event_room.is_reserved, True)
        self.assertEqual(ReservationRoom.objects.count(), 1)
        self.assertEqual(reservation_room.consumer, self.user)
        self.assertEqual(reservation_room.event_room, self.event_room)
        self.assertEqual(reservation_room.date, date(2025, 3, 3))
        self.assertEqual(reservation_room.start_time, time(16, 0))
        self.assertEqual(reservation_room.end_time, time(18, 0))
        self.assertEqual(
            str(reservation_room),
            "Réservation de testuser pour salle disponible sur réservation",
        )

    def test_reserve_room_conflict(self):
        """
        Test pour vérifier un conflit de réservation de salle
        """
        ReservationRoom.objects.reserve_room(
            consumer=self.user,
            event_room=self.event_room,
            date=date(2025, 3, 3),
            start_time=time(17, 0),
            end_time=time(19, 0),
        )
        with self.assertRaises(
            ValidationError, msg="Cette salle existe déjà pour ce créneau"
        ):
            ReservationRoom.objects.reserve_room(
                consumer=self.user,
                event_room=self.event_room,
                date=date(2025, 3, 3),
                start_time=time(18, 0),
                end_time=time(20, 0),
            )

    def test_reserve_material_success(self):
        """
        Test pour vérifier la résservation réussie d'un matériel
        """
        reservation_material = ReservationMaterial.objects.reserve_material(
            consumer=self.user,
            event_material=self.event_material,
            date=date(2025, 3, 3),
            start_time=time(17, 0),
            end_time=time(19, 0),
            quantity=10,
        )
        self.assertEqual(ReservationMaterial.objects.count(), 1)
        self.assertEqual(self.event_material.is_reserved, True)
        self.assertEqual(self.event_material.available_stock, 0)
        self.assertEqual(reservation_material.consumer, self.user)
        self.assertEqual(reservation_material.event_material, self.event_material)
        self.assertEqual(reservation_material.date, date(2025, 3, 3))
        self.assertEqual(reservation_material.start_time, time(17, 0))
        self.assertEqual(reservation_material.end_time, time(19, 0))
        self.assertEqual(reservation_material.quantity, 10)
        self.assertEqual(
            str(reservation_material),
            "Réservation de testuser pour Adaptateurs disponibles sur réservation (10 unités)",
        )

    def test_reserve_material_insufficient_stock(self):
        """
        Test pour vérifier la réservation avec stock insuffisant
        """
        with self.assertRaises(
            ValidationError, msg="Stock insuffisant pour cette réservation"
        ):
            ReservationMaterial.objects.reserve_material(
                consumer=self.user,
                event_material=self.event_material,
                date=date(2025, 3, 3),
                start_time=time(17, 0),
                end_time=time(19, 0),
                quantity=15,
            )

    def test_cancel_bus_reservation(self):
        """
        Test pour vérifier l'annulation d'une réservation de bus
        """
        reservation_bus = ReservationBus.objects.reserve_bus(
            consumer=self.user, event_bus=self.event_bus
        )
        ReservationBus.objects.cancel_bus_reservation(reservation_bus)
        self.assertEqual(self.event_bus.available_seats, 50)
        self.assertEqual(ReservationBus.objects.count(), 0)
        self.assertEqual(self.event_bus.is_reserved, False)

    def test_cancel_room_reservation(self):
        """
        Test pour vérifier l'annulation d'une réservation de salle
        """
        reservation_room = ReservationRoom.objects.reserve_room(
            consumer=self.user,
            event_room=self.event_room,
            date=date(2025, 3, 3),
            start_time=time(16, 0),
            end_time=time(18, 0),
        )
        ReservationRoom.objects.cancel_room_reservation(reservation_room)
        self.assertEqual(ReservationRoom.objects.count(), 0)
        self.assertEqual(self.event_room.is_reserved, False)

    def test_cancel_material_reservation(self):
        """
        Test pour vérifier l'annulation d'une réservation de matériel
        """
        reservation_material = ReservationMaterial.objects.reserve_material(
            consumer=self.user,
            event_material=self.event_material,
            date=date(2025, 3, 3),
            start_time=time(17, 0),
            end_time=time(19, 0),
            quantity=10,
        )
        ReservationMaterial.objects.cancel_material_reservation(reservation_material)
        self.assertEqual(self.event_material.available_stock, 10)
        self.assertEqual(ReservationMaterial.objects.count(), 0)
        self.assertEqual(self.event_material.is_reserved, False)


class ReservationViewsTests(ReservationTestSetup, APITestCase):
    """
    classe contenant les méthodes pour tester les vues liées aux réservations

    Args:
        ReservationTestSetup (class):Classe de configutation avec les données de test
        APITestCase (class): Classe de base pour tester les vues API de Django
    """

    def setUp(self):
        """
        force l'authentification de l'urilisateur 'self.user' avec le client API
        avant chaque test, afin de simuler des requêtes authentifés
        """
        self.client.force_authenticate(user=self.user)

    def test_make_bus_reservation_view(self):
        """
        teste la vue 'MakeBusReservationView"
        """
        url = reverse("make-bus-reservation")
        data = {"event_bus": self.event_bus.id}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ReservationBus.objects.count(), 1)
        self.assertEqual(ReservationBus.objects.first().consumer, self.user)

    def test_make_room_reservation_view(self):
        """
        teste la vue 'MakeRoomReservation'
        """
        url = reverse("make-room-reservation")
        data = {
            "event_room": self.event_room.id,
            "date": date(2025, 3, 3),
            "start_time": time(16, 0),
            "end_time": time(18, 0),
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ReservationRoom.objects.count(), 1)
        self.assertEqual(ReservationRoom.objects.first().consumer, self.user)

    def test_make_material_reservation_view(self):
        """
        teste la vue 'MakeMaterialReservation'
        """
        url = reverse("make-material-reservation")
        data = {
            "event_material": self.event_material.id,
            "date": date(2025, 3, 3),
            "start_time": time(16, 0),
            "end_time": time(18, 0),
            "quantity": 1,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ReservationMaterial.objects.count(), 1)
        self.assertEqual(ReservationMaterial.objects.first().consumer, self.user)

    def test_cancel_bus_reservation_view(self):
        """
        teste la vue 'CancelBusReservationView'
        """
        reservation_bus = ReservationBus.objects.reserve_bus(
            consumer=self.user, event_bus=self.event_bus
        )
        url = reverse("cancel-bus-reservation", args=[reservation_bus.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ReservationBus.objects.count(), 0)

    def test_cancel_room_reservation_view(self):
        """
        teste la vue 'CancelRoomReservationView'
        """
        reservation_room = ReservationRoom.objects.reserve_room(
            consumer=self.user,
            event_room=self.event_room,
            date=date(2025, 3, 3),
            start_time=time(16, 0),
            end_time=time(18, 0),
        )
        url = reverse("cancel-room-reservation", args=[reservation_room.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ReservationRoom.objects.count(), 0)

    def test_cancel_material_reservation_view(self):
        """
        teste la vue 'CancelMaterialReservationView'
        """
        reservation_material = ReservationMaterial.objects.reserve_material(
            consumer=self.user,
            event_material=self.event_material,
            date=date(2025, 3, 3),
            start_time=time(17, 0),
            end_time=time(19, 0),
            quantity=2,
        )
        url = reverse("cancel-material-reservation", args=[reservation_material.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ReservationMaterial.objects.count(), 0)

    def test_permission_required_for_reservation(self):
        """
        teste que l'utilisateur non authentifié reçoit une erreur 401 pour
        une tentative de réservation
        """
        self.client.force_authenticate(user=None)  # déconnecte l'utilisateur
        url = reverse("make-room-reservation")
        data = {"event_bus": self.event_bus.id}
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_401_UNAUTHORIZED
        )  # L'utilisateur n'est pas authentifié

    def test_permission_required_for_cancellation(self):
        """
        teste que l'utilisateur reçoit une erreur 403 pour annuler une réservation
        dont il n'est pas propriétaire
        """
        reservation_bus = ReservationBus.objects.reserve_bus(
            consumer=self.other_user, event_bus=self.event_bus
        )
        url = reverse("cancel-bus-reservation", args=[reservation_bus.id])
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN
        )  # L'utilisateur n'est pas propriétaire

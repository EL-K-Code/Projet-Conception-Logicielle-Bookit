"""
Ce module contient des tests unitaires pour les reservations de bus, salle et matérial
"""

from datetime import date, datetime, time

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
from evenements.models import Bus, EventBus, EventMaterial, EventRoom, Material, Room
from reservations.models import ReservationBus, ReservationMaterial, ReservationRoom
from userspace.models import User


class ReservationTestCase(TestCase):
    """
    Classe TestCase contenant les méthodes pour tester des scénarios
    de réservation et d'annulation
    """

    def setUp(self):
        """
        définie les données à utiliser dans les tests de ReservationTestCase
        (utilisateur, bus, salle, matériel, événements)
        """

        self.user = User.objects.create_user(
            username="testuser", password="12345678", email="testuser@gmail.com"
        )
        self.bus = Bus.objects.create(name="Bus 1", number_seats=50)
        self.room = Room.objects.create(name="101", description="Salle 112 niveau 1")
        self.material = Material.objects.create(
            name="Adaptateur USB C vers HDMI", stock=10
        )
        self.event_bus = EventBus.objects.create(
            description="Sortie gala de fin d'année",
            organizer=self.user,
            resource=self.bus,
            departure="Paris",
            destination="Lyon",
            departure_time=timezone.make_aware(datetime(2025, 3, 1, 18, 0, 0)),
            arrival_time=timezone.make_aware(datetime(2025, 3, 1, 19, 0, 0)),
        )
        self.event_room = EventRoom.objects.create(
            description="salle disponible sur réservation",
            organizer=self.user,
            resource=self.room,
        )
        self.event_material = EventMaterial.objects.create(
            description="Adaptateurs disponibles sur réservation",
            organizer=self.user,
            resource=self.material,
        )

    def test_reserve_bus_success(self):
        """
        Test pour vérifier la réservtaion réussie d'un bus
        """
        reservation_bus = ReservationBus.objects.reserve_bus(
            consumer=self.user, event_bus=self.event_bus
        )
        self.assertEqual(self.event_bus.available_seats, 49)
        self.assertEqual(reservation_bus.consumer, self.user)
        self.assertEqual(ReservationBus.objects.count(), 1)

    def test_reserve_bus_no_seats(self):
        """
        Test pour vérifier la réservation d'un bus sans places disponibles
        """
        self.event_bus.available_seats = 0
        self.event_bus.save()

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
        self.assertEqual(reservation_room.consumer, self.user)
        self.assertEqual(ReservationRoom.objects.count(), 1)

    def test_reserve_room_conflict(self):
        """
        Test pour vérifier un conflit de réservation de salle
        """
        ReservationRoom.objects.reserve_room(
            consumer=self.user,
            event_room=self.event_room,
            date=date(2025, 3, 3),
            start_time=time(16, 0),
            end_time=time(18, 0),
        )
        with self.assertRaises(
            ValidationError, msg="Cette salle existe déjà pour ce créneau"
        ):
            ReservationRoom.objects.reserve_room(
                consumer=self.user,
                event_room=self.event_room,
                date=date(2025, 3, 3),
                start_time=time(17, 0),
                end_time=time(19, 0),
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
            quantity=2,
        )
        self.assertEqual(reservation_material.quantity, 2)
        self.assertEqual(self.event_material.available_stock, 8)
        self.assertEqual(ReservationMaterial.objects.count(), 1)

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
            quantity=2,
        )
        ReservationMaterial.objects.cancel_material_reservation(reservation_material)
        self.assertEqual(self.event_material.available_stock, 10)
        self.assertEqual(ReservationMaterial.objects.count(), 0)

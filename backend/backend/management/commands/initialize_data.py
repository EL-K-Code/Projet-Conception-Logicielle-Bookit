"""
Ce script permet d'initialiser la base de données avec des utilisateurs,
des ressources(bus, salles, matériels) des événements associés à ces ressources,
et des réservations pour tester l'application.
"""

from datetime import date, datetime, time

from django.core.management.base import BaseCommand
from django.utils import timezone
from evenements.models import Bus, EventBus, EventMaterial, EventRoom, Material, Room
from reservations.models import ReservationBus, ReservationMaterial, ReservationRoom
from userspace.models import Group, User


class Command(BaseCommand):
    """
    commande personnalisée pour initialiser les données dans la base

    Args:
        BaseCommand (class): Classe de base pour la gestion des commandes Django.
    """

    help = """Initialise les données de l'application avec des utilisateurs, des ressources,
                des événements et des réservations"""

    def handle(self, *args, **kwargs):
        """
        Exécute la commande pour initialiser les données
        """

        # Création des utilisateurs
        event_admin_group = Group.objects.get(name="event_admin")

        users = {
            "event_admin": User.objects.create_user(
                username="Yatoute",
                email="mintoamayatoute@gmail.com",
                password="password123",
            ),
            "consumer": User.objects.create_user(
                username="Richard",
                email="gozamegborichard14@gmail.com",
                password="password123",
            ),
        }

        users["event_admin"].groups.add(event_admin_group)
        users["event_admin"].save()

        # Création des ressources (Bus, Salles, Matériels)
        resources = {
            "buses": [
                Bus.objects.create(name="Bus 1", number_seats=50),
                Bus.objects.create(name="Bus 2", number_seats=50),
                Bus.objects.create(name="Bus 3", number_seats=60),
                Bus.objects.create(name="Bus 4", number_seats=40),
            ],
            "rooms": [
                Room.objects.create(name="101", description="Salle 101 Niveau 1"),
                Room.objects.create(name="102", description="Salle 102 Niveau 1"),
                Room.objects.create(name="201", description="Salle 201 Niveau 2"),
                Room.objects.create(name="202", description="Salle 202 Niveau 2"),
            ],
            "materials": [
                Material.objects.create(name="Adaptateur USB C vers HDMI", stock=10),
                Material.objects.create(name="Vidéo Projecteurs", stock=20),
                Material.objects.create(name="Écran de Projection", stock=5),
                Material.objects.create(name="Microphones sans fil", stock=8),
            ],
        }

        # Création des événements de ressources (Bus, Salles, Matériels)
        events = {
            "event_buses": [
                EventBus.objects.create(
                    description="Sortie gala de fin d'année",
                    organizer=users["event_admin"],
                    resource=resources["buses"][0],
                    departure="ENSAI",
                    destination="Chateau d'Apigné",
                    start_time=timezone.make_aware(datetime(2025, 3, 29, 18, 0, 0)),
                    end_time=timezone.make_aware(datetime(2025, 3, 29, 19, 0, 0)),
                ),
                EventBus.objects.create(
                    description="Visite place de la mairie",
                    organizer=users["event_admin"],
                    resource=resources["buses"][1],
                    departure="ENSAI",
                    destination="République",
                    start_time=timezone.make_aware(datetime(2025, 3, 22, 10, 0, 0)),
                    end_time=timezone.make_aware(datetime(2025, 3, 22, 12, 0, 0)),
                ),
            ],
            "event_rooms": [
                EventRoom.objects.create(
                    description="Salle disponible",
                    organizer=users["event_admin"],
                    resource=resources["rooms"][0],
                ),
                EventRoom.objects.create(
                    description="Salle disponible",
                    organizer=users["event_admin"],
                    resource=resources["rooms"][1],
                ),
            ],
            "event_materials": [
                EventMaterial.objects.create(
                    description="Adaptateurs USB C vers HDMI disponibles",
                    organizer=users["event_admin"],
                    resource=resources["materials"][0],
                ),
                EventMaterial.objects.create(
                    description="Projecteurs vidéo disponibles",
                    organizer=users["event_admin"],
                    resource=resources["materials"][1],
                ),
            ],
        }

        # Création de réservations pour les événements

        # Réservation de bus
        reservation_bus1 = ReservationBus.objects.reserve_bus(
            consumer=users["consumer"], event_bus=events["event_buses"][0]
        )
        reservation_bus2 = ReservationBus.objects.reserve_bus(
            consumer=users["consumer"], event_bus=events["event_buses"][1]
        )
        self.print_reservation_success("bus", reservation_bus1)
        self.print_reservation_success("bus", reservation_bus2)

        # Réservation de salle
        reservation_room1 = ReservationRoom.objects.reserve_room(
            consumer=users["consumer"],
            event_room=events["event_rooms"][0],
            date=date(2025, 3, 3),
            start_time=time(9, 0),
            end_time=time(12, 0),
        )
        reservation_room2 = ReservationRoom.objects.reserve_room(
            consumer=users["consumer"],
            event_room=events["event_rooms"][1],
            date=date(2025, 3, 4),
            start_time=time(14, 0),
            end_time=time(17, 0),
        )
        self.print_reservation_success("salle", reservation_room1)
        self.print_reservation_success("salle", reservation_room2)

        # Réservation de matériel
        reservation_material1 = ReservationMaterial.objects.reserve_material(
            consumer=users["consumer"],
            event_material=events["event_materials"][0],
            date=date(2025, 3, 3),
            start_time=time(10, 0),
            end_time=time(12, 0),
            quantity=5,
        )
        reservation_material2 = ReservationMaterial.objects.reserve_material(
            consumer=users["consumer"],
            event_material=events["event_materials"][1],
            date=date(2025, 3, 3),
            start_time=time(13, 0),
            end_time=time(15, 0),
            quantity=3,
        )
        self.print_reservation_success("matériel", reservation_material1)
        self.print_reservation_success("matériel", reservation_material2)

    def print_reservation_success(self, reservation_type, reservation):
        """Affiche un message de succès pour la réservation."""
        self.stdout.write(
            self.style.SUCCESS(
                f"Réservation de {reservation_type} effectuée pour {reservation.consumer.username}"
            )
        )

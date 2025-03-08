from django.utils import timezone
from reservations.models import ReservationBus, ReservationMaterial, ReservationRoom


class ReservationService:
    """Service permettant de récupérer les réservations en fonction de leur statut dynamique."""

    @staticmethod
    def get_in_progress_reservations():
        """Retourne les réservations actuellement en cours."""
        now = timezone.now()
        return {
            "buses": ReservationBus.objects.filter(
                event_bus__start_time__lte=now, event_bus__start_time__gte=now
            ),
            "rooms": ReservationRoom.objects.filter(
                start_time__lte=now, end_time__gte=now
            ),
            "materials": ReservationMaterial.objects.filter(
                start_time__lte=now, end_time__gte=now
            ),
        }

    @staticmethod
    def get_upcoming_reservations():
        """Retourne les réservations à venir."""
        now = timezone.now()
        return {
            "buses": ReservationBus.objects.filter(event_bus__start_time__gt=now),
            "rooms": ReservationRoom.objects.filter(start_time__gt=now),
            "materials": ReservationMaterial.objects.filter(start_time__gt=now),
        }

    @staticmethod
    def get_past_reservations():
        """Retourne les réservations terminées."""
        now = timezone.now()
        return {
            "buses": ReservationBus.objects.filter(event_bus__start_time__lt=now),
            "rooms": ReservationRoom.objects.filter(end_time__lt=now),
            "materials": ReservationMaterial.objects.filter(end_time__lt=now),
        }

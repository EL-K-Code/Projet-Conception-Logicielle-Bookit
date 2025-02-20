"""
Module contenant les routes pour la gestion des réservations.
"""

from django.urls import path

from . import views

urlpatterns = [
    path(
        "make-reservation/bus/",
        views.MakeBusReservationView.as_view(),
        name="make-bus-reservation",
    ),
    path(
        "make-reservation/room/",
        views.MakeRoomReservationView.as_view(),
        name="make-room-reservation",
    ),
    path(
        "make-reservation/material/",
        views.MakeMaterialReservationView.as_view(),
        name="make-material-reservation",
    ),
    path(
        "cancel-reservation-bus/<int:id>",
        views.CancelBusReservation.as_view(),
        name="cancel-bus-reservation",
    ),
    path(
        "cancel-reservation-room/<int:id>",
        views.CancelRoomReservation.as_view(),
        name="cancel-room-reservation",
    ),
    path(
        "cancel-reservation-material/<int:id>",
        views.CancelMaterialReservation.as_view(),
        name="cancel-material-reservation",
    ),
]

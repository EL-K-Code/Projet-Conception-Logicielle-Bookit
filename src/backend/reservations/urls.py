"""
Module contenant les routes pour la gestion des réservations.
"""

from django.urls import path

from . import views

urlpatterns = [
    path(
        "make/bus/", views.MakeBusReservationView.as_view(), name="make-bus-reservation"
    ),
    path(
        "make/room/",
        views.MakeRoomReservationView.as_view(),
        name="make-room-reservation",
    ),
    path(
        "make/material/",
        views.MakeMaterialReservationView.as_view(),
        name="make-material-reservation",
    ),
    path(
        "cancel/bus/<int:id>",
        views.CancelBusReservation.as_view(),
        name="cancel-bus-reservation",
    ),
    path(
        "cancel/room/<int:id>",
        views.CancelRoomReservation.as_view(),
        name="cancel-room-reservation",
    ),
    path(
        "cancel/material/<int:id>",
        views.CancelMaterialReservation.as_view(),
        name="cancel-material-reservation",
    ),
]

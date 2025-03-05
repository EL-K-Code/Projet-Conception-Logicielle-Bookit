"""
Définition des routes pour l'application des événements.

Ce module contient les différentes URL permettant de lister, créer, mettre à jour
et supprimer des événements liés aux salles, aux bus et aux matériels.
"""

from django.urls import path

from . import views

urlpatterns = [
    path(
        "create-event/bus/", views.CreateEventBusView.as_view(), name="create-bus-event"
    ),
    path(
        "create-event/room/",
        views.CreateEventRoomView.as_view(),
        name="create-room-event",
    ),
    path(
        "create-event/material/",
        views.CreateEventMaterialView.as_view(),
        name="create-material-event",
    ),
    path("list-event/", views.EventListView.as_view(), name="list-event"),
    path(
        "get-all-bus-event/",
        views.GetAllBusEventView.as_view(),
        name="get-all-bus-event",
    ),
    path(
        "get-all-room-event/",
        views.GetAllRoomEventView.as_view(),
        name="get-all-room-event",
    ),
    path(
        "get-all-material-event/",
        views.GetAllMaterialEventView.as_view(),
        name="get-all-material-event",
    ),
    path(
        "delete-event-room/<int:id>",
        views.DeleteEventRoomView.as_view(),
        name="delete-room-event",
    ),
    path(
        "delete-event-bus/<int:id>",
        views.DeleteEventBusView.as_view(),
        name="delete-bus-event",
    ),
    path(
        "delete-event-material/<int:id>",
        views.DeleteEventMaterialView.as_view(),
        name="delete-material-event",
    ),
    path(
        "update-event-room/<int:id>",
        views.UpdateEventRoomView.as_view(),
        name="update-room-event",
    ),
    path(
        "update-event-bus/<int:id>",
        views.UpdateEventBusView.as_view(),
        name="update-bus-event",
    ),
    path(
        "update-event-material/<int:id>",
        views.UpdateEventMaterialView.as_view(),
        name="update-material-event",
    ),
    path(
        "list-all-bus-resource/", views.ListAllBusView(), name="list-all-bus-resource"
    ),
    path(
        "list-all-room-resource", views.ListAllRoomView(), name="list-all-room-resource"
    ),
    path(
        "list-all-material-resource",
        views.ListAllMaterialView(),
        name="list-all-material-resource",
    ),
]

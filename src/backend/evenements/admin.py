from django.contrib import admin
from evenements.models import Room, Bus, Material

for model in (Room, Bus, Material):
    admin.site.register(model)

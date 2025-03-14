"""
Configuration personnalisé du site d'administrateur
"""

import os

from django.contrib import admin
from dotenv import load_dotenv
from evenements.models import Bus, Material, Room
from userspace.models import Group, User

load_dotenv()


class BookitAdminSite(admin.AdminSite):
    "Site de l'Administrateur Bookit"

    site_header = "ESPACE ADMINISRATEUR"
    index_title = " "
    site_title = "Admin"
    site_url = os.getenv("HOME_URL", default="#")


bookit_admin_site = BookitAdminSite(name="admin")

for model in (User, Group, Room, Bus, Material):
    bookit_admin_site.register(model)

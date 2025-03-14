from django.contrib.admin.apps import AdminConfig


class BookitAdminConfig(AdminConfig):
    default_site = "backend.admin.BookitAdminSite"

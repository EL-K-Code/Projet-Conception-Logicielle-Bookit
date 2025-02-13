# Generated by Django 5.1.6 on 2025-02-14 17:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("evenements", "0002_initial"),
        ("reservations", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="reservationbus",
            name="consumer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="reservationbus",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="evenements.eventbus"
            ),
        ),
        migrations.AddField(
            model_name="reservationmaterial",
            name="consumer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="reservationmaterial",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="evenements.eventmaterial",
            ),
        ),
        migrations.AddField(
            model_name="reservationroom",
            name="consumer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="reservationroom",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="evenements.eventroom"
            ),
        ),
        migrations.AddConstraint(
            model_name="reservationroom",
            constraint=models.UniqueConstraint(
                fields=("event", "date", "start_time", "end_time"),
                name="unique_reservation_room",
            ),
        ),
    ]

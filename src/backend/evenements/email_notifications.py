"""
Module pour la gestion des notifications par email dans l'application Evenements.

Ce module définit des classes pour l'envoie des notifications par email concernant
la création d'événements.
"""

from abc import ABC, abstractmethod

from django.core.mail import EmailMessage
from userspace.models import Group

from .models import Event, EventBus


class SendEventNotification(EmailMessage, ABC):
    """
    Classe de base pour l'envoi de notifications par email lors de la création d'un événement.
    """

    def __init__(self, instance: Event):
        """
        Initialise l'objet avec l'instance de l'événement et configure le sujet,
        l'expéditeur et les destinataires de l'email.

        L'email sera envoyé à tous les utilisateurs du groupe 'consumer'.

        Args:
            instance (Event): L'instance de l'événement contenant les informations nécessaires.
        """
        self.instance = instance
        super().__init__(
            subject=self.instance.description,
            from_email=self.instance.organizer.email,
            to=[
                consumer.email
                for consumer in Group.objects.get(name="consumer").user_set.all()
            ],
        )

    @property
    @abstractmethod
    def email_content(self):
        """
        Propriété abstraite devant être définie dans les sous-classes pour
        spécifier le contenu de l'email.
        """
        pass

    @property
    def email_body_html(self):
        """
        Le corps de l'email.
        """
        return f"""
        <!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
    body {{
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(to right, #6a11cb, #2575fc);
        margin: 0;
        padding: 0;
        text-align: center;
    }}

    .details {{
        text-align: left;
    }}

    .details div {{
        margin-bottom: 20px;
    }}
    .container {{
        background: white;
        max-width: 600px;
        margin: 40px auto;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        text-align: justify;
    }}
    h2 {{
        color: #333;
        font-weight: bold;
        font-size: 24px;
    }}
    p {{
        font-size: 16px;
        color: #555;
        line-height: 1.6;
    }}
    .highlight {{
        font-weight: bold;
        color: #d9534f;
    }}
    .btn {{
    display: inline-block;
    margin-top: 20px;
    padding: 12px 25px;
    background-color: #28a745;
    color: white;
    text-decoration: none;
    font-size: 16px;
    font-weight: bold;
    border-radius: 5px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: background 0.3s ease;
    }}

    .btn:hover {{
        background-color: #218838;
    }}

</style>

            </head>
            <body>

                <div class="container">
                    {self.email_content}
                </div>

            </body>
        </html>
        """

    def send_email(self):
        """
        Méthode pour envoyer l'email.
        """
        self.content_subtype = "html"
        self.body = self.email_body_html
        return super().send()


class SendEventBusNotification(SendEventNotification):
    """Gestion d'envoi d'email lors  de la création d'un événement Bus"""

    def __init__(self, instance: EventBus):
        """Initialise l'object"""
        super().__init__(instance)

    @property
    def email_content(self):
        """Méthode pour renvoyer le contenu du mail"""

        return f"""
        <h2>🚍 Transport pour l'Événement - Sortie de Gala 🎉</h2>
        <p>Nous avons le plaisir de vous informer qu'un bus a été mis à disposition pour
        le transport des participants à l'événement de la sortie de gala.</p>

        <div class="details">
            <div>🪑 <strong>Disponibilité des places :</strong>
            <span class="highlight">{self.instance.available_seats} places</span></div>
            <div>📍 <strong>Lieu de départ :</strong>
            <span class="highlight">{self.instance.departure}</span></div>
            <div>📍 <strong>Destination :</strong>
            <span class="highlight">{self.instance.destination}</span></div>
            <div>🕒 <strong>Heure de départ :</strong>
            <span class="highlight">{self.instance.departure_time}</span></div>
            <div>🕒 <strong>Heure d'arrivée :</strong>
            <span class="highlight">{self.instance.arrival_time}</span></div>
       </div>

        <p>Les places étant limitées, nous vous encourageons à vous inscrire rapidement
        afin de garantir votre place dans le bus. Il s'agit d'un premier arrivé, premier servi !</p>

        <a href="https://reservation.example.com" class="btn">🔗 Réserver ma place</a>

        <p>Pour toute question ou si vous avez besoin de plus d'informations, n'hésitez
        pas à nous contacter.</p>

        <p>Cordialement,</p>
        <p><strong>L'équipe de l'événement</strong></p>
        """

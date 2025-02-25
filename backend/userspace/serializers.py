"""
Module de sérialisation des utilisateurs pour l'application userspace.

Ce module définit un serializer pour le modèle `User`, permettant de
convertir les instances du modèle en représentations JSON et vice-versa.
"""

from rest_framework import serializers
from userspace.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle `User`.

    Ce serializer gère la conversion des instances `User` en JSON
    et la création/mise à jour des utilisateurs en s'assurant que le mot de passe
    est correctement haché.

    Champs sérialisés :
        - `username` (str) : Nom d'utilisateur.
        - `password` (str, write_only) : Mot de passe (non retourné dans les réponses).
        - `email` (str, write_only) : Adresse email (non retournée dans les réponses).
    """

    class Meta:
        """
        Configuration de la sérialisation pour le modèle User.
        """

        model = User
        fields = ["username", "password", "email"]
        extra_kwargs = {"password": {"write_only": True}, "email": {"write_only": True}}

    def create(self, validated_data):
        """
        Crée un nouvel utilisateur avec un mot de passe haché.

        Args:
            validated_data (dict): Données validées du nouvel utilisateur.

        Returns:
            User: Instance du modèle `User` créée.
        """
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        """
        Met à jour un utilisateur en hachant le mot de passe avant sauvegarde.

        Si un mot de passe est fourni dans `validated_data`, il est haché
        avant d'être stocké.

        Args:
            instance (User): Instance existante de `User`.
            validated_data (dict): Données validées pour la mise à jour.

        Returns:
            User: Instance mise à jour du modèle `User`.
        """
        password = validated_data.pop(
            "password", None
        )  # On retire "password" de validated_data
        if password:
            instance.set_password(password)  # Hachage automatique
        return super().update(instance, validated_data)

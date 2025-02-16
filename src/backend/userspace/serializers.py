from rest_framework import serializers
from userspace.models import User


class UserSerializer(serializers.ModelSerializer):
    """Un serializer pour le modèle User"""

    class Meta:
        model = User
        fields = ["username", "password", "email"]
        extra_kwargs = {"password": {"write_only": True}, "email": {"write_only": True}}

    def create(self, validated_data):
        """Creé un nouveau utilisateur"""
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        """
        Hache le mot de passe lors de mise à jour du profil
        avant de sauvegarder l'utilisateur.
        """
        password = validated_data.pop(
            "password", None
        )  # On retire "password" de validated_data
        if password:
            instance.set_password(password)  # Hachage automatique
        return super().update(instance, validated_data)

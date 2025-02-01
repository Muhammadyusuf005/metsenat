from rest_framework import serializers
from .models import UserModel


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for CustomUser model. Handles validation and serialization of user data.
    """

    class Meta:
        model = UserModel
        fields = '__all__'
        read_only_fields = ['id', 'balance','available_balance']


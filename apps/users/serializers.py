from .models import UserModel
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for CustomUser model. Handles validation and serialization of user data.
    """

    class Meta:
        model = UserModel
        fields = '__all__'
        read_only_fields = ['id', 'balance','available_balance']

        def create(self, validated_data):
            if validated_data['role'] == UserModel.UserRole.STUDENT and not self.pk and validated_data['contact_amount'] is None:
                validated_data['balance'] = validated_data['university'].contract_amount
            return super().create(validated_data)




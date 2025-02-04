from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from rest_framework import serializers
from .models import University
from .models import PaymentMethod

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

    def update(self, instance, validated_data):
        if validated_data['contract_amount'] != instance.contract_amount:
            raise serializers.ValidationError({'contrack amount': "Contract amount must be the same."})



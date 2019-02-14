from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from phonenumber_field.serializerfields import PhoneNumberField

from apps.areas.models import ServiceArea


class ServiceAreaSerializer(serializers.ModelSerializer):
    provider_name = serializers.ReadOnlyField(
        source='provider.name'
    )

    class Meta:
        model = ServiceArea
        fields = (
            'id',
            'name',
            'area',
            'price',
            'provider',
            'provider_name',
        )

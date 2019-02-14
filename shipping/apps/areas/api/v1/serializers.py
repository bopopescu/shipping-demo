from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework_gis.fields import GeometryField

from apps.areas.models import ServiceArea


class ServiceAreaSerializer(serializers.ModelSerializer):
    provider_name = serializers.ReadOnlyField(
        source='provider.name'
    )
    area = GeometryField()

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


class QueryAreaSerializer(serializers.Serializer):
    provider_name = serializers.ReadOnlyField(source='provider.name')
    area_name = serializers.ReadOnlyField(source='name')
    area = GeometryField()

    class Meta:
        model = ServiceArea
        fields = (
            'provider_name',
            'area_name',
            'area',
        )

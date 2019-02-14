from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from phonenumber_field.serializerfields import PhoneNumberField
from languages.languages import LANGUAGES


from apps.providers.models import Provider
from django.contrib.auth.models import User

import uuid


class ProviderSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField()
    # language = serializers.ChoiceField(choices=LANGUAGES)
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = Provider
        fields = (
            'name',
            'phone',
            'language',
            'currency',
            'email',
        )

    def create(self, validated_data):
        email = validated_data.pop['email']
        user = User.objects.create_user(
            username=str(uuid.uuid4()),
            email=email,
        )
        return Provider(**validated_data, user=user)

    def update(self, instance, validated_data):
        instance_fields = ['name', 'phone', 'language', 'currency']

        for field_name in instance_fields:
            field_value = validated_data.get(
                field_name, getattr(instance, field_name))
            setattr(instance, field_name, field_value)

        user = instance.user
        user.email = validated_data.get('email', user.email)
        user.save()

        return instance

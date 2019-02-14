from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from languages.fields import LanguageField
from djmoney.models.fields import CurrencyField
from django.contrib.auth.models import User


class Provider(models.Model):
    """Model definition for Provider."""

    name = models.CharField("Provider's name.", max_length=50)
    phone = PhoneNumberField("Provider's phone number.")
    language = LanguageField("Provider's language.")
    currency = CurrencyField("Provider's currency.")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """Unicode representation of Provider."""
        return self.name

from django.contrib.gis.db import models
from providers.models import Provider
from djmoney.models.fields import MoneyField


class ServiceArea(models.Model):
    """This represents an area in which a Provider offers services."""

    name = models.CharField("Area name.", max_length=50)
    area = models.PolygonField()
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        """Unicode representation of ServiceArea."""
        return self.name

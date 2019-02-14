from rest_framework import generics, status, viewsets, filters, mixins
from rest_framework.permissions import IsAdminUser

from apps.providers.api.v1.serializers import ProviderSerializer
from apps.providers.models import Provider


class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()

    permission_classes = (IsAdminUser,)

from rest_framework import generics, status, viewsets, filters, mixins

from apps.areas.api.v1.serializers import ServiceAreaSerializer
from apps.areas.api.v1.permissions import IsAuthorized
from apps.areas.models import ServiceArea


class ServiceAreaViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()

    permission_classes = (IsAuthorized,)

from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework import generics, status, views, viewsets, filters, mixins

from apps.areas.api.v1.serializers import ServiceAreaSerializer, QueryAreaSerializer
from apps.areas.api.v1.permissions import IsAuthorized
from apps.areas.api.v1.filters import PointFilter
from apps.areas.models import ServiceArea


class ServiceAreaViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()

    permission_classes = (IsAuthorized,)


class FilteredAreaList(generics.ListAPIView):

    queryset = ServiceArea.objects.all()
    serializer_class = QueryAreaSerializer
    filter_backends = (PointFilter, )

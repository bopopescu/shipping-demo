
from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from apps.areas.models import ServiceArea


class PointFilter(GeoFilterSet):
    contains_point = GeometryFilter(name='area', lookup_expr='contains')

    class Meta:
        model = ServiceArea
        fields = ('contains_point',)

"""shipping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers

from apps.areas.api.v1 import views as api_v1_areas
from apps.providers.api.v1 import views as api_v1_providers


router = routers.DefaultRouter()

router.register(
    'api/v1/areas',
    api_v1_areas.ServiceAreaViewSet,
    'area',
)

router.register(
    'api/v1/providers',
    api_v1_providers.ProviderViewSet,
    'provider',
)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/v1/areas/filtered/', api_v1_areas.FilteredAreaList.as_view())
]

urlpatterns += router.urls

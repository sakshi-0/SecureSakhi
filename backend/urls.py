from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from alerts.views import AlertViewSet
from incidents.views import IncidentViewSet
from hotspots.views import HotspotViewSet

router = routers.DefaultRouter()
router.register(r'alerts', AlertViewSet)
router.register(r'incidents', IncidentViewSet)
router.register(r'hotspots', HotspotViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', TemplateView.as_view(template_name='index.html')),  # Serve the React app
]

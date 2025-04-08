from rest_framework import viewsets
from .models import Hotspot
from .serializers import HotspotSerializer

class HotspotViewSet(viewsets.ModelViewSet):
    queryset = Hotspot.objects.all().order_by('-incidents_count')
    serializer_class = HotspotSerializer 
from rest_framework import serializers
from .models import Hotspot

class HotspotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotspot
        fields = ['id', 'location', 'risk_level', 'incidents_count', 'last_updated', 'description'] 
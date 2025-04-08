from rest_framework import serializers
from .models import Incident
import logging

logger = logging.getLogger(__name__)

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ['id', 'location', 'incident_type', 'description', 'date_time', 
                 'severity', 'latitude', 'longitude', 'reported_at']
        read_only_fields = ['id', 'reported_at']

    def validate(self, data):
        logger.info(f"Validating incident data: {data}")
        
        try:
            # Validate required fields
            required_fields = ['location', 'incident_type', 'description', 'date_time', 'latitude', 'longitude']
            for field in required_fields:
                if not data.get(field):
                    raise serializers.ValidationError({field: f"{field} is required"})

            # Validate latitude
            try:
                lat = float(data.get('latitude', 0))
                if not -90 <= lat <= 90:
                    raise serializers.ValidationError({"latitude": "Latitude must be between -90 and 90"})
                data['latitude'] = lat
            except (TypeError, ValueError):
                raise serializers.ValidationError({"latitude": "Invalid latitude value"})

            # Validate longitude
            try:
                lon = float(data.get('longitude', 0))
                if not -180 <= lon <= 180:
                    raise serializers.ValidationError({"longitude": "Longitude must be between -180 and 180"})
                data['longitude'] = lon
            except (TypeError, ValueError):
                raise serializers.ValidationError({"longitude": "Invalid longitude value"})

            # Validate incident type
            if data.get('incident_type') not in dict(Incident.INCIDENT_TYPES):
                raise serializers.ValidationError({"incident_type": "Invalid incident type"})

            # Validate severity
            if data.get('severity') not in dict(Incident.SEVERITY_LEVELS):
                data['severity'] = 'Medium'  # Set default if invalid

            logger.info("Validation successful")
            return data
        except Exception as e:
            logger.error(f"Validation error: {str(e)}")
            raise 
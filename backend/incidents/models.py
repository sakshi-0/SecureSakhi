from django.db import models

class Incident(models.Model):
    INCIDENT_TYPES = (
        ('Harassment', 'Harassment'),
        ('Stalking', 'Stalking'),
        ('Theft', 'Theft'),
        ('Assault', 'Assault'),
        ('Suspicious Activity', 'Suspicious Activity'),
        ('Other', 'Other')
    )

    SEVERITY_LEVELS = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    )

    location = models.CharField(max_length=255)
    incident_type = models.CharField(max_length=50, choices=INCIDENT_TYPES)
    description = models.TextField()
    date_time = models.DateTimeField()
    severity = models.CharField(max_length=50, choices=SEVERITY_LEVELS, default='Medium')
    latitude = models.FloatField()
    longitude = models.FloatField()
    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'incidents_incident'
        ordering = ['-reported_at']

    def __str__(self):
        return f"{self.incident_type} at {self.location} ({self.date_time})"

    def save(self, *args, **kwargs):
        # First save the incident
        super().save(*args, **kwargs)
        
        # Then update the hotspot
        from hotspots.models import Hotspot
        hotspot, created = Hotspot.objects.get_or_create(
            location=self.location,
            defaults={
                'risk_level': 'Low',
                'description': f'Location with reported {self.incident_type}'
            }
        )
        hotspot.incidents_count += 1
        
        # Update risk level based on incident count
        if hotspot.incidents_count > 10:
            hotspot.risk_level = 'High'
        elif hotspot.incidents_count > 5:
            hotspot.risk_level = 'Medium'
            
        hotspot.save() 
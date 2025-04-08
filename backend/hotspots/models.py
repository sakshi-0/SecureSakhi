from django.db import models

class Hotspot(models.Model):
    RISK_LEVELS = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    )

    location = models.CharField(max_length=255)
    risk_level = models.CharField(max_length=50, choices=RISK_LEVELS, default='Low')
    incidents_count = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    description = models.TextField()

    class Meta:
        db_table = 'hotspots_hotspot'
        ordering = ['-incidents_count']

    def __str__(self):
        return f"{self.location} - {self.risk_level} Risk ({self.incidents_count} incidents)" 
from django.db import models

class Alert(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Active')

    class Meta:
        app_label = 'alerts'

    def __str__(self):
        return f"Alert at {self.location} - {self.status}" 
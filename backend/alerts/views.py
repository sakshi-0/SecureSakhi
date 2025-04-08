from rest_framework import viewsets
from rest_framework.response import Response
from alerts.models import Alert
from alerts.serializers import AlertSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all().order_by('-timestamp')
    serializer_class = AlertSerializer
    
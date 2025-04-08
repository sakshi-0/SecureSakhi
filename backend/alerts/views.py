from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from alerts.models import Alert
from alerts.serializers import AlertSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all().order_by('-timestamp')
    serializer_class = AlertSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status']
    search_fields = ['location']
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get only active alerts"""
        active_alerts = Alert.objects.filter(status='Active').order_by('-timestamp')
        serializer = self.get_serializer(active_alerts, many=True)
        return Response(serializer.data)
    
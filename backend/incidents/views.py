from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Incident
from .serializers import IncidentSerializer
import logging
import traceback

logger = logging.getLogger(__name__)

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all().order_by('-reported_at')
    serializer_class = IncidentSerializer

    def create(self, request, *args, **kwargs):
        try:
            logger.info(f"Received incident report data: {request.data}")
            serializer = self.get_serializer(data=request.data)
            
            if serializer.is_valid():
                logger.info("Data validation successful")
                try:
                    incident = serializer.save()
                    logger.info(f"Successfully created incident with ID: {incident.id}")
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except Exception as save_error:
                    logger.error(f"Error saving incident: {str(save_error)}")
                    logger.error(f"Traceback: {traceback.format_exc()}")
                    return Response(
                        {"error": "Failed to save incident", "details": str(save_error)},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                logger.error(f"Validation error: {serializer.errors}")
                return Response(
                    {"error": "Invalid data", "details": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            logger.error(f"Traceback: {traceback.format_exc()}")
            return Response(
                {"error": "Failed to create incident", "details": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            ) 
from rest_framework.viewsets import ModelViewSet

from .serializers import AppointmentSerializer
from .models import Appointment


class AppointmentViewSet(ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

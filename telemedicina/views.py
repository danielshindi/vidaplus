from rest_framework import viewsets
from telemedicina.models import Teleconsulta
from .serializers import TeleconsultaSerializer

class TeleconsultaViewSet(viewsets.ModelViewSet):
    queryset = Teleconsulta.objects.all()
    serializer_class = TeleconsultaSerializer
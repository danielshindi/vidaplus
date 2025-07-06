from rest_framework import viewsets
from telemedicina.models import Teleconsulta
from .serializers import TeleconsultaSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsPacienteOrProfissional

class TeleconsultaViewSet(viewsets.ModelViewSet):
    queryset = Teleconsulta.objects.all()
    serializer_class = TeleconsultaSerializer
    permission_classes = [IsAuthenticated, IsPacienteOrProfissional]
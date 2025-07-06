from rest_framework import viewsets
from agendamentos.models import Consulta
from .serializers import ConsultaSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministradorOrProfissional

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated, IsAdministradorOrProfissional]
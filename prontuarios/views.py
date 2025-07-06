from rest_framework import viewsets
from prontuarios.models import Prontuario
from .serializers import ProntuarioSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministradorOrProfissional

class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer
    permission_classes = [IsAuthenticated, IsAdministradorOrProfissional]
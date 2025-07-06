from rest_framework import viewsets
from telemedicina.models import Teleconsulta
from .serializers import TeleconsultaSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsPacienteOrProfissional

class TeleconsultaViewSet(viewsets.ModelViewSet):
    queryset = Teleconsulta.objects.all()
    serializer_class = TeleconsultaSerializer
    permission_classes = [IsAuthenticated, IsPacienteOrProfissional]

    def get_queryset(self):
        user = self.request.user
        if user.perfil.nome_perfil == 'Paciente':
            return Teleconsulta.objects.filter(paciente__usuario=user)
        elif user.perfil.nome_perfil == 'Profissional de Saúde':
            return Teleconsulta.objects.filter(profissional__usuario=user)
        return Teleconsulta.objects.none()
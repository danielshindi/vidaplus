from rest_framework import viewsets
from prontuarios.models import Prontuario
from .serializers import ProntuarioSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministradorOrProfissional

class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer
    permission_classes = [IsAuthenticated, IsAdministradorOrProfissional]

    def get_queryset(self):
        user = self.request.user
        if user.perfil.nome_perfil == 'Paciente':
            return Prontuario.objects.filter(paciente__usuario=user)
        elif user.perfil.nome_perfil == 'Profissional de Saúde':
            return Prontuario.objects.filter(paciente__isnull=False)
        return Prontuario.objects.none()
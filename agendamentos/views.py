from rest_framework import viewsets, filters
from agendamentos.models import Consulta
from .serializers import ConsultaSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministradorOrProfissional

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated, IsAdministradorOrProfissional]
    filter_backends = [filters.SearchFilter]
    search_fields = ['paciente__usuario__nome_completo', 'profissional__usuario__nome_completo']

    def get_queryset(self):
        user = self.request.user
        if user.perfil.nome_perfil == 'Paciente':
            return Consulta.objects.filter(paciente__usuario=user)
        elif user.perfil.nome_perfil == 'Profissional de Saúde':
            return Consulta.objects.filter(profissional__usuario=user)
        return super().get_queryset()
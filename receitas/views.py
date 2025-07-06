from rest_framework import viewsets

from receitas.models import Receita
from .serializers import ReceitaSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsProfissionalSaude

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    permission_classes = [IsAuthenticated, IsProfissionalSaude]

    def get_queryset(self):
        user = self.request.user
        if user.perfil.nome_perfil == 'Paciente':
            return Receita.objects.filter(paciente__usuario=user)
        elif user.perfil.nome_perfil == 'Profissional de Saúde':
            return Receita.objects.filter(profissional__usuario=user)
        return Receita.objects.none()
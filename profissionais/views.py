from rest_framework import viewsets
from profissionais.models import ProfissionalSaude
from .serializers import ProfissionalSaudeSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministrador

class ProfissionalSaudeViewSet(viewsets.ModelViewSet):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

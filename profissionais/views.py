from rest_framework import viewsets
from profissionais.models import ProfissionalSaude
from .serializers import ProfissionalSaudeSerializer

class ProfissionalSaudeViewSet(viewsets.ModelViewSet):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer
from rest_framework import viewsets
from auditoria.models import LogEntry
from .serializers import LogEntrySerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministrador

class LogEntryViewSet(viewsets.ModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    permission_classes = [IsAuthenticated, IsAdministrador]
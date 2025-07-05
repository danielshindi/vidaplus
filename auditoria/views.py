from rest_framework import viewsets
from auditoria.models import LogEntry
from .serializers import LogEntrySerializer

class LogEntryViewSet(viewsets.ModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer

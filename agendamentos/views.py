from rest_framework import viewsets, filters
from agendamentos.models import Consulta, Paciente
from .serializers import ConsultaSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsPacienteOrAdminOrProfissional
from auditoria.utils import registrar_log
from django.shortcuts import get_object_or_404

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all().select_related('paciente__usuario', 'profissional__usuario')
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated, IsPacienteOrAdminOrProfissional]
    filter_backends = [filters.SearchFilter]
    search_fields = ['status']

    def get_queryset(self):
        perfil = getattr(self.request.user.perfil, "nome_perfil", "").lower()
        if perfil == "paciente":
            return Consulta.objects.filter(paciente__usuario=self.request.user)
        return super().get_queryset()
    
    def perform_create(self, serializer):
        perfil = getattr(self.request.user.perfil, "nome_perfil", "").lower()

        if perfil == "paciente":
            paciente = get_object_or_404(Paciente, usuario=self.request.user)
            serializer.save(paciente=paciente)
        else:
            serializer.save()

        instance = serializer.instance
        registrar_log(
            usuario=self.request.user,
            acao='criar',
            entidade='Consulta',
            id_entidade=instance.id,
            descricao=f'Consulta criada para o paciente {instance.paciente} com o profissional {instance.profissional}.'
        )

    def perform_update(self, serializer):
        instance = self.get_object()  # Consulta antes da atualização
        dados_antigos = {field: getattr(instance, field) for field in serializer.fields}
        instance = serializer.save()  # Salva e atualiza os dados
        dados_novos = {field: getattr(instance, field) for field in serializer.fields}

        alteracoes = []
        for campo in dados_antigos:
            if dados_antigos[campo] != dados_novos[campo]:
                alteracoes.append(f"{campo}: '{dados_antigos[campo]}' → '{dados_novos[campo]}'")

        descricao = "Atualização da Consulta.\n" + "\n".join(alteracoes) if alteracoes else "Atualização sem mudanças detectadas."

        registrar_log(self.request.user, 'atualizar', 'Consulta', instance.id, descricao)


    def perform_destroy(self, instance):
        registrar_log(self.request.user, 'remover', 'Consulta', instance.id, 'Consulta cancelada.')
        instance.delete()
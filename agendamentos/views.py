from rest_framework import viewsets, filters
from agendamentos.models import Consulta
from .serializers import ConsultaSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministradorOrProfissional
from auditoria.utils import registrar_log

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
    
    def perform_create(self, serializer):
        instance = serializer.save()
        registrar_log(
            usuario=self.request.user,
            acao='criar',
            entidade='Consulta',
            id_entidade=instance.id,
            descricao=f'Consulta do paciente {instance.paciente.usuario.nome_completo} marcada com o profissional {instance.profissional.usuario.nome_completo} em {instance.data_hora}'
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
        registrar_log(self.request.user, 'remover', 'Consulta', instance.id, 'Consulta removida.')
        instance.delete()
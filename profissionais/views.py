from rest_framework import viewsets
from profissionais.models import ProfissionalSaude
from .serializers import ProfissionalSaudeSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministrador
from auditoria.utils import registrar_log


class ProfissionalSaudeViewSet(viewsets.ModelViewSet):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

    def perform_create(self, serializer):
        instance = serializer.save()
        registrar_log(
            usuario=self.request.user,
            acao='criar',
            entidade='ProfissionalSaude',
            id_entidade=instance.id,
            descricao=f'Profissional de saúde {instance} registrado.'
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

        descricao = "Atualização de ProfissionalSaude.\n" + "\n".join(alteracoes) if alteracoes else "Atualização sem mudanças detectadas."

        registrar_log(self.request.user, 'atualizar', 'ProfissionalSaude', instance.id, descricao)


    def perform_destroy(self, instance):
        registrar_log(self.request.user, 'remover', 'ProfissionalSaude', instance.id, 'ProfissionalSaude removido.')
        instance.delete()
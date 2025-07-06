from rest_framework import viewsets
from telemedicina.models import Teleconsulta
from .serializers import TeleconsultaSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsPacienteOrProfissional
from auditoria.utils import registrar_log


class TeleconsultaViewSet(viewsets.ModelViewSet):
    queryset = Teleconsulta.objects.all()
    serializer_class = TeleconsultaSerializer
    permission_classes = [IsAuthenticated, IsPacienteOrProfissional]

    def get_queryset(self):
        user = self.request.user
        if user.perfil.nome_perfil == 'Paciente':
            return Teleconsulta.objects.filter(paciente__usuario=user)
        elif user.perfil.nome_perfil == 'Profissional de Saúde':
            return Teleconsulta.objects.filter(profissional__usuario=user)
        return Teleconsulta.objects.none()
    
    def perform_create(self, serializer):
        instance = serializer.save()
        registrar_log(
            usuario=self.request.user,
            acao='criar',
            entidade='Teleconsulta',
            id_entidade=instance.id,
            descricao=f'Teleconsulta {instance} criada.'
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

        descricao = "Atualização da Teleconsulta.\n" + "\n".join(alteracoes) if alteracoes else "Atualização sem mudanças detectadas."

        registrar_log(self.request.user, 'atualizar', 'Teleconsulta', instance.id, descricao)


    def perform_destroy(self, instance):
        registrar_log(self.request.user, 'remover', 'Teleconsulta', instance.id, 'Teleconsulta removida.')
        instance.delete()
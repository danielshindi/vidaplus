from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from prontuarios.models import Prontuario, Paciente
from .serializers import ProntuarioSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministradorOrProfissional, IsProfissionalSaude
from auditoria.utils import registrar_log


class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer
    permission_classes = [IsAuthenticated, IsAdministradorOrProfissional]

    def get_queryset(self):
        user = self.request.user
        if user.perfil.nome_perfil == 'Paciente':
            return Prontuario.objects.filter(paciente__usuario=user)
        elif user.perfil.nome_perfil == 'Profissional de Saúde':
            return Prontuario.objects.filter(paciente__isnull=False)
        return Prontuario.objects.none()
    
    def perform_create(self, serializer):
        instance = serializer.save()
        registrar_log(
            usuario=self.request.user,
            acao='criar',
            entidade='Prontuario',
            id_entidade=instance.id,
            descricao=f'{instance} criado.'
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

        descricao = "Atualização do Prontuario.\n" + "\n".join(alteracoes) if alteracoes else "Atualização sem mudanças detectadas."

        registrar_log(self.request.user, 'atualizar', 'Prontuario', instance.id, descricao)


    def perform_destroy(self, instance):
        registrar_log(self.request.user, 'remover', 'Prontuario', instance.id, 'Prontuario removido.')
        instance.delete()


class HistoricoMedicoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        usuario = request.user
        paciente_id = request.query_params.get('paciente_id')

        if hasattr(usuario, 'paciente'):
            paciente = usuario.paciente
        elif hasattr(usuario, 'profissionalsaude'):
            if not paciente_id:
                return Response({'erro': 'É necessário informar paciente_id.'}, status=400)
            try:
                paciente = Paciente.objects.get(id=paciente_id)
            except Paciente.DoesNotExist:
                return Response({'erro': 'Paciente não encontrado.'}, status=404)
        else:
            return Response({'erro': 'Usuário sem permissão para acessar prontuários.'}, status=403)

        prontuarios = Prontuario.objects.filter(paciente=paciente)
        serializer = ProntuarioSerializer(prontuarios, many=True)
        return Response(serializer.data)
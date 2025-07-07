from rest_framework import serializers
from pacientes.models import Paciente
from usuarios.models import Usuario
from usuarios.serializers import UsuarioWriteSerializer

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class PacienteCompletoSerializer(serializers.ModelSerializer):
    usuario = UsuarioWriteSerializer()

    class Meta:
        model = Paciente
        fields = ['id', 'usuario', 'genero', 'convenio']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create_user(**usuario_data)
        return Paciente.objects.create(usuario=usuario, **validated_data)

    def update(self, instance, validated_data):
        usuario_data = validated_data.pop('usuario', None)

        if usuario_data:
            usuario_serializer = UsuarioWriteSerializer(
                instance=instance.usuario,
                data=usuario_data,
                partial=True
            )
            usuario_serializer.is_valid(raise_exception=True)
            usuario_serializer.save()

        # Atualiza os demais campos do paciente
        return super().update(instance, validated_data)
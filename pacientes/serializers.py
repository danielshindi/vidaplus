from rest_framework import serializers
from pacientes.models import Paciente
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class PacienteCompletoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Paciente
        fields = ['usuario', 'genero', 'convenio']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create_user(**usuario_data)
        return Paciente.objects.create(usuario=usuario, **validated_data)

    def update(self, instance, validated_data):
        usuario_data = validated_data.pop('usuario', {})
        usuario_serializer = UsuarioSerializer(instance.usuario, data=usuario_data, partial=True)
        if usuario_serializer.is_valid(raise_exception=True):
            usuario_serializer.save()
        return super().update(instance, validated_data)
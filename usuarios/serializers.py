from rest_framework import serializers

from usuarios.models import Usuario, PerfilUsuario

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'matricula', 'nome_completo', 'email', 'cpf', 'telefone', 'nascimento', 'endereco', 'ativo', 'perfil']


class UsuarioWriteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        exclude = ['last_login', 'groups', 'user_permissions']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario.objects.create_user(**validated_data, password=password)
        return user

    def validate_matricula(self, value):
        if self.instance:
            # Permite a mesma matrícula ao atualizar o mesmo usuário
            if self.instance.matricula == value:
                return value
            if Usuario.objects.exclude(id=self.instance.id).filter(matricula=value).exists():
                raise serializers.ValidationError("Já existe um usuário com essa matrícula.")
        else:
            if Usuario.objects.filter(matricula=value).exists():
                raise serializers.ValidationError("Já existe um usuário com essa matrícula.")
        return value

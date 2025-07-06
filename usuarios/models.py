from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class PerfilUsuario(models.Model):
    nome_perfil = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_perfil

class Permissao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class PerfilPermissao(models.Model):
    perfil = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    permissao = models.ForeignKey(Permissao, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('perfil', 'permissao')

class UsuarioManager(BaseUserManager):
    def create_user(self, matricula, password=None, **extra_fields):
        required_fields = ['nome_completo', 'email', 'cpf', 'telefone', 'nascimento', 'endereco']
        for field in required_fields:
            if not extra_fields.get(field):
                raise ValueError(f'O campo {field} é obrigatório.')

        if not matricula:
            raise ValueError('A matrícula é obrigatória.')

        user = self.model(matricula=matricula, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, matricula, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(matricula, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    matricula = models.CharField(max_length=7, unique=True)
    nome_completo = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    telefone = models.CharField(max_length=20, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)
    endereco = models.CharField(max_length=255, null=False, blank=False)
    ativo = models.BooleanField(default=True)
    perfil = models.ForeignKey(PerfilUsuario, on_delete=models.SET_NULL, null=True)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'matricula'
    REQUIRED_FIELDS = ['email', 'nome_completo', 'cpf', 'telefone', 'nascimento', 'endereco']

    objects = UsuarioManager()

    def __str__(self):
        return self.matricula

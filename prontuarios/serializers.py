from rest_framework import serializers
from prontuarios.models import Prontuario

class ProntuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prontuario
        fields = '__all__'
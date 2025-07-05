from rest_framework import serializers
from internacoes.models import Internacao, Leito

class InternacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internacao
        fields = '__all__'


class LeitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leito
        fields = '__all__'
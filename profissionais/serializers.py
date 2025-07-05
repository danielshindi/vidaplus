from rest_framework import serializers
from profissionais.models import ProfissionalSaude

class ProfissionalSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissionalSaude
        fields = '__all__'

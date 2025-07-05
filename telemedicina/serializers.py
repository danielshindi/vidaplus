from rest_framework import serializers
from telemedicina.models import Teleconsulta

class TeleconsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teleconsulta
        fields = '__all__'
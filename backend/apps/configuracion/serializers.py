from rest_framework import serializers
from .models import Configuracion


class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = ('id', 'numero_sensores')
        read_only_fields = ('id',)
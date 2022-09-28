from rest_framework import serializers
from .models import Modulo
from apps.sensor.serializers import SensorSerializer
from apps.sensor.models import Sensor


class ModuloSerializer(serializers.ModelSerializer):
    sensores = SensorSerializer(many=True)
    
    class Meta:
        model = Modulo
        fields = '__all__'
        read_only_fields = ('id',)
        
    def create(self, validated_data):
        sensores = validated_data.pop('sensores')
        modulo = Modulo.objects.create(**validated_data)
        if sensores:
            Sensor.objects.bulk_create(
                [Sensor(modulo=modulo, **sensor) for sensor in sensores]
            )
        return modulo
    
        
from rest_framework import serializers
from .models import Dato


class DatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dato
        fields = '__all__'
        read_only_fields = ('id',)
        
    def create(self, validated_data):
        print(validated_data)
        raise serializers.ValidationError('Nel perro')
        return super().create(validated_data)
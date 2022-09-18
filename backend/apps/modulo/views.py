from rest_framework.viewsets import ModelViewSet
from .serializers import ModuloSerializer
from .models import Modulo


class ModuloViewSet(ModelViewSet):
    serializer_class = ModuloSerializer
    queryset = Modulo.objects.all()
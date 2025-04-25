from rest_framework.viewsets import ModelViewSet
from garagem_app.models import Modelo
from garagem_app.serializers import ModeloSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
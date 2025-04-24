from garagem_app.models import Acessorio
from garagem_app.serializers import AcessorioSerializer
from rest_framework.viewsets import ModelViewSet

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer
from garagem_app.models import Veiculo
from garagem_app.serializers import VeiculoSerializer
from rest_framework.viewsets import ModelViewSet

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
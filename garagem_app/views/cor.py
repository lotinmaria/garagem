from garagem_app.models import Cor
from garagem_app.serializers import CorSerializer
from rest_framework.viewsets import ModelViewSet

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer
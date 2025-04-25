from rest_framework.serializers import ModelSerializer
from garagem_app.models import Modelo

class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'
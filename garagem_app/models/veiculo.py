from django.db import models
from garagem_app.models import Cor, Modelo, Acessorio

class Veiculo(models.Model):
    ano = models.IntegerField(default=0, blank=True, null=True)
    preco = models.DecimalField(default=0, max_digits=10, decimal_places=2, blank=True, null=True)
    acessorio = models.ManyToManyField(Acessorio,  null=True, blank=True)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE, null=True, blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.id} - {self.modelo.nome} - {self.cor.nome} - {self.ano}'
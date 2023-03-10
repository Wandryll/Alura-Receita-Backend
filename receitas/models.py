from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

class Receita(models.Model):
    pessoa = models.ForeignKey(to=Pessoa, on_delete=models.SET_NULL, null=True, blank=False)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        return  self.nome_receita
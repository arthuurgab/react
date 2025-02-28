from django.db import models
from auxiliares.models import tipoDespesa, tipoPrioridade

class Despesa(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.IntegerField()
    tipo = models.ForeignKey(tipoDespesa, on_delete=models.CASCADE)
    prioridade = models.ForeignKey(tipoPrioridade, on_delete=models.CASCADE)
    paga = models.BooleanField(default=False)
    data = models.DateField()

    class Meta:
        verbose_name = "Despesa"
        verbose_name_plural = "Despesas"

    def __str__(self):
        return f"{self.nome} - R$ {self.valor}"
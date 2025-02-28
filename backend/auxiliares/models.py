from django.db import models

class tipoDespesa(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class tipoPrioridade(models.Model):
    nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome

class tipoObjetivo(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
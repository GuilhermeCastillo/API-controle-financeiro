from django.db import models


class Receita(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=200, unique=True)
    valor = models.FloatField()
    data = models.DateField()

    def __str__(self):
        return self.descricao

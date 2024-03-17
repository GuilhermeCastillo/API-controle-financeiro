from django.db import models


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.descricao


class Despesa(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        default=8,
        blank=True,
        related_name="despesas",
    )
    descricao = models.CharField(max_length=200, unique=True)
    valor = models.FloatField()
    data = models.DateField()

    def __str__(self):
        return self.descricao

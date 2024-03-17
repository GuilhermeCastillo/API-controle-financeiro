from rest_framework import serializers
from despesas.models import Despesa


class DespesaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = ["descricao", "valor", "data", "categoria"]

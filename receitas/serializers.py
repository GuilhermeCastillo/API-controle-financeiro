from rest_framework import serializers
from receitas.models import Receita

class ReceitaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ["descricao", "valor", "data"]
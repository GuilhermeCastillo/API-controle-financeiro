from receitas.models import Receita
from rest_framework import generics
from receitas.serializers import ReceitaModelSerializer


class ReceitaCreateListView(generics.ListCreateAPIView):
    serializer_class = ReceitaModelSerializer

    def get_queryset(self):
        queryset = Receita.objects.all()
        descricao = self.request.query_params.get("descricao")

        if descricao is not None:
            queryset = queryset.filter(descricao=descricao)

        return queryset


class ReceitaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaModelSerializer

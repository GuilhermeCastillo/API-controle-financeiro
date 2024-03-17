from despesas.models import Despesa
from rest_framework import generics
from despesas.serializers import DespesaModelSerializer


class DespesaCreateListView(generics.ListCreateAPIView):
    serializer_class = DespesaModelSerializer

    def get_queryset(self):
        queryset = Despesa.objects.all()
        descricao = self.request.query_params.get("descricao")

        if descricao is not None:
            queryset = queryset.filter(descricao=descricao)

        return queryset


class DespesaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaModelSerializer

from despesas.models import Despesa
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from despesas.serializers import DespesaModelSerializer


class DespesaCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DespesaModelSerializer

    def get_queryset(self):
        queryset = Despesa.objects.all()
        descricao = self.request.query_params.get("descricao")
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")

        if descricao is not None:
            queryset = queryset.filter(descricao=descricao)

        if (year is not None) and (month is not None):
            queryset = Despesa.objects.filter(data__year=year, data__month=month)

        return queryset


class DespesaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Despesa.objects.all()
    serializer_class = DespesaModelSerializer

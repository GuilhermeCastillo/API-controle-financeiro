from receitas.models import Receita
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from receitas.serializers import ReceitaModelSerializer


class ReceitaCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReceitaModelSerializer

    def get_queryset(self):
        queryset = Receita.objects.all()
        descricao = self.request.query_params.get("descricao")
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")

        if descricao is not None:
            queryset = queryset.filter(descricao=descricao)

        if (year is not None) and (month is not None):
            queryset = Receita.objects.filter(data__year=year, data__month=month)

        return queryset


class ReceitaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Receita.objects.all()
    serializer_class = ReceitaModelSerializer

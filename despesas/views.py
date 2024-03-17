from despesas.models import Despesa
from rest_framework import generics
from despesas.serializers import DespesaModelSerializer


class DespesaCreateListView(generics.ListCreateAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaModelSerializer


class DespesaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaModelSerializer

from receitas.models import Receita
from rest_framework import generics
from receitas.serializers import ReceitaModelSerializer

class ReceitaCreateListView(generics.ListCreateAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaModelSerializer
    
class ReceitaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaModelSerializer
from django.db.models import Count, Sum
from rest_framework import views, response
from receitas.models import Receita
from despesas.models import Despesa, Categoria


class ResumoView(views.APIView):

    def get(self, request, year, month):

        sum_receitas = Receita.objects.filter(
            data__year=year, data__month=month
        ).aggregate(valor_total_receitas=Sum("valor"))["valor_total_receitas"]
        sum_despesas = Despesa.objects.filter(
            data__year=year, data__month=month
        ).aggregate(valor_total_despesas=Sum("valor"))["valor_total_despesas"]
        saldo_final = sum_receitas - sum_despesas

        valor_gasto_categoria = {}

        for i in range(1, 9):
            valor_gasto = Despesa.objects.filter(
                data__year=year, data__month=month, categoria=i
            ).aggregate(valor_gasto=Sum("valor"))["valor_gasto"]
            categoria = Categoria.objects.get(pk=i)
            valor_gasto_categoria[categoria.descricao] = (
                valor_gasto if valor_gasto is not None else 0
            )

        return response.Response(
            data={
                "valor_total_receitas": sum_receitas,
                "valor_total_despesas": sum_despesas,
                "saldo_final": saldo_final,
                "valor_gasto_categoria": valor_gasto_categoria,
            }
        )

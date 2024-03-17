from django.contrib import admin
from receitas.models import Receita


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = "id", "descricao", "valor", "data"

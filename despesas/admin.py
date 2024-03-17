from django.contrib import admin
from despesas.models import Despesa, Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = "id", "descricao"


@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = "id", "categoria", "descricao", "valor", "data"

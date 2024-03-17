from django.urls import path
from . import views

urlpatterns = [
    path("receitas/", views.ReceitaCreateListView.as_view(), name="receita"),
    path(
        "receitas/<int:pk>/",
        views.ReceitaRetrieveUpdateDestroyView.as_view(),
        name="receita-detail-view",
    ),
    path(
        "receitas/<int:year>/<int:month>/",
        views.ReceitaCreateListView.as_view(),
        name="receita-detail-date",
    ),
]

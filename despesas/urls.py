from django.urls import path
from . import views

urlpatterns = [
    path("despesas/", views.DespesaCreateListView.as_view(), name="receita"),
    path(
        "despesas/<int:pk>/",
        views.DespesaRetrieveUpdateDestroyView.as_view(),
        name="receita-detail-view",
    ),
    path(
        "despesas/<int:year>/<int:month>/",
        views.DespesaCreateListView.as_view(),
        name="despesa-detail-date",
    ),
]

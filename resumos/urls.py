from django.urls import path
from .views import ResumoView

urlpatterns = [
    path(
        "resumo/<int:year>/<int:month>/",
        ResumoView.as_view(),
        name="resumo-detail-date",
    )
]

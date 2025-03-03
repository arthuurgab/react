from django.urls import path
from . import views

app_name = 'despesas'

urlpatterns = [
    path('despesas/', views.DespesaListAPIView.as_view(), name='despesa-list'),
]
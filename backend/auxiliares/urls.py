from django.urls import path
from . import views

urlpatterns = [
    path('tipo-despesa/', views.tipoDespesaApiOverview, name='tipo-despesa-view'),
    path('tipo-prioridade/', views.tipoPrioridadeApiOverview, name='tipo-prioridade-view'),
    path('tipo-despesa/create/', views.tipoDespesaCreate, name='tipo-despesa-create'),

    path('tipo-despesa/all/', views.tipoDespesaView, name='tipo-despesa-view'),
    path('tipo-prioridade/all/', views.tipoPrioridadeView, name='tipo-prioridade-view'),
]
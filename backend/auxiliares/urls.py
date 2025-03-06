from django.urls import path
from . import views

urlpatterns = [
    path('', views.tipoDespesaApiOverview, name='home'),
    path('all/', views.tipoDespesaView, name='tipo-despesa-view'),

]
from django.urls import path
from . import views

app_name = 'despesas'

urlpatterns = [
    path('', views.despesaApiOverview, name='home'),
    path('create/', views.add_depesas, name='add-despesa'),
    path('all/', views.view_despesas, name='view-despesa')
]
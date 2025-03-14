from django.urls import path
from . import views

app_name = 'despesas'

urlpatterns = [
    path('', views.despesaApiOverview, name='home'),
    path('create/', views.add_depesas, name='add-despesa'),
    path('all/', views.view_despesas, name='view-despesa'),
    path('<int:pk>/delete/', views.delete_despesa, name='delete-despesa'),
    path('update/<int:pk>/', views.update_despesa, name='update-despesa')
]
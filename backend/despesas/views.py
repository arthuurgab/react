from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Despesa
from .serializers import DespesaSerializer 
from django.shortcuts import get_object_or_404

@api_view(['GET']) # Define que essa função só pode ser acessa através do metodo GET
def despesaApiOverview(request):
    api_urls = {
        'all_despesas': '/',
        'Add': '/create',
        'Update': '/update/id',
        'Delete': '/despesa/id/delete'
    } 
    return Response(api_urls)

@api_view(['POST']) # Define que essa função só pode ser acessa através do metodo POST
def add_depesas(request):
    despesa = DespesaSerializer(data=request.data)
    if Despesa.objects.filter(**request.data).exists(): # Verifica se o objeto já existe
        raise serializers.ValidationError("Essa despesa já existe!", status=status.HTTP_400_BAD_REQUEST)
    if despesa.is_valid():
        despesa.save()
        return Response(despesa.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_despesas(request):
    if request.query_params:
        despesa = Despesa.objects.filter(**request.query_params.dict()) # Permite Filtrar na URL http://127.0.0.1:8000/api/?category=category_name
    else:
        despesa = Despesa.objects.all() # Trás todos os objetos do banco
    
    if despesa:
        serializer = DespesaSerializer(despesa, many=True) # Many True é necessario qunado trazemos vários objetos do banco, sem ele dará erro
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_despesa(request, pk):
    despesa = get_object_or_404(Despesa, pk=pk)
    despesa.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
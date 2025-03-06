from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import tipoDespesa, tipoPrioridade
from .serializers import tipoDespesaSerializer, tipoPrioridadeSerializer

# ROTAS

@api_view(['GET']) # Define que essa função só pode ser acessa através do metodo GET
def tipoDespesaApiOverview(request):
    api_urls = {
        'all_tipoDespesa': '/',
        'Add': '/create',
        'Update': '/update/id',
        'Delete': '/tipoDespesa/id/delete'
    } 
    return Response(api_urls)

@api_view(['GET']) # Define que essa função só pode ser acessa através do metodo POST
def tipoPrioridadeApiOverview(request):
    api_urls = {
        'all_tipoPrioridade': '/',
        'Add': '/create',
        'Update': '/update/id',
        'Delete': '/tipoPrioridade/id/delete'
    } 
    return Response(api_urls)





@api_view(['GET']) # Define que essa função só pode ser acessa através do metodo POST
def tipoDespesaView(request):
    if request.query_params:
        tipoD = tipoDespesa.objects.filter(**request.query_params.dict()) # Permite Filtrar na URL http://
    else:
        tipoD = tipoDespesa.objects.all() # Trás todos os objetos do banco
    if tipoD:
        serializer = tipoDespesaSerializer(tipoD, many=True) # Many True é necessario qunado trazemos vários objetos do banco, sem ele dará erro
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET']) # Define que essa função só pode ser acessa através do metodo POST
def tipoPrioridadeView(request):
    if request.query_params:
        tipoP = tipoPrioridade.objects.filter(**request.query_params.dict()) # Permite Filtrar na URL http://
    else:
        tipoP = tipoPrioridade.objects.all() # Trás todos os objetos do banco
    if tipoP:
        serializer = tipoDespesaSerializer(tipoP, many=True) # Many True é necessario qunado trazemos vários objetos do banco, sem ele dará erro
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
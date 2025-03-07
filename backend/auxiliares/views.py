from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import tipoDespesa, tipoPrioridade
from .serializers import tipoDespesaSerializer, tipoPrioridadeSerializer

# ----------------------------- ROTAS -----------------------------
@api_view(['GET'])
def tipoDespesaApiOverview(request):
    api_urls = {
        'all_tipoDespesa': '/',
        'Add': '/create',
        'Update': '/update/id',
        'Delete': '/tipoDespesa/id/delete'
    } 
    return Response(api_urls)

@api_view(['GET'])
def tipoPrioridadeApiOverview(request):
    api_urls = {
        'all_tipoPrioridade': '/',
        'Add': '/create',
        'Update': '/update/id',
        'Delete': '/tipoPrioridade/id/delete'
    } 
    return Response(api_urls)
# -----------------------------------------------------------------=

@api_view(['GET']) 
def tipoDespesaView(request):
    if request.query_params:
        tipoD = tipoDespesa.objects.filter(**request.query_params.dict()) 
    else:
        tipoD = tipoDespesa.objects.all() 
    if tipoD:
        serializer = tipoDespesaSerializer(tipoD, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def tipoDespesaCreate(request):
    serializer = tipoDespesaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET']) 
def tipoPrioridadeView(request):
    if request.query_params:
        tipoP = tipoPrioridade.objects.filter(**request.query_params.dict())
    else:
        tipoP = tipoPrioridade.objects.all() 
    if tipoP:
        serializer = tipoDespesaSerializer(tipoP, many=True)  
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
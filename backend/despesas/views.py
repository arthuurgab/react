from rest_framework import generics, permissions
from .models import Despesa
from .serializers import DespesaSerializer

class DespesaListAPIView(generics.ListAPIView):
    serializer_class = DespesaSerializer
    permissions_classes = [permissions.AllowAny]
    queryset = Despesa.objects.all()
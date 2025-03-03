from rest_framework import serializers
from .models import Despesa

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'
        read_only_fields = ['id']
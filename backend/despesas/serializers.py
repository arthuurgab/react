from rest_framework import serializers
from .models import Despesa

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        modal = Despesa
        fields = '__all__'
        read_only_fields = ['id']
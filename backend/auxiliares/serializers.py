from rest_framework import serializers
from .models import tipoDespesa, tipoPrioridade

class tipoDespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoDespesa
        fields = '__all__'
        read_only_fields = ['id']

class tipoPrioridadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoPrioridade
        fields = '__all__'
        read_only_fields = ['id']

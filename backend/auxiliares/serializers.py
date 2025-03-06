from rest_framework import serializers
from .models import tipoDespesa

class tipoDespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoDespesa
        fields = '__all__'
        read_only_fields = ['id']
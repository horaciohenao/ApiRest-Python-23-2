from rest_framework import serializers
from .models import Mi_API_rest

class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = Mi_API_rest
        fields = ['name', 'info']
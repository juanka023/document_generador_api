from rest_framework import serializers
from .models import DocumentData


class DocumentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentData
        fields = '__all__'

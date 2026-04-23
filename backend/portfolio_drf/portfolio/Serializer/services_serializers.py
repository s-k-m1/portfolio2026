from rest_framework import serializers
from portfolio.models.services_models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'icon_name', 'order']
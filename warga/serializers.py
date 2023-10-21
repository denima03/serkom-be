from .models import Warga
from rest_framework import serializers


class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = '__all__'

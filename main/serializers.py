from rest_framework import  serializers
from .models import Gost


class GostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gost
        fields = '__all__'
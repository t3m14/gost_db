from rest_framework import generics
from rest_framework.response import Response
from .serializer import GostSerializer
from .models import Gost


class GostCreateApi(generics.CreateAPIView):
    queryset = Gost.objects.all()
    serializer_class = GostSerializer

class GostApi(generics.ListAPIView):
    queryset = Gost.objects.all()
    serializer_class = GostSerializer

class GostUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Gost.objects.all()
    serializer_class = GostSerializer

class GostDeleteApi(generics.DestroyAPIView):
    queryset = Gost.objects.all()
    serializer_class = GostSerializer
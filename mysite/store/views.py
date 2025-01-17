from rest_framework import viewsets
from .models import *
from .serialaizers import  *


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

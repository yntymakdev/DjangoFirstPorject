from rest_framework import viewsets
from .models import *
from .serialaizers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]  # Исправленный отступ
    filterset_class = ProductFilter  # Исправленный отступ
    search_fields = ['product_name']


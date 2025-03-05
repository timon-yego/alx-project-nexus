from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from .models import Product, Category, CarbonData
from .serializers import ProductSerializer, CategorySerializer, CarbonDataSerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """API endpoint for managing product categories."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
    """API endpoint for managing eco-friendly products."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'carbon_footprint']

class CarbonDataViewSet(viewsets.ModelViewSet):
    queryset = CarbonData.objects.all()
    serializer_class = CarbonDataSerializer
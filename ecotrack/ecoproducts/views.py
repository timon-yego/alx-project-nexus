from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from .models import Product, Category, CarbonData
from .serializers import ProductSerializer, CategorySerializer, CarbonDataSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """API endpoint for managing product categories."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductPagination(PageNumberPagination):
    page_size = 5  # Customize per page

class ProductViewSet(viewsets.ModelViewSet):
    """API endpoint for managing eco-friendly products."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category', 'carbon_footprint']
    ordering_fields = ['price', 'carbon_footprint']
    search_fields = ['name', 'description']
    pagination_class = ProductPagination


class CarbonDataViewSet(viewsets.ModelViewSet):
    queryset = CarbonData.objects.all()
    serializer_class = CarbonDataSerializer
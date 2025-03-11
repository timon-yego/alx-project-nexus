from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from .models import Product, Category, CarbonData
from .serializers import ProductSerializer, CategorySerializer, CarbonDataSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ecoproducts.tasks import update_product_stock

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """API endpoint for managing product categories."""
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProductPagination(PageNumberPagination):
    page_size = 10  # Customize per page
    page_size_query_param = 'page_size'
    max_page_size = 50

class ProductViewSet(viewsets.ModelViewSet):
    """API endpoint for managing eco-friendly products."""
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category', 'carbon_footprint']
    ordering_fields = ['price', 'carbon_footprint']
    search_fields = ['name', 'description']
    pagination_class = ProductPagination
    parser_classes = (MultiPartParser, FormParser)  # For image uploads


    @swagger_auto_schema(
        operation_description="Create a new product",
        request_body=ProductSerializer,
        responses={201: ProductSerializer, 400: "Bad Request"},
    )
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        product_id = response.data["id"]

        # Trigger background task to update stock levels
        update_product_stock.delay(product_id)

        return response


class CarbonDataViewSet(viewsets.ModelViewSet):
    queryset = CarbonData.objects.all()
    serializer_class = CarbonDataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
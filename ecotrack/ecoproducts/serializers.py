# ecoproducts/serializers.py
from rest_framework import generics, serializers
from .models import Category, Product, CarbonData

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CarbonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonData
        fields = ['manufacturing_emissions', 'transportation_emissions', 'disposal_emissions']
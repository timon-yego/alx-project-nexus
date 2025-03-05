# ecoproducts/serializers.py
from rest_framework import serializers
from .models import Category, Product, CarbonData

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock', 'carbon_footprint', 'image']

class CarbonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonData
        fields = ['manufacturing_emissions', 'transportation_emissions', 'disposal_emissions']
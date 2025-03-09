from django.contrib import admin
from .models import Category, Product, CarbonData

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock", "carbon_footprint")
    search_fields = ("name", "category__name")
    list_filter = ("category", "carbon_footprint")

@admin.register(CarbonData)
class CarbonDataAdmin(admin.ModelAdmin):
    list_display = ("product", "manufacturing_emissions", "transportation_emissions", "disposal_emissions")
    search_fields = ("product__name",)

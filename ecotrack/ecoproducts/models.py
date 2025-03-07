from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, db_index=True)
    stock = models.PositiveIntegerField()
    carbon_footprint = models.FloatField()  # Carbon footprint per unit
    image = models.ImageField(upload_to="product_images/", blank=True, null=True)

    def __str__(self):
        return self.name

class CarbonData(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='carbon_data')
    manufacturing_emissions = models.FloatField()  # Emissions from manufacturing
    transportation_emissions = models.FloatField()  # Emissions from transportation
    disposal_emissions = models.FloatField()  # Emissions from disposal

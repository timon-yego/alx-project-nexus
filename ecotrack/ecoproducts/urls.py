# ecoproducts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, CarbonDataViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carbon-data', CarbonDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
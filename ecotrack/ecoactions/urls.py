from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EcoActionViewSet, RewardViewSet, CarbonImpactViewSet

router = DefaultRouter()
router.register('actions', EcoActionViewSet)
router.register('rewards', RewardViewSet)
router.register('carbon-impact', CarbonImpactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

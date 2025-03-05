from django.urls import path
from .views import EcoActionListCreateView, RewardListCreateView, CarbonImpactListCreateView

urlpatterns = [
    path('actions/', EcoActionListCreateView.as_view(), name='action-list'),
    path('rewards/', RewardListCreateView.as_view(), name='reward-list'),
    path('carbon-impact/', CarbonImpactListCreateView.as_view(), name='carbon-impact-list'),
]

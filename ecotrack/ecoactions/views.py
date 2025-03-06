from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from .models import EcoAction, Reward, CarbonImpact
from .serializers import EcoActionSerializer, RewardSerializer, CarbonImpactSerializer

# Create your views here.


class EcoActionViewSet(viewsets.ModelViewSet):
    queryset = EcoAction.objects.all()
    serializer_class = EcoActionSerializer

class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

    
class CarbonImpactViewSet(viewsets.ModelViewSet):
    queryset = CarbonImpact.objects.all()
    serializer_class = CarbonImpactSerializer

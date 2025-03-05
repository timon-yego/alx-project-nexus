from django.shortcuts import render
from rest_framework import generics, permissions
from .models import EcoAction, Reward, CarbonImpact
from .serializers import EcoActionSerializer, RewardSerializer, CarbonImpactSerializer

# Create your views here.


class EcoActionListCreateView(generics.ListCreateAPIView):
    queryset = EcoAction.objects.all()
    serializer_class = EcoActionSerializer
    permission_classes = [permissions.IsAuthenticated]

class RewardListCreateView(generics.ListCreateAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [permissions.IsAuthenticated]

class CarbonImpactListCreateView(generics.ListCreateAPIView):
    queryset = CarbonImpact.objects.all()
    serializer_class = CarbonImpactSerializer
    permission_classes = [permissions.IsAuthenticated]

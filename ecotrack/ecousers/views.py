from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import Profile, SustainabilityGoal
from .serializers import UserSerializer, ProfileSerializer, SustainabilityGoalSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class SustainabilityGoalListCreateView(generics.ListCreateAPIView):
    queryset = SustainabilityGoal.objects.all()
    serializer_class = SustainabilityGoalSerializer
    permission_classes = [permissions.IsAuthenticated]


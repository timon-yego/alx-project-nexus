from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import Profile, SustainabilityGoal
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, SustainabilityGoalSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

class SustainabilityGoalListCreateView(generics.ListCreateAPIView):
    queryset = SustainabilityGoal.objects.all()
    serializer_class = SustainabilityGoalSerializer
    permission_classes = [permissions.IsAuthenticated]


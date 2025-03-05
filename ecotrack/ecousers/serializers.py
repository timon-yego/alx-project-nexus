# ecousers/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile, SustainabilityGoal

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_eco_enthusiast', 'carbon_footprint']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

class SustainabilityGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SustainabilityGoal
        fields = '__all__'


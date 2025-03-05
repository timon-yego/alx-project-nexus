from rest_framework import serializers
from .models import EcoAction, Reward, CarbonImpact

class EcoActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcoAction
        fields = '__all__'

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'

class CarbonImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonImpact
        fields = '__all__'

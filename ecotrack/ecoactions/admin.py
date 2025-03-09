from django.contrib import admin
from .models import EcoAction, Reward, CarbonImpact

# Register your models here.
@admin.register(EcoAction)
class EcoActionAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "carbon_saved", "timestamp")
    search_fields = ("user__username", "action")

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ("user", "points", "reason", "timestamp")
    search_fields = ("user__username", "reason")

@admin.register(CarbonImpact)
class CarbonImpactAdmin(admin.ModelAdmin):
    list_display = ("user", "total_carbon_saved", "last_updated")
    search_fields = ("user__username",)

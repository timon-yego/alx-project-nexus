from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, SustainabilityGoal

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_eco_enthusiast", "carbon_footprint", "is_staff")
    search_fields = ("username", "email")
    list_filter = ("is_eco_enthusiast", "is_staff")

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone_number", "city", "country", "eco_score")
    search_fields = ("user__username", "city", "country")

@admin.register(SustainabilityGoal)
class SustainabilityGoalAdmin(admin.ModelAdmin):
    list_display = ("user", "goal", "target", "progress")
    search_fields = ("user__username", "goal")

# ecousers/urls.py
from django.urls import path
from .views import UserListCreateView, ProfileDetailView, SustainabilityGoalListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('goals/', SustainabilityGoalListCreateView.as_view(), name='goal-list-create'),
]


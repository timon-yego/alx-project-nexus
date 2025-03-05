# ecousers/urls.py
from django.urls import path
from .views import UserListCreateView, ProfileDetailView, SustainabilityGoalListCreateView, UserRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('goals/', SustainabilityGoalListCreateView.as_view(), name='goal-list-create'),
]


# ecousers/urls.py
from django.urls import path
from .views import RegisterView, LoginView, UserListCreateView, ProfileView, SustainabilityGoalListCreateView
from rest_framework_simplejwt.views import  TokenRefreshView
from .views import LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('profile/', ProfileView.as_view(), name='user-profile'),
    path('goals/', SustainabilityGoalListCreateView.as_view(), name='goal-list-create'),
    path("logout/", LogoutView.as_view(), name="logout"),
]


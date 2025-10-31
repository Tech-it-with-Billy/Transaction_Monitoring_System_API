from django.urls import path
from .views import ProfileView, RegistrationView, AdminUserDetailView, UserListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/auth/register/', RegistrationView.as_view(), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/profile/', ProfileView.as_view(), name='profile'),
    path('api/users/', UserListView.as_view(), name='analyst'),
    path('api/user/admin/', AdminUserDetailView.as_view(), name='admin')
]

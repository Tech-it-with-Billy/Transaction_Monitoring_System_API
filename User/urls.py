from django.urls import path
from .views import RegistrationView, LoginView, ProfileView, AdminView

urlpatterns = [
    path('api/user/register/', RegistrationView.as_view(), name='register user'),
    path('api/user/login/', LoginView.as_view(), name='user login'),
    path('api/user/profile/', ProfileView.as_view(), name='user profile'),
    path('api/admin/', AdminView.as_view(), name='user manager')
]

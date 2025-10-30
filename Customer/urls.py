from django.urls import path
from .views import CustomerView

urlpatterns = [
    path('api/customers', CustomerView.as_view(), name='customers')
]

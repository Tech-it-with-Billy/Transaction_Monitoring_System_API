from django.urls import path
from .views import CreateCustomerView, ListCustomerView, CustomerDetailView, AdminView

urlpatterns = [
    path('api/customers/create/', CreateCustomerView.as_view(), name='create_customer'),
    path('api/customers/list/', ListCustomerView.as_view(), name='customer_list'),
    path('api/customers/detail/', CustomerDetailView.as_view(), name='customer_detail'),
    path('api/customers/admin/<uuid:pk>/', AdminView.as_view(), name='admin')
]

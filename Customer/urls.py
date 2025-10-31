from django.urls import path
from .views import CreateCustomerView, CustomersListView, CustomerDetailView, AdminCustomerManageView

urlpatterns = [
    path('api/customers/create/', CreateCustomerView.as_view(), name='create_customer'),
    path('api/customers/list/', CustomersListView.as_view(), name='customer_list'),
    path('api/customers/<uuid:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('api/admin/customers/<uuid:pk>/', AdminCustomerManageView.as_view(), name='admin')
]

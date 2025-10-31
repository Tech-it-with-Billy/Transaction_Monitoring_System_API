from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import generics, permissions
from .permissions import IsAdmin, IsAnalyst, IsOperator

class CreateCustomerView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsOperator]

class CustomersListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdmin | IsAnalyst | IsOperator]

class CustomerDetailView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdmin | IsAnalyst]
    

class AdminCustomerManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdmin]
    
    def get_object(self):
        return self.request.user
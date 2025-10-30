from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import generics, permissions

class CustomerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
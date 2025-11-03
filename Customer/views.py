from rest_framework import generics, permissions
from rest_framework.response import Response
from .permissions import IsAdmin, IsAnalyst, IsOperator
from .serializers import CustomerSerializer
from .models import Customer

class CreateCustomerView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated, (IsAdmin, IsOperator)]
    
    def perform_create(self, serializer):
        serializer.save(created_by= self.request.user)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                {'message': 'Customer created successfully!', 'data': serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

class ListCustomerView(generics.ListAPIView):
    queryset = Customer.objects.all().order_by('-created_at')
    serializer_class = CustomerSerializer
    pagination_class = [permissions.IsAuthenticated]
    

class CustomerDetailView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field  = 'id'
    
    def get_object(self, request):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(
                {'message': 'Customer retrieved successfully!'},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": f"Something went wrong: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class AdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return super().get_object()
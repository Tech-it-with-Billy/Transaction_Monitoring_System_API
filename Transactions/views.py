from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .serializers import TransactionSerializer
from .models import Transaction
from .permissions import IsAdmin, IsAnalyst, IsOperator
from Customer.models import Customer
from datetime import datetime

class CreateTransactionView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, (IsAdmin | IsOperator)]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'message': 'Transaction created successfully!',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )

class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, (IsAdmin | IsOperator | IsAnalyst)]
    queryset = Transaction.objects.all().order_by('-transaction_time')
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['transaction_time', 'amount']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:
            try:
                start = datetime.strptime(start_date, "%Y-%m-%d")
                end = datetime.strptime(end_date, "%Y-%m-%d")
                queryset = queryset.filter(transaction_time__date__range=(start, end))
            except ValueError:
                pass
        return queryset
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(
            {
                'message': 'Retrieval successful!',
                "count": self.paginator.page.paginator.count if self.paginator else len(response.data),
                "results": response.data
            },
            status=status.HTTP_200_OK
        )

class TransactionDetailView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, (IsAdmin | IsOperator | IsAnalyst)]
    lookup_field = 'id'
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {
                "message": "Transaction details retrieved successfully.",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

class CustomerListTransactionsView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, (IsAdmin | IsOperator | IsAnalyst)]
    
    def get_queryset(self):
        customer_id = self.kwargs.get('customer_id')
        return Transaction.objects.filter(customer_id=customer_id).order_by('-transaction_time')
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(
            {
                "message": "Customer transactions retrieved successfully.",
                "count": self.paginator.page.paginator.count if self.paginator else len(response.data),
                "results": response.data
            },
            status=status.HTTP_200_OK
        )

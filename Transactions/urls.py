from django.urls import path
from .views import CreateTransactionView, TransactionListView, CustomerListTransactionsView, TransactionDetailView

urlpatterns = [
    path('api/transactions/create/', CreateTransactionView.as_view(), name='create transaction'),
    path('api/transactions/list/', TransactionListView.as_view(), name='transactions list'),
    path('api/transactions/<uuid:id>/', TransactionDetailView.as_view, name='transaction detail'),
    path('api/customers/<uuid:customer_id>/transactions/', CustomerListTransactionsView.as_view, name='customers_transactions')
]

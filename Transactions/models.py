from django.db import models
import uuid
import shortuuid
from Customer.models import Customer
from django.conf import settings


def transaction_reference():
    short_id = shortuuid()[:8].upper()
    return f"TXN{short_id}"

class Transactions(models.Model):
    STATUS = [
        ('pending': 'pending'),
        ('complete': 'complete'),
        ('failed': 'failed'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True )
    reference = models.CharField(max_length=20, unique=True, default=transaction_reference, editable=False)
    account_number = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS, default='pending')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='transactions')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='transaction_author')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.reference} - {self.status}"
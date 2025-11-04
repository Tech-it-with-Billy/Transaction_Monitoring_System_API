from django.db import models
from django.conf import settings
import uuid
from Customer.models import Customer

class Transaction(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('completed', 'completed'),
        ('failed', 'failed'),
    )
    
    TRANSACTION_TYPE  = (
        ('withdrawal', 'withdrawal'),
        ('deposit', 'deposit'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reference = models.CharField(max_length=100, unique=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, 
        related_name='transactions_created', null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = f'TXN-{uuid.uuid4().hex[:10].upper()}'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.transaction_type.title()} - {self.amount} {self.status}'
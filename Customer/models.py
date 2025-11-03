from django.db import models
from django.conf import settings
import uuid

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=225)
    created_by = models.CharField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, 
        related_name='customers_created', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    account_number = models.BigIntegerField(unique=True)
    account_balance = models.DecimalField(max_digits= 12, decimal_place=2, default=0.00)
    
    def __str__(self):
        return f'Account: {self.first_name} {self.last_name}  Balance: {self.account_balance}'
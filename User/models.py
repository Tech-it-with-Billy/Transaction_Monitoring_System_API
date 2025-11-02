from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    ROLES = (
        ('admin': 'admin'),
        ('analyst': 'analyst'),
        ('operator': 'operator')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    role= models.CharField(max_length=20, choices=ROLES)
    
    def __str__(self):
        return f"{self.username} - {self.role}"
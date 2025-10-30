from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'admin'),
        ('analyst', 'analyst'),
        ('operator', 'operator'),
    )
    
    role = models.CharField(max_length=20, choices=ROLES, null=False, blank=False)
    
    def __str__(self):
        return f"{self.username} - {self.role}"
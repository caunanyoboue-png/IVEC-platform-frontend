from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('investisseur', 'Investisseur'),
        ('agent', 'Agent'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='investisseur')

    def __str__(self):
        return self.username
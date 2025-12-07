from django.db import models
from django.conf import settings

class Investor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='investor_profile')
    capital_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Investisseur: {self.user.username}"

class Transaction(models.Model):
    class Types(models.TextChoices):
        DEPOSIT = 'DEPOSIT', 'Dépôt'
        WITHDRAWAL = 'WITHDRAWAL', 'Retrait'
        INTEREST = 'INTEREST', 'Intérêts'

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'En attente'
        COMPLETED = 'COMPLETED', 'Terminé'
        REJECTED = 'REJECTED', 'Rejeté'

    investor = models.ForeignKey(Investor, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=20, choices=Types.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    processed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='processed_transactions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} - {self.amount} - {self.investor.user.username}"
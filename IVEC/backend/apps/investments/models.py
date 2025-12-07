from django.db import models
from django.utils import timezone

class Investment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    capital = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_interest(self):
        duration = (timezone.now() - self.created_at).days / 365  # Duration in years
        return self.capital * (self.interest_rate / 100) * duration

    def __str__(self):
        return f'Investment by {self.user.username} - Amount: {self.capital}'

class Transaction(models.Model):
    investment = models.ForeignKey(Investment, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10)  # e.g., 'deposit' or 'withdrawal'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Transaction {self.transaction_type} - Amount: {self.amount} for Investment ID: {self.investment.id}'
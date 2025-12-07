from rest_framework import serializers
from .models import Investment, Transaction

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = ['id', 'user', 'capital', 'interest_rate', 'created_at', 'updated_at']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'investment', 'amount', 'transaction_type', 'created_at']
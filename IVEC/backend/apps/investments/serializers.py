from rest_framework import serializers
from .models import Investor, Transaction
from apps.users.serializers import UserSerializer

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['investor', 'status', 'processed_by', 'created_at']

class InvestorDashboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    transactions = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Investor
        fields = ['id', 'user', 'capital_balance', 'created_at', 'transactions']
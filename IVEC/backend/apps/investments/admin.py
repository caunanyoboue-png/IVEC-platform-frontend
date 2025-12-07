from django.contrib import admin
from .models import Investment, Transaction

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'capital', 'interest_rate', 'created_at', 'updated_at')
    search_fields = ('id', 'capital', 'interest_rate')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'investment', 'amount', 'transaction_type', 'created_at')
    list_filter = ('transaction_type',)
    search_fields = ('id', 'investment__id', 'amount')
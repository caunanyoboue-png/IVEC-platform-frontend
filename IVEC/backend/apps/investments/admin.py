from django.contrib import admin
from .models import Investor, Transaction

@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('user', 'capital_balance', 'created_at')
    search_fields = ('user__username', 'user__email')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('investor', 'type', 'amount', 'status', 'created_at')
    list_filter = ('type', 'status')
    search_fields = ('investor__user__username',)
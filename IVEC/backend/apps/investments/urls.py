from django.urls import path
from .views import InvestmentListView, InvestmentDetailView, TransactionListView, TransactionDetailView

urlpatterns = [
    path('investments/', InvestmentListView.as_view(), name='investment-list'),
    path('investments/<int:pk>/', InvestmentDetailView.as_view(), name='investment-detail'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
]
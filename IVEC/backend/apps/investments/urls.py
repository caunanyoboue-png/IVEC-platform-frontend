from django.urls import path
from .views import (
    InvestmentListView, InvestmentDetailView,
    TransactionListView, TransactionDetailView,
    InvestorDashboardView, RequestWithdrawalView
)

urlpatterns = [
    path('', InvestmentListView.as_view(), name='investment-list'),
    path('<int:pk>/', InvestmentDetailView.as_view(), name='investment-detail'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('dashboard/', InvestorDashboardView.as_view(), name='investor-dashboard'),
    path('withdraw/', RequestWithdrawalView.as_view(), name='request-withdrawal'),
]
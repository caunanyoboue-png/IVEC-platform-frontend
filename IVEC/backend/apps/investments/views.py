from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from .models import Investor, Transaction
from .serializers import InvestorDashboardSerializer, TransactionSerializer

User = get_user_model()

class InvestmentListView(generics.ListAPIView):
    """
    Admin: list all investors
    """
    queryset = Investor.objects.select_related('user').all()
    serializer_class = InvestorDashboardSerializer
    permission_classes = [permissions.IsAdminUser]

class InvestmentDetailView(generics.RetrieveAPIView):
    """
    Admin: retrieve a single investor profile
    """
    queryset = Investor.objects.select_related('user').all()
    serializer_class = InvestorDashboardSerializer
    permission_classes = [permissions.IsAdminUser]

class TransactionListView(generics.ListAPIView):
    """
    - Admin: all transactions
    - Agent: pending withdrawals
    - Investor: own transactions
    """
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        roles = getattr(User, 'Roles', None)
        admin_role = getattr(roles, 'ADMIN', None) if roles else None
        agent_role = getattr(roles, 'AGENT', None) if roles else None

        if getattr(user, 'is_staff', False) or user.role == admin_role:
            return Transaction.objects.select_related('investor__user', 'processed_by').order_by('-created_at')
        if user.role == agent_role:
            return Transaction.objects.filter(type=Transaction.Types.WITHDRAWAL, status=Transaction.Status.PENDING).select_related('investor__user').order_by('-created_at')
        if hasattr(user, 'investor_profile'):
            return Transaction.objects.filter(investor=user.investor_profile).order_by('-created_at')
        return Transaction.objects.none()

class TransactionDetailView(generics.RetrieveUpdateAPIView):
    """
    Retrieve/update a single transaction.
    - Agents/Admins can update status (processing withdrawals).
    - Investors can only view their transactions.
    """
    queryset = Transaction.objects.select_related('investor__user', 'processed_by')
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        user = self.request.user
        roles = getattr(User, 'Roles', None)
        admin_role = getattr(roles, 'ADMIN', None) if roles else None
        agent_role = getattr(roles, 'AGENT', None) if roles else None

        if getattr(user, 'is_staff', False) or user.role in (admin_role, agent_role):
            return obj
        if hasattr(user, 'investor_profile') and obj.investor_id == user.investor_profile.id:
            return obj
        self.permission_denied(self.request, message="Not authorized to access this transaction")

class InvestorDashboardView(generics.RetrieveAPIView):
    serializer_class = InvestorDashboardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        if hasattr(user, 'investor_profile'):
            return user.investor_profile
        self.permission_denied(self.request, message='User is not an investor')

class RequestWithdrawalView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        if not hasattr(user, 'investor_profile'):
            return Response({'detail': 'Not an investor'}, status=status.HTTP_403_FORBIDDEN)
        investor = user.investor_profile
        amount = request.data.get('amount')
        try:
            amount = float(amount)
        except Exception:
            return Response({'detail': 'Invalid amount'}, status=status.HTTP_400_BAD_REQUEST)
        if amount <= 0 or amount > float(investor.capital_balance):
            return Response({'detail': 'Invalid withdrawal amount'}, status=status.HTTP_400_BAD_REQUEST)
        tx = Transaction.objects.create(
            investor=investor,
            type=Transaction.Types.WITHDRAWAL,
            amount=amount,
            status=Transaction.Status.PENDING
        )
        return Response(TransactionSerializer(tx).data, status=status.HTTP_201_CREATED)


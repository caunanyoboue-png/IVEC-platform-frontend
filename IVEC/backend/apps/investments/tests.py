from django.test import TestCase
from .models import Investment, Transaction

class InvestmentModelTest(TestCase):
    def setUp(self):
        self.investment = Investment.objects.create(
            capital=1000.00,
            interest_rate=5.0,
            duration_months=12
        )

    def test_investment_creation(self):
        self.assertEqual(self.investment.capital, 1000.00)
        self.assertEqual(self.investment.interest_rate, 5.0)
        self.assertEqual(self.investment.duration_months, 12)

    def test_calculate_interest(self):
        expected_interest = self.investment.calculate_interest()
        self.assertEqual(expected_interest, 50.00)  # Assuming interest calculation logic is correct

class TransactionModelTest(TestCase):
    def setUp(self):
        self.investment = Investment.objects.create(
            capital=1000.00,
            interest_rate=5.0,
            duration_months=12
        )
        self.transaction = Transaction.objects.create(
            investment=self.investment,
            amount=200.00,
            transaction_type='withdrawal'
        )

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.amount, 200.00)
        self.assertEqual(self.transaction.transaction_type, 'withdrawal')
        self.assertEqual(self.transaction.investment, self.investment)
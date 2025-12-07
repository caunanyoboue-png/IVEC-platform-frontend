from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Investment, Transaction
from .serializers import InvestmentSerializer, TransactionSerializer
from .services.interest_calculator import calculate_interest

class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            investment = serializer.save()
            return Response(InvestmentSerializer(investment).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        investments = self.queryset
        serializer = self.get_serializer(investments, many=True)
        return Response(serializer.data)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            transaction = serializer.save()
            return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        transactions = self.queryset
        serializer = self.get_serializer(transactions, many=True)
        return Response(serializer.data)

class InterestCalculationView(viewsets.ViewSet):
    def calculate(self, request):
        investments = Investment.objects.all()
        for investment in investments:
            interest = calculate_interest(investment)
            investment.interest += interest
            investment.save()
        return Response({"message": "Interest calculated for all investments."}, status=status.HTTP_200_OK)
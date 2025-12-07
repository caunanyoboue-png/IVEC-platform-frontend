from django.core.management.base import BaseCommand
from investments.models import Investment
from investments.services.interest_calculator import calculate_interest

class Command(BaseCommand):
    help = 'Calculate and update interests for all investments'

    def handle(self, *args, **kwargs):
        investments = Investment.objects.all()
        for investment in investments:
            interest = calculate_interest(investment)
            investment.interest += interest
            investment.save()
            self.stdout.write(self.style.SUCCESS(f'Updated interest for investment ID {investment.id}: {interest}'))
def calculate_interest(principal, rate, time):
    """
    Calculate the interest based on principal, rate, and time.
    
    :param principal: The initial amount of money invested.
    :param rate: The interest rate (as a decimal).
    :param time: The time the money is invested for (in years).
    :return: The calculated interest.
    """
    return principal * rate * time

def update_investment_with_interest(investment):
    """
    Update the investment with calculated interest.
    
    :param investment: The investment object to update.
    :return: The updated investment object.
    """
    interest = calculate_interest(investment.capital, investment.interest_rate, investment.time_period)
    investment.total_value = investment.capital + interest
    investment.save()
    return investment
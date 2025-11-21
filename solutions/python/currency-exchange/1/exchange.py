def exchange_money(budget, exchange_rate):
    return budget/exchange_rate
def get_change(budget, exchanging_value):
    return budget-exchanging_value
def get_value_of_bills(denomination, number_of_bills):
    return denomination*number_of_bills
def get_number_of_bills(amount, denomination):
    return amount//denomination
def get_leftover_of_bills(amount, denomination):
    return amount % denomination
def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread_percent = spread / 100
    actual_rate = exchange_rate * (1 + spread_percent)
    total_foreign_currency = budget / actual_rate
    number_of_bills = total_foreign_currency // denomination
    final_value = number_of_bills * denomination
    return final_value

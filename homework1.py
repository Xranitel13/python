from datetime import datetime
import random


# zadanie 1:
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()

def get_days_from_today(date):
    datatime = string_to_date(date)
    today = datetime.today().date()
    diff = (datatime-today).days
    return diff


print(get_days_from_today("2026-01-01"))




#zadanie 2:

def get_numbers_ticket(min, max, quantity):
    if min<1 or max>1000 or min>max or quantity<min or quantity>max:
        return []
    return sorted(random.sample(range(min, max+1), quantity))


lottery_numbers = get_numbers_ticket(1, 5, 2)
print("Ваші лотерейні числа:", lottery_numbers)
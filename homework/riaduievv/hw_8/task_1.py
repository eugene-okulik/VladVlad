import random

salary = int(input("What is your salary? "))
bonus = random.choice([True, False])

if bonus:
    bonus_amount = random.randint(1, 10000)
    total = salary + bonus_amount
    print(f"{salary}, {bonus} - ${total}")
else:
    print(f"{salary}, {bonus} - ${salary}")

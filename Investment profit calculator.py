import time

initial_investment = input("How much have you initially invested? ")

int_initial_investment = int(initial_investment)

current_amount = input("How much is the current amount the investment has risen or fallen to? ")

int_current_amount = int(current_amount)

profit = int_current_amount - int_initial_investment

profit_string = str(profit)

percentage_increase = profit/int_initial_investment * 100

percentage_increase_string = str(percentage_increase) + "%"

print("your investment has risen " + percentage_increase_string + ", and you have profited $" + profit_string + "!")


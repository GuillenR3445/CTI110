# This program calculates and displays travel expenses

# 28 Mar 2023

# CTI-110 P1HW1 - Travel Expense

# Ruben Guillen

#


budget = int(input("What is your budget for this trip? $"))
destination = input("Where are you traveling to? ")
gas_expense = int(input("How much will you spend on gas for this trip? $"))
accommodation_expense = int(input("How much will you spend on accommodation for this trip? $"))
food_expense = int(input("How much will you spend on food for this trip? $"))

total_expenses = gas_expense + accommodation_expense + food_expense
remaining_budget = budget - total_expenses

# Display results
print('----------Travel Expenses----------')
print('Travel Location:', destination)
print('Initial Budget:', budget)
print('Fuel:', gas_expense)
print('Accomodation:', accommodation_expense)
print('Food:', food_expense)
print('Total Expenses:', total_expenses)
print('Remaining Balance:', remaining_budget)
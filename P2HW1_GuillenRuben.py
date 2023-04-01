# This program calculates and displays travel expenses

# 01 Apr 2023

# CTI-110 P2HW1 - Travel

# Ruben Guillen

#


# Prompt the user for their budget for the trip
budget = float(input("What is your budget for this trip? $"))

# Prompt the user for their destination
destination = input("Where are you traveling to? ")

# Prompt the user for their estimated gas expense
gas_expense = float(input("How much will you spend on gas for this trip? $"))

# Prompt the user for their estimated accommodation expense
accommodation_expense = float(input("How much will you spend on accommodation for this trip? $"))

# Prompt the user for their estimated food expense
food_expense = float(input("How much will you spend on food for this trip? $"))

# Calculate the total expenses for the trip
total_expenses = gas_expense + accommodation_expense + food_expense

# Calculate the remaining budget after expenses
remaining_budget = budget - total_expenses

# Display the travel expenses in a table
print('----------Travel Expenses----------')
print(f'Travel Location:    {destination}')
print(f'Initial Budget:     ${budget:.2f}')
print(f'Fuel:               ${gas_expense:.2f}')
print(f'Accomodation:       ${accommodation_expense:.2f}')
print(f'Food:               ${food_expense:.2f}')
print(f'Total Expenses:     ${total_expenses:.2f}')
print('----------Travel Expenses----------')
print(f'Remaining Balance:  ${remaining_budget:.2f}')
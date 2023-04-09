# CTI-110
# P3HW2 - Salary
# Ruben Guillen
# 08 Apr 2023

# This program calculates an employee's pay.

# Get input about employee
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Check for overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)    
else:
    overtime_pay = 0

# Calculate Pay
regular_pay = 40 * pay_rate
gross_pay = overtime_pay + regular_pay

# Display results
print("Employee name: ", employee_name)
print("Pay rate       Hours Worked    Regular Pay    Overtime Hours   Overtime Pay    Gross Pay")
print("-----------------------------------------------------------------------------------------")
print(f"${pay_rate:<15.2f}{hours_worked:<15.2f}${regular_pay:<15.2f}{overtime_hours:<15.2f}${overtime_pay:<15.2f}${gross_pay:<15.2f}")
print("-----------------------------------------------------------------------------------------")

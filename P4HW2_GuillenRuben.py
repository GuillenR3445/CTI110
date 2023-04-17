# CTI-110
# P4HW2 - Salary
# Ruben Guillen
# 17 Apr 2023

# The program calculates individual pay for multiple employees, with the option to terminate employee input. It then displays the total amount paid for overtime and regular hours, the total gross pay, and the number of employees entered.

# Initialize variables as a starting point to prevent type errors later on.
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
num_employees = 0

# Prompt user to enter first employee name
employee_name = input("Enter employee's name or 'Done' when finished: ")

while employee_name.lower() != "done":
    # Prompt user to enter hours worked and pay rate
    hours_worked = float(input(f"Enter number of hours {employee_name} worked: "))
    pay_rate = float(input(f"Enter {employee_name}'s pay rate: "))

    # Check for overtime
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    else:
        overtime_hours = 0
        overtime_pay = 0
    
    # Calculate pay
    regular_pay = (hours_worked - overtime_hours) * pay_rate
    gross_pay = overtime_pay + regular_pay

    # Add pay values to total amount variables
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    # Increment number of employees entered
    num_employees += 1

    # Display employee pay information
    print("Employee name: ", employee_name)
    print("Pay rate       Hours Worked    Regular Pay    Overtime Hours   Overtime Pay    Gross Pay")
    print("-----------------------------------------------------------------------------------------")
    print(f"${pay_rate:<15.2f}{hours_worked:<15.2f}${regular_pay:<15.2f}{overtime_hours:<15.2f}${overtime_pay:<15.2f}${gross_pay:<15.2f}")
    print("-----------------------------------------------------------------------------------------")

    # Prompt user to enter employee name for next employee
    employee_name = input("Enter employee's name or 'Done' when finished: ")

# Display totals for all employees
print("Total number of employees:                ", num_employees)
print("Total amount paid for overtime hours:     $", total_overtime_pay)
print("Total amount paid for regular hours:      $", total_regular_pay)
print("Total gross pay:                          $", total_gross_pay)

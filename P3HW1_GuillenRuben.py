# CTI-110
# P2HW2 - List
# Ruben Guillen
# 08 Apr 2023

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Calculate the lowest and highest grades in the list
lowest_grade = min(grades)
highest_grade = max(grades)

# Calculate the sum and average of all grades in the list
sum_grades = sum(grades)
average_grade = sum_grades / len(grades)

# Display the lowest grade, highest grade, sum, and average in a formatted table
print("-----------Results-----------")
print(f"Lowest Grade:       {lowest_grade:.2f}")
print(f"Highest Grade:      {highest_grade:.2f}")
print(f"Sum of Grades:      {sum_grades:.2f}")
print(f"Average:            {average_grade:.2f}")
print("-----------Results-----------")

if average_grade >= 90:
    print('Your grade is: A')
elif average_grade >= 80:
    print('Your grade is: B')
elif average_grade >= 70:
    print('Your grade is: C')
elif average_grade >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
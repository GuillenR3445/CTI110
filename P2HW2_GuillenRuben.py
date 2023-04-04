# CTI-110
# P2HW2 - List
# Ruben Guillen
# 01 Apr 2023

# Prompt user to enter grades for each module and store in list
grades = []
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

# Calculate the lowest and highest grades in the list
lowest_grade = min(grades)
highest_grade = max(grades)

# Calculate the sum and average of all grades in the list
sum_grades = sum(grades)
average_grade = sum_grades / len(grades)

# Display the lowest grade, highest grade, sum, and average in a formatted table
print("--------Results--------")
print(f"Lowest Grade:       {lowest_grade:.2f}")
print(f"Highest Grade:      {highest_grade:.2f}")
print(f"Sum of Grades:      {sum_grades:.2f}")
print(f"Average:            {average_grade:.2f}")
print("--------Results--------")
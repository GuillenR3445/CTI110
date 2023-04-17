# CTI-110
# P4HW1 - Score List
# Ruben Guillen
# 17 Apr 2023

# Prompt user to enter how many scores
num_scores = int(input("How many scores would you like to enter? "))

# Create a loop to collect the number of scores
scores = []

for i in range(num_scores):
    score = -1
    while score < 0 or score > 100:
        score = float(input(f"Enter score {i+1}: "))
        if score < 0 or score > 100:
            print("Invalid score entered. Score must be between 0 and 100.")
    scores.append(score)

# Calculate the lowest score entered and display it.
lowest_score = min(scores)
print("------------Results------------")
print(f"Lowest score entered:      {lowest_score:.2f}")

# Sort the score list in ascending order and drop the lowest score.
scores.sort()
scores.pop(0)
print(f"Modified list of scores:   {scores}")

# Calculate the average of the scores in the modified list and display it.
average_score = sum(scores) / len(scores)
print(f"Average score:             {average_score:.2f}")

# Determine the letter grade for the calculated average and display it to the user.
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
    
print(f"Letter grade:              {letter_grade}")
print("------------Results------------")
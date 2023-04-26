# CTI-110
# P5HW - Math Quiz
# Ruben Guillen
# 25 Apr 2023

# This program runs a simple Math Quiz.

# Function that displays the menu and requests user's choice
def display_menu():
    print("Welcome to Math Quiz")
    print("Main Menu")
    print("----------------------------------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    return input("Please choose one of the menu options: ")

import random

# Function that generates two random numbers for addition or subtraction
def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

# Function that asks user for input and checks if it's correct
def check_answer(correct_answer):
    num_guesses = 1
    while True:
        guess = int(input("Enter your answer: "))
        if guess == correct_answer:
            print("Congratulations, you guessed correctly! It took you", num_guesses, "guesses.")
            break
        elif guess < correct_answer:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")
        num_guesses += 1

# Get user's choice from the menu
while True:
    choice = display_menu()

    if choice == '1':
        num1, num2 = generate_numbers()
        correct_answer = num1 + num2
        print(num1, "+", num2)
        check_answer(correct_answer)
    elif choice == '2':
        num1, num2 = generate_numbers()
        correct_answer = num1 - num2
        print(num1, "-", num2)
        check_answer(correct_answer)
    elif choice == '3':
        break
    else:
        print("Invalid input. Please enter 1, 2, or 3.")
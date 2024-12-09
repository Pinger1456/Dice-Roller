"""
This module handles the initialization and execution of the project.
Make sure to organize imports and configurations correctly.
"""

# main.py
import random
import time
from config import QUIZ_DURATION, MIN_DICE, MAX_DICE, REWARD, PENALTY
from dice import roll_dice, print_dice


def start_quiz():
    """Starting the main process"""
    score = 0
    print(f"Welcome to Dice Math! You have {QUIZ_DURATION} seconds to answer.")

    start_time = time.time()
    while time.time() - start_time < QUIZ_DURATION:
        number_of_dice = random.randint(MIN_DICE, MAX_DICE)
        # Random dice sides, can be adjusted
        number_of_sides = random.randint(4, 6)
        modifier = random.choice([0, random.randint(-3, 3)])  # Random modifier

        # Display question
        print(f"\nHow much is the sum of {number_of_dice}d{number_of_sides}"
              f"{'+' + str(modifier) if modifier else ''}?")

        # Roll dice and display them
        rolls, total = roll_dice(number_of_dice, number_of_sides, modifier)
        print_dice(rolls)
        print(f"Total (including modifier): {total}")

        # Get user input
        answer = input("Your answer: ")

        # Check answer
        if answer.strip().isdigit() and int(answer.strip()) == total:
            score += REWARD
            print(f"Correct! Your score: {score}")
        else:
            score -= PENALTY
            print(f"Incorrect. Your score: {score}")

    print(f"Quiz over! Your final score: {score}")


if __name__ == "__main__":
    start_quiz()

"""Dice Roller, by Al Sweigart al@inventwithpython.com
Simulates dice rolls using the Dungeons & Dragons dice roll notation.
This code is available
at https://nostarch.com/big-book-small-python-programming
Tags: short, simulation"""

# dice.py
import random

# Dice representations (visuals as strings and corresponding values)
DICE = {
    1: [
        '+-------+',
        '|       |',
        '|   O   |',
        '|       |',
        '+-------+'
    ],
    2: [
        '+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'
    ],
    3: [
        '+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'
    ],
    4: [
        '+-------+',
        '| O   O |',
        '|       |',
        '| O   O |',
        '+-------+'
    ],
    5: [
        '+-------+',
        '| O   O |',
        '|   O   |',
        '| O   O |',
        '+-------+'
    ],
    6: [
        '+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'
    ]
}


def roll_dice(number_of_dice, number_of_sides, modifier=0):
    """Rolling dice"""
    rolls = [random.randint(1, number_of_sides) for _ in range(number_of_dice)]
    total = sum(rolls) + modifier
    return rolls, total


def print_dice(rolls):
    """Demonstrating current dice"""
    for roll in rolls:
        print("\n".join(DICE[roll]))

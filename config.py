"""Constants for code"""

# config.py
# Configuration constants

DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3  # -3 for room to enter the sum at the bottom.

QUIZ_DURATION = 30  # Duration of the quiz in seconds
MIN_DICE = 2  # Minimum number of dice
MAX_DICE = 6  # Maximum number of dice

REWARD = 4  # Points awarded for correct answers
PENALTY = 1  # Points removed for incorrect answers

# Ensure the maximum dice fit on the screen
assert MAX_DICE <= 14

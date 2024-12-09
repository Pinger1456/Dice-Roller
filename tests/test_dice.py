"""tests/test_dice.py"""

import unittest
from dice import roll_dice


class TestDiceRoll(unittest.TestCase):
    """Class for testing"""
    def test_roll_dice(self):
        """Method test for constants"""
        rolls, total = roll_dice(3, 6)
        self.assertEqual(len(rolls), 3)
        self.assertTrue(all(1 <= roll <= 6 for roll in rolls))
        # Total should be within expected range
        self.assertTrue(3 <= total <= 18)


if __name__ == "__main__":
    unittest.main()

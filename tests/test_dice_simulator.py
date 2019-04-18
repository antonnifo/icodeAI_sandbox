from unittest import TestCase
from dice_simulator import roll_dice

class TestRollDiceTestCase(TestCase):
  
    def test_roll_dice(self):

        for n in range(1,100):
            self.assertIn(
            roll_dice(), [x for x in range(1,7)]
        )

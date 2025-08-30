import unittest
from core.dice import Dice

class TestDice(unittest.TestCase):

    def test_init_last_roll_is_zero_zero(self):
        dice = Dice()
        self.assertEqual(dice.__last_roll__, (0, 0))

    def test_roll_returns_two_values_between_1_and_6(self):
        dice = Dice()
        r = dice.roll()
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 2)
        self.assertTrue(all(1 <= v <= 6 for v in r))

    def test_roll_updates_internal_state(self):
        dice = Dice()
        result = dice.roll()
        self.assertEqual(dice.__last_roll__, result)


    def test_get_last_roll_after_roll(self):
        dice = Dice()
        rolled = dice.roll()
        self.assertEqual(dice.get_last_roll(), rolled)

    def test_set_last_roll_accepts_valid_values(self):
        dice = Dice()
        dice.set_last_roll((3, 5))
        self.assertEqual(dice.get_last_roll(), (3, 5))
        dice.set_last_roll((0, 0))
        self.assertEqual(dice.get_last_roll(), (0, 0))

    def test_set_last_roll_rejects_invalid_values(self):
        dice = Dice()
    
        with self.assertRaises(ValueError):
            dice.set_last_roll((7, 1))
        
        with self.assertRaises(ValueError):
            dice.set_last_roll((1,))
       
        with self.assertRaises(ValueError):
            dice.set_last_roll("2,2")

if __name__ == "__main__":
    unittest.main()

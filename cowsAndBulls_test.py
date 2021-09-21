#  ToRun
#  pytest .\cowsAndBulls_test.py

import unittest
from cowsAndBullsFunctions import check_guess, generate_random_number

class RandomNumberTestCase(unittest.TestCase):
    def test_cows_and_bulls_generate_random_number(self):
        result = generate_random_number()
        self.assertEqual(len(result), 4)

class GuessCheckTestCase(unittest.TestCase):
    def test_cows_and_bulls_check_guess(self):
        self.assertEqual(check_guess([4,5,6,7],[4,1,2,3]), (0, 1))
        self.assertEqual(check_guess([4,5,6,7],[9,1,2,3]), (0, 0))
        self.assertEqual(check_guess([4,5,6,7],[9,4,2,3]), (1, 0))
        self.assertEqual(check_guess([4,5,6,7],[4,5,6,7]), (0, 4))
        self.assertEqual(check_guess([4,5,6,7],[4,5,7,6]), (2, 2))


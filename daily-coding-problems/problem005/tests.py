import unittest
from solution.solution import *

class Tests(unittest.TestCase):
    def test_simple_cases(self):
        pair = cons(1, 2)
        self.assertEqual(car(pair), 1)
        self.assertEqual(cdr(pair), 2)

        self.assertEqual(car(cons(3,4)), 3)
        self.assertEqual(cdr(cons(3,4)), 4)

if __name__ == "__main__":
    unittest.main()
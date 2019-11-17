import unittest
from solution.solution import *

class Tests(unittest.TestCase):
    def tests_basic(self):
        self.assertEqual(solve('12'), 2)
        self.assertEqual(solve('123'), 3)
        self.assertEqual(solve('1234'), 3)
        self.assertEqual(solve('111'), 3)
        self.assertEqual(solve('1111'), 5)

if __name__ == "__main__":
    unittest.main()
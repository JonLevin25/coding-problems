import unittest
from solution.solution import *

class Tests(unittest.TestCase):
    def test_empty_array(self):
        self.assertFalse(solve([], 0))
        self.assertFalse(solve([], -1))
        self.assertFalse(solve([],-1))
        self.assertFalse(solve([],1))
        pass

    def test_single_item_arrays(self):
        self.assertFalse(solve([0],0))
        self.assertFalse(solve([314],314))
        self.assertFalse(solve([1],0))
        self.assertFalse(solve([-1],0))
        self.assertFalse(solve([314],7))
        pass

    def test_multi_item_arrays(self):
        self.assertTrue(solve([1, 2, 3],3))
        self.assertTrue(solve([1, 2, 3],4))
        self.assertTrue(solve([1, 2, 3],5))
        
        self.assertFalse(solve([1, 2, 3],1))
        self.assertFalse(solve([1, 2, 3],2))
        self.assertFalse(solve([1, 2, 3],6))
        self.assertFalse(solve([1, 2, 3],-3))
        pass


if __name__ == "__main__":
    unittest.main()
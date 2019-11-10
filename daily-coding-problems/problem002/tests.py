import unittest
from typing import List
from solution.solution import solve, solve_without_division

def test(test_object: unittest.TestCase, in_arr: List[int], expected_out: List[int]):
    test_object.assertEqual(solve(in_arr), expected_out)

class Tests(unittest.TestCase):
    def test_regular(self):
        test(self, [1, 2, 3, 4], [24, 12, 8, 6, 2])

    def test_edgecase_product_zero(self):
        test(self, [1], [0])
        test(self, [3, -5, -2], [10, -6, -15])
    def test_edgecase_zero_element(self):
        test(self, [0], [0])
        test(self, [0, 1], [1, 0])
        test(self, [1, 0, 1], [0, 1, 0])

if __name__ == "__main__":
    unittest.main()
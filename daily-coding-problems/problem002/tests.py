import unittest
from typing import List
from solution.solution import solve

def test(test_object: unittest.TestCase, in_arr: List[int], expected_out: List[int]):
    test_object.assertEqual(solve(in_arr), expected_out)

def test_raises(test_object: unittest.TestCase, in_arr: List[int], expected_error: type):
    with test_object.assertRaises(expected_error):
        solve(in_arr)

class Tests(unittest.TestCase):
    def test_regular(self):
        test(self, [1, 2, 3, 4], [24, 12, 8, 6])
        test(self, [1, 1, 1, 1], [1, 1, 1, 1])
        test(self, [-1, 1, 1, 1], [1, -1, -1, -1])

    def test_edgecase_product_zero(self):
        test(self, [1, -1], [-1, 1])
        test(self, [3, -5, -2], [10, -6, -15])

    def test_invalid_input(self):
        test_raises(self, [], ValueError)
        test_raises(self, [0], ValueError)
        test_raises(self, [-2], ValueError)
        test_raises(self, [4], ValueError)

    def test_edgecase_one_zero_element(self):
        test(self, [0, 1], [1, 0])
        test(self, [1, 0, 1], [0, 1, 0])

    def test_edgecase_multiple_zero_elements(self):
        test(self, [0, 0], [0, 0])
        test(self, [0, 1, 4, 0], [0, 0, 0, 0])
        test(self, [5, 1, -4, 0, 0], [0, 0, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()
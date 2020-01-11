import unittest
from typing import List
from solution.solution import *


def test(test_runner: unittest.TestCase, arr: List[int], expected: int):
    result = solve(arr)
    test_runner.assertEqual(result, expected)


class Tests(unittest.TestCase):
    def test_problem_examples(self):
        test(self, [3, 4, -1, 1], 2)
        test(self, [1, 2, 0], 3)
        test(self, [4, 3, 2, 1], 5)
        test(self, [4, 1, 3, 2], 5)
        test(self, [4, 0, 2, 1, 4, 9], 3)
        test(self, [3, 0, 2, 1, 3, 9], 4)

    def test2(self):
        pass

if __name__ == "__main__":
    unittest.main()
import unittest
from typing import List
from solution.solution import *


def test(test_runner: unittest.TestCase, arr: List[int], expected: int):
    result = solve(arr)
    test_runner.assertAlmostEqual(result, expected)


class Tests(unittest.TestCase):
    def test_problem_examples(self):
        test(self, [3, 4, -1, 1], 2)
        test(self, [1, 2, 0], 3)

    def test2(self):
        pass

if __name__ == "__main__":
    unittest.main()
import unittest
from solution.solution import *


def test_split_success(n, count, correct_p1, correct_p2):
    p1, p2 = split(n, count)
    assert p1 == correct_p1
    assert p2 == correct_p2

class TestSplit(unittest.TestCase):

    def test_split1(self):
        test_split_success(492, 1, 4, 92)
        test_split_success(492, 2, 49, 2)
    
    def test_failures(self):
        self.assertRaises(ValueError, split, 492, 0)
        self.assertRaises(ValueError, split, 492, -1)
        self.assertRaises(TypeError, split, 492, 'a')
        self.assertRaises(TypeError, split, 'asf', 2)


class TestSolution(unittest.TestCase):
    def test1(self):
        assert count_decode_perm(1) == 1
        assert count_decode_perm(11) == 2
        assert count_decode_perm(91) == 1
        assert count_decode_perm(99) == 1
        assert count_decode_perm(10) == 1
        assert count_decode_perm(20) == 1
        assert count_decode_perm(22) == 2
        assert count_decode_perm(26) == 2
        assert count_decode_perm(27) == 1

    def test2(self):
        assert count_decode_perm(111) == 3
        assert count_decode_perm(191) == 2
        assert count_decode_perm(272) == 1

    
    
import unittest
from solution.solution import *

class Tests(unittest.TestCase):
    def test1(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        self.assertEqual(deserialize(serialize(node)).left.left.val, 'left.left')

if __name__ == "__main__":
    unittest.main()
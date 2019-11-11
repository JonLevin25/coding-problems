import unittest
from solution.solution import *


class Tests(unittest.TestCase):


    def test1(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        self.assertEqual(deserialize(serialize(node)).left.left.val, 'left.left')

    def test_semicolons_in_value(self):
        orig_node = Node('r;oot', Node('left'), Node('right'))
        node = deserialize(serialize(orig_node))
        assert node.val == 'r;oot'
        assert node.left.val == 'left'
        assert node.left.left == None

if __name__ == "__main__":
    unittest.main()
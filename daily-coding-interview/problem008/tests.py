import unittest
from solution.solution import *
from queue import Queue


def left_setter(parent_node):
    def assign(node):
        parent_node.left = node
    return assign

def right_setter(parent_node):
    def assign(node):
        parent_node.right = node
    return assign

def create_tree(*args):
    open_spots = Queue()
    root = None
    for n in args:
        if not isinstance(n, int) and n is not None:
            raise TypeError("All args should be int or None!")
        
        if root == None:
            root = TreeNode(n)
            open_spots.put(left_setter(root))
            open_spots.put(right_setter(root))
            continue
        
        if len(open_spots) == 0:
            raise ValueError
        
        next_node_setter = open_spots.get()
        if n is None:
            continue
        
        new_node = TreeNode(n)
        next_node_setter(new_node)
        open_spots.put(left_setter(new_node))
        open_spots.put(right_setter(new_node))

    return root


        

class TestCreateTree(unittest.TestCase):
    def test(self):
        tree = create_tree(3, 4, 5)
        
        assert tree.value == 3
        
        assert tree.left is not None
        assert tree.left == 4
        
        assert tree.right is not None
        assert tree.right == 5



if __name__ == '__main__':
    unittest.main()
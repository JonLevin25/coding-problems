from typing import Tuple

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_unival(root: TreeNode) -> int:
    return _count_unival(root)[0]


def _count_unival(node: TreeNode) -> Tuple[int, bool]:
    ''' return an int counting the number of unival trees in children, 
        plus a boolean conveying whether this node is itself a unival tree all the way down '''
    if node == None:
        return (0, True)

    # add each child node if it has the same value 
    left_univals, left_is_unival = _count_unival(node.left)
    right_univals, right_is_unival = _count_unival(node.right)

    is_unival = child_unival_relevant(node, node.left) \
    and child_unival_relevant(node, node.right) \
    and left_is_unival and right_is_unival

    return (left_univals + right_univals + int(is_unival), is_unival)


def child_unival_relevant(node: TreeNode, child: TreeNode):
    ''' Check whether a child value can be counted towards 
    the parent being a unival tree (if the )'''
    if not node:
        raise ValueError("Parent node given must have value!")
    if not child:
        return True
    return node.val == child.val
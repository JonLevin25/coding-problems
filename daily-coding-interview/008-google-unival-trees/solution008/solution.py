class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    def is_leaf(self):
        return self.left == None and self.right == None

# TODO: document
def count_unival_trees(node):
    def is_unival_tree(val, left_val, right_val):
        return left_val in (val, None) and right_val in (val, None)
    
    if node.is_leaf():
        return (1, node.value)
    left_count, left_value = count_unival_trees(node.left)
    right_count, right_value = count_unival_trees(node.left)

    is_unival = is_unival_tree(node.value, left_value, right_value)
    return left_count + right_count + (1 if is_unival else 0)
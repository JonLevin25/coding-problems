import unittest
from solution.solution import *

class Tests(unittest.TestCase):
    def test1(self):
        tree = TreeNode(0,
            TreeNode(1),
            TreeNode(0,
                TreeNode(1,
                    TreeNode(1),
                    TreeNode(1)),
                TreeNode(0)))
        self.assertEqual(count_unival(tree), 5)

    def test2(self):
        tree = TreeNode(0)
        self.assertEqual(count_unival(tree), 1)
    def test3(self):
        tree = TreeNode(0, TreeNode(1), TreeNode(1))
        self.assertEqual(count_unival(tree), 2)

    def test4(self):
        tree = \
        TreeNode(1, 
            TreeNode(1,
                TreeNode(1,
                    TreeNode(0),
                    TreeNode(0)),

                TreeNode(1, 
                    None, 
                    TreeNode(0)
                )
            ),
            TreeNode(1,
                TreeNode(1,
                    TreeNode(0),
                    TreeNode(0)),
                TreeNode(1, 
                    None, 
                    TreeNode(0))
            )
        )
        self.assertEqual(count_unival(tree), 6)

if __name__ == "__main__":
    unittest.main()
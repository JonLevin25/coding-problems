import unittest
from solution.solution import WordTreeNode, build_word_tree, autocomplete

class Tests(unittest.TestCase):
    def test_tree_1(self):
        root = build_word_tree({'deer', 'dea', 'deeesus', 'deer'})
        pass

    def test2(self):
        pass

if __name__ == "__main__":
    unittest.main()
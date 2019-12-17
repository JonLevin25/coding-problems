import unittest
from solution.solution import WordTreeNode, build_word_tree, autocomplete
from typing import Set

def validate_tree_node(\
    tester: unittest.TestCase, \
    node: WordTreeNode, \
    expected_words: Set[str], \
    expected_children: Set[str]):
    
    tester.assertSetEqual(node.words, expected_words)
    tester.assertSetEqual(set(node.children.keys()), expected_children)

class Tests(unittest.TestCase):
    def testTree1(self):
        root = build_word_tree({'deer', 'dea', 'deeesus', 'deer'}, )

        # Tree built:      root
        #                   |
        #                   de  --- {'dea'}
        #                /     \
        #  {'deer'} --- er     ee    
        #                       |
        #                       su --- {'deeesus'}
        
        # validate root node
        validate_tree_node(self, root, set(), {'de'})

        # validate de node
        de_node = root.children['de']
        validate_tree_node(self, de_node, {'dea'}, {'ee', 'er'})
        
        # validate de -> er node
        deer_node = de_node.children['er']
        validate_tree_node(self, deer_node, {'deer'}, set())

        # validate de -> ee node
        deee_node = de_node.children['ee']
        validate_tree_node(self, deee_node,set(), {'su'})

        # validate de -> ee -> su node
        deeesu_node = deee_node.children['su']
        validate_tree_node(self, deeesu_node, {'deeesus'}, set())

    def testAutoComplete(self):
        results_list = list(autocomplete('de', {'dog', 'deer', 'deal', 'frog', 'deer', 'dealer', 'dealers', 'dealership'}))
        results_set = set(results_list)
        self.assertEqual(len(results_list), len(results_set)) # no duplicates
        self.assertSetEqual(results_set, {'deer', 'deal', 'dealer', 'dealers', 'dealership'})

    def testAutoComplete2(self):
        results_list = list(autocomplete('dea', 
        {'de', 'deb',
         'dea', 'deaa',
         'deal', 'deala', 'dealaa', 'dealer',
         'deer'}))

        results_set = set(results_list)
        self.assertEqual(len(results_list), len(results_set)) # no duplicates
        self.assertSetEqual(results_set, {'dea', 'deaa', 'deal', 'deala', 'dealaa', 'dealer'})

    def testAutoCompleteMissing(self):
        # TODO: create tree
        # TODO: ask for word not in tree
        # TODO: assert no words returned
        # TODO: assert tree was not changed
        pass

if __name__ == "__main__":
    unittest.main()
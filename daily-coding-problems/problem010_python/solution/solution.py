from typing import Set, Iterator, List, Dict

class WordTreeNode:
    words: List[str]
    children: Dict[str, WordTreeNode]

    def __init__(self, str, words: List[str], children: Dict[str, WordTreeNode] = None):
        self.words = words
        self.children = children


def build_word_tree(word_set: Set[str], chars_per_branch: int = 2):
    # TODO: optimize using word sorting?
    # sorted_words: List[str] = sorted(word_set)
    root_node = WordTreeNode("", None, None)
    for word in word_set:
        prefix_len = 0
        word_node = root_node

        while prefix_len + chars_per_branch < max_prefix_len:
            new_prefix = word[prefix_len: prefix_len + 2]
            prefix_len += 2
            

        dict_levels = len(word) / chars_per_branch # the number of nested dicts I'll need
        


    #  # Create dependant dictionaries until chars in word < chars per branch 
    #  # (ie. for 'deer' create <root>['de']['er'])
    #  # add word to bucket
    pass

def autocomplete(inp_str: str, word_set: Set[str]):
    pass

def _autocomplete(inp_str: str, tree_root: WordTreeNode):
    inp_len = len(inp_str)
    curr_prefix = ""

    while len(curr_prefix) <= inp_len:
        # TODO: edge case: at root of tree, found no child relevant
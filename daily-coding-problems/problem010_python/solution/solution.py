from typing import Set, Iterator, List, Dict

class WordTreeNode:
    words: Set[str]
    children: Dict # Dict[str, WordTreeNode]

    def __init__(self, str, words: List[str] = None, children: Dict = None):
        self.words = {word for word in words} if words else set()
        self.children = children if children else dict()

    def add_to_tree(self, word: str, split_len: int):
        word_node = self
        prefix_len = 0

        # Create dependant dictionaries
        while prefix_len + split_len <= len(word):
            new_prefix = word[prefix_len : prefix_len + split_len]
            prefix_len += split_len
            
            # add dict if doesn't exist
            if not new_prefix in word_node.children.keys():
                word_node.children[new_prefix] = WordTreeNode(new_prefix)
            word_node = word_node.children[new_prefix]
        
        # add word to final dict
        word_node.words.add(word)

    def __iter__(self):
        yield from self.words
        yield from (word for word in child.words for child in self.children)


def build_word_tree(word_set: Set[str], split_len: int = 2) -> WordTreeNode:
    # TODO: optimize using word sorting?
    # sorted_words: List[str] = sorted(word_set)
    root_node = WordTreeNode("", None, None)
    for word in word_set:
        root_node.add_to_tree(word, split_len)
    
    return root_node


def get_leaf_node(input_str: str):
    ''' Gets the inner-most node that contains the input string '''
    pass

# NOTE: this is inefficient, but in real world scenario word tree would be built once
# so I consider _autocomplete to be the real time complexity of this algorithm
def autocomplete(inp_str: str, word_set: Set[str]):
    word_tree = build_word_tree(word_set)
    return _autocomplete(inp_str, word_tree)

def _autocomplete(inp_str: str, tree_root: WordTreeNode):
    inp_len = len(inp_str)
    curr_prefix = ""

    while len(curr_prefix) <= inp_len:
        # TODO: edge case: at root of tree, found no child relevant
        raise NotImplementedError
    raise NotImplementedError
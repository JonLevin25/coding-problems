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

    def find_words_with_prefix(self, prefix: str, split_len: int) -> Iterator[str]:
        word_node = self
        prefix_len = 0

        # follow tree "path" until reach closest node to prefix.
        while prefix_len + split_len <= len(prefix):
            new_prefix = prefix[prefix_len : prefix_len + split_len]
            prefix_len += split_len
            
            # path missing- no words exist
            if not new_prefix in word_node.children.keys():
                raise StopIteration
            word_node = word_node.children[new_prefix]

        # prefix is exactly current tree "path". Yield everything below
        if prefix_len == len(prefix):
            yield from self
            raise StopIteration

        # prefix is longer then current tree "path". Filter and yield
        # filter words and yield
        yield from (word for word in word_node if word.startswith(prefix))
        
        # filter children and yield
        remaining_prefix = prefix[prefix_len:]
        filtered_child_keys = (key for key in self.children if key.startswith(remaining_prefix))
        filtered_children = (self.children[key] for key in filtered_child_keys)
        for child in filtered_children:
            yield from child



    def __iter__(self) -> Iterator[str]:
        for child in self.children.values():
            yield from child.words
        yield from self.words


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
def autocomplete(inp_str: str, word_set: Set[str]) -> Iterator[str]:
    split_len = 2
    word_tree = build_word_tree(word_set, split_len)
    return _autocomplete(inp_str, word_tree, split_len)

def _autocomplete(inp_str: str, tree_root: WordTreeNode, split_len: int) -> Iterator[str]:
    yield from tree_root.find_words_with_prefix(inp_str, split_len)
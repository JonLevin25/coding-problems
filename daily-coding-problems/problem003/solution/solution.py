from typing import Iterator, Tuple, Dict, List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NodeReference:
    def __init__(self, id, val, left_id, right_id):
        self.id = id
        self.val = val
        self.left_id = left_id
        self.right_id = right_id


def serialize(tree: Node) -> str:
    result = ""
    
    # Could use any traversal, serialization doesn't care
    for node in preorder_traverse(tree):
        result += f"{serialize_single(node)};"

    result = result[:-1] # remove last semicolon (;)
    return result

def deserialize(treeStr: str) -> Node:
    references = list(deserialize_single(node_str) for node_str in treeStr.split(";"))
    root_id = references[0].id
    ref_dict = {ref.id : ref for ref in references}
    return _deserialize(root_id, ref_dict)

def _deserialize(node_id: int, ref_dict: Dict[int, NodeReference]) -> Node:
    if node_id == 0:
        return None
    node_ref = ref_dict[node_id]

    left_ref = _deserialize(node_ref.left_id, ref_dict)
    right_ref = _deserialize(node_ref.left_id, ref_dict)
    return Node(node_ref.val, left_ref, right_ref)

def serialize_single(node: Node) -> str:
    if node is None:
        return f"0,0,0|"
    return f"{guid(node)},{guid(node.left)},{guid(node.right)}|{node.val}"

# TODO: escape semicolons in value
def deserialize_single(s: str) -> NodeReference:
    (ids, value) = s.split("|", maxsplit=1) # should support pipe characters in node value
    (node, left, right) = ids.split(",")
    return NodeReference(int(node), value, int(left), int(right))

def preorder_traverse(node: Node) -> Iterator[Node]:
    yield node
    if node is not None:
        yield from preorder_traverse(node.left)
        yield from preorder_traverse(node.right)

def guid(node: Node):
    return id(node) if node else 0

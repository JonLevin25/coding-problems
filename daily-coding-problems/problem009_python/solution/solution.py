from typing import List, Tuple, Callable

class ListItem:
    def __init__(self, idx: int, value: int):
        self.idx = idx
        self.value = value

    def __repr__(self):
        return f"(idx: {self.idx}, value: {self.value})"

    def __gt__(self, item2):
        return self.value > item2.value


class LargestList:
    #TODO: make generic?
    def __init__(self, size: int):
        self.list: List[ListItem] = []
        self.size: int = size

    def tryAdd(self, item: ListItem):
        for i in range(0, self.size):
            if len(self.list) < i + 1:
                self.list.append(item)
                return
            elif item > self.list[i]:
                self.list.insert(i, item)
                self._remove_excess()
                return

    def _remove_excess(self):
        delta = len(self.list) - self.size
        if delta <= 0:
            return
        for i in range(delta):
            self.list.pop()

    def __getitem__(self, i: int):
        return self.list[i]

# TODO: NOT PASSING. Added testcase to demonstrate
def max_non_neighbor_sum(arr: List[int]) -> int:
    # 1. get the largest 4 numbers in the array
    largest = LargestList(4)
    for i in range(len(arr)):
        largest.tryAdd(ListItem(i, arr[i]))
    
    # possible sums (assuming largest = [a, b, c, d] where a is the largest, b 2nd largest etc...):
    # a+b, a+c, b+c, a+d (b+d is irrelevant, proof omitted)
    
    # (if largest two values are not neighbors, they're definitely the largest.
    if not are_neighbors(largest[0], largest[1]):
        return largest[0].value + largest[1].value

    # assume input larger than 2, because then the solution would be undefined
    # otherwise, check all other possible pairs, filter only those that are not neighbors, return max
    possible_pairs = [
        (largest[0], largest[2]),  
        (largest[1], largest[2])]

    if len(arr) > 3:
        possible_pairs.append((largest[0], largest[3]))

    return max((i1.value + i2.value for (i1,i2) in possible_pairs if not are_neighbors(i1, i2)))

    


    # if first two are not neighbors- their sum is definitely largest
    


def are_neighbors(i1: ListItem, i2: ListItem) -> bool:
    idx1 = i1.idx
    idx2 = i2.idx
    return abs(idx1 - idx2) == 1
    

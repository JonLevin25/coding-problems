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
        largest.tryAdd((i, arr[i]))

    # 2. find largest non-neighboring in largest list
    


    # if first two are not neighbors- their sum is definitely largest
    


def are_neighbors(idx1: int, idx2: int) -> bool:
    return abs(idx1 - idx2) == 1
    

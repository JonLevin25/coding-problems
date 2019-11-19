from typing import List, Tuple, Callable

class LargestList:
    #TODO: make generic?
    def __init__(self, size: int, largerThanFunc):
        self.list: List[Tuple[int, int]] = []
        self.size: int = size
        self.largerThanFunc: Callable[Tuple[int, int], bool] = largerThanFunc

    def tryAdd(self, item):
        if len(self.list) == 0:
            self.list.append(item)
            return
        for i in range(0, self.size):
            # if list empty at this point: add item here
            # TODO: if list should support None as an item in the future, add support
            if self.list[i] == None:
                self.list[i] = item
                return

            elif self.largerThanFunc(item, self.list[i]):
                self.list.insert(i, item)
                self._remove_excess()
                return

    def _remove_excess(self):
        delta = len(self.list) - self.size
        if delta <= 0:
            return
        for i in range(delta):
            self.list.pop()

# TODO: NOT PASSING. Added testcase to demonstrate
def max_non_neighbor_sum(arr: List[int]) -> int:
    
    # 1. get the three largest numbers in the array
    def compare_tuples(idx_val_tup1, idx_val_tup2):
        return idx_val_tup1[1] > idx_val_tup2[1]
    
    largest = LargestList(3, compare_tuples)
    for i in range(len(arr)):
        largest.tryAdd((i, arr[i]))

    # 2. find largest non-neighboring in largest list

    # if first two are not neighbors- their sum is definitely largest
    ((i1, val1), (i2, val2), (i3, val3)) = largest.list

    if not are_neighbors(i1, i2):
        return val1, val2
    

    sum13 = val1 + val3
    sum23 = val2 + val3

    if are_neighbors(i1, i3):
        return sum23
    elif are_neighbors(i2, i3):
        return sum13
    
    return max(sum13, sum23)
    


def are_neighbors(idx1: int, idx2: int) -> bool:
    return abs(idx1 - idx2) == 1
    

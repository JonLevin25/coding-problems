from typing import List
from functools import reduce

def solve(arr: List[int]) -> int:
    # High level:
    # (1) Find min:= minimum of all *positive* numbers in array  | Time: O(n) | Space: O(1) [one variable, one iteration]
    # (2) if min > 1: return 1                                   | Time: O(1) | Space: O(1)
    # (3) "Sort" array to form [1, 2, 3, ..., n-1]               | Time: O(n) | Space: O(1) [modify array in place, one iteration]
    #     but with zeros for any number NOT found in the array (O(n))
    #     e.g. [6, 1, 2, 4, 3] will become [1, 2, 3, 4, 0]
    # (4) iterate over array, if 0 element: return index + 1     | Time: O(n) | Space: O(1)
    #     in example: 0 is at index 4: return 5
    # (5) if no 0 encountered: return array length + 1           | Time: O(1) | Space: O(1)
    #
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    # (1)
    min_positive = reduce(lambda min, x: x if pos(x) and x < min else min, arr, len(arr) + 1)

    # (2)
    if min_positive > 1:
        return 1

    # (3)
    sortof_sort_array(arr, min_positive)

    # (4)
    for i in range(len(arr)):
        if arr[i] == 0: return i + 1
    
    # (5)
    return len(arr) + 1

# TODO: this doesn't work since I'm modifying elements of the array I haven't accessed yet. (So I never actually process them)
# TODO: try to find solution to this problem within constraints
def sortof_sort_array(arr: List[int], min_positive: int):
    def idx_in_range(i):
        return i >= 0 and i < len(arr)

    for i in range(len(arr)):
        val = arr[i]

        # check if this index was already "sorted"
        # if it isn't- set it as "missing" (0 value)
        curr_idx_sorted = val == i + 1
        if (not curr_idx_sorted):
            arr[i] = 0

        # sort the value found to it's "correct" index, if within bounds
        target_idx = val - 1
        if idx_in_range(target_idx):
            arr[target_idx] = val


def pos(x): return x > 0

    
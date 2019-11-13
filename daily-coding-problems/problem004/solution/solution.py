from typing import List

def solve(arr: List[int]) -> int:
    pass

    # High level:
    # 1) Find min:= minimum of all *positive* numbers in array
    # 2) if min > 1: return 1
    # 3) Rewrite array to form [1, 2, 3, ..., n-1], but with zeros for any number NOT found in the array
    #    e.g. [6, 1, 2, 4, 3] will become [1, 2, 3, 4, 0, 6]
    # 4) go through array, if you reach a 0: return the index + 1 (in example: 0 is at index 4: return 5)
    # 5) if no 0 encountered: return array length + 1

    
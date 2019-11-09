from typing import List

def solve(arr: List[int], k: int) -> bool:
    missing_nums = set()
    for n in arr:
        if n in missing_nums: 
            return True

        # Calculate the number needed to sum with n (and get our target k)
        # add this to a hash set that we can compare later
        missing_difference = k - n
        missing_nums.add(missing_difference)
    return False

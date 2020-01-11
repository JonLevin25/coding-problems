from typing import List

def solve(arr: List[int], debug: bool = False) -> int:
    ''' see solution_doc.md for algorithm description '''
    n = len(arr)

    if debug: print(f"0) Solve: input: {arr}")
    
    # (1) Clean array
    for i in range(n):
    """ Possible optimization: in certain scenarios you might want to keep a flag for whether 1 was found here, 
    and if not return 1 without running step (2). You could technically keep m flags
    for the first m natural numbers, but you get diminishing returns for each flag added
    """
        if arr[i] < 0 or arr[i] > n:
            arr[i] = 0
    
    if debug: print(f"1) Solve: cleaned: {arr}")

    # (2) map array
    map_array(arr, n)
    
    if debug: print(f"2) Solve: mapped: {arr}")

    # (3)
    for i in range(len(arr)):
        if arr[i] == 0: 
            print(f"3) Solve: found: {i+1}")
            return i + 1
    
    # (4)
    if debug: print(f"4) Solve: finished: {i+1}")
    return len(arr) + 1

def map_array(cleaned_arr, n):
    for i in range(n):
        x = cleaned_arr[i]
        expected = i+1

        if x == 0:
            continue

        # If negative, <expected> was found previously in the array.
        # Extract previous value and set element to final expected value
        if x < 0:
            x *= -1
            cleaned_arr[i] = expected
        else:
            # if i+1 value wasn't previously found and it's not a fixed point, set 0
            cleaned_arr[i] = 0

        # We have what we came for - set and continue
        if x == expected:
            cleaned_arr[i] = expected
            continue
        
        target_idx = x-1
        other_x = cleaned_arr[target_idx]

        # if we're "going back" - then <target_idx> has already been handled
        # and is either 0 or the target number. Overwrite in both cases
        if target_idx < i:
            cleaned_arr[target_idx] = x
            continue

        # if set to negative - x has already been found, continue
        elif other_x < 0:
            continue

        # if x hasn't been found yet, encode it into arr[target_idx]
        if other_x == 0:
            cleaned_arr[target_idx] = x
        else:
            cleaned_arr[target_idx] = -other_x

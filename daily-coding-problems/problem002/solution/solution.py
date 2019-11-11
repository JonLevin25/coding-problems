from typing import List, Iterator, Callable
from functools import reduce
from itertools import repeat


def naive_solution(arr: List[int]) -> List[int]:
    '''Get product, then divide each member of array from that product. 
    Works if you have no zeros in the array
    '''

    product = get_product(arr)
    return [product / x for x in arr]


def solve(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        raise ValueError("Expected array with at least two values")

    # Could save iteration by counting zeros as we go (time complexity is O(n) regardless)
    # But I think it's more elegant and readble this way.
    zeros = arr.count(0)

    # If there's more than one zero, the results will all be zero
    if zeros > 1:
        return list_of_zeros(len(arr))

    # if there's exactly one zero in the array, everything *except* that zero will become zero.
    # the zero will become the product of everything else
    if zeros == 1:
        product = get_product_ignore_zeros(arr)
        return [0 if n != 0 else product for n in arr]
    
    # If no zeros found
    return naive_solution(arr)


def get_product_ignore_zeros(arr: List[int]):
    '''Get the product for all non-0 ints in the array'''
    return get_product((n for n in arr if n != 0))


def get_product(arr: Iterator[int]) -> int:
    return reduce(lambda acc, n: acc * n, arr, 1)


def list_of_zeros(count: int) -> List[int]:
    return list(repeat(0, count))


# Bonus: solving without division:
# You can replace division with negative power, i.e. x / y == x * (y ** -1)
# This feels a bit like cheating since its practically division.
#
# Also you could probably use the definition of addition (a * 3 = a + a + a etc.) in some way
# There's probably a better solution
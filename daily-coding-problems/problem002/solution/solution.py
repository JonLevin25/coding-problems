from typing import List, Iterator, Callable
from functools import reduce
from itertools import repeat
import operator

def solve(arr: List[int]) -> List[int]:
    return _solve(lambda x, y: x / y, arr)

# problem: [0, 1] => [0, 1]
def _solve(divisionFunc: Callable[[int, int], float], arr: List[int]) -> List[int]:
    if len(arr) < 2:
        raise ValueError("Expected array with at least two values")

    # Could save an iteration by counting zeros we go (time complexity will remain O(n) regardless)
    # But I think it's more elegant and readble this way.
    zeros = arr.count(0)

    # If there's more than one zero, products for any item (excluding themselves) will be 0
    if zeros > 1:
        return list(repeat(0, len(arr)))

    if zeros == 1:
        product = product_ignore_zeros(arr)
        print(f"ONE ZERO: input: {arr}. product: {product}")
        return [0 if n != 0 else product for n in arr]
    
    # If no zeros found
    product = get_product(arr)
    return [divisionFunc(product, x) for x in arr]

def solve_without_division(arr: List[int]):
    pass

def product_ignore_zeros(arr: List[int]):
    return get_product((n for n in arr if n != 0))

def get_product(arr: Iterator[int]) -> int:
    return reduce(lambda acc, n: acc * n, arr, 1)
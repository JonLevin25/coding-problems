from typing import List
from functools import reduce
import operator

def solve(arr: List[int]):
    product = reduce(operator.mul, arr)
    print("Product: " + str(product))
    return [product / x for x in arr]

def solve_without_division(arr: List[int]):
    pass
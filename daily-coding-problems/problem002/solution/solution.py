from typing import List
from functools import reduce
import operator

def solve(arr: List[int]):
    product = reduce(operator.mul, arr)
    return [x / product for x in arr]

def solve_without_division(arr: List[int]):
    pass
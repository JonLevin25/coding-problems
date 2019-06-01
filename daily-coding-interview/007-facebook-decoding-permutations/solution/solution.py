from math import log, floor

def has_two_perms(n):
    if n < 11: return False
    if n > 26: return False
    if n == 20: return False
    return True

def split(n, count):
    if type(n) != int or type(count) != int: 
        raise TypeError('Split arguments should be ints!')
    if count <= 0 or n <= 0: raise ValueError('Count must be positive!')

    totalDigits = floor(log(n, 10)) + 1

    if count > totalDigits:
        raise ValueError(f'Count must be less than the digits of n! (n: {n}, count: {count}, totalDigits: {totalDigits})')

    divisor = 10 ** (totalDigits - count)

    first_part = n // divisor # the first <count> digits of n
    second_part = n - (first_part * divisor) # the remainder of n's digits
    return first_part, second_part

# TODO: Test
def count_decode_perm(n):
    if n < 10: return 1

    curr, n2 = split(n, 2)
    n1 = split(n, 1)[1]

    if (has_two_perms(curr)):
        return count_decode_perm(n1) + count_decode_perm(n2)

    return count_decode_perm(n1)
def solve(input: str) -> int:
    if not input_valid(input): 
        raise ValueError(f"Input {input} is not valid!")

    if len(input) == 1:
        return repr_count(input)
    
    # split into two options- "1 char parsed" and "2 chars parsed"
    # the number of solutions is the sum of these provided the "chars parsed" are a valid solution
    # e.g. "1234" -> "1", "234"
    parsed1,remaining1 = input[:1], input[1:]
    perms1 = solve(remaining1) if repr_count(parsed1) else 0

    # if only 2 chars remaining - split isn't relevant
    if len(input) == 2:
        return perms1 + repr_count(input)

    parsed2,remaining2 = input[:2], input[2:]
    
    # only count permutations if relevant
    # e.g. for "2933" - count "2", solve("933") but not "29", solve(33) because 29 is invalid
    perms2 = solve(remaining2) if repr_count(parsed2) else 0
    return perms1 + perms2


# returns the number of ways the input can be represented in the system
# valid input- a 1 or 2 digit integer string
def repr_count(inp: str) -> int:
    if len(inp) > 2:
        raise ValueError("has_repr should only be called with inputs that have 1 or 2 digits!")
    
    n = int(inp)
    if n == 0:
        return 0
    if n <= 26:
        return 1
    return 0

def input_valid(input: str) -> bool:
    # TODO
    return True
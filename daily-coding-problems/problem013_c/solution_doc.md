
 1. Naive solution:
    1. define "walk" operation for string: iterate over string counting until 
    2. Walk each character, count substring
    3. For all substring counts, return max
 
 
 
 2. Solution:
    1. Create LinkedList, where each node represents a substring (just the conuts of letters)
       e.g. "add" yields the node a1d2, "addab" yields a2d2b2 (order of letters is irrelevant in node notation)
    2. Foreach   
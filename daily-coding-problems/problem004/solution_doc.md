Key insights:
  - If the array was sorted, you could iterate over it and see where a number is missing
  
  - Since there can be at most n-1 unique numbers in the array, 
    - so either a missing number x where 1 < x < n-1, 
    - or the array has exactly all the numbers between [1, n-1], meaning n is the missing number
  
  - The conclusion of the above is that the result will always be between [1, n] (inclusive)
  
  - Looking at arrays like this: [1, 2, 4, 5, 7, 8, 3, 6], you can see iterating over it you'll
    have to "remember" multiple sequences of numbers that may (or may not) be filled out later.
    The worst case (I think) is where you have no contiguous numbers, meaning n "sequences".
    This is a strong hint that you NEED O(n) space to solve this (or O(n^2) time)
    Since you have O(1) space to work with- that leads to modifying the array in-place

 High level Algorithm:
 (1) Iterate over array, replace any numbers not in the range [1, n] with 0 in-place
 (2) Modify array in-place to an array of flags, where arr[i] is non-zero only if
     the number i+1 was in the original array - explained in detail below.
 (3) iterate over array, if 0 encountered: return index + 1
     in example: 0 is at index 4: return 5
 (4) if no 0 encountered: return array length + 1

Examples:
* Input: [1, 3, 4, 9, -2]
  1)  -> [1, 3, 4, 0, 0]
  2)  -> [1, 0, 1, 1, 0]
  3)  -> 2

* Input: [4, 0, 2, 1, 4, 9]
  1)  -> [4, 0, 2, 1, 4, 0]
  2)  -> [1, 2, 0, 4, 0]
  3)  -> 3

(2): High level mapping:
 * We start with a cleaned array (only numbers between 1 and n inclusive)
 * To know whether a number is missing, we'll sort the numbers in the array, with 0 for missing numbers
 * Starting at 1 means arr[i] will correspond with the number i+1

Encoding:
   * if (arr[i] == 0) => i+1 is missing from the array
   * if (arr[i] == i+1) => i+1 is present in the array
   * if (arr[i] < 0) => ONLY EXISTS DURING SORTING - negative means we found the number i+1, but needed to remember the old value at arr[i]. the old value is the positive version (arr[i] * -1)

  * optimization - keep flags for the first m natural numbers, set if encountered. After | Time: O(1) | Space: O

 Time Complexity: O(n)
 Space Complexity: O(1)
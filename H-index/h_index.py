# Problem description
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.

# If there are several possible values for h, the maximum one is taken as the h-index.

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
from typing import List
# Solution 1
# Sort array the find the n - i where the current citation at index i is >= n - i
# this means that h = n - i (at least h of them have values greater than n - i)
# Otherwise return 0
# Time O(N)
# Constant space
def hIndex(citations: List[int]) -> int:
    n = len(citations)
    citations.sort()
    for i in range(n):
        if citations[i] >= (n - i):
            return n - i
    return 0

print(hIndex([3, 0, 6, 1, 5]))
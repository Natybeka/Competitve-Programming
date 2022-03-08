# Problem description
# You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.
# Return the minimum size of the set so that at least half of the integers of the array are removed.
# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.



# Solution count the frequencies of the elements, sort by value and decrement until size reaches half

from typing import List

from collections import Counter     
def setMinSize(arr: List[int]) -> int:
    counts = Counter(arr)
    counts = list(counts.values())
    counts.sort()


    half = len(arr) // 2
    removalCounter = len(arr)
    operations = 0
    while removalCounter > half:
        operations += 1
        removalCounter -= counts.pop()

    return operations
print(setMinSize([3,3,3,3,5,5,5,2,2,7]))
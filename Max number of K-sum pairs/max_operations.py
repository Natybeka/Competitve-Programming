from typing import List
from collections import Counter
import math
def maxOperations(nums: List[int], k: int) -> int:
    counts = Counter(nums)
    nums.sort()
    left = 0
    right = len(nums) - 1
    no_of_operations = 0
    while left < right:
        
        # if nums[left] * 2 is k floor(count(x) / 2)
        if k / 2 == nums[left]:
            print("Code here")
            no_of_operations += math.floor(counts[nums[left]] / 2)
            left += counts[nums[left]]
            print(right)

        # if k - x is found then min(count(x), count(k - x))
        else:
            pairIndex = find(nums, left + 1, right, k - nums[left])
            print(pairIndex)
            if (pairIndex != -1):
                no_of_operations += min(counts[nums[left]], counts[nums[pairIndex]])
                right = pairIndex
                left += counts[nums[left]]
            else:
                left += 1
    return no_of_operations
# helper find binary search option
def find(arr, start, end, key):
    left = start
    right = end
    mid = start
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] < key:
            left = mid + 1
        elif arr[mid] > key:
            right = mid - 1
        else:
            return mid
    return -1
    
# Another solution
# from collections import Counter
# import math
# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         counts = Counter(nums)
#         result = 0
#         for number in counts:
#             temp = k - number
#             if temp == number:
#                 result += counts[number] // 2
#                 continue
#             if temp in counts.keys() and temp < number:
#                 result += min(counts[number], counts[temp])
#         return result
print(maxOperations([2,2,2,3,1,1,4,1],4))
# Problem description
# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [1], k = 1
# Output: 1

# Example 3:
# Input: nums = [2,-1,2], k = 3
# Output: 3
from pickle import SHORT_BINUNICODE
from typing import List
import collections

# Brute force solution
# Check every posible subarray 
# O(n2)
# def shortestSubArray(nums: List[int], k: int) -> int:
#     N = len(nums)
#     validWindow = float('inf')
#     for i in range(N):
#         sum = nums[i]
#         if sum >= k:
#             validWindow = min(validWindow, 1)
#             continue
#         for j in range(i + 1, N):
#             sum += nums[j]
#             if sum >= k:
#                 validWindow = min(validWindow, j - i + 1)
#                 break
#     return validWindow if validWindow != float('inf') else -1
# Solution 2
def shortestSubArray(nums: List[int], k: int) -> int:
    n = len(nums)
    prefixSum = [0]
    # store the sums of nums upto index i - 1 into an array
    for num in nums:
        prefixSum.append(prefixSum[-1] + num)
    
    ans = n + 1
    monoQueue = collections.deque()
    for i, preSum in enumerate(prefixSum):
        # maintain a monoqueue by keeping it increasing
        while monoQueue and preSum <= monoQueue[-1]:
            monoQueue.pop()
        # If the sum upto index i is greater than or equal k
        # pop from the monoQueue (essentially trying to find smaller windows that satisfy
        # the condition presum >= k)
        while monoQueue and preSum - prefixSum[monoQueue[0]] >= k:
             ans = min(ans, i - monoQueue.popleft())
        monoQueue.append(preSum)

    return ans if ans < n + 1 else -1
print(shortestSubArray([2, -1, 2, 3], 3))
    




 
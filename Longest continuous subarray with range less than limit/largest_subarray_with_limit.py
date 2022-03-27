# Problem description
# Given an array of integers nums and an integer limiInput: nums = [8,2,4,7], limit = 4

# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.
from typing import List
import collections
# Solution
# Two deques for keeping track of the mins and the max
# one deque is increasing monoqueue (finds the minimum)
# The other is decreasing monoqueue (finds the maximum)
# two pointers, move the right pointer until the subarr violates the condition
# if so move the left pointer and adjust the monoqueues
def longestSubarray(nums: List[int], limit: int) -> int:
    n = len(nums)
    maxLength = -1
    minQueue = collections.deque()
    maxQueue = collections.deque()
    left = 0 
    for right in range(n):
        while minQueue and nums[right] <= nums[minQueue[-1]]:
            minQueue.pop()
        while maxQueue and nums[right] >= nums[maxQueue[-1]]:
            maxQueue.pop()

        minQueue.append(right)
        maxQueue.append(right)

        # Check for the limit violation
        while nums[maxQueue[0]] - nums[minQueue[0]] > limit:
            left += 1
            if left > minQueue[0]:
                minQueue.popleft()
            if left > maxQueue[0]:
                maxQueue.popleft()
        maxLength = max(maxLength, right - left + 1)
    return maxLength

print(longestSubarray([8,2,4,7], 4))
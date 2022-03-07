from typing import List
def minPairSum(nums: List[int]) -> int:
    # solution sort and maintain two pointers for the max and the min
    nums.sort()
    left = 0
    right = len(nums) - 1
    maximized = 0
    while left < right:
        tempSum = nums[left] + nums[right]
        maximized = max(maximized, tempSum)
        left += 1
        right -= 1
    return maximized
    
print(minPairSum([3,5,4,2,4,6,3]))
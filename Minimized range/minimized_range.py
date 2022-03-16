from typing import List
def smallestRangeII(nums: List[int], k: int )-> int:
    nums.sort()
    minimized = nums[len(nums) - 1] - nums[0]

    for i in range(len(nums) - 1):
        minimum = min(nums[0] + k, nums[i + 1] - k)
        maximum = max(nums[len(nums) - 1] - k, nums[i] + k)
        minimized = min(minimized, maximum - minimum)
        print(maximum, minimum, minimized)
    return minimized

print(smallestRangeII([1, 3, 10], 4))
# [5 || -1, 6]
# [5 7 ||  6]
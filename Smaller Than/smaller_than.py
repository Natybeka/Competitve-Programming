class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller_than = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[j] < nums[i]):
                    smaller_than[i] += 1
        return smaller_than

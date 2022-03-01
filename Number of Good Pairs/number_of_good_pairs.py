from typing import List
from collections import Counter
# Good pairs defined as nums[i] == nums[j] and i < j
# solution for n appearances of an element in nums n * (n- 1) // 2,
# good pairs can be formed
def numIdenticalPairs(self, nums: List[int]) -> int:

        counts = Counter(nums)
        total = 0
        for num in counts.keys():
            total += counts[num] * (counts[num] - 1) // 2
        return total
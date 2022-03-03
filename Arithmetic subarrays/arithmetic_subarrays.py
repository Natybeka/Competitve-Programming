# problem description
# find arithmetic sequences given array num, left sequence l and right sequence r
# Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
# Output: [true,false,true]
# Explanation:
# In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
# In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
# In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], which is an arithmetic sequence

from typing import List

def checkArithmeticSubarray(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    res = [False] * len(l)
    for i in range(len(l)):
        seq = sorted(nums[l[i]: r[i] + 1])
        if len(seq) <= 2:
            res[i] = True
        else:
            isArithmetic = True
            diff = seq[1] - seq[0]
            for j in range(1, len(seq) - 1):
                if seq[j + 1] - seq[j] != diff:
                    isArithmetic = False
                    break
            if isArithmetic:
                res[i] = True
    return res
print(checkArithmeticSubarray([4,6,5,9,3,7],[0,0,2],[2,3,5]))
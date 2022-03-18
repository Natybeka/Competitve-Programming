# Problem description
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.


# Solution find the element in the larger list
# Iterate from that index to the end of the list
# until you find a larger element
from typing import List


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    retArr = [-1] * len(nums1)
    for i in range(len(nums1)):
        startIndex = nums2.index(nums1[i])
        if startIndex == len(nums2) - 1:
            continue

        for j in range(startIndex + 1, len(nums2)):
            if nums2[j] > nums2[startIndex]:
                retArr[i] = nums2[j]
                break
    return retArr

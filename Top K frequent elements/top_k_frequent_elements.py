# Problem description
# Given an integer array nums and an integer k, 
# return the k most frequent elements. You may return the answer 
# in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]


# Solution maintain a sorted counter dictionary in decreasing order
# choose the first k elements in the counter dict

from collections import Counter
from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:
    counts = Counter(nums)
    counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    kList = []
    for i in range(k):
        kList.append(counts[i][0])
    return kList
from typing import List
import collections


def minIncrementsForUnique(nums: List[int]) -> int:
    max_val = max(nums)
    counts = collections.Counter(nums)

    moves = 0
    duplicates = []
    for x in range(len(nums) + max_val):
        if counts[x] >= 2:
            duplicates.extens([x] * (counts[x] - 1))
        elif duplicates and counts[x] == 0:
            moves += x - duplicates.pop()

    return moves

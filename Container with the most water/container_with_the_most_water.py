# Proble description
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

from typing import List
# Solution
# Sliding window
# Maximized the width first
# the try to increase the area by increasing the minumum area
# Time complexity O(N)
# Space O(1)
def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    area = 0
    while left < right:
        minHeight = min(height[right], height[left])
        area = max(area, minHeight * (right - left))
        if height[left] == minHeight:
            left += 1
        else:
            right -= 1
    return area
print(maxArea([1,8,6,2,5,4,8,3,7]))

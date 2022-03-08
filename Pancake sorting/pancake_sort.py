# Given an array of integers arr, sort the array by performing a series of pancake flips.

# In one pancake flip we do the following steps:

# Choose an integer k where 1 <= k <= arr.length.
# Reverse the sub-array arr[0...k-1] (0-indexed).
# For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

# Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.


# Solution is a variation of the selection sort
# find the maximum number in the list and perform flips until the maxIndex and
# then flip again to put the max in the appropriate place 
# decrement the pointer to find the next highest number
from typing import List
def pancakeSort(arr: List[int]) -> List[int]:
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        return []
    subArr = len(arr)
    opArray = []
    while subArr > 1:
        maxIndex = findMax(arr, subArr)
        if maxIndex != subArr - 1:
            if maxIndex != 0:
                flipArray(arr, maxIndex)
                opArray.append(maxIndex + 1)

            flipArray(arr, subArr - 1)
            opArray.append(subArr)
        subArr -= 1    
    return opArray

# Find the maximum in each iteration
def findMax(arr, n):
    maxIndex = 0
    for i in range(1, n):
        if arr[i] > arr[maxIndex]:
            maxIndex = i
    return maxIndex
# two flips takes the maximum to the proper index
def flipArray(arr, i):
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

print(pancakeSort([3,4,2,1]))    
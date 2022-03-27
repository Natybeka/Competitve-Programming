# Problem description
# Given two integer arrays pushed and popped each with distinct values, 
# return true if this could have been the result of a sequence of push 
# and pop operations on an initially empty stack, or false otherwise.

# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

from typing import List
# Maintain two pointer for the push and pop operations
# As soon as an element can be popped pop it
# if not continue to push
# return true if the stack is empty or all the elements have been popped
def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    n = len(pushed)
    stack = []
    poppedPointer = 0
    for pushedPointer in range(n):
        stack.append(pushed[pushedPointer])
        while stack and stack[-1] == popped[poppedPointer]:
            stack.pop()
            poppedPointer += 1
    return True if poppedPointer == n else False 

print(validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
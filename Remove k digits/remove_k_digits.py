# Problem description
# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

# Solution 
# Pass through the string array
# Maintain an increasing monotonic stack
# Pop while there are still operations from the stack

# Key conditions
# 1. If k is still available remove the last k elements from the stack
# 2. zeros are only added in the middle of the monostack
def removeKdigits(num: str, k: int) -> str:
    monoStack = []
    for digit in num:
        while monoStack and k and monoStack[-1] > digit:
            monoStack.pop()
            k -= 1
        
        if monoStack or digit is not '0':
            monoStack.append(digit)
    
    if k:
        monoStack = monoStack[0:-k]

    return "".join(monoStack) or '0'

print(removeKdigits("1432219",3))
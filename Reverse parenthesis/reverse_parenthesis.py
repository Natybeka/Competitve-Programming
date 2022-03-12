# # Problem description
# You are given a string s that consists of lower case English letters and brackets.

# Reverse the strings in each pair of matching parentheses, starting from the innermost one.

# Your result should not contain any brackets.

# Input: s = "(abcd)"
# Output: "dcba"
# Solution utilize a stack one pass then when ) occurs append the chracters
# and reverse them
# the top of the stack will contain the reversed
  
def reverseParenthesis(s: str) -> str:
    stack = ['']
    for c in s:
        if c == '(':
            stack.append('')
        elif c == ')':
            add = stack.pop()[::-1]
            stack[-1] += add
        else:
            stack[-1] += c
    return stack.pop()[::-1]
print(reverseParenthesis("(u(love)I"))

# Alternate solutions
# Check other solutions

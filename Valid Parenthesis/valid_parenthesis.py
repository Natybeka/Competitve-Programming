# Problem description
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

def isValid(self, s: str) -> bool:
    stack = []
    openings = ['(', '{', '[']
    symbolDict = {")" : "(", "]" :"[", "}": "{" }
    for symbol in s:
        if symbol in openings:
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return False
            if symbolDict[symbol] != stack.pop():
                return False
    if stack:
        return False
    return True

print(isValid("[{]}"))
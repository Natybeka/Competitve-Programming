# Problem description
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

# Solution for each entry store a pair of value and min value of stack when 
# a value is entered
class Node:
    def __init__(self, value, minValue):
        self.value = value
        self.min = minValue
class MinStack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, val: int) -> None:
        if self.size == 0:
            self.stack.append(Node(val, val))
            self.size += 1

        else:
            self.stack.append(Node(val, min(val, self.stack[self.size - 1].min)))
            self.size += 1
    def pop(self) -> None:
        self.stack.pop()
        self.size -= 1

    def top(self) -> int:
        return self.stack[self.size - 1].value

    def getMin(self) -> int:
        return self.stack[self.size - 1].min

# Some test code
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) #return -3
print(minStack.pop())
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2

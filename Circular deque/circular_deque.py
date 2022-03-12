# Problem description
# Design your implementation of the circular double-ended queue (deque).

# Implement the MyCircularDeque class:

# MyCircularDeque(int k) Initializes the deque with a maximum size of k.
# boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
# int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
# int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
# boolean isEmpty() Returns true if the deque is empty, or false otherwise.
# boolean isFull() Returns true if the deque is full, or false otherwise.
class MyCircularDeque:

    def __init__(self, k: int):
        self.circularDeque = []
        self.size = k
        self.numberOfElements = 0
        

    # insert to the front of the queue
    def insertFront(self, value: int) -> bool:
        
        if self.numberOfElements == self.size:
            return False
        
        self.circularDeque.insert(0, value)
        self.numberOfElements += 1
        return True

    # insert at the end of the queue
    def insertLast(self, value: int) -> bool:
        if self.numberOfElements == self.size:
            return False
        self.circularDeque.append(value)
        self.numberOfElements += 1
        return True
    
        
    def deleteFront(self) -> bool:
        if self.numberOfElements == 0:
            return False
        self.circularDeque.pop(0)
        self.numberOfElements -= 1
        return True


    def deleteLast(self) -> bool:
        if self.numberOfElements == 0:
            return False
        self.circularDeque.pop(self.numberOfElements - 1)
        self.numberOfElements -= 1
        return True
        

    def getFront(self) -> int:
        return self.circularDeque[0]

    def getRear(self) -> int:
        
        return self.circularDeque[self.numberOfElements - 1]
        

    def isEmpty(self) -> bool:
        return self.numberOfElements == 0
        

    def isFull(self) -> bool:
        return self.numberOfElements == self.size

myCircularDeque = MyCircularDeque(3);
print(myCircularDeque.insertLast(1))  # return True
print(myCircularDeque.insertLast(2))  # return True
print(myCircularDeque.insertFront(3)) # return True
 # return False, the queue is full.
print(myCircularDeque.insertFront(4))
print(myCircularDeque.getRear())  # return 2
print(myCircularDeque.isFull())       # return True
print(myCircularDeque.deleteLast())   # return True
print(myCircularDeque.getRear())
print(myCircularDeque.insertFront(5)) # return True
print(myCircularDeque.getFront())     # return 4
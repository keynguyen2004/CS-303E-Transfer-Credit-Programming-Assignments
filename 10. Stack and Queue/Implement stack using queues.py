"""
We are given a queue data structure with enque and deque 
operations, the task is to implement a stack using instances 
of queue data structure and operations on them.

A queue can be implemented using two queues, queue1 and queue2. 
There are two methods of implementation

    1. Make push operation O(n): The newly entered value is always 
       at the front of queue1 so that pop operation dequeues from 
       queue1. queue2 is used to put every new value in front of queue1.
    2. Make pop operation O(n): The newly entered value is always enqueued 
       to queue1. In the pop operation, if queue2 is empty then all the 
       values except the last are moved to queue2. Finally, the last value
       is dequeued from qqueue1 and returned.
"""

# Method 1: Make push operation O(n)


from collections import deque

class Stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    # Push a value to the stack
    def push(self, value):

        # Push the value into the empty queue2
        self.queue2.append(value)
 
        # Push all the remaining values from queue1 to queue2.
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
 
        # Swap the values inside the two queues
        self.queue1, self.queue2 = self.queue2, self.queue1

    # Pop a value out from the stack
    def pop(self):

        if self.queue1:
            print(self.queue1.popleft())

        else:
            print("The stack is empty")


if __name__ == '__main__':
    s = Stack()
    s.push("a")
    s.push("b")
    s.pop()
    s.push("c")
    s.pop()
    s.pop()
    s.pop()



# Method 2: Make pop operation O(n)


from collections import deque

class Stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    # Push a value to the stack
    def push(self, value):
        self.queue1.append(value)

    # Pop a value out from the stack
    def pop(self):

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        # Swap the values inside the two queues
        self.queue1, self.queue2 = self.queue2, self.queue1

        if self.queue2:
            print(self.queue2.popleft())
        else:
            print("The stack is empty")
        

if __name__ == '__main__':
    s = Stack()
    s.push("a")
    s.push("b")
    s.pop()
    s.push("c")
    s.pop()
    s.pop()
    s.pop()
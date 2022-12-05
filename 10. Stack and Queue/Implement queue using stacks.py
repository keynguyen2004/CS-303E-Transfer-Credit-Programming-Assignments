"""
We are given a stack data structure with push and pop 
operations, the task is to implement a queue using instances 
of stack data structure and operations on them.

A queue can be implemented using two stacks, stack1 and stack2. 
There are two methods of implementation

    1. Make enqueue operation O(n): The oldest entered value 
       is always at the top of stack1 so that deQueue operation 
       just pops from stack1. To put the value at top of stack1, 
       stack2 is used.
    2. Make dequeue operation O(n): In the en-queue operation, the
       new value is entered at the top of stack1. In the de-queue 
       operation, if stack2 is empty then all the values are moved 
       to stack2 and finally top of stack2 is returned. 
"""

# Method 1: Make enqueue operation O(n)

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    # Enqueue a value to the queue
    def enqueue(self, value):
         
        # Move all values from stack1 to stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        # Push newly entered value into stack1
        self.stack1.append(value)
 
        # Push all value back to stack1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

 
    # Dequeue a value from the queue
    def dequeue(self):
         
        # If stack1 is empty
        if not self.stack1:
            print("The queue is empty")

        else:
            # Return the top of stack1
            print(self.stack1.pop())
 

if __name__ == '__main__':
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.dequeue()
    q.enqueue("c")
    q.dequeue()
    q.dequeue()
    q.dequeue()
 

# Method 2: Make dequeue operation O(n)

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    # Enqueue a value to the queue
    def enqueue(self, value):
        self.stack1.append(value)

    # Dequeue a value from the queue
    def dequeue(self):

        # If both stacks are empty
        if not self.stack1 and not self.stack2:
            print("The queue is empty")

        else:
            # If stack2 is empty
            if not self.stack2:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
                
            print(self.stack2.pop())


if __name__ == '__main__':
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.dequeue()
    q.enqueue("c")
    q.dequeue()
    q.dequeue()
    q.dequeue()
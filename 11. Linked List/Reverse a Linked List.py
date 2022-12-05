"""
We can reverse a linked list by the following 3 methods:

    1. Iterative method
    2. Recursive method
    3. Using stack

Assignments:

    1. Exercise #1: Reverse a linked list by iteration
    2. Exercise #2: Reverse a linked list by recursion
    3. Exercise #3: Reverse a linked list by stack
"""

# Exercise #1: Reverse a linked list by iteration

class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.pointer = self.head
        self.head = new_node
    
    def reverse(self):
        if self.head == None:
                return
        prev_node = None
        current_node = self.head
        while current_node != None:
            next_node = current_node.pointer
            current_node.pointer = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
    
    def PrintLinkedList(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.pointer

# Use push() to construct below
# llist: 1 -> 2 -> 3
if __name__ == '__main__':            
    llist = LinkedList()
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print("Given linked list: ")
    llist.PrintLinkedList()
    print("Reversed linked list: ")
    llist.reverse()
    llist.PrintLinkedList()



# Exercise #2: Reverse a linked list by recursion

class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.pointer = self.head
        self.head = new_node
    
    def reverseRest(self, current_node, prev_node):
 
        # If last node, mark it head
        if current_node.pointer == None: # if this is True we return/end the function                        
            self.head = current_node
 
            # Update next to prev_node
            current_node.pointer = prev_node
            return                       # the function end here
        
        # Save current_node.pointer node for recursive call
        next_node = current_node.pointer
 
        # And update the pointer to point back at the prev_node
        current_node.pointer = prev_node
 
        self.reverseRest(next_node, current_node)
 
    # This function mainly calls reverseRest()
    # with prev_node as None
 
    def reverse(self):
        if self.head == None: # if this is True we return/end the function
            return            # the function end here
        self.reverseRest(self.head, None)
    
    def PrintLinkedList(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.pointer

# Use push() to construct below
# llist: 1 -> 2 -> 3
if __name__ == '__main__':            
    llist = LinkedList()
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print("Given linked list: ")
    llist.PrintLinkedList()
    print("Reversed linked list: ")
    llist.reverse()
    llist.PrintLinkedList()



# Exercise #3: Reverse a linked list by stack

class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.pointer = self.head
        self.head = new_node
    
    def reverse(self):
        
        if self.head == None:
            return
        
        # Initialize the variables
        stack = []
        node = self.head
        
        while node != None:
            stack.append(node)
            node = node.pointer
            
        node = stack.pop()
        self.head = node
        while len(stack) > 0:
            node.pointer = stack.pop()
            node = node.pointer
        node.pointer = None
    
    def PrintLinkedList(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.pointer

# Use push() to construct below
# llist: 1 -> 2 -> 3
if __name__ == '__main__':            
    llist = LinkedList()
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print("Given linked list: ")
    llist.PrintLinkedList()
    print("Reversed linked list: ")
    llist.reverse()
    llist.PrintLinkedList()

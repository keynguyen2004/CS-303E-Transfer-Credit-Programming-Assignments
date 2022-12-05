"""
We can add two numbers represented by linked lists by using

    1. Traversal Approach
    2. Using Stack

Assignments:

    1. Add two linked lists by traversal
    2. Add two linked lists by stack
"""

# Exercise #1: Add two linked lists by traversal

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
        
    def AddTwoLinkedList(self, llist1, llist2):
        if llist1.head == None:
            return llist2
        if llist2.head == None:
            return llist1
				
        # reverse both linked lists    
        llist1.reverse()
        llist2.reverse()
        node1 = llist1.head
        node2 = llist2.head
        result = LinkedList()
        carry = 0

				# while end of both linked list is not reached
        while node1 != None or node2 != None:
            sum = 0
            
						# add value from llist1
            if node1 != None:
                sum += node1.data
                node1 = node1.pointer
            
						# add value from llist2   
            if node2 != None:
                sum += node2.data
                node2 = node2.pointer
            
						# add carry    
            sum += carry
            
            value = sum % 10
            carry = sum // 10
            result.push(value)
        
				# if carry is present       
        if carry > 0:
            result.push(1)
                   
        return result

    def PrintLinkedList(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.pointer

# Use push() to construct below
if __name__ == '__main__': 
    # llist1: 1 -> 2 -> 3
    llist1 = LinkedList()
    llist1.push(3)
    llist1.push(2)
    llist1.push(1)
    print("Given linked list 1: ")
    llist1.PrintLinkedList()
    # llist2: 9 -> 8 -> 7
    llist2 = LinkedList()
    llist2.push(7)
    llist2.push(8)
    llist2.push(9)
    print("Given linked list 2: ")
    llist2.PrintLinkedList()
    result = LinkedList()
    final_llist = result.AddTwoLinkedList(llist1, llist2)
    print("Resultant linked list: ")
    final_llist.PrintLinkedList()



# Exercise #2: Add two linked lists by stack

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
        
    def AddTwoLinkedList(self, llist1, llist2):
        if llist1.head == None:
            return llist2
        if llist2.head == None:
            return llist1
            
        stack1 = []
        stack2 = []
            

        node1 = llist1.head
        while node1 != None:
            stack1.append(node1.data)
            node1 = node1.pointer
        
        node2 = llist2.head
        while node2 != None:
            stack2.append(node2.data)
            node2 = node2.pointer
        
        result = LinkedList()
        sum = 0
        carry = 0
        
        # add the popped digits till one of the stacks becomes empty
        while len(stack1) > 0 and len(stack2) > 0:
            value1 = stack1.pop()
            value2 = stack2.pop()
            
            sum = (value1 + value2 + carry) % 10
            carry = (value1 + value2 + carry) // 10
            
            result.push(sum)
                
        # if stack1 still has some digits left, add them to the sum
        while len(stack1) > 0:
            value1 = stack1.pop()
            
            sum = (value1 + carry) % 10
            carry = (value1 + carry) // 10
            
            result.push(sum)
  
     
        # if stack1 still has some digits left, add them to the sum
        while len(stack2) > 0:
            value2 = stack2.pop()
            
            sum = (value2 + carry) % 10
            carry = (value2 + carry) // 10
            
            result.push(sum)
     
        # add remaining carry to the sum
        if carry > 0:
            result.push(1)

        return result

    def PrintLinkedList(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.pointer

# Use push() to construct below
if __name__ == '__main__': 
    # llist1: 4 -> 3 -> 1 -> 2 -> 3
    llist1 = LinkedList()
    llist1.push(3)
    llist1.push(2)
    llist1.push(1)
    llist1.push(3)
    llist1.push(4)
    print("Given linked list 1: ")
    llist1.PrintLinkedList()
    # llist2: 9 -> 0 -> 7 
    llist2 = LinkedList()
    llist2.push(7)
    llist2.push(0)
    llist2.push(9)
    print("Given linked list 2: ")
    llist2.PrintLinkedList()
    result = LinkedList()
    final_llist = result.AddTwoLinkedList(llist1, llist2)
    print("Resultant linked list: ")
    final_llist.PrintLinkedList()
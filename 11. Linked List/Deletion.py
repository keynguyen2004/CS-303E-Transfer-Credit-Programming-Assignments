"""
A node can be deleted for either

    1. A given data
    2. A given key/position

Assignments:

    1. Exercise #1: Delete a node for a given data
    2. Exercise #2: Delete a node for a given key/position
"""

# Exercise #1: Delete a node for a given data

class Node:   
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data       # Assign data
        self.pointer = None    # Initialize pointer as null
   
# Linked List class
class LinkedList:     
    # Function to initialize the Linked List object
    def __init__(self): 
        self.head = None
    
    # This function is in the LinkedList class
	# Function to insert a new node at the beginning    
    def DeleteNode(self, data):
        
        if self.head == None:
            return

        # Step 1: Traverse the linked list until next_node is found
        node = self.head
        prev_node = None
        while node.data != data and node!= None:
            prev_node = node
            node = node.pointer
            
        # Step 2: Check if the given next_node is in the LinkedList)   
        if node == None:
            print("The given next node must be in LinkedList.")
        
        else:
            
            # Case #1: Data is located in the head/first node
            if node == self.head:
                self.head = node.pointer
                node.pointer = None  # Alternatively, we can write
																		 # node = None
                
            # Case #2: Data is located at the end of the LinkedList
            elif node.pointer == None:
                prev_node.pointer = None
								# We can add node = None here
        
            # Case #3: Data is located in the middle of the LinkedList
            else:
                prev_node.pointer = node.pointer
                node.pointer = None  # Alternatively, we can write
																		 # node = None
            
    def PrintLinkedList(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.pointer
    
# Code execution starts here
if __name__=='__main__':
  
    # Start with the empty list
    llist = LinkedList()
  
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.pointer = second
    second.pointer = third
    llist.DeleteNode(2)
    llist.PrintLinkedList()


# Exercise #2: Delete a node for a given key/position

class Node:   
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data       # Assign data
        self.pointer = None    # Initialize pointer as null
   
# Linked List class
class LinkedList:     
    # Function to initialize the Linked List object
    def __init__(self): 
        self.head = None
    
    # This function is in the LinkedList class
	# Function to insert a new node at the beginning    
    def DeleteNode(self, key):
        
        if self.head == None:
            return
        
        # Case 1: Data is located in the head/first node
        if key == 0:
            node = self.head
            self.head = node.pointer
            node.pointer = None   # Or node = None
            
        else:
            node = self.head
            prev_node = None
            # Step 1: Traverse the linked list until the position is reached
            node = self.head
            prev_node = None
            index = 0
            while node != None and index < key:
                prev_node = node
                node = node.pointer
                index += 1
            
            # Step 2: Check if the index is out of range 
            if node == None:
                print("Key/index is outside the range of the LinkedList.")
            
            else:
                    
                # Case #2: Data is located at the end of the LinkedList
                if node.pointer == None:
                    prev_node.pointer = None   # Or node = None 
            
                # Case #3: Data is located in the middle of the LinkedList
                else:
                    prev_node.pointer = node.pointer
                    node.pointer = None  # Or node = None
            
    def PrintLinkedList(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.pointer
    
# Code execution starts here
if __name__=='__main__':
  
    # Start with the empty list
    llist = LinkedList()
  
    llist.head = Node("A")
    second = Node("B")
    third = Node("C")
    llist.head.pointer = second
    second.pointer = third
    llist.DeleteNode(1)   # Index start with 0
    llist.PrintLinkedList()
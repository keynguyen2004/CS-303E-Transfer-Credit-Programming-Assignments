"""
A node can be added in three ways

    1. At the front of the linked list
    2. Before a given node
    3. After a given node.
    4. At the end of the linked list.

Assignments:

    1. Exercise #1: Insertion in front
    2. Exercise #2: Insertion before a given node
    3. Exercise #3: Insertion after a given node
    4. Exercise #4: Insertion at the end
"""

# Exercise #1: Insertion in front

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
    def push(self, new_data):
		  
	    # Step 1: Allocate the Node &
	    # Step 2: Put in the data
        new_node = Node(new_data)
        
        # Step 3: Make the pointer of new_node point to the initial head node
        new_node.pointer = self.head
	          
	    # Step 4: Assign the head node to be the new_node  
        self.head = new_node
        
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
    llist.push("0")
    llist.PrintLinkedList()



# Exercise #2: Insertion before a given node

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
    def push(self, next_node, new_data):
        
        # Step 1: Traverse the linked list until next_node is found
        node = self.head
        prev_node = None
        while node != next_node and node!= None:
            prev_node = node
            node = node.pointer
        
        # Step 2: Check if the given next_node is in the LinkedList)   
        if node == None:
            print("(The given next node must be in LinkedList.")
            
        else:
            # Step 3: Create a new node
            # Step 4: Put in the data
            new_node = Node(new_data)
            
            # If next_node is the head node
            if prev_node == None:
                # Step 5: Make the pointer of new_node point to the initial head node
                new_node.pointer = self.head
	          
	            # Step 6: Assign the head node to be the new_node 
                self.head = new_node
                
            else:
                
                # Step 7: Make the pointer of new_node as the pointer of prev_node
                new_node.pointer = prev_node.pointer

                # Step 8: Make the pointer of prev_node as new_node
                prev_node.pointer = new_node
            
                # Alternatively, it can be express in one line
                # prev_node.pointer, new_node.pointer = new_node, prev_node.pointer
     
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
    llist.push(second, 1.5)
    llist.PrintLinkedList()



# Exercise #3: Insertion after a given node

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
    def push(self, prev_node, new_data):
        
        # Step 1: Check if the given prev_node exists
        if prev_node == None:
            print("The given previous node must be in LinkedList.")
        
        else:
            # Step 2: Create a new node
            # Step 3: Put in the data
            new_node = Node(new_data)
            
            # Step 4: Make the pointer of new_node as the pointer of prev_node
            new_node.pointer = prev_node.pointer
  
            # Step 5: Make the pointer of prev_node as new_node
            prev_node.pointer = new_node
            
            # Alternatively, it can be express in one line
            # prev_node.pointer, new_node.pointer = new_node, prev_node.pointer
        
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
    llist.push(second, 2.5)
    llist.PrintLinkedList()



# Exercise #4: Insertion at the end
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
    def push(self, new_data):
	    
		    # Step 1: Create a new node
        # Step 2: Put in the data
        # Step 3: Set pointer as None (already set in class Node)
        new_node = Node(new_data)
  
        # Step 4: If the Linked List is empty, then make new_node as head 
        if self.head == None:
            self.head = new_node
  
        # Step 5: Else traverse till the last node is found
        else:
            last_node = self.head
						# Notice it's last_node.pointer != None, not last_node != None																			
            while last_node.pointer != None:
                last_node = last_node.pointer
  
            # 6. Change the pointer of last_node
            last_node.pointer = new_node
        
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
    llist.push(4)
    llist.PrintLinkedList()
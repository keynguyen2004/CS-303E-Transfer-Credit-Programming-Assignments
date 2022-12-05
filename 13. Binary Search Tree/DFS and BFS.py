"""
Depth First Search: There are 3 types of DFS

    1. Inorder Traversal
    2. Preoder Traversal
    3. Postorder Traversal

Breadth First Search: Also known as Level Order Traversal, there’s 
2 methods of implementation
    1. Using function to print a current level
    2. Using queue

Assignments:

    1. Exercise #1: All types of DFS
    2. Exercise #2: BFS with height function
    3. Exercise #3: BFS without height function
"""

# Exercise #1: All types of DFS

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def insert(root, key):
    if root == None:
        root = Node(key)
    if key == root.val:
        return root
    elif key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
        
def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.val, end = " ")
        inorder(root.right)

def preorder(root):
    if root != None:
        print(root.val, end = " ")
        inorder(root.left)
        inorder(root.right)

def postorder(root):
    if root != None:
        inorder(root.left)
        inorder(root.right)
        print(root.val, end = " ")

if __name__ == "__main__":
    r = Node(8)
    # Can remove the r = 
    insert(r, 3)
    insert(r, 10)
    insert(r, 1)
    insert(r, 6)
    insert(r, 14)
    insert(r, 4)
    insert(r, 7)
    insert(r, 13)
    print(inorder(r))
    print(preorder(r))
    print(postorder(r))



# Exercise #2: BFS with height function

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def insert(root, key):
    if root == None:
        root = Node(key)
    if key == root.val:
        return root
    elif key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
        
def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.val, end = " ")
        inorder(root.right)

# Function to  print level order traversal of tree        
def printLevelOrder(root):
    h = height(root) 
    for level in range (1, h + 1):
        printCurrentLevel(root, level)

# Print nodes at a current level
def printCurrentLevel(root, level):

		# base case
    if root == None:
        return None
    if level == 1:
        print(root.val, end = " ")
    else:
        printCurrentLevel(root.left, level - 1)
        printCurrentLevel(root.right, level - 1)

""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""
    
def height(root):
    if root == None:
        return 0
    else:
				# Compute the height of each subtree
        LeftHeight = height(root.left)
        RightHeight = height(root.right)
        
				# Use the larger one
        if LeftHeight > RightHeight:
            return LeftHeight + 1
        else:
            return RightHeight + 1
    
        
if __name__ == "__main__":
    r = Node(8)
    # Can remove the r = 
    insert(r, 3)
    insert(r, 10)
    insert(r, 1)
    insert(r, 6)
    insert(r, 14)
    insert(r, 4)
    insert(r, 7)
    insert(r, 13)
    print(inorder(r))
    print(printLevelOrder(r))



# Exercise #3: BFS without height function

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def insert(root, key):
    if root == None:
        root = Node(key)
    if key == root.val:
        return root
    elif key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
        
def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.val, end = " ")
        inorder(root.right)

# Function to  print level order traversal of tree        
def printLevelOrder(root):
    h = height(root) 
    for level in range (1, h + 1):
        printCurrentLevel(root, level)

# Print nodes at a current level
def printCurrentLevel(root, level):

		# base case
    if root == None:
        return None
    if level == 1:
        print(root.val, end = " ")
    else:
        printCurrentLevel(root.left, level - 1)
        printCurrentLevel(root.right, level - 1)

""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""
    
def height(root):
    if root == None:
        return 0
    else:
				# Compute the height of each subtree
        LeftHeight = height(root.left)
        RightHeight = height(root.right)
        
				# Use the larger one
        if LeftHeight > RightHeight:
            return LeftHeight + 1
        else:
            return RightHeight + 1
    
        
if __name__ == "__main__":
    r = Node(8)
    # Can remove the r = 
    insert(r, 3)
    insert(r, 10)
    insert(r, 1)
    insert(r, 6)
    insert(r, 14)
    insert(r, 4)
    insert(r, 7)
    insert(r, 13)
    print(inorder(r))
    print(printLevelOrder(r))
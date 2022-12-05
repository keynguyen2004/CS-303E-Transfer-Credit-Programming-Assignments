"""
Search and Insertion steps

1. Start at the root
2. Compare the value to be searched with the value of the root
    a. If it’s equal, the search is done
    b. If it’s smaller, go to the left subtree
    c. If it’s greater, go to the right subtree
3. Repeat this step until the key/searched value is found/needed to be inserted

Assignments:

    1. Exercise #1: Iterative search and insertion
    2. Exercise #2: Recursive search and insertion
"""

# Exercise #1: Iterative search and insertion

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def search (root, key):
    if root == None:
        return str(key) + " is not found!"
    
    curr = root
    # place curr != None first before curr.val != key
    # else, if it reach curr == None, it will result in 
    # error where NoneType doesn't have access to val
    while curr != None and curr.val != key:
        if curr.val < key:
            curr = curr.right
        else:
            curr = curr.left
    
    if curr == None:
        return str(key) + " is not found!"
    else:
        return str(curr.val) + " is found!"
        
def insert(root, key):
    if root == None:
        return Node(key)
    
    curr = root
    while True:
        if curr.val < key:
            if curr.right:
                curr = curr.right
            else:
                curr.right = Node(key)
                break

        else:
            if curr.left:
                curr = curr.left
            else:
                curr.left = Node(key)
                break
    return root
    

if __name__ == "__main__":
    # Start with the empty BST
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
    print(search(r, 20))  
    print(search(r, 50))
    print(search(r, 90))


# Exercise #2: Recursive search and insertion

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def search (root, key):

	# Base case 1: Root is null
    if root == None:
        return str(key) + " is not found!"

	# Base case 2: Key is present at node
    if key == root.val:
        return str(root.val) + " is found!"

    elif key < root.val:
        # this recursive call pass this parameter back
        # to the parameter at the top of the function
        return search (root.left, key)

    else:
        # this recursive call pass this parameter back
        # to the parameter at the top of the function
        return search (root.right, key)
        
def insert(root, key):
    if root == None:
        return Node(key)
    if key == root.val:
        return root
    elif key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
    

if __name__ == "__main__":
    # Start with the empty BST
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
    print(search(r, 20))  
    print(search(r, 50))
    print(search(r, 90))
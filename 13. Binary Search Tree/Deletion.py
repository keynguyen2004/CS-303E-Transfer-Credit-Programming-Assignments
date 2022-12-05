"""
When we delete a node, 3 possibilities arise

1. No child (leaf node): Simply remove from the tree
2. 1 child: Copy the child to the node and delete the child
3. 2 child: Find inorder successor of the node. Copy contents 
   of the inorder successor to the node and delete the inorder 
   successor. Note that inorder predecessor can also be used.

Assignments:

    1. Exercise #1: Deletion using successor node
    2. Exercise #2: Deletion using predecessor node
"""

# Exercise #1: Deletion using successor node

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def search(root, key):
    if root == None:
        return str(key) + " is not found!"
    if key == root.val:
        return str(root.val) + " is found!"
    if key < root.val:
        return search (root.left, key)
    if key > root.val:
        return search (root.right, key)
        
def insert(root, key):
    if root == None:
        return Node(key)
    if key == root.val:
        return root
    if key < root.val:
        root.left = insert(root.left, key)
    if key > root.val:
        root.right = insert(root.right, key)
    return root

# Function to perform inorder traversal on the BST
def inorder(root):
    if root != None:
        inorder(root.left)
        print (root.val, end = " ")
        inorder(root.right)

# Function to find the inorder successor in the subtree rooted at "root"
def MinimumKey(root):
    # Inorder successor is the leftmost of the right subtree
    while root.left != None:
        root = root.left
    return root
    
def delete(root, key):
	# base case: the key is not found in the tree
    if root == None:
        return root

	# if the given key is less than the root node, recur for the left subtree
    if key < root.val:
        root.left = delete (root.left, key)

	# if the given key is more than the root node, recur for the right subtree
    elif key > root.val:
        root.right = delete (root.right, key)

	# key found
    else:

		# Case 1: node to be deleted has no children (it is a leaf node)
        if root.left == None and root.right == None:
            return None

		# Case 2: node to be deleted has two children
        elif root.left != None and root.right != None:
            # find its inorder successor node
            successor = MinimumKey(root.right)
 
            # copy value of the successor to the current node
			# this root will be return at the end (the return root line of code)
            root.val = successor.val
 
            # recursively delete the successor. Note that the
            # successor will have at most one child (right child)
            root.right = delete(root.right, successor.val)
        
        # Case 3: node to be deleted has only one child
        else:
            # choose a child node
            if root.left != None:
                child = root.left
                root = child
            else:
                child = root.right
                root = child

            # We use the child node - all three the value, left, and right pointer 
            # - to replace the current node. Since the child node has no child - both 
            # left pointer and right pointer is null - this conveniently 
            # delete the pointer for the current node

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
    print(inorder(r))
    delete(r, 20)
    print(inorder(r))
    delete(r, 50)
    print(inorder(r))
    delete(r, 90)
    print(inorder(r))



# Exercise #2: Deletion using predecessor node

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def search(root, key):
    if root == None:
        return str(key) + " is not found!"
    if key == root.val:
        return str(root.val) + " is found!"
    if key < root.val:
        return search (root.left, key)
    if key > root.val:
        return search (root.right, key)
        
def insert(root, key):
    if root == None:
        return Node(key)
    if key == root.val:
        return root
    if key < root.val:
        root.left = insert(root.left, key)
    if key > root.val:
        root.right = insert(root.right, key)
    return root

# Function to perform inorder traversal on the BST
def inorder(root):
    if root != None:
        inorder(root.left)
        print (root.val, end = " ")
        inorder(root.right)

# Function to find the inorder predeccessor in the subtree rooted at "root"
def MaximumKey(root):
    # Predecessor successor is the rightmost of the left subtree
    while root.right != None:
        root = root.right
    return root

def delete(root, key):
	# base case: the key is not found in the tree
    if root == None:
        return root

	# if the given key is less than the root node, recur for the left subtree
    if key < root.val:
        root.left = delete (root.left, key)

	# if the given key is more than the root node, recur for the right subtree
    elif key > root.val:
        root.right = delete (root.right, key)

	# key found
    else:

        # Case 1: node to be deleted has no children (it is a leaf node)
        if root.left == None and root.right == None:
            return None

				# Case 2: node to be deleted has two children
        elif root.left != None and root.right != None:
            # find its inorder successor node
            predecessor = MaximumKey(root.left)
 
            # copy value of the successor to the current node
						# this root will be return at the end (the return root line of code)
            root.val = predecessor.val
 
            # recursively delete the successor. Note that the
            # successor will have at most one child (right child)
            root.left = delete(root.left, predecessor.val)
        
        # Case 3: node to be deleted has only one child
        else:
            if root.left != None:
                child = root.left
                root = child
            else:
                child = root.right
                root = child
        
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
    print(inorder(r))
    delete(r, 20)
    print(inorder(r))
    delete(r, 50)
    print(inorder(r))
    delete(r, 90)
    print(inorder(r))
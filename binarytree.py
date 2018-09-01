"""Creating a binary tree"""

# first create a node class
# second create a tree class

class Node()
"""Creating a Node"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree()
"""Creating a tree"""
    def __init__(self, root):
        self.root = Node(root)      # create a root node

#           1
#         /     \
#        2      3
#       /   \   /   \
#       4   5   6   7

# set up a tree
tree = BinaryTree(1)            # created an object of tree and a root node 1
tree.root.left = Node(2)       # added a left child to the root Node
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node (7)
tree.root.right.right.right = Node(8)

class Node(object):
    """Creating a node."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    """Creating a binary tree"""
    def __init__(self, root):
        self.root = Node(root)

    def Inorder(self, start, traversal):
        """Left-->Root-->Right"""
        if start:
            traversal = self.Inorder(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.Inorder(start.right, traversal)
        return traversal

    def preorder(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        """Left-->Right-->Root"""
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def printTree(self, traversal_type):
        """Printing the tree."""
        if traversal_type == 'preorder':
            return self.preorder(tree.root, "")
        elif traversal_type == 'Inorder':
            return self.Inorder(tree.root, "")
        else:
            return self.postorder(tree.root, "")

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
#tree.root.right.right.right = Node(8)

print(tree.printTree('preorder'))
print(tree.printTree('Inorder'))
print(tree.printTree('postorder'))


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, curr_node):
        if value < curr_node.value:
            if curr_node.left is None:
                curr_node.left = Node(value)
            else:
                self._insert(self, value, curr_node.left)
        if value > curr_node.value:
            if curr_node.right is None:
                curr_node.right = Node(value)
            else:
                self._insert(self, value, curr_node.right)
        else:
            print (" Value already in tree")

    def print_tree(self):
        if self.root is None:
            return "The tree is empty"
        else:
            self._print(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.right)

        

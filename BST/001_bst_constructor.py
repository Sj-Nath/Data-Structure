class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value=value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp.value == new_node.value:
                return False  # Value already exists
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:  # new_node.value > temp.value
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # In-order traversal
    def print_in_order(self, node):
        if node is not None:
            self.print_in_order(node.left)
            print(node.value, end=" ")
            self.print_in_order(node.right)

# Create an instance of BinarySearchTree
bst = BinarySearchTree()

# Insert values into the binary search tree
for i in [2, 6, 1, 7, 3]:
    bst.insert(i)

# Print the tree in in-order traversal
print("In-order Traversal:")
bst.print_in_order(bst.root)

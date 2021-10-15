class BinaryTree():
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.lef_child = self.right_child
            self.right_child = bin_tree

def invertTree(root):
    if root:
        root.left_child, root.right_child = invertTree(root.right_child), invertTree(root.left_child)
        return root


tree = BinaryTree(0)
tree.insert_left(10)
tree.insert_right(4)
tree.insert_left(3)
tree.insert_right(5)
print(invertTree(tree))

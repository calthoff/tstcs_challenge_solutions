class Node:
    def __init__(self, val, left_child=None, right_child=None):
        self.val = val
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return str(self.val)


class Tree:
    def __init__(self, root_val):
        self.root = Node(root_val)

    def insert_left(self, value):
        node = Node(value)
        if self.left_child == None:
            self.left_child = node
        else:
            node.left_child = self.root.left_child
            self.root.left_child = node

    def insert_right(self, value):
        node = Node(value)
        if self.right_child == None:
            self.right_child = node
        else:
            node.right_child = self.root.right_child
            self.root.right_child = node


def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
        return root


tree = Tree(0)
tree.insert_left(10)
tree.insert_right(4)
tree.insert_left(3)
tree.insert_right(5)
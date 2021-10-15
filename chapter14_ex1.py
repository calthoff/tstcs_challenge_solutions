# This question actually does not make much sense
# because it is impossible to make a binary tree with no
# leaf nodes! My mistake!

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

    def has_leaf_nodes(self, root):
        current = [root]
        next = []
        while current:
            leaf = True
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                    leaf = True
                if node.right_child:
                    next.append(node.right_child)
                    leaf = True
            if leaf:
                return True
            current = next
            next = []
        return False


tree = BinaryTree(0)
tree.insert_left(10)
tree.insert_right(4)
tree.insert_left(3)
tree.insert_right(5)
print(tree.has_leaf_nodes(tree))
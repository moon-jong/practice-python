class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_value(self, node, key):
        if node is None:
            self.root = Node(key)
        else:
            if key <= node.data:
                node.left = self._insert_value(node.left, key)
            else:
                node.right = self._insert_value(node.right, key)
        return node

    def insert(self, key):
        self.root = self._insert_value(self.root, key)
        return self.root is not None

    def _find_node(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_node(root.left, key)
        else:
            return self._find_node(root.right, key)

    def findNode(self, key):
        return self._find_node(self.root, key)

    def _delete_Node(self, node, key):
        if node is None:
            return node is None
        delete = False

        if node.data == key:
            delete = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child

        elif node.left or node.right:
            node = node.left or node.right
        else:
            node = None
        return node, delete
    def delete(self, key):
        self.root, delete = self._delete_Node(self.root, key)
        return delete
BST = BinarySearchTree()
array = [9, 12, 6, 8, 10, 13, 7, 28]
for i in array:
    BST.insert(i)
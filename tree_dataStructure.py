class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right =None

class BinaryTree:
    def __init__(self):
        self.root = None

    def _insert_node(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_node(node.left, data)
            else:
                node.right = self._insert_node(node.right, data)
        return node

    def insert(self,data):
        self.root = self._insert_node(self.root, data)
        return self.root is not None

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value( root.left, key)
        else:
            return self._find_value(root.right, key)
    def find(self, key):
        return self._find_value(self.root, key)

    def _delete_node(self, node, key):
        if node is None:
            return node, False
        deleted = False

        if node.data == key:
            deleted = True
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
        elif key < node.data:
            node.left, deleted = self._delete_node(node.left, key)
        else:
            node.right, deleted = self._delete_node(node.right, key)
        return node, deleted
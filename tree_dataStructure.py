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
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)
    def find(self, key):
        return self._find_value(self.root, key)


bin = BinaryTree()
x = [12, 34, 45, 56 , 2, 3, 4, 76, 9]
for i in x:
    bin.insert(i)

bin.find(45)
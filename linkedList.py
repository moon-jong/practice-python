#linkedList practice

class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

node1 = Node(100)
node2 = Node(200)
node3 = Node(300)
node4 = Node(400)

class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    def iter(self):
        current = self.head
        while True:
            print("%d" %(current.value))
            if current.nextNode == None:
                    break
            current = current.nextNode
    def

linkedList = LinkedList(node1,node4)

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

linkedList.iter()
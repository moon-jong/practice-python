class Node:
    def __init__(self,value):
        self.value = value
        self.nextNode = None

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head
    def iteration(self):
        current = self.head
        while True:
            print("%d" %(current.value))
            if current.nextNode == None:
                break
            current = current.nextNode
    def append(self, newNode):
        self.tail.nextNode = newNode
        self.tail = newNode


node1 = Node(100)
node2 = Node(200)
node3 = Node(300)
node4 = Node(400)

linkedList = LinkedList(node1)

linkedList.append(node2)
linkedList.append(node3)
linkedList.append(node4)

linkedList.iteration()


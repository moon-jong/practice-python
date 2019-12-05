class Node:
    def __init__(self,value):
        self.value = value
        self.nextNode = None

class LinkedList:

    def __init__(self, head):
        self.head = head
        self.tail = headp
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

    def insert(self, target, index):
        if index == 0:
            target.nextNode = self.head
            self.head = target
        elif self.count() <= index:
            self.tail.nextNode = target
            self.tail = target
        else:
            current = self.head
            for i in range(1, index):
                current = current.nextNode
            target.nextNode = current.nextNode
            current.nextNode = target

    def count(self):
        current = self.head
        count = 1
        while True:
            if current.nextNode == None:
                return count
            current = current.nextNode
            count += 1





node1 = Node(100)
node2 = Node(200)
node3 = Node(300)
node4 = Node(400)
newNode = Node(500)
newNode_2 = Node(600)
linkedList = LinkedList(node1)
linkedList.append(node2)
linkedList.append(node3)
linkedList.append(node4)
linkedList.iteration()
node1


linkedList.insert(newNode, 15)
linkedList.insert(newNode_2, 4)
linkedList.count()


newNode_3 = Node(700)
linkedList.insert(newNode_3, 1)

newNode_4 = Node(800)
linkedList.insert(newNode_4, 5)
newNode_5 = Node(900)
linkedList.insert(newNode_5, 3)
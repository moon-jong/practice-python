class Stack:
    pushedList = list()
    def push(self, data):
        self.pushedList.append(data)
    def pop(self):
        print(self.pushedList.pop())
    def printStack(self):
            for i in range(self.count()):
                print("-----------")
                print("     %d     " %(self.pushedList[self.count() - (i + 1)]))
    def count(self):
        count = len(self.pushedList)
        return count

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)

stack.pushedList
stack.pop()
stack.printStack()


stack.count()

len(stack.pushedList)

stack.push(8)
stack.pushedList[2]
stack.printStack()



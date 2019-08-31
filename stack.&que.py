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

class Que:
    pushedList = []
    def put(self,data):
        self.pushedList.append(data)
    def delete(self):
        self.pushedList.pop(0)
    def quePrint(self):
        for i in range(self.count()):
            print('-----------')
            print('     %d     ' %(self.pushedList[i]))
    def count(self):
        count = len(self.pushedList)
        return count

que =Que()
que.put(2)
que.put(3)
que.put(4)
que.put(5)
que.put(6)
que.put(7)
que.count()
que.quePrint()
que.pushedList


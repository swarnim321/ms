from _collections import deque
class Stack:
    def __init__(self):
        self.stack=[]
        deque(self.stack)

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def exist(self,data):
        for i in len(self.stack):
            if stack[i]==data:
                return True
            else:
                return False
    def reverse(self):
        temp=deque()
        for i in range (len(self.stack)):
            temp.append(self.stack.pop())
        self.stack=temp


stack=Stack()
stack.push(2)
stack.push(5)
stack.push(8)
stack.push(7)
stack.push(9)
#print(stack)
print("pop",stack.pop())

print("peek",stack.peek())

stack.reverse()
print("reverse peek",stack.peek())
print(stack)


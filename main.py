class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

stack = Stack()

print(stack.isEmpty())

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.isEmpty())

print(stack.peek())

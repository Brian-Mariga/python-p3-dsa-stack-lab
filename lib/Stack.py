class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise Exception("Stack is full")

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            raise Exception("Stack is empty")
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return self.size() - self.items.index(target) - 1
        else:
            return -1

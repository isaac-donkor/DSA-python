#Intialise stack
class Stack:
    def __init__(self):
        self.items = []

#Add an item to the top of the stack
    def push(self, item):
        self.items.append(item)

#Add an item to the top of the stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

#Remove and return the top item
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

#Look at the top item without removing it
    def is_empty(self):
        return len(self.items) == 0

#Return the number of items in the stack
    def size(self):
        return len(self.items)

# Test
s = Stack()
s.push(1)
s.push(2)
print(s.pop())  # 2
print(s.peek()) # 1

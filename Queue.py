from collections import deque

queue = deque()

# Enqueue
queue.append("customer1")
queue.append("customer2")

# Dequeue
print(queue.popleft())  # customer1

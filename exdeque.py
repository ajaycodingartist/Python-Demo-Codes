from collections import deque

# Create a new queue
my_stack = deque()

# Enqueue (add) elements to the queue
my_stack.append("Item 1")
my_stack.append("Item 2")
my_stack.append("Item 3")

# Dequeue (remove) elements from the queue
item = my_stack.pop()
print("Dequeued item:", item)

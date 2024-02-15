from queue import Queue

# Create a new queue
my_queue = Queue()

# Enqueue (add) elements to the queue
my_queue.put("Item 1")
my_queue.put("Item 2")
my_queue.put("Item 3")

# Dequeue (remove) elements from the queue
item = my_queue.get()
print("Deleted item:", item)

# Check if the queue is empty
is_empty = my_queue.empty()
print("Is the queue empty?", is_empty)

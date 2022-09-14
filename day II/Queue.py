print("\n"*100) # Unnecessary Line: to clear up the console for a better presentation. Yes.

# This Demo is an implementation using List
class Queue:
    def __init__(self):     # Queue Object Constructor
        self.entries = []   # List
        self.length = 0     # Length of the list
        self.front = 0

    def __str__(self):      # Function use to return the "string representation" of the object. [ Called when using print() or str() ]
        string = f"<{str(self.entries)[1:-1]}>"
        return string

    def size(self):         # Function to return size of the list (this.entries)
        return self.length

    # --- Enqueues (Singular item to enqueue)---
    def put(self, item):
        self.entries.append(item)       # Adding item to the list
        self.length = self.length + 1   # Updating length of list

    # --- Enqueues (Get Item at the front of the entries) ---
    def get_front(self):
        return self.entries[0]

    # --- Dequeues (Removes item at the front of the current queue) ---
    def get(self):
        self.length = self.length - 1
        dequeued = self.entries[self.front]
        self.entries = self.entries[1:]
        return dequeued

    # --- Rotate Queue (Moving first element to the back of the queue)---
    def rotate(self, rotation):
        for i in range(rotation): # Number of times to rotate queue
            self.put(self.get())
    

# -----------------------------------------------------------------------
#                           <  Main Demo >
# -----------------------------------------------------------------------
queue = Queue()                     # Initialize queue object
print(f"Initial Queue: {queue} \n") # Calls the __str__ function

# Adding (Enqueue) items to our queue
queue.put("Wai Hang")
queue.put("Shan Lun")
queue.put("Addison")
print(f"Current Queue Size: {queue.size()}")
print(f"Current Queue: {queue} \n")

# Retrieving the FIRST item
print(f"First item: {queue.get_front()} \n")

# Rotating Queue
queue.rotate(2) # Rotate Queue 2 times
print(f"Rotated Queue: {queue} \n")

# Removing (Dequeue) FIRST item from our queue
print(f"Dequeued: {queue.get()}")
print(f"Current Queue: {queue}")


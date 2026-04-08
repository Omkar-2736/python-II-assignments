from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(item, " added to the queue.")

    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty. Cannot dequeue.")
            return None
        
        else:
            return self.queue.popleft()
        
    def display(self):
        print("Queue contents:", list(self.queue))

q = Queue()

while True:
    print("\nMenu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display Queue")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter the item to enqueue: ")
        q.enqueue(item)
    elif choice == '2':
        dequeued_item = q.safe_dequeue()
        if dequeued_item is not None:
            print(dequeued_item, " removed from the queue.")
    elif choice == '3':
        q.display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
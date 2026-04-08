class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(item, "pushed to stack.")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty. Cannot pop.")
            return None
        
        else:
            return self.stack.pop()
        
    def display(self):
        print("Stack contents:", self.stack)

s = Stack() 
while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = int(input("Enter an item to push: "))
        s.push(item)

    elif choice == '2':  
        item = s.pop()
        if item is not None:
            print(item, "popped from stack.")
    elif choice == '3':
        s.display()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
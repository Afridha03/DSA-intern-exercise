class Node:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.next = None

def insert_at_end(head, name, location):
    new_node = Node(name, location)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def insert_at_first(head, name, location):
    new_node = Node(name, location)
    new_node.next = head
    return new_node

def insert_at_position(head, name, location, position):
    new_node = Node(name, location)
    if position <= 1 or head is None:
        return insert_at_first(head, name, location)
    current = head
    count = 1
    while current.next and count < position - 1:
        current = current.next
        count += 1
    new_node.next = current.next
    current.next = new_node
    return head

def delete_by_name(head, target_name):
    if head is None:
        return None
    if head.name == target_name:
        return head.next
    current = head
    while current.next and current.next.name != target_name:
        current = current.next
    if current.next:
        current.next = current.next.next
    else:
        print("Name not found.")
    return head

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def display_list(head):
    print("\n--- Linked List ---")
    if head is None:
        print("List is empty.")
    else:
        current = head
        count = 1
        while current:
            print(f"Node {count}: {current.name}, {current.location}")
            current = current.next
            count += 1

# 🌟 Step 1: Create Linked List at Start
head = None
print("Create your linked list:")
ask = "yes"
while ask.lower() == "yes":
    name = input("Enter Name: ")
    location = input("Enter Location: ")
    head = insert_at_end(head, name, location)
    ask = input("Add another node? (yes/no): ")

# 🌟 Step 2: Menu Options
while True:
    print("\nChoose an option:")
    print("1. Add node at the end")
    print("2. Add node at the first")
    print("3. Add node at position")
    print("4. Delete a node by name")
    print("5. Display the linked list")
    print("6. Reverse the linked list")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter Name: ")
        location = input("Enter Location: ")
        head = insert_at_end(head, name, location)

    elif choice == "2":
        name = input("Enter Name: ")
        location = input("Enter Location: ")
        head = insert_at_first(head, name, location)

    elif choice == "3":
        name = input("Enter Name: ")
        location = input("Enter Location: ")
        position = int(input("Enter position: "))
        head = insert_at_position(head, name, location, position)

    elif choice == "4":
        name = input("Enter name to delete: ")
        head = delete_by_name(head, name)

    elif choice == "5":
        display_list(head)

    elif choice == "6":
        head = reverse_list(head)
        print("Linked list reversed.")
        display_list(head)

    elif choice == "7":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
